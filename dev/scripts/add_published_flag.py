#!/usr/bin/env python3
"""
Add `published: true` to the *bottom* of YAML front matter for each project index.md.

Assumptions:
- Repo structure: <repo_root>/portfolio/projects/<slug>/index.md
- This script lives at:   dev/scripts/add_published_flag.py
- YAML front matter is delimited with:
      ---
      (front matter)
      ---
- Adds the line ONLY if not already present.
- Adds it immediately *before* the final closing '---'.

Example usage (from repo root):

  # Run on all projects
  python dev/scripts/add_published_flag.py --all

  # Run on a single project
  python dev/scripts/add_published_flag.py --project wireless-mobile-feeder-robot
"""

import argparse
import sys
import re
from pathlib import Path
from typing import Tuple


def split_front_matter_and_body(text: str) -> Tuple[str, str]:
    """
    Extract (front_matter, body) from a markdown file containing YAML front matter.
    Returns the front matter *without* the surrounding --- lines.
    """
    match = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not match:
        raise RuntimeError("File does not contain valid YAML front matter.")
    return match.group(1), match.group(2)


def add_published_flag(front_matter: str) -> str:
    """
    Append `published: true` to the bottom of the front matter.
    Do nothing if the front matter already contains a `published:` line.
    """
    if re.search(r"^\s*published\s*:", front_matter, re.MULTILINE):
        return front_matter  # already present; no changes

    # Append to bottom with a newline if needed
    if not front_matter.endswith("\n"):
        front_matter += "\n"

    front_matter += "published: true\n"
    return front_matter


def process_index_file(index_path: Path) -> None:
    """Read, transform, write the updated front matter."""
    text = index_path.read_text(encoding="utf-8")

    try:
        front_matter, body = split_front_matter_and_body(text)
    except RuntimeError as e:
        print(f"Skipping {index_path}: {e}")
        return

    new_front_matter = add_published_flag(front_matter)

    if new_front_matter == front_matter:
        print(f"No changes needed: {index_path}")
        return

    new_text = f"---\n{new_front_matter}---\n{body}"
    index_path.write_text(new_text, encoding="utf-8")
    print(f"Updated: {index_path}")


def find_projects_root() -> Path:
    """
    Infer repo root from this script's location.
    Expect: dev/scripts/add_published_flag.py
    Repo root = two levels up.
    """
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    projects_root = repo_root / "portfolio" / "projects"
    if not projects_root.is_dir():
        raise RuntimeError(f"Could not find portfolio/projects at: {projects_root}")
    return projects_root


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Append `published: true` to project index.md front matter."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--project", help="Process only a single project by slug.")
    group.add_argument("--all", action="store_true", help="Process all projects.")

    args = parser.parse_args(argv)
    projects_root = find_projects_root()

    if args.project:
        target = projects_root / args.project / "index.md"
        if not target.is_file():
            raise SystemExit(f"index.md not found: {target}")
        print(f"Processing single project: {target}")
        try:
            process_index_file(target)
        except Exception as e:
            raise SystemExit(f"ERROR while processing {target}:\n{e}")

    else:  # --all
        project_dirs = sorted(d for d in projects_root.iterdir() if d.is_dir())
        if not project_dirs:
            raise SystemExit(f"No project folders found under {projects_root}")

        for d in project_dirs:
            index_path = d / "index.md"
            if not index_path.is_file():
                print(f"Skipping {d} (no index.md)")
                continue
            print(f"Processing project: {index_path}")
            try:
                process_index_file(index_path)
            except Exception as e:
                print(f"ERROR processing {index_path}:\n{e}", file=sys.stderr)


if __name__ == "__main__":
    main()
