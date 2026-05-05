# awesome-ChatGPT-repositories — Claude Code Guide

This repository is a curated list of 2500+ open-source GitHub repositories related to ChatGPT and LLMs. It includes a searchable skill for Claude Code.

## Repository structure

```
awesome-ChatGPT-repositories.json   ← main data (all 2500+ repos)
skills/search/
  SKILL.md                          ← skill definition (with YAML frontmatter)
  scripts/search.py                 ← standalone search CLI
.claude/commands/awesome-chatgpt.md ← slash command for local (unnamespaced) use
.claude-plugin/
  plugin.json                       ← plugin manifest (name: "awesome-chatgpt")
  marketplace.json                  ← marketplace catalog
```

## Plugin skill (when installed via /plugin)

After installation, invoke as:
```
/awesome-chatgpt:search RAG retrieval
/awesome-chatgpt:search category:CLIs agent
/awesome-chatgpt:search language:Python langchain
/awesome-chatgpt:search list categories
```

## Local standalone command (when repo is cloned)

```
/awesome-chatgpt RAG retrieval
/awesome-chatgpt category:CLIs agent
```

## Search script

```bash
python3 skills/search/scripts/search.py "fine-tuning" --limit 10
python3 skills/search/scripts/search.py --category NLP --language Python
python3 skills/search/scripts/search.py --list-categories
```

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
