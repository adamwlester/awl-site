"""
build_site_reference_bundle.py

Collects key site implementation files into a single Markdown document
for easier review and sharing.

Each source file is concatenated into the output with a top-level
Markdown header built from the file's basename in ALL CAPS, e.g.:

    # README.MD
    # CUSTOM.CSS
    # PROJECT-DETAIL-PAGE.HTML

The script assumes it lives in:  dev/scripts/
and that the repo root is two levels up from this file.

Output:
    dev/scripts/output/site_implementation_reference.md

Example CLI (from the repo root):

    python dev/scripts/build_site_reference_bundle.py
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIG: EDIT THIS LIST TO CONTROL WHICH FILES ARE INCLUDED
# Paths are relative to the repo root (two levels above this script).
# ---------------------------------------------------------------------------
SOURCE_FILES = [
    "README.md",
    "assets/css/custom.css",
    "_layouts/default.html",
    "_layouts/portfolio-list-page.html",
    "_layouts/project-detail-page.html",
    "_includes/section.html",
    "_includes/project-grid.html",
    "_includes/project-card.html",
]

# Name of the output Markdown file (inside dev/scripts/output/)
OUTPUT_FILENAME = "site_implementation_reference.md"


def main() -> None:
    # Resolve paths based on the script location
    script_path = Path(__file__).resolve()
    scripts_dir = script_path.parent              # dev/scripts
    repo_root = scripts_dir.parent.parent         # repo root

    output_dir = scripts_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / OUTPUT_FILENAME

    sections = []

    for rel_path_str in SOURCE_FILES:
        rel_path = Path(rel_path_str)
        src_path = repo_root / rel_path

        if not src_path.is_file():
            # Emit a simple warning to the terminal but keep going
            print(f"[WARN] Skipping missing file: {rel_path}")
            continue

        header_title = src_path.name.upper()
        try:
            content = src_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # Fallback in case of odd encoding; still try to include the file.
            content = src_path.read_text(errors="replace")

        section_md = f"# {header_title}\n\n{content.rstrip()}\n"
        sections.append(section_md)

    if not sections:
        print("[INFO] No sections were generated. Check SOURCE_FILES paths.")
        return

    combined_markdown = "\n\n".join(sections) + "\n"

    output_path.write_text(combined_markdown, encoding="utf-8")
    print(f"[OK] Wrote combined Markdown to: {output_path}")


if __name__ == "__main__":
    main()
