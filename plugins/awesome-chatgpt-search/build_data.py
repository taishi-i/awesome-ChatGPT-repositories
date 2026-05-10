#!/usr/bin/env python3
"""
Generate compact search data files for the awesome-chatgpt-search plugin.

Usage:
    python3 plugins/awesome-chatgpt-search/build_data.py

Reads:  awesome-ChatGPT-repositories.json  (repo root)
Writes: plugins/awesome-chatgpt-search/data/repos-<category>.json
        Large categories (>200 entries) are split into -a and -b halves.
"""

import json
import math
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
    path.write_text(
        json.dumps(records, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    kb = path.stat().st_size / 1024
    print(f"  {path.name}: {len(records)} entries  ({kb:.0f} KB)")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with SOURCE.open(encoding="utf-8") as f:
        data = json.load(f)

    for category, entries in data["contents"].items():
        slug = SLUG.get(category)
        if not slug:
            print(f"[skip] unknown category: {category}")
            continue

        records = [
            to_compact(url, entry, category)
            for url, entry in entries.items()
        ]

        if len(records) > SPLIT_THRESHOLD:
            mid = math.ceil(len(records) / 2)
            write_json(OUT_DIR / f"{slug}-a.json", records[:mid])
            write_json(OUT_DIR / f"{slug}-b.json", records[mid:])
        else:
            write_json(OUT_DIR / f"{slug}.json", records)

    print("\nDone.")


if __name__ == "__main__":
    main()
