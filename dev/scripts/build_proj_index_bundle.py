"""
build_proj_index_bundle.py

Collects all project index.md files into a single Markdown document
for easier review and sharing.

For each project index.md, this script:

    - Derives a section heading from either:
        * the `title` field in front matter (if present), OR
        * the parent directory name (slug), if no title is found.
    - The heading text is rendered as ALL CAPS, e.g.:

        # WIRELESS MOBILE FEEDER ROBOT
        # CLOSED LOOP HEAD-FIXATION RIG

It assumes:

    - This script lives in: dev/scripts/
    - The repo root is two levels up from this file.
    - Project index files live under one or more configured directories,
      each containing subdirectories with index.md files, e.g.:

        portfolio/projects/<slug>/index.md

Output:
    dev/scripts/output/project_index_reference.md

Example CLI (from the repo root):

    python dev/scripts/build_proj_index_bundle.py
"""

from pathlib import Path
from typing import List

# ---------------------------------------------------------------------------
# CONFIG: EDIT THESE TO MATCH YOUR REPO STRUCTURE
# ---------------------------------------------------------------------------

# Directories (relative to repo root) to search for project index.md files.
# Each directory is expected to contain project subdirectories with index.md.
PROJECT_INDEX_DIRS: List[str] = [
    "portfolio/projects",
]

# Name of the output Markdown file (inside dev/scripts/output/)
OUTPUT_FILENAME = "project_index_reference.md"


def extract_heading_base(index_path: Path) -> str:
    """
    Try to extract a human-readable heading base from the file's front matter.

    Priority:
      1) `title` field in YAML front matter (if present)
      2) Parent directory name (slug)

    Returns the chosen base (not yet uppercased).
    """
    slug = index_path.parent.name

    try:
        text = index_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = index_path.read_text(errors="replace")

    # Basic front matter detection: starts with '---' and has a second '---'
    if not text.lstrip().startswith("---"):
        return slug

    # Find the front matter block
    lines = text.splitlines()
    if not lines:
        return slug

    if lines[0].strip() != "---":
        return slug

    title_value = None
    for line in lines[1:]:
        if line.strip() == "---":
            break  # end of front matter
        # Very simple "title:" lookup; robust enough for typical usage
        if line.strip().lower().startswith("title:"):
            _, _, value = line.partition(":")
            value = value.strip().strip('"').strip("'")
            if value:
                title_value = value
                break

    return title_value or slug


def main() -> None:
    # Resolve paths based on the script location
    script_path = Path(__file__).resolve()
    scripts_dir = script_path.parent              # dev/scripts
    repo_root = scripts_dir.parent.parent         # repo root

    output_dir = scripts_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / OUTPUT_FILENAME

    # Collect all index.md files under the configured directories
    index_files = []

    for rel_dir in PROJECT_INDEX_DIRS:
        dir_path = repo_root / rel_dir
        if not dir_path.is_dir():
            print(f"[WARN] Skipping missing directory: {rel_dir}")
            continue

        # Only pick index.md files; adjust to rglob if you ever need deeper nesting
        for index_path in dir_path.rglob("index.md"):
            index_files.append(index_path)

    if not index_files:
        print("[INFO] No index.md files found. Check PROJECT_INDEX_DIRS.")
        return

    # Sort for stable, predictable ordering (by parent directory / slug)
    index_files.sort(key=lambda p: (p.parent.as_posix().lower(), p.name.lower()))

    sections = []

    for index_path in index_files:
        heading_base = extract_heading_base(index_path)
        heading_text = heading_base.upper()

        try:
            content = index_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = index_path.read_text(errors="replace")

        relative_display = index_path.relative_to(repo_root)
        print(f"[INFO] Including: {relative_display} → {heading_text}")

        # Compose the section: heading + full file content
        section_md = f"# {heading_text}\n\n{content.rstrip()}\n"
        sections.append(section_md)

    combined_markdown = "\n\n".join(sections) + "\n"
    output_path.write_text(combined_markdown, encoding="utf-8")

    print(f"[OK] Wrote project index bundle to: {output_path}")


if __name__ == "__main__":
    main()
