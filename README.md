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
_config.yml                                 # Jekyll site settings + global configuration
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

- **Page Header Text (`portfolio/index.md`)**  
  – Full-width introductory block at the top of the portfolio list page, displaying page title and lead.
- **Project Card Grid**  
  – Responsive grid of uniformly styled project cards, each showing the project hero image, title, and summary.

**Front Matter Content (`portfolio/index.md`):** 
- `page_title`: Page title (e.g., “Portfolio”).  
- `page_lead`: Short introductory paragraph describing the portfolio list page.
- `projects:`: Array of project slugs determining which projects to show and their order.
- Example front matter:
  ```yaml
  ---
  layout: portfolio-list-page
  page_title: "Portfolio"
  page_lead: "A collection of open-source research instruments, behavioral platforms, and supporting hardware developed across neuroscience and biomedical engineering projects. Each entry links to a detailed project page with full narrative, images, and a 3D model."
  projects:
    - nc4touch-behavioral-apparatus
    - omniroute-maze-system
    - instantaneous-cue-rotation-arena
  ---
  ```

#### Page Header Text

**Component:**  
- Full-width introductory block at the top of the portfolio list page.
- *Rendered as the header region in `_layouts/portfolio-list-page.html`, optionally wrapped with `_includes/section.html` for consistent spacing.*

**Data source:**  
`portfolio/index.md` front matter: `page_title` and `page_lead`.

**Behavior:**  
- Renders as a single, full-width header above the project card grid.  
- Provides context for the portfolio list and orients the user to the content below.

**Constraints / Notes:**  
- Typography, spacing, and alignment are controlled via `assets/css/custom.css` for visual consistency with other site sections.

#### Project Card Grid

**Component:**  
- Responsive grid of uniformly styled project cards.
- *Rendered via `_includes/project-grid.html`, which loops over `projects:` and uses `_includes/project-card.html` for each card inside `_layouts/portfolio-list-page.html`.*

**Data source:**  
Each card pulls content from its project `portfolio/projects/<slug>/index.md` front matter:
- `hero`: The project’s hero image (thumbnail) in a fixed-aspect-ratio area.  
  - The `hero` field is a path relative to the project folder (for example, `images/render_3.png` in `portfolio/projects/<slug>/images/`).
- `title`: The project title displayed below the image.  
- `summary`: A short project summary displayed below the title.

**Behavior:**  
- Generates one card per slug listed in the `projects:` array in `portfolio/index.md`.  
- The order of slugs in this list (each entry is a project slug matching `portfolio/projects/<slug>/`) determines the order of cards in the grid from top-left to bottom-right.
- Each card displays its hero image, title, and summary in a consistent layout.  
- The **entire card is clickable**, linking to `/portfolio/projects/<slug>/`.  
- Subtle hover and active states provide visual feedback (gentle lift or shadow change on hover; slight depress on click).

**Constraints / Notes:**  
- Card dimensions, spacing, typography, and hover states are controlled via `assets/css/custom.css` for a cohesive presentation across all projects.  
- Thumbnail aspect ratio is kept consistent so the grid remains visually balanced.

#### Layout

**Desktop / large screens:**  
- The page stacks elements vertically in this order:
  1. **Page Header Text** (full-width block at the top)
     - `page_title` as the primary heading.
     - `page_lead` as a descriptive paragraph directly below the title.
  2. **Project Card Grid**
     - Cards arranged in multiple columns (e.g., 2–4, depending on viewport width).
     - Cards maintain consistent aspect ratio, spacing, and typography across the grid.

**Mobile / small screens:**  
- All elements stack vertically in this order:
  1. Page Header Text (full-width, with `page_title` and `page_lead` stacked)
  2. Project Card Grid
     - Grid collapses to fewer columns as the viewport narrows, eventually to a single column on very small screens.
     - Vertical spacing and padding are preserved so cards remain readable and visually distinct.

**Layout Notes:**  
- Overall layout, spacing, and responsive breakpoints are handled via `assets/css/custom.css` to keep the portfolio list visually consistent with project detail pages and other site components.

### Project Detail Page Overview

#### Main Elements

- **Image-Viewer (banner):** 
  - Full-width media strip at the top of the project detail page.
  - Displays the primary render and secondary images via a carousel/thumbnail interface.
- **3D-Viewer (window):** 
  - Right-aligned, fixed-width panel positioned below the image-viewer. 
  - Renders the single `.glb` model associated with the project.
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
- *Markup for the banner is defined in `_layouts/project-detail-page.html` as the full-width media strip at the top of the page.*

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
- *The `<model-viewer>` element is rendered in the right column of `_layouts/project-detail-page.html`.*

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

#### Project Detail Content

**Component:**  
- Includes header and text for the project detail page.
- *Injected by `_layouts/project-detail-page.html` as the main Markdown content region (both columns), using the project’s `index.md` front matter and body.*

**Front Matter Content (`portfolio/projects/<slug>/index.md`):**  
- It includes the following fields:
  - `title`: Full project title shown on the card and project detail page. Rendered as the first element in the left column on the project detail page.
  - `summary`: One-line summary used for the project card on the portfolio list page and directly beneath the title on the project detail page.
  - `hero`: Path (relative to the project folder) to the hero image file in that project’s `images/` subfolder.
    - Example: `images/render_1.png`.
    - This image is used as the project card thumbnail on the portfolio list page.
    - The value of `hero` must exactly match the `src` of one of the entries in the `images` array.
    - The hero image does not need to be first in the `images` list; it is selected solely by matching `hero` to an `images.src` value.
  - `model`: Path (relative to the project folder) to the `.glb` file in that project’s `models/` subfolder.
    - Example: `models/nc4touch-behavioral-apparatus.glb`.
    - This file is loaded into the 3D-viewer window on the project detail page.
  - `images`: List of supporting render or photo entries, each with:
    - `src`: Path to the `.png` file, relative to the project folder, typically in that project’s `images/` subfolder.
      - Used by the image-viewer banner at the top of the project detail page.
    - `caption`: Optional description for context and accessibility
      - *Unused for V1*.
  - *(Future fields, if added)* should follow this explicit key-value format; no implicit defaults or fallback behavior.
- Example front matter:
  ```yaml
  ---
  title: "NC4Touch Behavioral Apparatus"
  summary: "An open-source, modular behavioral apparatus for rodent cognitive experiments."
  hero: "images/render_1.png"
  model: "models/nc4touch-behavioral-apparatus.glb"
  images:
    - src: "images/render_1.png"
      caption: "Isometric view of the NC4Touch apparatus."
    - src: "images/photo_1.png"
      caption: "Photograph of the assembled apparatus in the lab."
  ---
  ```

**Markdown Content Sections (`portfolio/projects/<slug>/index.md`):**  
- All narrative content is authored in a single Markdown flow (content body) directly after the front matter. 
- The following is the required authoring order in each project’s `index.md`. This is **authoring order only**, not the final DOM or visual order.
- The project detail layout (`_layouts/project-detail-page.html`) and CSS handle desktop/tablet/mobile behavior, determining final visual placement and column grouping, and **may reorder sections in the DOM** (see Layout below).
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

**Layout Notes:**
- The DOM order matches the mobile stacking order above **not the source Markdown file content body**.  
- The desktop layout is achieved purely via CSS (grid/flex) positioning of these groups.
- The `Included files` section in the source Markdown file content body is **not used in V1** and is ignored by the layout.

## Implementation Status
*A concise overview of what currently exists in the site and how the core pieces are structured.*

### Structure & Content
*Overall site foundation, routing, and project content.*

**Done:**
- Jekyll site scaffolded with `index.md` as the home page (just a stub right now).
- Portfolio section implemented (`/portfolio/`) with project-specific routes under `portfolio/projects/<slug>/`.
- Standardized project folder pattern established (`images/`, `models/`, `index.md`).
- All professional project folders added with full image sets, model files, and `index.md` content.
- Portfolio index configured with project slugs in the intended display order.

**To Do:**
- Populate and style the home page (`index.md` at the site root).

### Layouts & Includes
*Templates responsible for rendering pages and reusable components.*

**Done:**
- Nothing

**To Do:**
- `default.html` functioning as the global page wrapper.
- `portfolio-list-page.html` implemented for the project listing view.
- `project-detail-page.html` implemented for individual project pages.
- Includes added for grid and card rendering (`project-grid.html`, `project-card.html`).
- Section wrapper include (`section.html`) available for consistent spacing and structure.

### Styling & Components
*Global styles and UI behavior.*

**Done:**
- Nothing

**To Do:**
- `custom.css` implemented with core typography, layout, grid, and responsive rules.
- Image viewer banner and thumbnail strip styled and functional.
- Base two-column layout for project detail pages in place with mobile fallback.
