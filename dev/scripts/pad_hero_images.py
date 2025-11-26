#!/usr/bin/env python3
"""
Pad existing hero.png images with fixed white margins.

For each project, this script:

  1. Reads images/hero.png
  2. Adds fixed padding on all sides (default: 100 px)
  3. Overwrites hero.png with the padded version

Assumptions:
- Repo structure: <repo_root>/portfolio/projects/<slug>/images/hero.png
- Script lives at: dev/scripts/pad_hero_images.py
- Output overwrites <project>/images/hero.png

Requirements:
- Pillow (PIL) Python package:
    pip install Pillow

Usage (from repo root):

  # Single project
  python dev/scripts/pad_hero_images.py --project instantaneous-cue-rotation-arena

  # All projects
  python dev/scripts/pad_hero_images.py --all

  # Custom padding
  python dev/scripts/pad_hero_images.py --all --padding 150
"""

import argparse
from pathlib import Path
import sys

try:
    from PIL import Image
except ImportError:
    raise SystemExit(
        "This script requires the Pillow library.\n\n"
        "Install it with:\n"
        "  pip install Pillow\n"
    )

# ---------------------------------------------------------
# Hardcoded defaults (you can adjust these)
# ---------------------------------------------------------
DEFAULT_PADDING = 250  # px on each side


def find_projects_root() -> Path:
    """
    Infer repo root from this script's location.
    Expect: dev/scripts/pad_hero_images.py
    Repo root = two levels up.
    """
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    projects_root = repo_root / "portfolio" / "projects"
    if not projects_root.is_dir():
        raise RuntimeError(f"Could not find portfolio/projects at: {projects_root}")
    return projects_root


def pad_hero_image(src: Path, padding: int) -> None:
    """
    Open hero.png at `src`, add padding around all sides,
    and overwrite hero.png.
    """
    if not src.is_file():
        print(f"❌  Missing hero.png: {src}")
        return

    try:
        img = Image.open(src)
    except Exception as e:
        print(f"❌  Failed to open {src}: {e}")
        return

    orig_w, orig_h = img.size

    # Normalize to RGB/RGBA so white background is consistent
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")

    # Determine output dimensions
    new_w = orig_w + 2 * padding
    new_h = orig_h + 2 * padding

    # Choose canvas mode + white color
    mode = "RGBA" if img.mode == "RGBA" else "RGB"
    white = (255, 255, 255, 255) if mode == "RGBA" else (255, 255, 255)

    canvas = Image.new(mode, (new_w, new_h), white)
    canvas.paste(img, (padding, padding))

    try:
        canvas.save(src)
        print(f"✅  hero.png padded ({padding}px each side) in: {src.parent}")
    except Exception as e:
        print(f"❌  Failed to save padded hero.png to {src}: {e}")


def process_project(project_dir: Path, padding: int) -> None:
    """
    Process hero.png inside a project folder.
    """
    images_dir = project_dir / "images"
    src = images_dir / "hero.png"

    if not images_dir.is_dir():
        print(f"⚠️  No images/ directory in project, skipping: {project_dir}")
        return

    pad_hero_image(src, padding)


def process_single(project_slug: str, padding: int) -> None:
    projects_root = find_projects_root()
    proj_dir = projects_root / project_slug

    if not proj_dir.is_dir():
        raise SystemExit(f"Project not found: {proj_dir}")

    process_project(proj_dir, padding)


def process_all(padding: int) -> None:
    projects_root = find_projects_root()
    proj_dirs = sorted(d for d in projects_root.iterdir() if d.is_dir())

    if not proj_dirs:
        raise SystemExit(f"No project folders found under {projects_root}")

    for d in proj_dirs:
        process_project(d, padding)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Pad hero.png for each project by adding fixed white margins on all sides."
        )
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--project",
        help="Process only a specific project slug (folder under portfolio/projects).",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Process all projects under portfolio/projects.",
    )

    parser.add_argument(
        "--padding",
        type=int,
        default=DEFAULT_PADDING,
        help=f"Padding (in px) added to each side (default: {DEFAULT_PADDING}).",
    )

    args = parser.parse_args(argv)

    if args.project:
        process_single(args.project, padding=args.padding)
    else:
        process_all(padding=args.padding)


if __name__ == "__main__":
    main()
