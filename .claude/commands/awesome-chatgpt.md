Search **awesome-ChatGPT-repositories** for open-source GitHub repositories related to ChatGPT and LLMs.

The user's query is: $ARGUMENTS

---

Parse the query and run the appropriate search:

1. If query is `list categories` or `categories` → run with `--list-categories`
2. If query contains `category:<name>` → extract and pass as `--category <name>`
3. If query contains `language:<lang>` → extract and pass as `--language <lang>`
4. Remaining text is the keyword search query

Run the search script (from the repository root):
```bash
python3 skills/search/scripts/search.py $ARGUMENTS
```

If the script is unavailable, read `awesome-ChatGPT-repositories.json` from the repo root and search it. The JSON structure is:
```
data.contents.<category_name>.<github_url> = {
  repository_name, user_name, language, license, description, topics[], multilingual_descriptions{}
}
```

Categories: Awesome-lists, Prompts, Chatbots, Browser-extensions, CLIs, Reimplementations, Tutorials, NLP, Langchain, Unity, Openai, Others

Present results as a clean markdown list with repository name (linked), category, language, and description. Show at most 10 results.
