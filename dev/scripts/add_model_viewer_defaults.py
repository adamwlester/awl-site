#!/usr/bin/env python3
"""
Add default <model-viewer> configuration fields to project index.md front matter.

For each project index.md that contains a `model_src:` field, this script ensures
the following keys exist immediately after `model_src:`:

  model_camera_orbit: "auto auto auto"
  model_camera_target: "auto auto auto"
  model_fov: "auto"

If any of these keys already exist in the front matter, they are left unchanged
and not duplicated.

Usage (from repo root):

  # Single project
  python dev/scripts/add_model_viewer_defaults.py --project wireless-mobile-feeder-robot

  # All projects
  python dev/scripts/add_model_viewer_defaults.py --all
"""

import argparse
import re
from pathlib import Path


def find_projects_root() -> Path:
    """
    Locate <repo_root>/portfolio/projects/ based on this script's path:
    dev/scripts/add_model_viewer_defaults.py
    """
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]  # dev/scripts/ → dev/ → repo root
    projects_root = repo_root / "portfolio" / "projects"

    if not projects_root.is_dir():
        raise RuntimeError(f"Could not find projects directory at: {projects_root}")

    return projects_root


def process_index_file(index_path: Path) -> None:
    """
    Load index.md, add model_* defaults in front matter (if missing),
    and write back to file.

    New fields are inserted directly below the `model_src:` line, preserving
    indentation and avoiding duplicates.
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

    # Check if model_src and any of the target keys already exist
    has_model_src = any(re.match(r"\s*model_src:", line) for line in front)
    has_orbit = any(re.match(r"\s*model_camera_orbit:", line) for line in front)
    has_target = any(re.match(r"\s*model_camera_target:", line) for line in front)
    has_fov = any(re.match(r"\s*model_fov:", line) for line in front)

    if not has_model_src:
        print(f"Skipping (no model_src field): {index_path}")
        return

    # Regex to detect the model_src line and capture indentation
    model_src_re = re.compile(r'^(\s*)model_src:\s*".*"$')

    new_front = []
    inserted_for_this_file = False

    for line in front:
        new_front.append(line)

        match = model_src_re.match(line)
        if match and not inserted_for_this_file:
            indent = match.group(1)

            # Insert missing fields directly after model_src line
            if not has_orbit:
                new_front.append(f'{indent}model_camera_orbit: "auto auto auto"')
            if not has_target:
                new_front.append(f'{indent}model_camera_target: "auto auto auto"')
            if not has_fov:
                new_front.append(f'{indent}model_fov: "auto"')

            inserted_for_this_file = True

    # If we found model_src earlier but didn't match the regex (unlikely formatting),
    # just leave the file alone to avoid messing up formatting.
    if has_model_src and not inserted_for_this_file:
        print(f"Warning: model_src present but not updated (unexpected format): {index_path}")
        return

    # Reassemble file
    new_content = "\n".join(new_front + body) + "\n"
    index_path.write_text(new_content, encoding="utf-8")

    print(f"Updated model viewer defaults in: {index_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Add default model viewer fields to project front matter."
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
