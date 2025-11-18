#!/usr/bin/env python3
"""
Normalize all image captions in project index.md files to sentence case:
- Only the first character is capitalized.
- All other characters remain unchanged.

Usage (from repo root):

  # Single project
  python dev/tools/fix_caption_case.py --project wireless-mobile-feeder-robot

  # All projects
  python dev/tools/fix_caption_case.py --all
"""

import argparse
import re
from pathlib import Path


def find_projects_root() -> Path:
    """
    Locate <repo_root>/portfolio/projects/ based on this script's path:
    dev/tools/fix_caption_case.py
    """
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]        # dev/tools/ → dev/ → repo root
    projects_root = repo_root / "portfolio" / "projects"

    if not projects_root.is_dir():
        raise RuntimeError(f"Could not find projects directory at: {projects_root}")

    return projects_root


def fix_caption_sentence_case(caption: str) -> str:
    """
    Convert caption to sentence case, preserving everything except the first letter.
    Example:
        "three-quarter view ..." → "Three-quarter view ..."
    """
    if not caption:
        return caption
    return caption[0].upper() + caption[1:]


def process_index_file(index_path: Path) -> None:
    """
    Load index.md, modify image captions in front matter, and write back to file.
    Only caption fields in the YAML front matter are modified.
    """
    text = index_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=False)

    if not lines or lines[0].strip() != "---":
        print(f"Skipping (missing front matter): {index_path}")
        return

    # Find closing front matter marker
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break

    if end is None:
        print(f"Skipping (unterminated front matter): {index_path}")
        return

    front = lines[: end + 1]
    body = lines[end + 1 :]

    # Match:   caption: "some text here"
    caption_re = re.compile(r'(\s*caption:\s*")([^"]*)(")')

    new_front = []
    for line in front:
        match = caption_re.match(line)
        if match:
            indent, inner_text, closing = match.groups()
            updated = fix_caption_sentence_case(inner_text)
            new_front.append(f"{indent}{updated}{closing}")
        else:
            new_front.append(line)

    # Reassemble file
    new_content = "\n".join(new_front + body) + "\n"
    index_path.write_text(new_content, encoding="utf-8")

    print(f"Updated captions in: {index_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Fix image captions in project front matter to sentence case."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--project", help="Process a single project by slug")
    group.add_argument("--all", action="store_true", help="Process all projects")

    args = parser.parse_args()

    projects_root = find_projects_root()

    if args.project:
        index_path = projects_root / args.project / "index.md"
        if not index_path.is_file():
            raise SystemExit(f"index.md not found for project: {args.project}")
        process_index_file(index_path)
    else:
        # --all
        for proj_dir in sorted(projects_root.iterdir()):
            index_path = proj_dir / "index.md"
            if index_path.is_file():
                process_index_file(index_path)
            else:
                print(f"Skipping (no index.md): {proj_dir}")


if __name__ == "__main__":
    main()
