# awesome-chatgpt-search

Search 2,500+ ChatGPT and LLM open-source repositories directly from [Claude Code](https://claude.ai/code).

This plugin provides a single skill that searches across all categories of [awesome-ChatGPT-repositories](https://github.com/taishi-i/awesome-ChatGPT-repositories): chatbots, CLIs, NLP tools, Langchain integrations, prompts, browser extensions, tutorials, and more.

## Install

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

## Update

```shell
/plugin update awesome-chatgpt-search@awesome-chatgpt-repositories
```

## Usage

```shell
/awesome-chatgpt-search:search <query>
```

### Examples

```shell
/awesome-chatgpt-search:search RAG retrieval
/awesome-chatgpt-search:search category:CLIs agent
/awesome-chatgpt-search:search language:Python langchain
/awesome-chatgpt-search:search fine-tuning
/awesome-chatgpt-search:search list categories
```

Queries in any language are supported — the skill converts them to English keywords automatically.

## Ranking

Search results are ranked by a combined score:

1. **Text relevance** — keyword matches in name (+20/+10), description (+5), topics (+3), and category (+2)
2. **Quality signal** — pre-computed score reflecting description richness and topic coverage
3. **Claude re-ranking** — the final top-20 are re-ordered by Claude's semantic judgment (category fit, specificity, language match)

## Data coverage

All data is bundled in the plugin and sourced from `awesome-ChatGPT-repositories.json`.

| Category | Count |
|----------|-------|
| Awesome-lists | 95 |
| Prompts | 182 |
| Chatbots | 375 |
| Browser-extensions | 250 |
| CLIs | 227 |
| Reimplementations | 42 |
| Tutorials | 21 |
| NLP | 405 |
| Langchain | 178 |
| Unity | 17 |
| Openai | 325 |
| Others | 451 |
| **Total** | **2,568** |

## License

CC0-1.0 — Public Domain
