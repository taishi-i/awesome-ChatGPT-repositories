Search **awesome-ChatGPT-repositories** for open-source GitHub repositories related to ChatGPT and LLMs.

The user's query is: $ARGUMENTS

---

## Instructions

### Step 1 — Interpret the query

Supported modifiers:
- `category:<name>` — filter to one category
- `language:<lang>` — filter by programming language
- `list categories` / `categories` — show category list instead
- Plain text — keyword search

The data descriptions are in **English**. Convert non-English queries to English keywords before searching.

### Step 2 — Select which data files to read

Data files are in `plugins/awesome-chatgpt-search/data/` (relative to repo root / PWD).

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

Each file is a JSON array of items with: `u` (URL), `n` (name), `d` (description), `c` (category), `l` (language, optional), `t` (topics comma-separated, optional), `sc` (quality score 0–8).

**Which files to read — read only what the query needs:**

**Rule A — category: specified:** read only that category's file(s).

**Rule B — list categories:** no file reads, jump straight to the output.

**Rule C — keyword routing for general queries:**

For each row below, check if the query contains any of the listed keywords (case-insensitive).
Read that row's files only if there is a match.
Collect all matching rows' files (deduplicated).
If **no rows match**, default to: `repos-chatbots-a.json`, `repos-nlp-a.json`, `repos-openai-a.json`, `repos-others-a.json`.

| If query mentions… | Read these files |
|--------------------|-----------------|
| chatbot, bot, chat, dialog, conversation, assistant, discord, slack | repos-chatbots-a.json, repos-chatbots-b.json |
| RAG, retrieval, vector, embed, semantic, FAISS, Chroma, Pinecone, similarity, index | repos-nlp-a.json, repos-nlp-b.json, repos-langchain.json |
| NLP, text, classify, classification, NER, POS, sentiment, translation, extraction, summariz | repos-nlp-a.json, repos-nlp-b.json |
| agent, agentic, workflow, autonomous, orchestrat, tool use, function call, multi-agent | repos-others-a.json, repos-others-b.json, repos-langchain.json |
| OpenAI, GPT-3, GPT-4, gpt4, gpt3, completion, fine-tun, API key, endpoint | repos-openai-a.json, repos-openai-b.json |
| browser, extension, Chrome, Firefox, sidebar, popup, Tampermonkey | repos-browser-extensions.json |
| CLI, terminal, shell, command-line, command line | repos-clis.json |
| tutorial, learn, course, beginner, guide, example, cookbook, sample | repos-tutorials.json |
| prompt, prompting, few-shot, chain-of-thought, jailbreak, injection | repos-prompts.json |
| Unity, game engine, 3D, game development | repos-unity.json |
| LangChain, LlamaIndex, Haystack, chain, index, LangGraph | repos-langchain.json |
| reimplement, from scratch, reproduce, train, training, PyTorch | repos-reimplementations.json |
| awesome list, curated, collection, survey, compilation | repos-awesome-lists.json |
| code, coding, IDE, VS Code, copilot, autocomplete, interpreter | repos-others-a.json, repos-others-b.json, repos-clis.json |
| image, vision, multimodal, DALL-E, Stable Diffusion, drawing | repos-others-a.json, repos-nlp-a.json |
| voice, speech, audio, TTS, ASR, Whisper | repos-others-a.json, repos-nlp-b.json |

### Step 3 — Filter by language (if `language:<lang>` given)

Keep only items where `l` matches (case-insensitive).

### Step 4 — Score candidates

Per keyword (case-insensitive):
- Name exact match: +20 pts
- Name contains: +10 pts
- Description contains: +5 pts
- Topics contains: +3 pts
- Category contains: +2 pts

Quality bonus: `min(4, sc * 0.5)`

Exclude items with zero keyword hits. Take top 20 by combined score.

### Step 5 — Re-rank and output

Apply semantic judgment: prefer repos that directly address the query's core intent, with the right category and higher quality score when otherwise tied.

Present up to **10** results:

```
## Search results for "$ARGUMENTS"

*(Searched for: keyword1, keyword2, ...)*

Found N result(s).

### 1. [name](url)
**Category:** category  ·  **Language:** language
Description.
*Topics: tag1, tag2*
```

For `list categories`, present:

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

If no results, suggest alternate keywords and link to https://github.com/taishi-i/awesome-ChatGPT-repositories
