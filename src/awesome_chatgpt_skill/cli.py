"""CLI entry point for awesome-chatgpt-skill."""
import sys
from pathlib import Path


def main():
    # Locate the canonical search script
    pkg_root = Path(__file__).parent
    candidates = [
        pkg_root.parent.parent.parent / "skills" / "awesome-chatgpt" / "scripts" / "search.py",
        pkg_root.parent.parent / "skills" / "awesome-chatgpt" / "scripts" / "search.py",
    ]
    for script in candidates:
        if script.exists():
            import runpy
            sys.argv[0] = str(script)
            runpy.run_path(str(script), run_name="__main__")
            return

    print("Error: search.py not found. Please clone the full repository.", file=sys.stderr)
    sys.exit(1)
