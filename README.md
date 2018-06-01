# WEBSITE OVERVIEW & ROADMAP
This document defines the site structure, requirements, and specifications.

We will build in stages and are focusing on V1 elements now:
- Full support for **Portfolio**.
- Needs foundations in place for **V2** expansion.

## Site Map (rough draft)

```yaml
/
  ├─ Portfolio                                    # section page (index.md) -> section intro + project grid
  │   ├─ Project: nc4touch-behavioral-apparatus   # /portfolio/professional/nc4touch-behavioral-apparatus  -> project page
  │   ├─ Project: omniroute-maze-system           # /portfolio/professional/omniroute-maze-system   -> project page
  │   └─ Project: <slug>                          # /portfolio/professional/<slug>    -> project page
  └─ Future V2 Top-Level Pages                    # placeholders for site expansion
      ├─ Home                                     # landing page (optional later)
      ├─ About                                    # bio/overview (optional later)
      └─ Contact                                  # email/links/form (optional later)
```

## Stack Overview (rough draft)

- **Platform:** Jekyll static site generator (GitHub Pages).
- **Templating:** Liquid templates.
- **Styling:** Custom CSS (no framework).
- **3d-viewer:** Google `<model-viewer>`.
- **image-viewer:** Custom CSS scroll-snap carousel with lightweight vanilla-JS arrows + thumbnails.

## GitHub Repo Structure (rough draft)

```yaml
Repo: adamwlester-site
Deploy: GitHub Pages (project site)
Public URL now: https://github.com/adamwlester/adamwlester-site/
Future (V2): map to a custom domain without changing content.

# repo root == site root (GitHub Pages/Jekyll)
_config.yml
index.md                                    # homepage (**site root** or chosen root page)
├── assets/
│   └── css/
│       └── custom.css                      # single stylesheet for colors, spacing, typography, visual treatments
├── _includes/
│   ├── section.html                        # wrapper include for styled sections (optional background/spacing)
│   ├── grid.html                           # include for simple two/three-column content grids
│   └── card.html                           # markup for a single **project card** in the grid
├── _layouts/
│   └── project.html                        # layout used by each **project detail page**
└── portfolio/                              # section container
    ├── index.md                            # **project list page** (section intro + project grid)
    └── projects/                           # only this section’s projects live here
        └── <slug>/                         # slug is the folder name (becomes the URL tail)
            ├── index.md                    # **project detail page** (front matter + full narrative; single source of truth)
            ├── hero.png                    # banner/card image referenced in the project detail page
            ├── images/                     # additional images referenced in Markdown
            │   └── <image>.png
            └── models/                     # 3D assets (only one model per project)
                └── <slug>.glb              # GLB model file (≤ 100 MB)

```

## Key Components & Behavior

**Note:** I am open to changing or modifying some of these requirements based on practicality and optimal approach.

### Project Detail Page Overview

#### Main Elements
- **Image Viewer (banner):** Full-width media strip at the top of the project detail page. Displays the primary render and secondary images via a carousel/thumbnail interface.
- **3D Viewer (window):** Right-aligned, fixed-width panel positioned below the image viewer. Renders the single `.glb` model associated with the project.
- **Project Detail Content (`portfolio/projects/<slug>/index.md`):** The full narrative and structured Markdown for the project. All text on the project detail page (both columns) is derived from this file.
- **Independence of components:** The image viewer and 3D viewer are independent in implementation; the image viewer handles all image media, and the 3D viewer handles the single model. Their behavior and rendering do not affect how the Markdown content is authored.

#### Layout
- The image viewer banner spans the full content width at the top of the project detail page.
- Directly beneath the banner, the page uses a **two-column layout** on desktop:
  - A **right column** that contains the 3D viewer, followed by sidebar-style text blocks derived from the project detail content.
  - A **wider left column** that contains the remaining project detail content and flows alongside the 3D viewer until its bottom.
- On smaller screens, the layout **stacks vertically** in this order:
  1. Image viewer (banner)
  2. 3D viewer (window)
  3. All project detail content in a single column.

#### Media Image-Viewer Banner
- **Component:** Peeking carousel banner for render and photo images, implemented as a **custom CSS scroll-snap carousel** with lightweight vanilla-JS controls.
- Horizontal snap-scrolling viewport with fixed aspect-ratio slides and `object-fit: cover`.
- Supports click or swipe navigation on the main carousel.
- Includes a clickable thumbnail strip; thumbnail clicks scroll the main carousel to the selected slide.
- Shows peeking neighbors by sizing slides slightly narrower than the viewport.
- Provides prev/next arrow buttons wired to smooth scroll between slides.
- All non-hero slides use native `loading="lazy"` for images; nonvisible slides are lazy-loaded where supported.
- **Images**:
  - Renders and photos are standardized at 2000 px height (up to 5000 px width).
  - All image files are PNG.
  - Assume these both as the default for all project image media. 

#### 3D Model Viewer Integration
- **Component:** Single 3D viewer window, implemented with one `<model-viewer>` element in the right column of the project detail page.
- **Behavior:**
  - On page load, the 3D viewer autoloads the single `.glb` file defined in the front matter `model` field.
  - The `model` field must point to the project’s model file in the `models/` folder, e.g. `model: "models/<slug>.glb"`.
  - The viewer presents basic interactive controls (orbit, zoom, pan) using `<model-viewer>`’s built-in functionality; the camera is initialized to a sensible default view on load.
- **Front matter requirement:**
  - Each project detail page must define:
    - `model`: string path to the `.glb` file in `models/` (e.g. `model: "models/nc4touch-behavioral-apparatus.glb"`).
- **Constraints:**
  - Exactly one `.glb` file per project; it must reside under `models/` and be ≤ 100 MB.

#### Project Markdown (`portfolio/projects/<slug>/index.md`)

**Includes header and text for the project detail page.**

**Header Content**  
The header provides: the project title, a short card summary line, the hero image, the single 3D model, and the set of images to load.  
It includes the following fields:

- `title`: Full project title shown on the card and project detail page. Rendered as the first element in the left column on the project detail page.
- `card_summary`: One-line card summary used on the project list page and directly beneath the title on the project detail page.
- `hero`: Filename of the thumbnail image used for the project card on the project list page. Not used on the project detail page.
- `model`: String path to the `.glb` file in the `/models/` folder.  
  - Example: `model: "models/nc4touch-behavioral-apparatus.glb"`
- `images`: List of supporting render or photo entries, each with:
  - `src`: Path to the `.png` file in the `/images/` folder.
  - `caption`: Optional description for context and accessibility.
- *(Future fields, if added)* should follow this explicit key-value format; no implicit defaults or fallback behavior.

**Core Markdown Content Sections (authoring order)**  
All narrative content is authored in a single Markdown flow directly after the front matter. Sections appear in this order in the source file:

1. Lead sentence (no heading): Single sentence stating system and purpose. First sentence after the header.
2. Description
3. Role and Contributions
4. Highlights & Key Specs
5. Materials and Fabrication
6. Validation and Performance
7. Deployment and Status
8. Licensing
9. Release
10. References

Headings use normal Markdown syntax (`#`, `##`, `###`); their visual sizes, spacing, and hierarchy are controlled globally in `assets/css/custom.css` so the same Markdown renders consistently across all project pages.

**Layout Mapping (desktop)**  

On the project detail page, these authored sections are rendered into two columns under the media band, in this order:

- **Left-column narrative (wide):**
  - `title` from the header
  - `card_summary` from the header
  - lead sentence (first sentence after the header)
  - Description
  - Validation and Performance
  - Materials and Fabrication
  - Release
  - References

- **Right-column summary blocks (sidebar below 3D viewer):**
  - Role and Contributions
  - Highlights & Key Specs
  - Deployment and Status
  - Licensing

The 3D viewer sits at the top of the right column and loads the model defined by `model`. The summary blocks listed above render **below** the 3D viewer, using the content from their corresponding Markdown sections.

On smaller screens, all sections stack into a **single column** in the same logical order as authored.

### Project List Page Overview

#### Main Elements
- **Page Header (`portfolio/index.md`):**  
  Full-width introductory block at the top of the portfolio section page.  
  It displays two fields sourced from the section’s `index.md` front matter:  
  - `header_title`: Page title (e.g., “Portfolio”).  
  - `header_lead`: Short introductory paragraph describing the portfolio section.

- **Project Card Grid:**  
  Responsive grid of uniformly styled project cards.  
  Each card displays:  
  - The project’s `hero` image (thumbnail) in a fixed-aspect-ratio area.  
  - The project `title`.  
  - The project `card_summary` (one-line summary).  
  Each card links directly to its corresponding project detail page.

#### Content Source & Ordering
- **Header content** comes exclusively from `portfolio/index.md` front matter:  
  - `header_title`  
  - `header_lead`

- **Project ordering** is defined by the `projects:` list in `portfolio/index.md`; cards render in that order, from top-left to bottom-right in the grid.
  - Example `projects:` list:
  ```yaml
  projects:
    - nc4touch-behavioral-apparatus
    - omniroute-maze-system
    - instantaneous-cue-rotation-icr-arena
    # ...in desired display order

- Each listed slug corresponds to a project folder located at:

```yaml
portfolio/projects/<slug>/index.md
```

- For each slug in `projects:`, the project card pulls these fields from its project `index.md`:  
  - `title`  
  - `card_summary`  
  - `hero`

#### Card Composition
- **Hero image:**  
  Rendered in a fixed-aspect-ratio top region of the card.  
  The `hero` field must reference a valid image file located in the project’s folder.

- **Card text:**  
  - `title` displayed beneath the hero image.  
  - `card_summary` displayed beneath the title in a consistent style across all cards.

- **Interactivity:**  
  - The **entire card is clickable**, linking to `/portfolio/projects/<slug>/`.  
  - Subtle hover and active states provide visual feedback (gentle lift or shadow change on hover; slight depress on click).

#### Layout
- **Single-column structure:**  
  The page stacks a full-width header block followed by a full-width card grid.

- **Responsive grid:**  
  - Cards arrange into multiple columns on larger screens.  
  - On smaller screens, the grid collapses to fewer columns, eventually to a single column, while preserving card aspect and spacing.

- **Consistency:**  
  Card dimensions, spacing, typography, and hover states are controlled via `assets/css/custom.css` for a cohesive presentation across all projects.

#### Behavior Summary
- The project list page is declarative and fully data-driven.  
- Ordering, visibility, and card content are entirely defined by:  
  - `portfolio/index.md` → header + ordered `projects:` list  
  - `portfolio/projects/<slug>/index.md` → project card fields (`title`, `card_summary`, `hero`)

