---
description: Search 2500+ curated ChatGPT and LLM open-source repositories. Use when the user asks to find tools, libraries, or repos related to ChatGPT, LLMs, RAG, agents, langchain, NLP, or AI.
---

Search awesome-ChatGPT-repositories for: **$ARGUMENTS**

Run the search script and show the results:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/search/scripts/search.py" $ARGUMENTS
```

Parse the user's query for modifiers before passing to the script:
- `category:<name>` → add `--category <name>` flag (categories: Awesome-lists, Prompts, Chatbots, Browser-extensions, CLIs, Reimplementations, Tutorials, NLP, Langchain, Unity, Openai, Others)
- `language:<lang>` → add `--language <lang>` flag
- `list categories` or `categories` → use `--list-categories` flag instead
- Plain text → pass as the positional query argument

Present the results as a clear markdown list. If no results are found, suggest trying different keywords or running with `list categories` to browse available categories.
