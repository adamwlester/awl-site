# WEBSITE OVERVIEW & ROADMAP
This document defines the site structure, requirements, and specifications.

We will build in stages and are focusing on V1 elements now:
- Full support for **Portfolio**.
- Minimal support for **Home**.
- Needs foundations in place for **V2** expansion.

## Site Map

```markdown
/
  ├─ Home                                       # site root (/index.md) -> landing page + link to portfolio
  ├─ Portfolio                                  # /portfolio/index.md -> section intro + project grid
  │   ├─ Project: nc4touch-behavioral-apparatus # /portfolio/projects/nc4touch-behavioral-apparatus -> project page
  │   ├─ Project: omniroute-maze-system         # /portfolio/projects/omniroute-maze-system -> project page
  │   └─ Project: <slug>                        # /portfolio/projects/<slug> -> project page
  └─ Future V2 Top-Level Pages                  # placeholders for site expansion
      ├─ About                                  # bio/overview (optional later)
      └─ Contact                                # email/links/form (optional later)
```

## Stack Overview

- **Platform:** Jekyll static site generator (GitHub Pages).
- **Templating:** Liquid templates.
- **Styling:** Custom CSS (no framework).
- **3D-viewer:** Google `<model-viewer>`.
- **image-viewer:** Custom CSS scroll-snap carousel with lightweight vanilla-JS arrows + thumbnails.

## GitHub Repo Structure

```markdown
Repo: adamwlester-website
Deploy: GitHub Pages (project site)
Public URL now: https://adamwlester.github.io/adamwlester-website/
Future (V2): map to a custom domain without changing content.

# repo root == site root (GitHub Pages/Jekyll)
_config.yml
index.md                                    # homepage (**site root**) -> minimal landing + link to /portfolio/
├── assets/
│   └── css/
│       └── custom.css                      # single stylesheet for colors, spacing, typography, visual treatments
├── _includes/
│   ├── section.html                        # generic wrapper include for styled sections (spacing, background)
│   ├── project-grid.html                   # include for the **portfolio project grid** on /portfolio/
│   └── project-card.html                   # include for a single **portfolio project card** (thumbnail + title + summary)
├── _layouts/
│   ├── default.html                        # base site layout (html/head/body shell, global header/footer)
│   ├── portfolio-list-page.html            # layout for the **portfolio list page** (/portfolio/ grid view)
│   └── project-detail-page.html            # layout for each **project detail page** (banner + 3D viewer + content columns)
└── portfolio/                              # portfolio section container
    ├── index.md                            # **portfolio list page** (uses layout: portfolio-list-page; section intro + project grid)
    └── projects/                           # only this section’s projects live here
        └── <slug>/                         # slug is the folder name (becomes the URL tail)
            ├── index.md                    # **project detail page** (uses layout: project-detail-page; front matter + content body; single source of truth)
            ├── images/                     # image assets referenced in front matter + Markdown content
            |    └── <image>.png
            └── models/                     # 3D assets (only one model per project)
                └── <slug>.glb              # GLB model file (≤ 100 MB; referenced by the `model` front matter field)
```

## Key Components & Behavior

**Note:** I am open to changing or modifying some of these requirements based on practicality and optimal approach.

### Portfolio List Page Overview

#### Main Elements

**Page Header Text (`portfolio/index.md`):**  
- Full-width introductory block at the top of the portfolio list page.  
- It displays two fields sourced from the `portfolio/index.md` front matter:  
  - `page_title`: Page title (e.g., “Portfolio”).  
  - `page_lead`: Short introductory paragraph describing the portfolio list page.

**Project Card Grid:**  
- Responsive grid of uniformly styled project cards.  
- Each card displays the following content pulled from its project `portfolio/projects/<slug>/index.md` front matter:  
  - The project’s `hero` image (thumbnail) in a fixed-aspect-ratio area.  
    - The `hero` field is a path relative to the project folder (for example, `images/render_3.png` in `portfolio/projects/<slug>/images/`)
  - The project `title` below the image.  
  - The project `summary` below the title.  
- Each card links directly to its corresponding project detail page.
- The **entire card is clickable**, linking to `/portfolio/projects/<slug>/`.  
- Subtle hover and active states provide visual feedback (gentle lift or shadow change on hover; slight depress on click).

#### Layout

**Card ordering** is defined by the `projects:` list in `portfolio/index.md` front matter:
- The order of slugs in this list (each entry is a project slug matching `portfolio/projects/<slug>/`) determines the order of cards in the grid from top-left to bottom-right.
- Example `projects:` list:
  - nc4touch-behavioral-apparatus
  - omniroute-maze-system
  - instantaneous-cue-rotation-icr-arena

**Consistency:**  
- Card dimensions, spacing, typography, and hover states are controlled via `assets/css/custom.css` for a cohesive presentation across all projects.

**Single-column structure:**  
- The page stacks a full-width header block followed by a full-width card grid in a single vertical flow.

**Responsive grid:**  
- Cards arrange into multiple columns on larger screens.  
- On smaller screens, the grid collapses to fewer columns, eventually to a single column, while preserving card aspect and spacing.

### Project Detail Page Overview

#### Main Elements
- **Image-Viewer (banner):** 
  - Full-width media strip at the top of the project detail page. Displays the primary render and secondary images via a carousel/thumbnail interface.
- **3D-Viewer (window):** 
  - Right-aligned, fixed-width panel positioned below the image-viewer. Renders the single `.glb` model associated with the project.
- **Project Detail Content (`portfolio/projects/<slug>/index.md`):** 
  - The full structured Markdown (front matter + content body) for the project. 
  - All text on the project detail page (both columns) is derived from this file.
- **Independence of components:** 
  - The image-viewer and 3D-viewer are independent in implementation
  - The image-viewer handles all image media, and the 3D-viewer handles the single model.
  - Their behavior and rendering do not affect how the Markdown content is authored.

#### Media Image-Viewer Banner

**Component:** 
- Peeking carousel banner for render and photo images, implemented as a **custom CSS scroll-snap carousel** with lightweight vanilla-JS controls.

**Data source:**  
- The banner loads all images listed in the `images:` field of the project’s front matter (`portfolio/projects/<slug>/index.md`).  
- Images should be shown in the order they are listed in the front matter.  
- Each `images.src` value is a path **relative to the project folder** pointing to a `.png` file in that project’s local `images/` subfolder.  
  - Example front matter entry: `- src: "images/render_1.png"`  
  - Example corresponding filesystem path:  
    `portfolio/projects/nc4touch-behavioral-apparatus/images/render_1.png`

**Behavior:**  
- Horizontal snap-scrolling viewport with fixed aspect-ratio slides and `object-fit: cover`.
- Supports click or swipe navigation on the main carousel.
- Includes a clickable thumbnail strip; thumbnail clicks scroll the main carousel to the selected slide.
- Shows peeking neighbors by sizing slides slightly narrower than the viewport.
- Provides prev/next arrow buttons wired to smooth scroll between slides.
- All non-visible slides use native `loading="lazy"` for images where supported.

**Constraints:**  
  - Renders and photos are standardized at 2000 px height (up to 5000 px width).
  - All image files are PNG.
  - These are required constraints for all images in the `images:` front matter list.

#### 3D Model Viewer Integration

**Component:**  
- Single 3D-viewer window implemented with one `<model-viewer>` element in the right column of the project detail page.

**Data source:**  
- The viewer uses the `model` field in the project’s front matter (`portfolio/projects/<slug>/index.md`).  
- `model` is a path **relative to the project folder** pointing to the `.glb` file in that project’s local `models/` subfolder.  
  - Example front matter: `model: "models/nc4touch-behavioral-apparatus.glb"`  
  - Example corresponding filesystem path:  
    `portfolio/projects/nc4touch-behavioral-apparatus/models/nc4touch-behavioral-apparatus.glb`

**Behavior:**  
- On page load, `<model-viewer>` autoloads the `.glb` file referenced by `model`.  
- Provides basic interactive controls (orbit, zoom, pan) using `<model-viewer>`’s built-in functionality.  
- Initializes the camera to a sensible default view on load.

**Constraints:**  
- Exactly one `.glb` file per project is supported.  
- The `.glb` file must reside under the project’s `models/` subfolder.  
- Recommended maximum file size: ≤ 100 MB.

#### Project Markdown (`portfolio/projects/<slug>/index.md`)

**Includes header and text for the project detail page.**

**Front Matter Content**  
The front matter provides: the project title, a short summary line, the hero image (referencing one of the 'images.src' entries), the single 3D model, and the set of images to load for the project detail page banner.  
It includes the following fields:

- `title`: Full project title shown on the card and project detail page. Rendered as the first element in the left column on the project detail page.
- `summary`: One-line summary used for the project card on the portfolio list page and directly beneath the title on the project detail page.
- `hero`: Path (relative to the project folder) to the hero image file (for example, `images/render_1.png`).
  - This image is used as the project card thumbnail on the portfolio list page.
  - The value of 'hero' must exactly match the 'src' of one of the entries in the 'images:' array.
  - The hero image does not need to be first in the images: list; it is selected solely by matching hero to an images.src value.
- `model`: String path to the `.glb` file in the `/models/` folder.
  - Example: `model: "models/nc4touch-behavioral-apparatus.glb"`
- `images`: List of supporting render or photo entries, each with:
  - `src`: Path to the `.png` file in the `/images/` folder.
  - `caption`: Optional description for context and accessibility (*unused for V1*).
- *(Future fields, if added)* should follow this explicit key-value format; no implicit defaults or fallback behavior.

**Core Markdown Content Sections (authoring order)**  
- All narrative content is authored in a single Markdown flow (content body) directly after the front matter. 
- The following is the required authoring order in each project’s `index.md`. This is **authoring order only**, not the final DOM or visual order.
- The layout engine (desktop/tablet/mobile) reads these sections and determines the final visual placement, column grouping, and **may reorder sections in the DOM** (see Layout below).
- Sections appear in this order in the source Markdown file content body:
  - `Description`
  - `Role & Contributions`
  - `Highlights & Key Specs`
  - `Materials & Fabrication`
  - `Validation & Performance`
  - `Deployment & Status`
  - `Release`
  - `Licensing`
  - `References`
  - `Included files`
- Headings use normal Markdown syntax (`#`, `##`, `###`); their visual sizes, spacing, and hierarchy are controlled globally in `assets/css/custom.css` so the same Markdown renders consistently across all project pages.

#### Layout

**Desktop**
- **Image-viewer** (banner), which spans the full content width at the top of the project detail page.
- Directly beneath the banner, the page uses a **two-column layout**:
  - **Left-column:**
    - `title` (from front matter)
    - `summary` (from front matter)
    - `Description` (from content body)
    - `Validation & Performance` (from content body)
    - `Materials & Fabrication` (from content body)
    - `Release` (from content body)
    - `References` (from content body)
  - **Right-column:**
    - **3D-viewer** window at the top
    - `Role & Contributions` (from content body)
    - `Highlights & Key Specs` (from content body)
    - `Deployment & Status` (from content body)
    - `Licensing` (from content body)

**Mobile / small screens**
- On smaller screens, all elements stack vertically in this order:
  1. Image-viewer (banner)
  2. 3D-viewer (window)
  3. Left-column front matter and content body sections
    - `title` (from front matter)
    - `summary` (from front matter)
    - `Description` (from content body)
    - `Validation & Performance` (from content body)
    - `Materials & Fabrication` (from content body)
    - `Release` (from content body)
    - `References` (from content body)
  4. Right-column content body sections
    - `Role & Contributions` (from content body)
    - `Highlights & Key Specs` (from content body)
    - `Deployment & Status` (from content body)
    - `Licensing` (from content body)

**Notes:**
- The DOM order matches the mobile stacking order above **not the source Markdown file content body**.  
- The desktop layout is achieved purely via CSS (grid/flex) positioning of these groups.
- The `Included files` section in the source Markdown file content body is **not used in V1** and is ignored by the layout.
