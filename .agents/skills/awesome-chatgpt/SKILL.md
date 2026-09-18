---
name: awesome-chatgpt
description: Search this repository's awesome-ChatGPT-repositories list for open-source ChatGPT and LLM projects such as RAG frameworks, agents, chatbots, CLIs, prompts, and browser extensions. Use when the user asks to find tools, libraries, or repos related to ChatGPT, LLMs, or AI development; not for editing or adding list entries.
---

Repository-local Codex entry point for the awesome-chatgpt-search skill (the counterpart of the Claude Code command `.claude/commands/awesome-chatgpt.md`).

Read `plugins/awesome-chatgpt-search/skills/search/SKILL.md` under the repository root (the directory that contains `.agents/`) and follow it exactly, including its ground rules and output templates, with two local specifics:
- The query is the user's message minus the `$awesome-chatgpt` mention.
- The data directory is `plugins/awesome-chatgpt-search/data` under the repository root.
