---
description: Search 2500+ curated ChatGPT and LLM open-source repositories. Use when the user asks to find tools, libraries, or repos related to ChatGPT, LLMs, RAG, agents, langchain, NLP, AI development, or any open-source AI tooling.
---

Search the awesome-ChatGPT-repositories database for: "$ARGUMENTS"

## Instructions

### Step 1 — Interpret the query

The user's query is: "$ARGUMENTS"

Supported query modifiers:
- `category:<name>` — filter to one category
- `language:<lang>` — filter by programming language
- `list categories` or `categories` — skip to Step 5b
- Plain text — keyword search across all categories

The descriptions are in **English**, so convert non-English queries to English keywords before searching.

Examples:
| User query | English keywords to search |
|------------|---------------------------|
| RAGを使ったチャットボット | RAG, retrieval, chatbot, vector |
| 코드 생성 도구 (Korean) | code generation, copilot, autocomplete |
| 中文问答系统 | chinese, QA, question answering |
| outil de résumé (French) | summarization, summary, text |
| LLMを使ったエージェント | agent, autonomous, LLM, tool use |

**Keyword tips:**
- **Use stems, not full words.** Substring match catches variants: `embed` → embedding/embeddings, `retriev` → retrieval/retrieve, `classif` → classification/classifier, `generat` → generation/generative, `fine-tun` → fine-tune/fine-tuning, `summari` → summarize/summarization, `orchestrat` → orchestrate/orchestration.
- **Add domain-specific names.** For common LLM/AI domains, include well-known tool or framework names present in the database:

| Domain (query hint) | Stem keywords | Tool/library names to add |
|---|---|---|
| RAG / 検索拡張生成 | `retriev`, `rag`, `embed`, `vector` | `langchain`, `llamaindex`, `haystack`, `faiss`, `chroma`, `pinecone` |
| Agent / エージェント | `agent`, `autonom`, `orchestrat` | `autogpt`, `langchain`, `langgraph`, `crewai` |
| Fine-tuning / ファインチューニング | `fine-tun`, `lora`, `peft`, `finetun` | `lora`, `peft`, `qlora` |
| Code generation / コード生成 | `code`, `coding`, `copilot`, `autocomplet` | `copilot`, `codex`, `interpreter` |
| Chatbot / チャットボット | `chat`, `bot`, `dialog`, `convers` | `discord`, `telegram`, `slack` |
| Prompt engineering | `prompt`, `few-shot`, `chain-of-thought`, `jailbreak` | `promptflow`, `dspy` |
| Evaluation / 評価 | `evaluat`, `benchmark`, `metric` | `evals`, `lm-eval`, `deepeval` |
| Image / 画像生成 | `image`, `vision`, `multimodal` | `dall-e`, `stable-diffusion`, `midjourney` |
| Voice / 音声 | `voice`, `speech`, `audio`, `tts`, `asr` | `whisper`, `eleven` |

- **Aim for 3–6 keywords.** Too few miss items; too many inflate low-quality partial matches.

### Step 2 — Select which data files to read

Data is split into per-category files. Each file is a JSON array of items with fields:
- `u`: GitHub URL · `n`: repository name · `d`: English description
- `c`: category · `l`: language (optional) · `t`: topics comma-separated (optional)
- `sc`: quality score 0–8

**File list** (all under `data/` relative to this plugin; the four largest categories are split a/b):

| Category | File(s) |
|----------|---------|
| Awesome-lists | `repos-awesome-lists.json` |
| Prompts | `repos-prompts.json` |
| Chatbots | `repos-chatbots-a.json`, `repos-chatbots-b.json` |
| Browser-extensions | `repos-browser-extensions.json` |
| CLIs | `repos-clis.json` |
| Reimplementations | `repos-reimplementations.json` |
| Tutorials | `repos-tutorials.json` |
| NLP | `repos-nlp-a.json`, `repos-nlp-b.json` |
| Langchain | `repos-langchain.json` |
| Unity | `repos-unity.json` |
| Openai | `repos-openai-a.json`, `repos-openai-b.json` |
| Others | `repos-others-a.json`, `repos-others-b.json` |

**Which files to read — read the minimum set that covers the query:**

**Rule A — category: specified:** read only that category's file(s), skip routing below.

**Rule B — list categories:** skip all file reads, jump to Step 5b.

**Rule C — keyword routing for general queries:**

Use the **English keywords from Step 1** (not the original query text) for routing.
For each row below, check if any English keyword contains or matches the listed terms (case-insensitive substring).
Read that row's file(s) only if there is a match.
If multiple rows match, collect all their files (deduplicated).
If **no rows match**, use the default: `repos-chatbots-a.json`, `repos-nlp-a.json`, `repos-openai-a.json`, `repos-others-a.json`.

| If query mentions… | Read these files |
|--------------------|-----------------|
| chatbot, bot, chat, dialog, conversation, assistant, discord, slack | repos-chatbots-a.json, repos-chatbots-b.json |
| RAG, retrieval, vector, embed, semantic, FAISS, Chroma, Pinecone, similarity, index | repos-nlp-a.json, repos-nlp-b.json, repos-langchain.json |
| NLP, text, classify, classification, NER, POS, sentiment, translation, extraction, summariz | repos-nlp-a.json, repos-nlp-b.json |
| agent, agentic, workflow, autonomous, orchestrat, tool use, function call, multi-agent | repos-others-a.json, repos-others-b.json, repos-langchain.json |
| OpenAI, GPT-3, GPT-4, gpt4, gpt3, completion, fine-tun, API key, endpoint | repos-openai-a.json, repos-openai-b.json |
| browser, extension, Chrome, Firefox, sidebar, popup, Tampermonkey | repos-browser-extensions-a.json, repos-browser-extensions-b.json |
| CLI, terminal, shell, command-line, command line | repos-clis-a.json, repos-clis-b.json |
| tutorial, learn, course, beginner, guide, example, cookbook, sample | repos-tutorials.json |
| prompt, prompting, few-shot, chain-of-thought, jailbreak, injection | repos-prompts.json |
| Unity, game engine, 3D, game development | repos-unity.json |
| LangChain, LlamaIndex, Haystack, chain, index, LangGraph | repos-langchain.json |
| lora, peft, qlora, finetun, fine-tuning, quantiz | repos-reimplementations.json, repos-nlp-a.json, repos-openai-a.json |
| evaluat, benchmark, metric, assess, leaderboard | repos-nlp-a.json, repos-nlp-b.json, repos-others-a.json |
| reimplement, from scratch, reproduce, train, training, PyTorch | repos-reimplementations.json |
| awesome list, curated, collection, survey, compilation | repos-awesome-lists.json |
| code, coding, IDE, VS Code, copilot, autocomplete, interpreter | repos-others-a.json, repos-others-b.json, repos-clis-a.json |
| image, vision, multimodal, DALL-E, Stable Diffusion, drawing | repos-others-a.json, repos-nlp-a.json |
| voice, speech, audio, TTS, ASR, Whisper | repos-others-a.json, repos-nlp-b.json |

To locate a file, use:
```
find "${HOME}/.claude/plugins" "${PWD}" -type f -name "<filename>" -path "*awesome-chatgpt-search*" 2>/dev/null | head -1
```

Then use the Read tool on the returned path.

### Step 3 — Filter by language (if `language:<lang>` was given)

After reading, keep only items where `l` matches the specified language (case-insensitive).

### Step 4 — Score candidates

Using the English keywords from Step 1, compute a **relevance score** for each item across all loaded files:

**Text match score** (case-insensitive, per keyword):
- Name (`n`) exact keyword match: +20 pts
- Name (`n`) contains keyword: +10 pts
- Description (`d`) contains keyword: +5 pts
- Topics (`t`) contains keyword: +3 pts
- Category (`c`) contains keyword: +2 pts

**Popularity bonus** (added once per item):
- If `ns` (normalized star score) is present: `min(4, ns * 0.4)`
- Otherwise: `min(4, sc * 0.5)`

**Quality bonus** (always added): `min(2, sc * 0.25)`

**Combined score = text_match + popularity_bonus + quality_bonus**

Exclude items with **text_match < 5** (catches only accidental partial hits). Collect top **20** candidates by combined score.

### Step 5a — Re-rank with your judgment

Apply semantic judgment to produce the final ordered list of up to **10** results.

Re-rank by evaluating each candidate on:
1. **Semantic centrality** — how directly does this repo address the query's core intent?
2. **Quality signal** — higher `sc` means a richer, better-documented project.
3. **Category fit** — match the repo type to the implied need:
   - "build a chatbot / ボット" → prefer `Chatbots`, `CLIs`
   - "learn / tutorial / 勉強" → prefer `Tutorials`
   - "prompt engineering" → prefer `Prompts`
   - "use from browser" → prefer `Browser-extensions`
   - "NLP task" → prefer `NLP`, `Langchain`
   - "OpenAI API" → prefer `Openai`
4. **Specificity** — a repo specialized for the exact use-case beats a general one.
5. **Language fit** — if the user implied a language, prefer repos with matching `l`.

### Step 5b — List categories (only if query was `list categories` / `categories`)

Skip scoring. Present:

```
## Available categories

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
```

### Step 6 — Format the output

```
## Search results for "$ARGUMENTS"

*(Searched for: keyword1, keyword2, ...)*

Found N result(s).

### 1. [repository-name](url)
**Category:** category  ·  **Language:** language  ·  ⭐ {st} stars
Description text here.
*Topics: tag1, tag2, tag3*

### 2. ...
```

Omit the Language line if `l` is absent. Omit `⭐ stars` if `st` is absent. Omit the Topics line if `t` is absent.

If no results found, suggest alternate keywords and link to:
https://github.com/taishi-i/awesome-ChatGPT-repositories

### Step 7 — Output use-case selection guide

After the search results list, append a guide table to help users pick the right repo for their specific situation.

**Match the section heading and table language to the query language** — if the query was in Japanese, use Japanese for the heading and column headers; otherwise use English.

```
## Use-case Selection Guide

| Use case | Recommended | Score | Why |
|---|---|---|---|
| ... | [name](url) | sc=N | short reason |
```

**Rules:**
- List **3–6 distinct use cases** derived from the top 10 results. Each row should represent a meaningfully different scenario (e.g., "deploy a self-hosted chatbot" vs. "build a RAG pipeline"), not just a restatement of the query.
- For each row, select the **single best repo** from the top 10 results.
- **Score column**: show `sc=N` using the item's quality score.
- **Why**: write a 10–15 word reason in the query language explaining the practical benefit. Do not copy the description verbatim.
- If two use cases map to the same repo, merge them into one row or drop the weaker one.
- If there are fewer than 3 meaningfully distinct use cases in the results, output as many rows as make sense (minimum 1).
