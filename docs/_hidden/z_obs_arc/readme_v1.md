# WEBSITE OVERVIEW & ROADMAP
This document defines the site structure, requirements, and specifications.

We will build in stages and are focusing on V1 elements now:
- Full support for **Professional Portfolio**.
- Needs foundations in place for **V2** expansion.

## ID Convention

**Purpose:** Stable, human-readable IDs for consistent referencing in this document.

### Syntax
- **Form:** `<namespace>:<id>`
- **Namespaces:**
  - **page**
    - Description: routable page (has URL and renders content).
  - **nav**
    - Description: non-routable navigation node (menu parent; no URL).
  - **component**
    - Description: UI widgets.
  - **block**
    - Description: layout regions.
  - **string**
    - Description: text inside components and blocks.

## Site Map (rough draft)

```text
/
  ├─ Portfolio                                # primary content area for launch
  │   ├─ Professional                         # section page (index.md) -> section intro + project grid
  │   │   ├─ Project: nc4touch                # /portfolio/professional/nc4touch  -> project page
  │   │   ├─ Project: nc4gate                 # /portfolio/professional/nc4gate   -> project page
  │   │   └─ Project: <slug>                  # /portfolio/professional/<slug>    -> project page
  │   └─ Personal (V2)                        # planned second section; same template/schema as Professional
  └─ Future V2 Top-Level Pages                # placeholders for site expansion
      ├─ Home                                 # landing page (optional later)
      ├─ About                                # bio/overview
      └─ Contact                              # email/links/form
```

## Stack Overview (rough draft)

- **Platform:** Jekyll static site generator (GitHub Pages).
- **Templating:** Liquid templates.
- **Styling:** Custom CSS (no framework).
- **`component:3d-viewer`:** Google `<model-viewer>`.
- **`component:image-viewer`:** Undecided.

## GitHub Repo Structure

```text
Repo: adamwlester-website
Deploy: GitHub Pages (project site)
Public URL now: https://adamwlester.github.io/adamwlester-website/
Future (V2): map to a custom domain without changing content.
Future (V2): add personal portfolio at portfolio/personal/

# repo root == site root (GitHub Pages/Jekyll)
_config.yml
index.md                                    # homepage (or chosen root page)
├── assets/
│   └── css/
│       └── custom.css                      # single stylesheet for colors, spacing, typography, visual treatments
├── _includes/
│   ├── section.html                        # wrapper include for styled sections (optional background/spacing)
│   ├── grid.html                           # include for simple two/three-column content grids
│   └── card.html                           # single project card markup
├── _layouts/
│   └── project.html                        # project page layout that frames nav, media, and Markdown body
└── portfolio/
    └── professional/                       # section container
        ├── index.md                        # section intro; renders above this section’s grid
        └── projects/                       # only this section’s projects live here
            └── <slug>/                     # slug is the folder name (becomes the URL tail)
                ├── index.md                # front matter + full narrative (single source of truth)
                ├── hero.png                # banner/card image referenced in index.md
                ├── images/                 # additional images referenced in Markdown
                │   └── <image>.png
                └── models/                 # optional 3D assets
                    └── <name>.glb          # GLB model file (≤ 100 MB)
```

## Requirements & Specifications

**Note:** I am open to changing or modifying some of these requirements based on practicality and optimal approach.

### `nav:folio` Overview
Description: top-level navigation node for portfolio projects.

#### Scope
- Two pages live under the navigation node `nav:folio`:
  - `page:folio-prof`: professional projects (V1 focus).
  - `page:folio-pers`: personal projects (planned V2).
- Both pages share identical structure and layout, with different project content.
- V1 launches with only `page:folio-prof`, which will be fully specified below.
- This document outlines `page:folio-prof` in full detail.

### `page:folio-prof` Overview
Description: section page introducing and linking to all professional portfolio projects.
Notes:
- Project slug is the folder name under portfolio/professional/projects/ (e.g., "nc4touch-behavioral-apparatus")

#### `block:folio-prof-header`
- Description: renders the page title and intro copy
- Placement: full-width, renders first
- Child components:
  - `string:folio-prof-header-title`
  - `string:folio-prof-header-lead`

#### `string:folio-prof-header-title`
- Description: page title text
- Content source:
  - `portfolio/professional/index.md` front matter field: `header_title`

##### `string:folio-prof-header-lead`
- Description: page intro/lead paragraph text
- Content source:
  - `portfolio/professional/index.md` front matter field: `header_lead`

#### `block:folio-prof-grid`
- Description: container region for the project card grid
- Placement: full-width below header
- Child components:
  - `component:folio-prof-card-grid`

#### `component:folio-prof-card-grid`
- Description: responsive grid of project cards
- Notes: 
  - Uniform card size and aspect ratio
  - Adapts to viewport
- Child components:
  - `component:folio-prof-card-<slug>` (one per project)

#### `component:folio-prof-card-<slug>`
- Description: single project card used by the grid
- Notes:
  - All details in this section apply across all cards in the grid 
- Fields:
  - `hero`: hero image thumbnail (required; always defined)
  - `title`: project title
  - `summary`: one-line summary
  - `link`: URL to project page
- Content source:
  - `portfolio/professional/projects/<slug>/index.md` front matter fields: 
    - `title`
    - `summary`
    - `hero` (image path)
- Link construction:
  - Slug: folder name under portfolio/professional/projects/ (e.g., nc4touch-behavioral-apparatus).
  - URL: [need to define how this is constructed]

### `project page` Overview

#### Main Elements and Organization
- Media `image viewer` Banner: left column (≈ 2/3 width) at the top of the page.
- Media `3d viewer` Window: right column (≈ 1/3 width) aligned with the banner.
- Markdown-Beased Project Text: full-width content immediately below the two media areas.
- Structure and platform: 
  - Note, the `image viewer` and the `3d model viewer` are independent
  - Stay side-by-side on desktop; on smaller screens they stack in the same order.

#### Media `image viewer` Banner
- **Component:** Peeking carousel banner for render and photo images.
- Horizontal snap-scrolling viewport.
- Supports carousel click or swipe with a fixed aspect ratio.
- Supports clickable thumbnail strip.
- Supports peeking neighbors.
- Supports arrows and thumbnail strip.
- Lazy-loads nonvisible slides to protect bandwidth.
- Use native lazy loading where/when/if supported.

#### 3D Model Viewer Integration
- **Component:** Single `3d model viewer` (not part of the `image viewer`).
- **Behavior:** 
  - Autoloads the first 3D model in `models[0]` when the page renders. 
  - Prev/Next arrows swap the active model; each subsequent model loads on demand. 
  - One `<model-viewer>` instance source swaps per navigation; camera resets on change.
- **Header fields required per model:** `src` (path to `.glb` in `/models/`), `caption` (short label).
- **If no 3D models are defined:** the `3d model viewer` is omitted.
- **Constraints:** Each `.glb` must be ≤ 100 MB; build fails if required assets are missing.
- **Error handling:** If a model fails to load (e.g., 404), show a visible error message in the viewer; no silent fallbacks.
- Use native lazy loading where/when/if supported.

#### Markdown Project Text
- Title and subtitle appear immediately below the banner.
- Full Markdown body renders verbatim below (Description → Role → Key Specs → …).

**Contingencies**
- All media use native lazy loading where supported.
- Omit the `3d model viewer` if no models are defined.

**Project Markdown as Source of Truth**
- Entire project narrative stored as a single `project markdown` file.
- Standard Markdown elements must render faithfully: headings, lists, tables, emphasis, inline links, images.

### Project Markdown (`index.md`)

**Includes header and text for the `project page`.**

**Header Content**
The header provides: the project title, a short summary, the hero image, and explicit lists of 3D models *(optional)* and images to load.
It includes the following fields:
- `title`: Full project title shown on the card and `project page`.
- `summary`: One-line summary used beneath the title and in the project grid.
- `hero`: Filename of the banner image located in the project folder.
- `models` *(optional)*: List of 3D model entries, each with:
- `src`: Path to the `.glb` file in the `/models/` folder.
- `caption`: Short descriptive label for the model.
- `images`: List of supporting render or photo entries, each with:
- `src`: Path to the `.png` file in the `/images/` folder.
- `caption`: Optional description for context and accessibility.
- *(Future fields, if added)* should follow this explicit key-value format; no implicit defaults or fallback behavior.

**Core Markdown Content Sections**
- One-line summary (no heading): Single sentence stating system and purpose. First sentence after header
- Description: Full narrative; includes inline Markdown links `[text](url)` to related entries and external sources.
- Role and Contributions: Bulleted ownership across design/build/integration/validation/docs/maintenance.
- Key Specs: Bulleted technical parameters and interfaces.
- Materials and Fabrication: Bulleted materials and processes (frame/panels/electronics/mounts/custom parts).
- Validation and Performance: Bulleted results and quantitative metrics.
- Deployment and Status: Development window, deployments, current status.
- Release: Links to CAD/firmware/ROS/related entries using standard Markdown link syntax.
- Licensing: Explicit hardware/software/docs licenses.
- References: Preprints/papers with Markdown hyperlinks.

### Other Directives

**Visual and Accessibility Standards**
- Consistent banner and card image ratios.
- Alt text for images.c

**Minimal Front Matter**
- Per project: title, short summary for the card, path to hero image, optional `3d model viewer` reference.
- All other content lives in the Markdown.

**URL and Metadata Requirements**
- Stable, human-readable URLs for main pages.
- Stable, human-readable per-project URLs.
- Page-level metadata fields for title and description.
- Social share image per project (uses hero if none specified).

**Consistency and Taxonomy**
- Uniform section order across project pages.

### Current Asset Formats and Storage

**Project Count**
- There will be 5 `personal portfolio` (future) and 11 `professional portfolio` projects to support for launch.

**`image viewer` Images**
- Renders and photos are standardized at 2000 px height (up to 5000 px width).
- All image files are PNG.
- Assume these both as the default for all project image media.

**3D Models**
- Source format is STEP AP214 (`.step`) converted to GLB (using CAD Assistant) with preserved part colors.

**Source of Truth**
- All other project information (descriptions, specs, licensing, links, artifact lists) is already captured in single Markdown files per project and must be rendered verbatim.

**Average File Sizes (per project)**
- total assets ≈ 50–100 MB
- GLB ≈ 10–50 MB total (avg 19.9 MB each), may be up to 75 MB
- images ≈ 20–30 MB total (avg 2.24 MB each)
- Markdown ≈ 0.05 MB
- Expect GLB to dominate and vary significantly by project.

**Viewer**
- Google’s `<model-viewer>`, self-hosted, inline “Load 3D” behavior.

**Targets**
- Keep per-model GLB ≤ 100 MB; serve GLB.

### Text Formatting and Visual Treatment

**Purpose:** Site-level control over Markdown rendering and reusable **visual treatments** with a minimal set of files, keeping content in `index.md` and styling opt-in.
- `/site/assets/css/custom.css` — Defines all typography, spacing, and visual rules so Markdown sections render cleanly and consistently.  
  *Example:* ensures headings in “Role and Contributions” or “Key Specs” share spacing and hierarchy across every project page.
- `/site/_includes/section.html` — Wraps any Markdown block in a styled section with optional background and padding.  
  *Example:* show “Validation and Performance” in a soft `brand-50` background to separate it from “Materials and Fabrication.”
- `/site/_includes/grid.html` — Builds a simple two- or three-column grid for evenly spaced content blocks or links.  
  *Example:* in “Release,” present GitHub, OSF, and Preprint links side-by-side in a 3-column layout.
- `/site/_layouts/project.html` — Provides the project page frame (left navigation pane, `image viewer`, 3D model viewer area, Markdown body below).  
  *Example:* wraps `project.md` so the carousel sits at the top and the Markdown sections scroll in the defined order underneath.

## Other Notes

**General Preferences**
- I would like to do as much of the dev for this project on VS Code. 
- I am open to terminal commands but I prefer scripting and generally working from code files.
- I would like to keep the overall project as centralized as is practical.
- We need to build this so that I can test with only 1-2 complete projects.
  - Can assume these will be complete all assets in place (e.g., `hero`, `models`).

**Future Expansion**
Should factor these into the design to the extent it does not introduce significant complications in implementation.
*All this subject to the level of complexity it adds and delay to get this launched in the time window required*
- Structure must scale into a full multi-page site (Home, Projects, About, Contact) without altering project content or URLs.
- Support separate Instrument and Personal project pages using the same template and schema, each with a dedicated index and stable URLs.
- Project layout should remain reusable as a template within a broader framework or CMS.
- Content format (Markdown + front matter) must stay portable to platforms like Webflow, Hugo, or Framer.
- Allow support for embedded GIFs or short video clips to demonstrate mechanical motion or example behavior within projects.
- Ensure overall design and metadata scheme remain extensible for new sections and site-wide navigation.
- Will consider batch STEP to GLB conversion with 3D viewer.

## Glossary

- **Carousel**: the main horizontal, snap-scrolling viewport.  
- **Slide**: a single image in the carousel.  
- **Peeking carousel**: carousel with partially visible adjacent slides.  
- **Thumbnail strip / filmstrip**: small image row used for quick navigation.  
- **Tile**: generic term for a slide layout (image tile).   
