#!/usr/bin/env python3
"""
Generate compact search data files for the awesome-chatgpt-search plugin.
The same files are used by the Claude Code and Codex versions of the skill.

Usage:
    python3 plugins/awesome-chatgpt-search/build_data.py

Reads:  awesome-ChatGPT-repositories.json  (repo root)
Writes: plugins/awesome-chatgpt-search/data/repos-<category>.json
        Large categories (>200 entries) are split into -a and -b halves.
        skills/awesome-chatgpt-search/  (repo root): the standalone copy of the
        search skill that `npx skills add taishi-i/awesome-ChatGPT-repositories`
        installs: SKILL.md and agents/openai.yaml derived from skills/search/,
        plus a copy of data/. Don't edit that directory by hand.
"""

import json
import math
import shutil
from pathlib import Path


def normalize_stars(stars: int) -> float:
    """Log-scaled star score 0–10.
    ~10 stars → 2.1,  ~100 → 4.0,  ~1k → 6.0,  ~10k → 8.0,  ~100k → 10.0
    """
    if not stars:
        return 0.0
    return round(min(10.0, math.log10(stars + 1) * 2.0), 1)

REPO_ROOT = Path(__file__).parent.parent.parent
SOURCE = REPO_ROOT / "awesome-ChatGPT-repositories.json"
OUT_DIR = Path(__file__).parent / "data"

# The plugin's search skill, and its standalone copy for `npx skills`
# (https://github.com/vercel-labs/skills). That installer copies only the skill's
# own directory, so the copy bundles data/ and looks for it next to its SKILL.md.
SKILL_DIR = Path(__file__).parent / "skills" / "search"
STANDALONE_DIR = REPO_ROOT / "skills" / "awesome-chatgpt-search"

# (plugin text, standalone text) pairs applied to skills/search/SKILL.md.
# Each plugin text must appear exactly once. When you reword one of these
# passages in the plugin SKILL.md, update its pair here as well.
STANDALONE_SKILL_MD_EDITS = [
    ("name: search\n", "name: awesome-chatgpt-search\n"),
    (
        "(the same skill runs in Claude Code and Codex):\n"
        "- **Claude Code:** the arguments of `/awesome-chatgpt-search:search`, appended at the end as `ARGUMENTS: …`.\n"
        "- **Codex:** the user's message that invoked `$awesome-chatgpt-search:search`, minus the `$…` mention itself.\n",
        "(the same skill runs in Claude Code, Codex, and other agents):\n"
        "- **Claude Code:** the arguments of `/awesome-chatgpt-search`, appended at the end as `ARGUMENTS: …`.\n"
        "- **Codex and other agents:** the user's message that invoked this skill (`$awesome-chatgpt-search` in Codex), minus the skill mention itself.\n",
    ),
    ("relative to this plugin", "next to this SKILL.md"),
    (
        "it is the plugin's `data/` folder, two levels above this SKILL.md:\n"
        "- **Claude Code:** `${CLAUDE_PLUGIN_ROOT}/data`\n"
        "- **Codex:** `<directory of this SKILL.md>/../../data`, built from the absolute path you loaded this SKILL.md from.\n",
        "it is the `data/` folder next to this SKILL.md:\n"
        "- **Claude Code:** `${CLAUDE_SKILL_DIR}/data`\n"
        "- **Codex and other agents:** `<directory of this SKILL.md>/data`, built from the absolute path you loaded this SKILL.md from.\n",
    ),
    (
        'find "${CODEX_HOME:-$HOME/.codex}/plugins" "$HOME/.claude/plugins" "$PWD" ',
        'find "$PWD" "$HOME/.agents/skills" "$HOME/.claude/skills" "${CODEX_HOME:-$HOME/.codex}/skills" ',
    ),
]

# Same for skills/search/agents/openai.yaml (Codex UI metadata).
STANDALONE_OPENAI_YAML_EDITS = [
    ("$awesome-chatgpt-search:search", "$awesome-chatgpt-search"),
]

# Categories with more than ~200 entries are split into -a / -b.
# This includes Browser-extensions (~250) and CLIs (~230).
SPLIT_THRESHOLD = 200

# Slug map: category name → file stem
SLUG = {
    "Awesome-lists": "repos-awesome-lists",
    "Prompts": "repos-prompts",
    "Chatbots": "repos-chatbots",
    "Browser-extensions": "repos-browser-extensions",
    "CLIs": "repos-clis",
    "Reimplementations": "repos-reimplementations",
    "Tutorials": "repos-tutorials",
    "NLP": "repos-nlp",
    "Langchain": "repos-langchain",
    "Unity": "repos-unity",
    "Openai": "repos-openai",
    "Others": "repos-others",
}


def compute_sc(entry: dict) -> float:
    """Quality score 0–8 based on metadata richness."""
    score = 0.0

    en_desc = (
        (entry.get("multilingual_descriptions") or {}).get("en")
        or entry.get("description")
        or ""
    )
    if en_desc:
        score += 1.0
        if len(en_desc) > 50:
            score += 1.0
        if len(en_desc) > 120:
            score += 1.0

    topics = entry.get("topics") or []
    if topics:
        score += 1.0
        if len(topics) >= 3:
            score += 1.0
        if len(topics) >= 6:
            score += 1.0

    if entry.get("language"):
        score += 1.0

    license_ = entry.get("license") or ""
    if isinstance(license_, str) and license_ and license_.lower() not in ("other", ""):
        score += 0.5

    ml = entry.get("multilingual_descriptions") or {}
    if len(ml) >= 2:
        score += 0.5

    return round(min(8.0, score), 1)


def to_compact(url: str, entry: dict, category: str) -> dict:
    """Convert a verbose entry to compact search record."""
    en_desc = (
        (entry.get("multilingual_descriptions") or {}).get("en")
        or entry.get("description")
        or ""
    )
    # Truncate long descriptions
    if len(en_desc) > 200:
        en_desc = en_desc[:197] + "..."

    record = {
        "u": url,
        "n": entry.get("repository_name", ""),
        "d": en_desc,
        "c": category,
        "sc": compute_sc(entry),
    }

    lang = entry.get("language")
    if lang:
        record["l"] = lang

    topics = entry.get("topics") or []
    if topics:
        record["t"] = ",".join(topics)

    stars = entry.get("star_count")
    if stars is not None and stars > 0:
        record["st"] = stars
        record["ns"] = normalize_stars(stars)

    return record


def write_json(path: Path, records: list) -> None:
    # One record per line. The file stays a valid JSON array, but the layout
    # lets the search skill `grep` for matching repos and read only those lines
    # instead of loading whole category files into context (far fewer tokens).
    body = ",\n".join(
        json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in records
    )
    path.write_text(f"[\n{body}\n]\n", encoding="utf-8")
    kb = path.stat().st_size / 1024
    print(f"  {path.name}: {len(records)} entries  ({kb:.0f} KB)")


def apply_edits(text: str, edits: list[tuple[str, str]], name: str) -> str:
    for old, new in edits:
        if text.count(old) != 1:
            raise SystemExit(
                f"\nCannot build the standalone skill: {name} no longer contains "
                f"exactly one copy of:\n{old}\n"
                "Update the matching STANDALONE_*_EDITS pair in build_data.py."
            )
        text = text.replace(old, new)
    return text


def build_standalone_skill() -> None:
    """Refresh skills/awesome-chatgpt-search/ from the plugin's search skill and data."""
    data_dir = STANDALONE_DIR / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    for stale in data_dir.glob("repos-*.json"):
        stale.unlink()
    for src in sorted(OUT_DIR.glob("repos-*.json")):
        shutil.copyfile(src, data_dir / src.name)

    skill_md = apply_edits(
        (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"),
        STANDALONE_SKILL_MD_EDITS,
        "skills/search/SKILL.md",
    )
    openai_yaml = apply_edits(
        (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8"),
        STANDALONE_OPENAI_YAML_EDITS,
        "skills/search/agents/openai.yaml",
    )
    (STANDALONE_DIR / "SKILL.md").write_text(skill_md, encoding="utf-8")
    (STANDALONE_DIR / "agents").mkdir(exist_ok=True)
    (STANDALONE_DIR / "agents" / "openai.yaml").write_text(openai_yaml, encoding="utf-8")
    print("\nStandalone skill (npx skills) refreshed: skills/awesome-chatgpt-search/")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with SOURCE.open(encoding="utf-8") as f:
        data = json.load(f)

    cat_counts: dict[str, int] = {}
    for category, entries in data["contents"].items():
        slug = SLUG.get(category)
        if not slug:
            print(f"[skip] unknown category: {category}")
            continue

        records = [
            to_compact(url, entry, category)
            for url, entry in entries.items()
        ]
        cat_counts[category] = len(records)

        if len(records) > SPLIT_THRESHOLD:
            mid = math.ceil(len(records) / 2)
            write_json(OUT_DIR / f"{slug}-a.json", records[:mid])
            write_json(OUT_DIR / f"{slug}-b.json", records[mid:])
        else:
            write_json(OUT_DIR / f"{slug}.json", records)

    build_standalone_skill()

    print("\nDone.")

    # Category-count table — copy into the plugin README.md and awesome-chatgpt.md
    # whenever the data is regenerated. (SKILL.md counts the data files directly.)
    print("\nCategory counts (sync into the docs' count tables):")
    print("| Category | Count |")
    print("|----------|-------|")
    total = 0
    for category in SLUG:
        n = cat_counts.get(category, 0)
        total += n
        print(f"| {category} | {n} |")
    print(f"| **Total** | **{total:,}** |")


if __name__ == "__main__":
    main()
