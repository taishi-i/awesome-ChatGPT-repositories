# awesome-chatgpt-search

Search 2,500+ ChatGPT and LLM open-source repositories directly from [Claude Code](https://claude.ai/code) or [Codex](https://developers.openai.com/codex).

This plugin provides a single skill that searches across all categories of [awesome-ChatGPT-repositories](https://github.com/taishi-i/awesome-ChatGPT-repositories): chatbots, CLIs, NLP tools, Langchain integrations, prompts, browser extensions, tutorials, and more.

Claude Code and Codex share the same skill (`skills/search/SKILL.md`) and the same bundled data (`data/`). Each tool reads its own manifest: `.claude-plugin/plugin.json` for Claude Code and `.codex-plugin/plugin.json` for Codex.

## Install

### Claude Code

**Inside Claude Code:**
```shell
/plugin marketplace add taishi-i/awesome-ChatGPT-repositories
/plugin install awesome-chatgpt-search@awesome-chatgpt-repositories
```

**Via CLI:**
```bash
claude plugin marketplace add taishi-i/awesome-ChatGPT-repositories
claude plugin install awesome-chatgpt-search@awesome-chatgpt-repositories
```

**From a local clone:**
```bash
git clone https://github.com/taishi-i/awesome-ChatGPT-repositories
cd awesome-ChatGPT-repositories
claude plugin marketplace add ./.claude-plugin/marketplace.json
claude plugin install awesome-chatgpt-search
```

### Codex

```bash
codex plugin marketplace add taishi-i/awesome-ChatGPT-repositories
codex plugin add awesome-chatgpt-search@awesome-chatgpt-repositories
```

Start a new Codex session afterwards so the skill is loaded. Once the marketplace is added, the plugin can also be installed from `/plugins` inside Codex.

**From a local clone:**
```bash
git clone https://github.com/taishi-i/awesome-ChatGPT-repositories
cd awesome-ChatGPT-repositories
codex plugin marketplace add .
codex plugin add awesome-chatgpt-search@awesome-chatgpt-repositories
```

## Update

**Claude Code:**
```shell
/plugin update awesome-chatgpt-search@awesome-chatgpt-repositories
```

**Codex:**
```bash
codex plugin marketplace upgrade awesome-chatgpt-repositories
codex plugin add awesome-chatgpt-search@awesome-chatgpt-repositories
```

## Usage

**Claude Code:**
```shell
/awesome-chatgpt-search:search <query>
```

**Codex:**
```shell
$awesome-chatgpt-search:search <query>
```

Codex also picks the skill up on its own for requests such as "find open-source RAG frameworks", but mentioning it with `$` gives the most consistent output.

### Examples

```shell
/awesome-chatgpt-search:search RAG retrieval
/awesome-chatgpt-search:search category:CLIs agent
/awesome-chatgpt-search:search language:Python langchain
/awesome-chatgpt-search:search fine-tuning
/awesome-chatgpt-search:search list categories
```

In Codex, use the same queries with `$awesome-chatgpt-search:search` instead.

Queries in any language are supported — the skill converts them to English keywords automatically.

### Without installing (inside a clone of this repository)

- **Claude Code:** `/awesome-chatgpt <query>` (from `.claude/commands/awesome-chatgpt.md`)
- **Codex:** `$awesome-chatgpt <query>` (from `.agents/skills/awesome-chatgpt/SKILL.md`, which reuses this plugin's skill and data)

## Ranking

Search results are ranked by a combined score:

1. **Text relevance** — keyword matches in name (+20/+10), description (+5), topics (+3), and category (+2)
2. **Quality signal** — pre-computed score reflecting description richness and topic coverage
3. **Agent re-ranking** — the final top-20 are re-ordered by Claude's or Codex's semantic judgment (category fit, specificity, language match)

## Data coverage

All data is bundled in the plugin and generated from `awesome-ChatGPT-repositories.json` by `build_data.py`. `list categories` counts the bundled data directly, so its numbers always match the installed version.

| Category | Count |
|----------|-------|
| Awesome-lists | 99 |
| Prompts | 192 |
| Chatbots | 386 |
| Browser-extensions | 259 |
| CLIs | 277 |
| Reimplementations | 42 |
| Tutorials | 21 |
| NLP | 433 |
| Langchain | 180 |
| Unity | 17 |
| Openai | 331 |
| Others | 486 |
| **Total** | **2,723** |

## License

CC0-1.0 — Public Domain
