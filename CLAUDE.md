# awesome-ChatGPT-repositories — Claude Code Guide

This repository is a curated list of 2500+ open-source GitHub repositories related to ChatGPT and LLMs. It includes a searchable skill for Claude Code.

## Repository structure

```
awesome-ChatGPT-repositories.json   ← main data (all 2500+ repos, verbose format)
plugins/awesome-chatgpt-search/
  README.md                         ← plugin documentation
  data/repos-<category>.json        ← compact search data split by category (12 files)
  skills/search/SKILL.md            ← markdown-only skill (no Python required)
.claude/commands/awesome-chatgpt.md ← slash command for local (unnamespaced) use
.claude-plugin/
  plugin.json                       ← plugin manifest
  marketplace.json                  ← marketplace catalog (git-subdir source)
```

## Plugin skill (when installed via /plugin)

After installation, invoke as:
```
/awesome-chatgpt-search:search RAG retrieval
/awesome-chatgpt-search:search category:CLIs agent
/awesome-chatgpt-search:search language:Python langchain
/awesome-chatgpt-search:search list categories
```

## Local standalone command (when repo is cloned)

```
/awesome-chatgpt RAG retrieval
/awesome-chatgpt category:CLIs agent
```

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
