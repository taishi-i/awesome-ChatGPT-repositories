#!/usr/bin/env python3
"""Search awesome-ChatGPT-repositories from CLI or Claude Code skills."""
import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path
from typing import Optional

DATA_URL = "https://raw.githubusercontent.com/taishi-i/awesome-ChatGPT-repositories/main/awesome-ChatGPT-repositories.json"
CACHE_PATH = Path.home() / ".cache" / "awesome-chatgpt" / "data.json"


def load_data() -> dict:
    candidates = [
        Path.cwd() / "awesome-ChatGPT-repositories.json",
        Path(__file__).parent.parent.parent.parent / "awesome-ChatGPT-repositories.json",
    ]
    for path in candidates:
        if path.exists():
            with open(path) as f:
                return json.load(f)
    return _fetch_from_github()


def _fetch_from_github() -> dict:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    import time
    if CACHE_PATH.exists() and (time.time() - CACHE_PATH.stat().st_mtime) < 86400:
        with open(CACHE_PATH) as f:
            return json.load(f)
    with urllib.request.urlopen(DATA_URL, timeout=15) as resp:
        data = json.loads(resp.read())
    with open(CACHE_PATH, "w") as f:
        json.dump(data, f)
    return data


def search(data, query, category, language, limit):
    results = []
    q = query.lower() if query else None

    for cat_name, repos in data["contents"].items():
        if category and category.lower() not in cat_name.lower():
            continue
        for url, repo in repos.items():
            lang = repo.get("language") or ""
            if language and language.lower() != lang.lower():
                continue
            if q:
                haystack = " ".join([
                    repo.get("repository_name", ""),
                    repo.get("description") or "",
                    " ".join(repo.get("topics", [])),
                    cat_name,
                    repo.get("multilingual_descriptions", {}).get("en") or "",
                    repo.get("multilingual_descriptions", {}).get("ja") or "",
                ]).lower()
                if q not in haystack:
                    continue
            results.append({
                "url": url,
                "name": repo["repository_name"],
                "user": repo.get("user_name", ""),
                "category": cat_name,
                "language": lang or None,
                "license": repo.get("license"),
                "description": repo.get("description") or "",
                "topics": repo.get("topics", []),
            })
            if len(results) >= limit:
                return results

    return results


def list_categories(data: dict) -> list:
    return [(cat, len(repos)) for cat, repos in data["contents"].items()]


def format_results(results: list) -> str:
    if not results:
        return "No repositories found."
    lines = [f"Found {len(results)} repositories:\n"]
    for r in results:
        lines.append(f"### [{r['name']}]({r['url']})")
        meta = [f"**Category:** {r['category']}"]
        if r["language"]:
            meta.append(f"**Language:** {r['language']}")
        lines.append(" · ".join(meta))
        if r["description"]:
            lines.append(r["description"])
        if r["topics"]:
            lines.append(f"*Topics: {', '.join(r['topics'][:6])}*")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Search awesome-ChatGPT-repositories",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  search.py "RAG retrieval"
  search.py "chatbot" --category CLIs --limit 5
  search.py --language Python --limit 20
  search.py --list-categories
  search.py --json "langchain"
""",
    )
    parser.add_argument("query", nargs="?", help="Search keywords")
    parser.add_argument("-c", "--category", help="Filter by category (partial match)")
    parser.add_argument("-l", "--language", help="Filter by programming language")
    parser.add_argument("-n", "--limit", type=int, default=10, help="Max results (default: 10)")
    parser.add_argument("--list-categories", action="store_true", help="Show all categories")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    data = load_data()

    if args.list_categories:
        cats = list_categories(data)
        print(f"Categories ({len(cats)} total):\n")
        for name, count in cats:
            print(f"  {name}: {count} repositories")
        return

    results = search(data, args.query, args.category, args.language, args.limit)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(format_results(results))


if __name__ == "__main__":
    main()
