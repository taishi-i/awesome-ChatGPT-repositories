# awesome-ChatGPT-repositories — Claude Code Guide

This repository is a curated list of 2500+ open-source GitHub repositories related to ChatGPT and LLMs. It includes a searchable skill that Claude Code and Codex share.

## Repository structure

```
awesome-ChatGPT-repositories.json   ← main data (all 2500+ repos, verbose format)
plugins/awesome-chatgpt-search/     ← one plugin directory for both Claude Code and Codex
  README.md                         ← plugin documentation
  build_data.py                     ← regenerates data/ from the main JSON
  .claude-plugin/plugin.json        ← Claude Code plugin manifest
  .codex-plugin/plugin.json         ← Codex plugin manifest
  data/repos-<category>.json        ← compact search data split by category (18 files), shared
  skills/search/SKILL.md            ← markdown-only skill shared by both tools (no Python required)
  skills/search/agents/openai.yaml  ← Codex UI metadata for the skill
.claude/commands/awesome-chatgpt.md ← Claude Code slash command for local (unnamespaced) use
.agents/skills/awesome-chatgpt/SKILL.md ← Codex skill for local use (delegates to the shared SKILL.md)
.claude-plugin/
  plugin.json                       ← legacy root manifest (not referenced by the marketplace)
  marketplace.json                  ← Claude Code marketplace catalog (git-subdir source)
.agents/plugins/marketplace.json    ← Codex marketplace catalog (local source)
```

`skills/search/SKILL.md` is read by both tools, so keep it agent-neutral: don't rely on `$ARGUMENTS` (Claude Code appends `ARGUMENTS: …` on its own), and keep the per-tool lines for locating `data/` (`${CLAUDE_PLUGIN_ROOT}/data` for Claude Code, relative to the SKILL.md for Codex). Keep the version in both plugin manifests in sync.

## Plugin skill (when installed via /plugin)

After installation, invoke as:
```
/awesome-chatgpt-search:search RAG retrieval
/awesome-chatgpt-search:search category:CLIs agent
/awesome-chatgpt-search:search language:Python langchain
/awesome-chatgpt-search:search list categories
```

In Codex (installed with `codex plugin marketplace add taishi-i/awesome-ChatGPT-repositories` and `codex plugin add awesome-chatgpt-search@awesome-chatgpt-repositories`), use the same queries with `$awesome-chatgpt-search:search`.

## Local standalone command (when repo is cloned)

```
/awesome-chatgpt RAG retrieval
/awesome-chatgpt category:CLIs agent
```

In Codex, the repo-local skill is `$awesome-chatgpt`.

## Compact data format (`plugins/awesome-chatgpt-search/data/`)

Data is split into 18 per-category JSON files (5–70 KB each, all under the Read tool's limits).
The six categories with more than ~200 entries (Chatbots, NLP, Openai, Others, Browser-extensions, CLIs) are split into `-a` / `-b` halves:

```
repos-awesome-lists.json          repos-prompts.json
repos-chatbots-a.json             repos-chatbots-b.json
repos-browser-extensions-a.json   repos-browser-extensions-b.json
repos-clis-a.json                 repos-clis-b.json
repos-reimplementations.json      repos-tutorials.json
repos-nlp-a.json                  repos-nlp-b.json
repos-langchain.json              repos-unity.json
repos-openai-a.json               repos-openai-b.json
repos-others-a.json               repos-others-b.json
```

Each file is a JSON array with **one record per line** (a valid array, but newline-delimited) so the search skill can `grep` for matching repos and score only those lines — instead of reading whole files into context, which keeps token use low:

```json
[
{"u":"https://github.com/user/repo","n":"repo-name","d":"...","c":"Category","l":"Python","t":"tag1,tag2","sc":6.5,"st":1234,"ns":6.4},
...
]
```

Expanded, each record has these fields:

```json
[
  {
    "u": "https://github.com/user/repo",
    "n": "repo-name",
    "d": "English description (≤200 chars)",
    "c": "Category",
    "l": "Python",
    "t": "tag1,tag2,tag3",
    "sc": 6.5,
    "st": 1234,
    "ns": 6.4
  }
]
```

Fields: `u` URL · `n` name · `d` description · `c` category · `l` language (optional) · `t` topics comma-separated (optional) · `sc` quality score 0–8 · `st` star count (optional) · `ns` normalized star score 0–10 (optional)

## Data file format

`awesome-ChatGPT-repositories.json` has this structure:

```json
{
  "version": "2.1.0",
  "contents": {
    "<category>": {
      "<github_url>": {
        "repository_name": "...",
        "user_name": "...",
        "language": "Python",
        "license": "MIT",
        "description": "...",
        "topics": ["..."],
        "multilingual_descriptions": { "en": "...", "ja": "...", "zh-hans": "...", "zh-hant": "..." }
      }
    }
  }
}
```

Categories: `Awesome-lists` · `Prompts` · `Chatbots` · `Browser-extensions` · `CLIs` · `Reimplementations` · `Tutorials` · `NLP` · `Langchain` · `Unity` · `Openai` · `Others`

## Contributing new repositories

See `contributing.md`. The `develop` branch is used for additions; PRs are merged to `main`.
