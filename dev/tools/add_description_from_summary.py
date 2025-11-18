#!/usr/bin/env python3
"""
Add `description:` to project index.md front matter by duplicating the existing `summary:` field.

Assumptions:
- Repo structure: <repo_root>/portfolio/projects/<slug>/index.md
- This script lives at:   dev/tools/add_description_from_summary.py

Example usage (from repo root):

  # Run on all projects
  python dev/tools/add_description_from_summary.py --all

  # Run on a single project
  python dev/tools/add_description_from_summary.py --project wireless-mobile-feeder-robot
"""

import argparse
import sys
import re
from pathlib import Path
from typing import List, Tuple


def split_front_matter_and_body(lines: List[str]) -> Tuple[List[str], List[str]]:
    """Split lines into (front_matter_lines, body_lines)."""
    if not lines:
        raise RuntimeError("File is empty.")

    if lines[0].strip() != "---":
        raise RuntimeError("Expected YAML front matter starting with '---' on the first line.")

    # Find closing '---'
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            front = lines[: i + 1]  # includes closing ---
            body = lines[i + 1 :]
            return front, body

    raise RuntimeError("Could not find closing '---' for YAML front matter.")


def add_description_to_front_matter(front_lines: List[str]) -> List[str]:
    """
    Given front matter lines (including opening and closing '---'),
    insert a `description:` line immediately above the first `summary:` line,
    copying its value, if `description:` is not already present.
    """
    # Work on the body of the front matter (between the --- lines)
    header = front_lines[0]
    footer = front_lines[-1]
    body_lines = front_lines[1:-1]

    # If description already exists, do nothing
    for line in body_lines:
        if re.match(r"^\s*description\s*:", line):
            return front_lines

    new_body_lines: List[str] = []
    inserted = False

    summary_pattern = re.compile(r"^(\s*)summary\s*:(.*)$")

    for line in body_lines:
        m = summary_pattern.match(line)
        if m and not inserted:
            indent, value = m.groups()
            # Preserve indentation and value (including quotes / spacing)
            description_line = f"{indent}description:{value}"
            new_body_lines.append(description_line)
            inserted = True
        new_body_lines.append(line)

    # If no summary found, just return original
    if not inserted:
        return front_lines

    return [header] + new_body_lines + [footer]


def process_index_file(index_path: Path) -> None:
    """Read, transform, and overwrite a single index.md file."""
    text = index_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    front, body = split_front_matter_and_body(lines)
    new_front = add_description_to_front_matter(front)

    new_lines = new_front + body
    new_text = "".join(new_lines)

    if new_text != text:
        index_path.write_text(new_text, encoding="utf-8")
        print(f"Updated: {index_path}")
    else:
        print(f"No changes needed: {index_path}")


def find_projects_root() -> Path:
    """
    Infer repo root from this script location and return portfolio/projects path:
    <repo_root>/portfolio/projects
    """
    script_path = Path(__file__).resolve()
    # .../dev/tools/add_description_from_summary.py -> repo root is two levels up
    repo_root = script_path.parents[2]
    projects_root = repo_root / "portfolio" / "projects"
    if not projects_root.is_dir():
        raise RuntimeError(f"Could not find portfolio/projects at: {projects_root}")
    return projects_root


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Add description fields to project index.md front matter by copying summary."
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
