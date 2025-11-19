#!/usr/bin/env python3
"""
setup_scaffold.py

One-time helper to scaffold the remaining Jekyll files and directories
for the awl-site repo.

Usage (from the repo root):

    python dev/scripts/setup_scaffold.py

The script is idempotent:
- If a directory or file already exists, it will be skipped.
- Otherwise, it will be created with a minimal stub.
"""

from pathlib import Path


def create_dir(path: Path) -> None:
    """Create a directory (and parents) if it does not exist."""
    if path.exists():
        print(f"[skip] dir exists: {path}")
        return
    path.mkdir(parents=True, exist_ok=True)
    print(f"[ ok ] dir created: {path}")


def create_text_file(path: Path, content: str) -> None:
    """Create a text file with the given content if it does not exist."""
    if path.exists():
        print(f"[skip] file exists: {path}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"[ ok ] file created: {path}")


def create_binary_file(path: Path) -> None:
    """Create an empty binary file if it does not exist (for PNG/PDF stubs)."""
    if path.exists():
        print(f"[skip] file exists: {path}")
        return
    path.write_bytes(b"")
    print(f"[ ok ] binary stub created: {path}")


def main() -> None:
    # Resolve repo root from this script location:
    # dev/scripts/setup_scaffold.py -> dev -> repo root
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[2]

    print(f"Repo root resolved to: {repo_root}")

    # --- Directories to ensure exist ---
    layouts_dir = repo_root / "_layouts"
    includes_dir = repo_root / "_includes"
    assets_dir = repo_root / "assets"
    assets_css_dir = assets_dir / "css"
    assets_images_dir = assets_dir / "images"
    docs_dir = repo_root / "docs"

    dirs_to_create = [
        layouts_dir,
        includes_dir,
        assets_css_dir,
        assets_images_dir,
        docs_dir,
    ]

    for d in dirs_to_create:
        create_dir(d)

    # --- Text file stubs ---

    # _config.yml
    config_path = repo_root / "_config.yml"
    config_content = """url: "https://adamwlester.github.io"
baseurl: "/awl-site"
title: "Adam W. Lester"
description: "Research instruments portfolio."
exclude:
  - .github/
  - .vscode/
  - README.md
  - date-debug.txt
  - verify.txt
markdown: kramdown
"""

    # _layouts/default.html
    default_layout_path = layouts_dir / "default.html"
    default_layout_content = """---
layout: null
---

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{% if page.title %}{{ page.title }} · {{ site.title }}{% else %}{{ site.title }}{% endif %}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{{ site.description | default: '' }}">
    <link rel="stylesheet" href="{{ site.baseurl }}/assets/css/custom.css">
    <!-- TODO: add <model-viewer> script import here for the 3D viewer -->
  </head>
  <body>
    <header class="site-header">
      <nav class="site-nav">
        <div class="site-nav-left">
          <a href="{{ site.baseurl }}/portfolio/">Portfolio</a>
          <a href="{{ site.baseurl }}/docs/CV.pdf">CV</a>
          <a href="{{ site.baseurl }}/docs/Resume.pdf">Resume</a>
        </div>
        <div class="site-nav-right">
          <span class="site-title">{{ site.title }}</span>
        </div>
      </nav>
    </header>

    <main class="site-main">
      {{ content }}
    </main>
  </body>
</html>
"""

    # _layouts/portfolio-list-page.html
    portfolio_layout_path = layouts_dir / "portfolio-list-page.html"
    portfolio_layout_content = """---
layout: default
---

<div class="page-banner">
  <!-- Optional banner image + title/subtitle driven by front matter -->
  {% if page.banner_image %}
    <div class="page-banner-image">
      <img src="{{ site.baseurl }}{{ page.banner_image }}" alt="{{ page.banner_alt | default: page.title }}">
    </div>
  {% endif %}
  <div class="page-banner-text">
    <h1>{{ page.title }}</h1>
    {% if page.banner_subtitle %}
      <p class="page-banner-subtitle">{{ page.banner_subtitle }}</p>
    {% endif %}
    {% if page.page_lead %}
      <p class="page-lead">{{ page.page_lead }}</p>
    {% endif %}
  </div>
</div>

<section class="portfolio-section">
  {% include project-grid.html %}
</section>
"""

    # _layouts/project-detail-page.html
    project_layout_path = layouts_dir / "project-detail-page.html"
    project_layout_content = """---
layout: default
---

<article class="project-detail">
  <header class="project-header">
    <h1>{{ page.title }}</h1>
    {% if page.summary %}
      <p class="project-summary">{{ page.summary }}</p>
    {% endif %}
  </header>

  <section class="project-media">
    <!-- TODO: image-viewer banner + 3D <model-viewer> window -->
    <!-- This will be wired up in a later pass. -->
  </section>

  <section class="project-content">
    {{ content }}
  </section>

  <!-- TODO: inline JS for carousel behavior can live here in V1. -->
</article>
"""

    # _includes/section.html
    section_include_path = includes_dir / "section.html"
    section_include_content = """<section class="section {{ include.class | default: '' }}">
  <div class="section-inner">
    {{ include.content }}
  </div>
</section>
"""

    # _includes/project-grid.html
    project_grid_path = includes_dir / "project-grid.html"
    project_grid_content = """<div class="project-grid">
  {% assign project_slugs = page.projects %}
  {% for slug in project_slugs %}
    {% assign project = site.pages | where: "slug", slug | first %}
    {% if project %}
      {% include project-card.html project=project %}
    {% endif %}
  {% endfor %}
</div>
"""

    # _includes/project-card.html
    project_card_path = includes_dir / "project-card.html"
    project_card_content = """{% assign project = include.project %}

<article class="project-card">
  <a href="{{ project.url | prepend: site.baseurl }}">
    {% if project.hero %}
      <div class="project-card-image">
        <img src="{{ site.baseurl }}/{{ project.hero }}" alt="{{ project.title }}">
      </div>
    {% endif %}
    <div class="project-card-body">
      <h2 class="project-card-title">{{ project.title }}</h2>
      {% if project.summary %}
        <p class="project-card-summary">{{ project.summary }}</p>
      {% endif %}
    </div>
  </a>
</article>
"""

    # assets/css/custom.css
    custom_css_path = assets_css_dir / "custom.css"
    custom_css_content = """/* Minimal V1 base styles for awl-site */

:root {
  --ff-body: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --ff-heading: var(--ff-body);
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--ff-body);
  line-height: 1.5;
  color: #111;
  background-color: #fff;
}

/* Global header */

.site-header {
  border-bottom: 1px solid #ddd;
  padding: 0.75rem 1.5rem;
}

.site-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.site-nav a {
  text-decoration: none;
  color: inherit;
  opacity: 0.85;
}

.site-nav a:hover {
  opacity: 1;
}

.site-title {
  font-weight: 600;
}

/* Layout */

.site-main {
  padding: 2rem 1.5rem 3rem;
  max-width: 960px;
  margin: 0 auto;
}

/* Basic page banner */

.page-banner {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(0, 3fr);
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.page-banner-image img {
  display: block;
  width: 100%;
  height: auto;
}

.page-banner-text h1 {
  margin-top: 0;
}

/* Project card grid (placeholder styles) */

.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5rem;
}

.project-card {
  border: 1px solid #eee;
  border-radius: 0.5rem;
  overflow: hidden;
  background-color: #fff;
}

.project-card a {
  color: inherit;
  text-decoration: none;
  display: block;
  height: 100%;
}

.project-card-image img {
  display: block;
  width: 100%;
  height: auto;
}

.project-card-body {
  padding: 1rem;
}

.project-card-title {
  margin: 0 0 0.5rem;
}

.project-card-summary {
  margin: 0;
  font-size: 0.95rem;
  opacity: 0.9;
}

/* Basic project detail */

.project-detail .project-summary {
  font-size: 1.05rem;
  opacity: 0.9;
}
"""

    text_files = [
        (config_path, config_content),
        (default_layout_path, default_layout_content),
        (portfolio_layout_path, portfolio_layout_content),
        (project_layout_path, project_layout_content),
        (section_include_path, section_include_content),
        (project_grid_path, project_grid_content),
        (project_card_path, project_card_content),
        (custom_css_path, custom_css_content),
    ]

    for path, content in text_files:
        create_text_file(path, content)

    # --- Binary stubs for images and docs (can be replaced later) ---
    home_banner_path = assets_images_dir / "home-banner.png"
    portfolio_banner_path = assets_images_dir / "portfolio-list-banner.png"
    cv_pdf_path = docs_dir / "CV.pdf"
    resume_pdf_path = docs_dir / "Resume.pdf"

    binary_files = [
        home_banner_path,
        portfolio_banner_path,
        cv_pdf_path,
        resume_pdf_path,
    ]

    for path in binary_files:
        create_binary_file(path)

    print("\nScaffold setup complete.")


if __name__ == "__main__":
    main()
