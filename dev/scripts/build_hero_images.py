#!/usr/bin/env python3
"""
Build normalized hero.png images for project cards.

For each project, this script:

  1. Reads images/render_1.png
  2. Creates / overwrites images/hero.png with:
       - A fixed target width (default: 3200 px)
       - No distortion:
           * If render_1.png is narrower than target width:
               - Pad equally with white on left/right
           * If render_1.png is wider than target width:
               - Crop equally from left/right
           * If equal width: copy as-is

Assumptions:
- Repo structure: <repo_root>/portfolio/projects/<slug>/images/render_1.png
- Script lives at: dev/scripts/build_hero_images.py
- Output: <project>/images/hero.png (always overwritten)

Requirements:
- Pillow (PIL) Python package:
    pip install Pillow

Usage (from repo root):

  # Single project
  python dev/scripts/build_hero_images.py --project nc4gate-automatable-gate-module

  # All projects
  python dev/scripts/build_hero_images.py --all

  # Custom target width
  python dev/scripts/build_hero_images.py --all --target-width 3000
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


DEFAULT_TARGET_WIDTH = 3200  # px


def find_projects_root() -> Path:
    """
    Infer repo root from this script's location.
    Expect: dev/scripts/build_hero_images.py
    Repo root = two levels up.
    """
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    projects_root = repo_root / "portfolio" / "projects"
    if not projects_root.is_dir():
        raise RuntimeError(f"Could not find portfolio/projects at: {projects_root}")
    return projects_root


def normalize_hero_image(src: Path, dst: Path, target_width: int) -> None:
    """
    Open src (render_1.png), create a hero.png at dst with:
      - fixed width target_width
      - identical height
      - centered content
      - white padding for narrow images
      - symmetric crop for wide images
    Always overwrites dst.
    """
    if not src.is_file():
        print(f"❌  Missing source image (render_1.png): {src}")
        return

    try:
        img = Image.open(src)
    except Exception as e:
        print(f"❌  Failed to open {src}: {e}")
        return

    orig_w, orig_h = img.size

    # Normalize to RGB so white background is consistent
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")

    if orig_w == target_width:
        # No resize, just save as hero.png
        img.save(dst)
        print(f"✅  hero.png created (no width change): {dst.parent}")
        return

    # If image is narrower than target → pad with white
    if orig_w < target_width:
        pad_total = target_width - orig_w
        pad_left = pad_total // 2

        # Choose mode and white color
        mode = "RGBA" if img.mode == "RGBA" else "RGB"
        white = (255, 255, 255, 255) if mode == "RGBA" else (255, 255, 255)

        canvas = Image.new(mode, (target_width, orig_h), white)
        canvas.paste(img, (pad_left, 0))
        canvas.save(dst)
        print(
            f"✅  hero.png padded from {orig_w}px → {target_width}px in: {dst.parent}"
        )
        return

    # If image is wider than target → crop equally from left/right
    if orig_w > target_width:
        crop_total = orig_w - target_width
        crop_left = crop_total // 2
        crop_right = crop_left + target_width
        cropped = img.crop((crop_left, 0, crop_right, orig_h))
        cropped.save(dst)
        print(
            f"✅  hero.png cropped from {orig_w}px → {target_width}px in: {dst.parent}"
        )
        return


def process_project(project_dir: Path, target_width: int) -> None:
    """
    For a single project directory, build/overwrite images/hero.png
    from images/render_1.png.
    """
    images_dir = project_dir / "images"
    src = images_dir / "render_1.png"
    dst = images_dir / "hero.png"

    if not images_dir.is_dir():
        print(f"⚠️  No images/ directory in project, skipping: {project_dir}")
        return

    normalize_hero_image(src, dst, target_width)


def process_single(project_slug: str, target_width: int) -> None:
    projects_root = find_projects_root()
    proj_dir = projects_root / project_slug

    if not proj_dir.is_dir():
        raise SystemExit(f"Project not found: {proj_dir}")

    process_project(proj_dir, target_width)


def process_all(target_width: int) -> None:
    projects_root = find_projects_root()
    proj_dirs = sorted(d for d in projects_root.iterdir() if d.is_dir())

    if not proj_dirs:
        raise SystemExit(f"No project folders found under {projects_root}")

    for d in proj_dirs:
        process_project(d, target_width)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Create/overwrite hero.png for each project by copying and "
            "normalizing images/render_1.png to a fixed width."
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
        "--target-width",
        type=int,
        default=DEFAULT_TARGET_WIDTH,
        help=f"Target hero image width in pixels (default: {DEFAULT_TARGET_WIDTH}).",
    )

    args = parser.parse_args(argv)

    if args.project:
        process_single(args.project, target_width=args.target_width)
    else:
        process_all(target_width=args.target_width)


if __name__ == "__main__":
    main()
