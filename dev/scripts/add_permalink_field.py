#!/usr/bin/env python3
"""
Add `permalink:` to project index.md front matter using the project folder name.

Assumptions:
- Repo structure: <repo_root>/portfolio/projects/<slug>/index.md
- This script lives at:   dev/scripts/add_permalink_field.py
- Each target file has YAML front matter starting with '---' and ending with '---'
- The permalink format should be:  /portfolio/<slug>/

Example usage (from repo root, in VS Code terminal):

  # Run on all projects
  python dev/scripts/add_permalink_field.py --all

  # Run on a single project
  python dev/scripts/add_permalink_field.py --project adjustable-projector-mount
"""

import argparse
import sys
import re
from pathlib import Path
from typing import Tuple


def split_front_matter_and_body(text: str) -> Tuple[str, str]:
    """
    Split a markdown file into (front_matter_text, body_text).

    Expects front matter of the form:

        ---
        key: value
        ...
        ---
        (rest of file)

    Returns (front_matter_without_delimiters, body_text).
    """
    match = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not match:
        raise RuntimeError("File does not contain valid YAML front matter.")
    front_matter = match.group(1)
    body = match.group(2)
    return front_matter, body


def add_permalink(front_matter: str, slug: str) -> str:
    """
    Given the YAML front matter *without* the surrounding --- lines,
    insert a `permalink:` line in a stable location:

    - Prefer immediately below the first `title:` line.
    - Else, immediately below the first `layout:` line.
    - Else, at the top of the front matter.

    The permalink value is based on the project folder name:

        /portfolio/<slug>/

    If `permalink:` already exists, the original front matter is returned unchanged.
    """
    # If permalink already exists, don't touch it
    if re.search(r"^\s*permalink\s*:", front_matter, re.MULTILINE):
        return front_matter

    permalink_value = f"/portfolio/{slug.strip('/')}/"
    permalink_line_template = "permalink: {value}"

    lines = front_matter.split("\n")
    new_lines = []
    inserted = False

    for idx, line in enumerate(lines):
        stripped = line.lstrip()

        # Prefer inserting after the first title: line
        if not inserted and stripped.startswith("title:"):
            # Preserve indentation
            indent_len = len(line) - len(stripped)
            indent = line[:indent_len]
            permalink_line = f"{indent}{permalink_line_template.format(value=permalink_value)}"
            new_lines.append(line)
            new_lines.append(permalink_line)
            inserted = True
        else:
            new_lines.append(line)

    # If we didn't find a title: line, try inserting after layout:
    if not inserted:
        temp_lines = []
        for idx, line in enumerate(new_lines):
            stripped = line.lstrip()
            if not inserted and stripped.startswith("layout:"):
                indent_len = len(line) - len(stripped)
                indent = line[:indent_len]
                permalink_line = f"{indent}{permalink_line_template.format(value=permalink_value)}"
                temp_lines.append(line)
                temp_lines.append(permalink_line)
                inserted = True
            else:
                temp_lines.append(line)
        new_lines = temp_lines

    # If still not inserted, put it at the top
    if not inserted:
        new_lines = [permalink_line_template.format(value=permalink_value)] + new_lines

    return "\n".join(new_lines)


def process_index_file(index_path: Path) -> None:
    """Read, transform, and overwrite a single index.md file."""
    text = index_path.read_text(encoding="utf-8")

    try:
        front_matter, body = split_front_matter_and_body(text)
    except RuntimeError as e:
        print(f"Skipping {index_path}: {e}")
        return

    # Use the immediate parent folder name as the slug
    slug = index_path.parent.name

    new_front_matter = add_permalink(front_matter, slug)

    if new_front_matter == front_matter:
        print(f"No changes needed: {index_path}")
        return

    new_text = f"---\n{new_front_matter}\n---\n{body}"
    index_path.write_text(new_text, encoding="utf-8")
    print(f"Updated: {index_path}")


def find_projects_root() -> Path:
    """
    Infer repo root from this script location and return portfolio/projects path:
    <repo_root>/portfolio/projects
    """
    script_path = Path(__file__).resolve()
    # .../dev/scripts/add_permalink_field.py -> repo root is two levels up
    repo_root = script_path.parents[2]
    projects_root = repo_root / "portfolio" / "projects"
    if not projects_root.is_dir():
        raise RuntimeError(f"Could not find portfolio/projects at: {projects_root}")
    return projects_root


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Add permalink fields to project index.md front matter using project folder names."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--project",
        help="Process a single project by slug (subfolder under portfolio/projects).",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Process all projects under portfolio/projects.",
    )

    args = parser.parse_args(argv)

    projects_root = find_projects_root()

    if args.project:
        target = projects_root / args.project / "index.md"
        if not target.is_file():
            raise SystemExit(f"index.md not found for project: {target}")
        print(f"Processing single project: {target}")
        try:
            process_index_file(target)
        except Exception as e:
            raise SystemExit(f"ERROR while processing {target}:\n{e}")
    else:
        # --all
        project_dirs = sorted(d for d in projects_root.iterdir() if d.is_dir())
        if not project_dirs:
            raise SystemExit(f"No project directories found under {projects_root}")

        for d in project_dirs:
            index_path = d / "index.md"
            if not index_path.is_file():
                print(f"Skipping {d} (no index.md)")
                continue
            print(f"Processing project: {index_path}")
            try:
                process_index_file(index_path)
            except Exception as e:
                print(f"ERROR while processing {index_path}:\n{e}", file=sys.stderr)


if __name__ == "__main__":
    main()
