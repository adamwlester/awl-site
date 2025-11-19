#!/usr/bin/env python3
"""
Create hero.png for project cards by copying render_1.png.

This script copies:
    <project>/images/render_1.png  →  <project>/images/hero.png

Usage:

  python dev/scripts/clone_hero_images.py --project wireless-mobile-feeder-robot
  python dev/scripts/clone_hero_images.py --all
  python dev/scripts/clone_hero_images.py --all --force
"""

import argparse
import shutil
from pathlib import Path
import sys


def find_projects_root() -> Path:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]
    projects_root = repo_root / "portfolio" / "projects"
    if not projects_root.is_dir():
        raise RuntimeError(f"Could not find portfolio/projects at: {projects_root}")
    return projects_root


def copy_hero_image(project_dir: Path, force: bool = False) -> None:
    images_dir = project_dir / "images"
    src = images_dir / "render_1.png"
    dst = images_dir / "hero.png"

    if not src.exists():
        print(f"❌  Missing render_1.png → skipping: {project_dir}")
        return

    if dst.exists() and not force:
        print(f"↪️   hero.png already exists (use --force to overwrite): {project_dir}")
        return

    try:
        shutil.copy(src, dst)
        print(f"✅  Created hero.png in: {project_dir}")
    except Exception as e:
        print(f"❌  Error copying in {project_dir}: {e}")


def process_single(project_slug: str, force: bool) -> None:
    projects_root = find_projects_root()
    proj_dir = projects_root / project_slug

    if not proj_dir.is_dir():
        raise SystemExit(f"Project not found: {proj_dir}")

    copy_hero_image(proj_dir, force=force)


def process_all(force: bool) -> None:
    projects_root = find_projects_root()
    proj_dirs = sorted(d for d in projects_root.iterdir() if d.is_dir())

    if not proj_dirs:
        raise SystemExit(f"No project folders found under {projects_root}")

    for d in proj_dirs:
        copy_hero_image(d, force=force)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Create hero.png for each project by copying render_1.png."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--project", help="Process only a specific project slug.")
    group.add_argument("--all", action="store_true", help="Process all projects.")  # FIXED LINE

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing hero.png files."
    )

    args = parser.parse_args(argv)

    if args.project:
        process_single(args.project, force=args.force)
    else:
        process_all(force=args.force)


if __name__ == "__main__":
    main()
