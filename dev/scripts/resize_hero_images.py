#!/usr/bin/env python3
"""
Resize hero.png images for project cards to a standardized 4:3 resolution.

For each project, this script:

  1. Locates: <project>/images/hero.png
  2. Resizes the image proportionally so its height is 1920 px.
  3. Center-crops the width from both sides to 2560 px.
  4. Overwrites hero.png with the processed image.

Resulting hero size: 2560 x 1920 (width x height), 4:3 aspect ratio.

Requirements:
  - Python 3.x
  - Pillow (PIL):  pip install pillow

Example usage:

  # Process a single project by slug
  python dev/scripts/resize_hero_images.py --project wireless-mobile-feeder-robot

  # Process all projects under portfolio/projects
  python dev/scripts/resize_hero_images.py --all

  # Process all projects with more verbose logging
  python dev/scripts/resize_hero_images.py --all --verbose
"""

import argparse
from pathlib import Path
import sys

from PIL import Image  # pip install pillow


TARGET_HEIGHT = 1920
TARGET_WIDTH = 2560


def find_projects_root() -> Path:
    """
    Resolve the repo root from this script's location and return portfolio/projects.
    Assumes script lives under dev/scripts/ (same pattern as clone_hero_images.py).
    """
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    projects_root = repo_root / "portfolio" / "projects"
    if not projects_root.is_dir():
        raise RuntimeError(f"Could not find portfolio/projects at: {projects_root}")
    return projects_root


def resize_and_crop_hero(project_dir: Path, verbose: bool = False) -> None:
    """
    For a single project directory, resize and crop images/hero.png to 2560x1920.

    Steps:
      - Load hero.png.
      - Scale proportionally so height == TARGET_HEIGHT (1920 px).
      - Center-crop width to TARGET_WIDTH (2560 px).
      - Overwrite hero.png.
    """
    images_dir = project_dir / "images"
    src = images_dir / "hero.png"

    if not src.exists():
        print(f"❌  Missing hero.png → skipping: {project_dir}")
        return

    try:
        img = Image.open(src)
    except Exception as e:
        print(f"❌  Could not open hero.png in {project_dir}: {e}")
        return

    orig_w, orig_h = img.size
    if verbose:
        print(f"   Original size for {project_dir.name}: {orig_w}x{orig_h}")

    # Compute scale factor to reach target height, but never upscale.
    if orig_h <= 0:
        print(f"❌  Invalid image height (0) in {project_dir}")
        return

    scale = TARGET_HEIGHT / orig_h

    if scale >= 1.0:
        # Image is already <= target height; avoid upscaling.
        # We still may crop horizontally if it's wider than TARGET_WIDTH.
        scaled_w, scaled_h = orig_w, orig_h
        resized = img
        if verbose:
            print(
                f"   Height ≤ {TARGET_HEIGHT}px; skipping height downscale "
                f"(scale={scale:.3f})."
            )
    else:
        scaled_w = int(round(orig_w * scale))
        scaled_h = TARGET_HEIGHT
        resized = img.resize((scaled_w, scaled_h), Image.LANCZOS)
        if verbose:
            print(f"   Resized to: {scaled_w}x{scaled_h} (scale={scale:.3f})")

    # Ensure we have enough width to crop to TARGET_WIDTH
    if scaled_w < TARGET_WIDTH:
        # Fallback: do not crop; just center the image on a TARGET_WIDTH canvas.
        # This should be rare given your original sizes, but keeps things safe.
        if verbose:
            print(
                f"   Width {scaled_w}px < {TARGET_WIDTH}px; "
                f"centering on a wider canvas instead of cropping."
            )

        canvas = Image.new(resized.mode, (TARGET_WIDTH, resized.size[1]))
        offset_x = (TARGET_WIDTH - scaled_w) // 2
        canvas.paste(resized, (offset_x, 0))
        final = canvas
    else:
        # Center-crop width to TARGET_WIDTH.
        left = (scaled_w - TARGET_WIDTH) // 2
        right = left + TARGET_WIDTH
        final = resized.crop((left, 0, right, resized.size[1]))
        if verbose:
            print(
                f"   Cropped horizontally: left={left}, right={right}, "
                f"final size={final.size[0]}x{final.size[1]}"
            )

    # Ensure final height is exactly TARGET_HEIGHT (if we scaled).
    final_w, final_h = final.size
    if final_h > TARGET_HEIGHT:
        # Safe-guard: crop any extra vertical pixels from top/bottom if they exist.
        top = (final_h - TARGET_HEIGHT) // 2
        bottom = top + TARGET_HEIGHT
        final = final.crop((0, top, final_w, bottom))
        final_w, final_h = final.size
        if verbose:
            print(
                f"   Extra vertical pixels cropped: final size={final_w}x{final_h}"
            )

    # Save back to hero.png (overwrite in-place).
    try:
        final.save(src)
        print(f"✅  Resized hero.png in: {project_dir} → {final_w}x{final_h}")
    except Exception as e:
        print(f"❌  Error saving hero.png in {project_dir}: {e}")


def process_single(project_slug: str, verbose: bool = False) -> None:
    projects_root = find_projects_root()
    proj_dir = projects_root / project_slug

    if not proj_dir.is_dir():
        raise SystemExit(f"Project not found: {proj_dir}")

    resize_and_crop_hero(proj_dir, verbose=verbose)


def process_all(verbose: bool = False) -> None:
    projects_root = find_projects_root()
    proj_dirs = sorted(d for d in projects_root.iterdir() if d.is_dir())

    if not proj_dirs:
        raise SystemExit(f"No project folders found under {projects_root}")

    for d in proj_dirs:
        resize_and_crop_hero(d, verbose=verbose)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Resize hero.png images to 2560x1920 (shrink to 1920px height, "
            "then center-crop width to 2560px)."
        )
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--project",
        help="Process only a specific project slug (folder name under portfolio/projects).",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Process all projects under portfolio/projects.",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed information while processing.",
    )

    args = parser.parse_args(argv)

    if args.project:
        process_single(args.project, verbose=args.verbose)
    else:
        process_all(verbose=args.verbose)


if __name__ == "__main__":
    main()
