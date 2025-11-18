#!/usr/bin/env python3
"""
Reflow project sections into left/right column wrappers for project detail pages.

Assumptions:
- Repo structure: <repo_root>/portfolio/projects/<slug>/index.md
- This script lives at:   dev/tools/reflow_project_sections.py
- All required headings are present and consistently named.

Example usage (from repo root, in VS Code terminal):

  # Test on a single project
  python dev/tools/reflow_project_sections.py --project nc4touch-behavioral-apparatus

  # Run on all projects
  python dev/tools/reflow_project_sections.py --all
"""

import argparse
import sys
from pathlib import Path
from typing import List, Tuple, Dict


# Column layout configuration
LEFT_HEADINGS = [
    "Description",
    "Validation & Performance",
    "Materials & Fabrication",
    "Release",
    "References",
]

RIGHT_HEADINGS = [
    "Role & Contributions",
    "Highlights & Key Specs",
    "Deployment & Status",
    "Licensing",
]

REQUIRED_HEADINGS = LEFT_HEADINGS + RIGHT_HEADINGS


def split_front_matter_and_body(lines: List[str]) -> Tuple[List[str], List[str]]:
    """Split lines into (front_matter_lines, body_lines)."""
    if not lines:
        raise RuntimeError("File is empty.")

    if lines[0].strip() != "---":
        raise RuntimeError("Expected YAML front matter starting with '---' on the first line.")

    # Find closing '---'
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            front = lines[: i + 1]
            body = lines[i + 1 :]
            return front, body

    raise RuntimeError("Could not find closing '---' for YAML front matter.")


def find_h2_headings(body_lines: List[str]) -> List[Tuple[int, str]]:
    """
    Return list of (line_index, heading_title) for all '## ' level-2 headings
    in the body.
    """
    headings = []
    for idx, line in enumerate(body_lines):
        stripped = line.lstrip()
        if stripped.startswith("## "):
            title = stripped[3:].strip()
            headings.append((idx, title))
    return headings


def build_sections_by_heading(
    body_lines: List[str], all_h2: List[Tuple[int, str]]
) -> Dict[str, Tuple[int, int, List[str]]]:
    """
    Build a mapping: heading_title -> (start_idx, end_idx, section_lines)

    start_idx is inclusive, end_idx is exclusive (relative to body_lines).
    Sections are delimited by successive H2 headings.
    """
    if not all_h2:
        raise RuntimeError("No '##' level headings found in body content.")

    sections: Dict[str, Tuple[int, int, List[str]]] = {}
    indices = [idx for idx, _ in all_h2] + [len(body_lines)]

    for i, (start_idx, title) in enumerate(all_h2):
        end_idx = indices[i + 1]
        section_lines = body_lines[start_idx:end_idx]
        # Only store sections we care about; others can be ignored
        if title in REQUIRED_HEADINGS:
            sections[title] = (start_idx, end_idx, section_lines)

    return sections


def reflow_body(body_lines: List[str], index_path: Path) -> List[str]:
    """
    Reflow the body content into column wrappers and return the new body_lines.
    """
    all_h2 = find_h2_headings(body_lines)

    # Build sections keyed by heading title
    sections = build_sections_by_heading(body_lines, all_h2)

    # Check all required headings are present
    missing = [h for h in REQUIRED_HEADINGS if h not in sections]
    if missing:
        raise RuntimeError(
            f"Missing expected headings in {index_path}:\n  "
            + ", ".join(missing)
        )

    # Compute spans for all column sections
    column_spans = []
    for h in REQUIRED_HEADINGS:
        start_idx, end_idx, _ = sections[h]
        column_spans.append((start_idx, end_idx))

    earliest_start = min(start for start, _ in column_spans)
    latest_end = max(end for _, end in column_spans)

    before_columns = body_lines[:earliest_start]
    after_columns = body_lines[latest_end:]

    # Drop any trailing H2 sections whose headings are not in our configured lists
    # (e.g. "Included files" blocks imported from CadCrowd).
    # We only do this if the first non-blank line in `after_columns` is an H2.
    if after_columns:
        j = 0
        while j < len(after_columns) and after_columns[j].strip() == "":
            j += 1
        if j < len(after_columns):
            stripped = after_columns[j].lstrip()
            if stripped.startswith("## "):
                title = stripped[3:].strip()
                if title not in REQUIRED_HEADINGS:
                    after_columns = []

    # Build left and right column content in the configured order
    left_lines: List[str] = []
    for h in LEFT_HEADINGS:
        _, _, sec_lines = sections[h]
        left_lines.extend(sec_lines)

    right_lines: List[str] = []
    for h in RIGHT_HEADINGS:
        _, _, sec_lines = sections[h]
        right_lines.extend(sec_lines)

    new_body: List[str] = []
    new_body.extend(before_columns)

    # Ensure a blank line before our wrapper if necessary
    if new_body and new_body[-1].strip() != "":
        new_body.append("\n")

    # Column wrapper with Kramdown markdown="1" so inner Markdown is processed
    new_body.append('<div class="content-groups">\n')
    new_body.append('<div class="content-group content-group-primary" markdown="1">\n\n')
    new_body.extend(left_lines)
    if not new_body[-1].endswith("\n"):
        new_body[-1] = new_body[-1] + "\n"
    new_body.append("\n</div>\n")
    new_body.append('<div class="content-group content-group-secondary" markdown="1">\n\n')
    new_body.extend(right_lines)
    if not new_body[-1].endswith("\n"):
        new_body[-1] = new_body[-1] + "\n"
    new_body.append("\n</div>\n")
    new_body.append("</div>\n")

    # Ensure a blank line before any trailing content we decided to keep
    if after_columns:
        if new_body and new_body[-1].strip() != "":
            new_body.append("\n")
        new_body.extend(after_columns)

    return new_body


def process_index_file(index_path: Path) -> None:
    """Read, transform, and overwrite a single index.md file."""
    text = index_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    front, body = split_front_matter_and_body(lines)

    new_body = reflow_body(body, index_path)

    new_lines = front + new_body

    # Optional: make a simple backup beside the original (overwritten each run)
    # backup_path = index_path.with_suffix(".md.bak")
    # backup_path.write_text(text, encoding="utf-8")

    index_path.write_text("".join(new_lines), encoding="utf-8")


def find_projects_root() -> Path:
    """
    Infer repo root from this script location and return portfolio/projects path:
    <repo_root>/portfolio/projects
    """
    script_path = Path(__file__).resolve()
    # .../dev/tools/reflow_project_sections.py -> repo root is two levels up
    repo_root = script_path.parents[2]
    projects_root = repo_root / "portfolio" / "projects"
    if not projects_root.is_dir():
        raise RuntimeError(f"Could not find portfolio/projects at: {projects_root}")
    return projects_root


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Reflow project index.md files into left/right column wrappers."
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
        project_dirs = sorted(
            d for d in projects_root.iterdir() if d.is_dir()
        )
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
