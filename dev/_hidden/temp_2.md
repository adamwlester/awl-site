# PROMPT
The site repo is fully scaffolded. All other site content has been added.

Here’s the current status:

Files that are complete:
- _assets/css/custom.css
- _config.yml
- _layouts/default.html
- _layouts/portfolio-list-page.html
- _layouts/project-detail-page.html
- _includes/section.html

Files that still need content:
- _includes/project-card.html
- _includes/project-grid.html

For this step, focus only on:
- _includes/project-card.html
- _includes/project-grid.html

I am working with another GPT to generate these remaining files, but I want you to act as a careful second check.

I am sharing the relevant files from the site repo:
1. README.md
2. assets\css\custom.css
3. _layouts\default.html
4. _layouts\portfolio-list-page.html
5. _layouts\project-detail-page.html


The file contents will be pasted below this prompt (separated by `#` markdown headings).

First, thoroughly review and cross-reference the README and the current CSS, as well as the provided layout files. Build and store a clear mental model of:
- Overall site architecture and routing
- Layout responsibilities and inheritance
- How each remaining file is expected to behave and interact with the others
- How the CSS constrains and expects the HTML structure

Then, write out a concise but complete summary of your understanding of the site: how it works, how the main layouts and includes should fit together, and how the CSS ties into that structure.

Do not generate any of the remaining files yet. After your summary, I will share what the other GPT generated for review.

# README
This document defines the site structure, requirements, and specifications.

We will build in stages and are focusing on V1 elements now:
- Full support for **Portfolio**.
- Minimal support for **Home**.
- Needs foundations in place for **V2** expansion.

## SITE MAP

```markdown
/
  ├─ Home                                       # site root (/index.md) -> landing page + link to portfolio
  ├─ Portfolio                                  # /portfolio/index.md -> section intro + project grid
  │   ├─ Project: nc4touch-behavioral-apparatus # /portfolio/projects/nc4touch-behavioral-apparatus -> project page
  │   ├─ Project: omniroute-maze-system         # /portfolio/projects/omniroute-maze-system -> project page
  │   └─ Project: <slug>                        # /portfolio/projects/<slug> -> project page
  └─ Future V2 Top-Level Pages                  # placeholders for site expansion
      ├─ About                                  # bio/overview
      └─ Contact                                # email/links/form
```

## STACK OVERVIEW

- **Platform:** Jekyll static site generator (GitHub Pages).
- **Templating:** Liquid templates.
- **Styling:** Custom CSS (no framework) with a single main stylesheet.
- **3D-viewer (window):** Google `<model-viewer>`.
- **image-viewer (media carousel):** Custom CSS scroll-snap carousel with lightweight vanilla-JS arrows + thumbnails.

> **URL note:**  
> In production, public URLs are constructed as  
> `{{ site.baseurl }}` + the paths shown in the Site Map above  
> (for example:  
> `{{ site.baseurl }}/portfolio/` and  
> `{{ site.baseurl }}/portfolio/projects/<slug>/`).  
>  
> Internal links in templates should always prepend `{{ site.baseurl }}`,  
> as described in the Jekyll Config Conventions section.

## GITHUB REPO STRUCTURE

```markdown
Repo: awl-site
Deploy: GitHub Pages (project site)
Public URL now: https://adamwlester.github.io/awl-site/
Future (V2): map to a custom domain without changing content.

# repo root == site root (GitHub Pages/Jekyll)
_config.yml                                 # Jekyll site settings + global configuration
index.md                                    # homepage (**site root**) -> minimal landing + link to {{ site.baseurl }}/portfolio/
├── assets/
│   ├── css/
│   │   └── custom.css                      # single stylesheet for colors, spacing, typography, global header, banner, layout
│   └── images/
│       ├── home-banner.png                 # used by homepage front matter: banner_image: /assets/images/home-banner.png
│       └── portfolio-list-banner.png       # used by portfolio/index.md front matter: banner_image: /assets/images/portfolio-list-banner.png
├── docs/
│   ├── CV.pdf                              # full academic CV (served directly via GitHub Pages)
│   └── Resume.pdf                          # short professional resume (also served directly)
├── _includes/
│   ├── section.html                        # generic wrapper include for styled sections
│   ├── project-grid.html                   # include for the **portfolio project grid** on the portfolio list page ({{ site.baseurl }}/portfolio/)
│   └── project-card.html                   # include for a single **portfolio project card**
├── _layouts/
│   ├── default.html                        # base site layout (html/head/body shell + global header)
│   ├── portfolio-list-page.html            # layout for the **portfolio list page** ({{ site.baseurl }}/portfolio/)
│   └── project-detail-page.html            # layout for each **project detail page**
└── portfolio/                              # portfolio section container
    ├── index.md                            # **portfolio list page** (uses layout: portfolio-list-page; section intro + project grid)
    └── projects/                           # only this section’s projects live here
        └── <slug>/                         # slug is the folder name (becomes the URL tail)
            ├── index.md                    # **project detail page** (uses layout: project-detail-page; front matter + content body; single source of truth)
            ├── images/                     # image assets referenced in front matter + Markdown content
            │    └── <image>.png            # PNG image files (renders, photos; referenced by the `images` and `hero` front matter fields)
            └── models/                     # 3D assets (only one model per project)
                └── <slug>.glb              # GLB model file (≤ 50 MB; referenced by the `model_src` front matter field)
```
### Jekyll Config Conventions

- `_config.yml` is the single source of truth for site-level settings:
  - `url: "https://adamwlester.github.io"`
  - `baseurl: "/awl-site"` (matches the repo name and GitHub Pages path).
  - `title: "Adam W. Lester"`
  - `description`: Short metadata description.
    - Used as the global fallback for `<meta name="description">` when a page does not define its own `description` in front matter.
  - `exclude`: Files and folders that **must** not be processed or published by Jekyll (e.g., `.github/`, `.vscode/`, `README.md`, `dev/`; see `_config.yml` for the current list).
- All templates **must** use `{{ site.baseurl }}` when building internal links so they resolve correctly on GitHub Pages:
  - Example: `href="{{ site.baseurl }}/portfolio/"`
  - Example: `href="{{ site.baseurl }}/docs/CV.pdf"`
- Front matter paths for images and models remain repo-relative strings (e.g., `images/render_1.png`, `/assets/images/home-banner.png`).
  - Layouts prepend `{{ site.baseurl }}` when generating final URLs.

## Layout & CSS Responsibilities (Quick Map)

- `_layouts/default.html`  
  - Global page shell: wraps every page, renders the site-wide header and shared banner region (for pages using a banner).
- `_layouts/portfolio-list-page.html`  
  - Specializes the layout for the portfolio list page: page lead/intro text and the project card grid.
- `_layouts/project-detail-page.html`  
  - Project detail layout: image-viewer media carousel, 3D-viewer window, and two-column narrative content.
- `_includes/section.html`  
  - Generic section wrapper for consistent spacing and max-width across different page sections.
- `_includes/project-grid.html`  
  - Renders the portfolio grid by looping over the configured list of projects.
- `_includes/project-card.html`  
  - Renders a single project card (hero image, title, summary, link to the detail page).
- `assets/css/custom.css`  
  - Single stylesheet that defines base typography, colors, layout, header/banner styling, and responsive behavior across pages.

### Layout Inheritance & Relationships

- `_layouts/default.html` is the **base layout**: HTML shell, global CSS, header, and shared banner region.
- `_layouts/portfolio-list-page.html` and `_layouts/project-detail-page.html` set `layout: default` and only define page-specific content.
- Layout usage:
  - `index.md` → `layout: default`
  - `portfolio/index.md` → `layout: portfolio-list-page`
  - `portfolio/projects/<slug>/index.md` → `layout: project-detail-page`
- This keeps the header/banner in one place and avoids duplicating the outer shell.

## CSS STYLE BASELINES (GLOBAL DESIGN CONVENTIONS)

This section defines the implicit global style conventions used across `assets/css/custom.css`. These choices are not restated elsewhere in the README but serve as **ground truth** for all visual styling.

### Typography

**Font family:**  
- Single **system sans-serif stack** used for all text (body + headings).  
- No external web fonts or font-loading behavior.

**Headings:**  
- Standard Markdown headings (`#`, `##`, `###`) map to a simple, consistent hierarchy (size/weight) controlled entirely in `assets/css/custom.css`.  
- No per-page or per-component overrides.

### Spacing & Layout Scale

**Spacing scale:**  
- A small global spacing system (`--space-1` … `--space-5`) defines all padding, gaps, and vertical rhythm.  
- Section spacing (`_includes/section.html`) uses this same scale.

**Max content width:**  
- Primary content areas use a standardized max-width container of **960px** (`--max-width-content`) for consistent readable line-length.

**Border radius:**  
- A minimal set of radii tokens (`--radius-sm`, `--radius-md`) applied consistently across cards, media containers, and interactive elements.

### Color & Surfaces

**Neutral palette:**  
- Background: white  
- Text: near-black  
- Surfaces (e.g., cards, media blocks): white with subtle borders/shadows  

**Shadows:**  
- Very light default shadow on cards and media containers.  
- Slightly stronger shadow + gentle lift on hover (portfolio cards, interactive tiles).  

**Links:**  
- Subtle underline-on-hover behavior; no brand color palette.

### Responsive Behavior

**Breakpoints:**  
- Major layout transitions occur at **768px** (small → medium) and **1024px** (medium → large).  
- Additional layout tweaks apply at **480px and below** for very small screens.

**Desktop vs mobile ordering:**  
- **DOM order = mobile visual order** across all pages.  
- Desktop layout uses CSS grid/flex positioning without content reordering.

### Banner & Media Conventions

**Shared banner:**  
- Used on the **Home** page and **Portfolio list** page.  
- Fixed-height panoramic band (`--page-banner-height`).  
- Background images are centered and cover-filled with a soft overlay for text readability.

**Image-viewer (media carousel):**  
- Used on **Project detail** pages.  
- Each slide uses a **fixed aspect ratio** (default `16:9`) with `object-fit: cover` for consistent height.  
- Carousel uses CSS scroll-snap with lightweight JS only for arrow/thumbnail control.

**3D-viewer (window):**  
- Used on **Project detail** pages.  
- Uses `<model-viewer>` with:
  - A fixed **4:3 aspect ratio** (`aspect-ratio: 4 / 3`)
  - A **max-height of 480px** to visually align with the left-column narrative.

### Interactions & Motion

**Hover states:**  
- Only cards and explicitly interactive elements exhibit scale/shadow/brightness changes.  
- No global hover animations.

**Motion preferences:**  
- All transitions respect `prefers-reduced-motion` with fallbacks defined in CSS.

### Utilities
A small set of global utility classes exist (`.stack`, `.text-muted`, `.text-small`) to enforce consistent micro-layout and typography without introducing framework-like patterns.

## KEY COMPONENTS & BEHAVIOR

### Shared Page Components

#### Global Header

**Component:**  
- Site-wide header bar rendered at the top of every page.  
- Displays the site title (my name: `Adam W. Lester`) on the left and navigation links on the right, matching the reference layout.  
- *Implemented directly in `_layouts/default.html`.*

**Data source:**  
- Site title text (e.g., “Adam W. Lester”) is defined once in `_config.yml` as `title` and referenced in the header via `{{ site.title }}`.  
- Navigation links are defined in the header markup in `_layouts/default.html` using `{{ site.baseurl }}` so they work both locally and on GitHub Pages. The canonical targets are:
  - `{{ site.baseurl }}/portfolio/` (Portfolio)
  - `{{ site.baseurl }}/docs/CV.pdf` (CV)
  - `{{ site.baseurl }}/docs/Resume.pdf` (Resume)

**Behavior:**  
- The header appears on all pages that use `layout: default` or layouts extending it (`portfolio-list-page`, `project-detail-page`).  
- On desktop, the site title is aligned to the left and the navigation links are aligned to the right.  
- On mobile, the title and links stack or compress according to the responsive rules in `assets/css/custom.css`.

**Constraints / Notes:**  
- Styling (typography, spacing, alignment, hover states) is controlled via `assets/css/custom.css`.  
- The header is consistent across Home, Portfolio, and Project Detail pages.

#### Banner Region

**Component:**  
- Page-level banner rendered directly below the global header and above the main page content.  
- Displays a large banner image with a title and subtitle text.  
- *Implemented once in `_layouts/default.html` and automatically used on any page that defines `banner_image`, `banner_title`, and `banner_subtitle` in its front matter.*

**Data source:**  
- Front matter fields defined in each page’s `index.md`:
  - `banner_image`: Path to the banner image file, always a root-relative path (e.g., `/assets/images/home-banner.png`).
  - `banner_title`: Short title rendered over or adjacent to the banner image.  
  - `banner_subtitle`: One- or two-line subtitle providing additional context.

- Used on:
  - `index.md` at the site root (Home page).  
  - `portfolio/index.md` (Portfolio list page).

**Behavior:**  
- When `banner_image`, `banner_title`, and `banner_subtitle` are present in front matter, the layout renders the banner at the top of the page content area.  
- The banner appears directly under the global header and directly above any page-specific content (such as intro text or the project grid).  
- If the front matter banner fields are not present, the banner region is omitted and the page content starts immediately below the header.

**Constraints / Notes:**  
- Banner images should be created at **1920 × 300 px** to maintain the intended thin panoramic visual style across pages.  
- Banner image sizing, aspect ratio, and responsive behavior are controlled via `assets/css/custom.css`.  
- The home page and portfolio list page both use this shared banner pattern for consistent visual branding.  
- Project detail pages do not use this shared banner; they instead use the media image-viewer media carousel described in the Project Detail section.

### Home Page Overview

#### Main Elements

**Main elements of the home page include:**
- **Banner Region (`index.md`):**  
  – Top-of-page banner using the shared banner component (image, title, subtitle).
- **Intro Text Block (`index.md`):**  
  – Short welcome/identity copy introducing you and the purpose of the site.
- **Primary Call-to-Action (CTA):**  
  – Prominent link or button that routes users to the portfolio list page (`{{ site.baseurl }}/portfolio/`).


**Front Matter Content (`index.md`):**  
- `layout`: Must be set to `default`.  
- `title`: Page title (i.e., `Home`) used for metadata (browser tab, SEO).
- `description`: Short one-line description for the home page; used for the `<meta name="description">` tag.
- `banner_image`: Path to the banner image file.  
- `banner_title`: Text title (i.e., `Adam W. Lester`) displayed in the banner.  
- `banner_subtitle`: Supporting subtitle text displayed in the banner.

#### Intro Text Block

**Component:**  
- Short introductory block rendered below the banner region on the home page.  
- *Rendered as part of the Markdown body content of `index.md` inside the main content area of `_layouts/default.html`.*

**Data source:**  
- Markdown body content of the site-root `index.md`, immediately after the front matter.  
- Front matter field `title` may also be used as a page-level heading if desired.

**Behavior:**  
- Displays a brief description of who you are and what the site contains.  
- Provides enough context that the “View portfolio” CTA is clear and actionable.  
- Appears above the primary call-to-action link/button.

**Constraints / Notes:**  
- Kept to 1–3 short paragraphs.  
- Typography, spacing, and alignment are controlled via `assets/css/custom.css` for consistency with the portfolio list and project detail pages.

#### Primary Call-to-Action (CTA)

**Component:**  
- Visually prominent link or button directing users to the portfolio list page.  
- *Rendered as a standard link element (`<a>`) in the `index.md` body and styled via `assets/css/custom.css`.*

**Data source:**  
- Markdown link in `index.md` pointing to the portfolio list page via `{{ site.baseurl }}`, for example:  
  - `[View Portfolio]({{ site.baseurl }}/portfolio/)`  
  - Optionally annotated with a class (e.g., `{: .button-link }`) for button-style styling.

**Behavior:**  
- Positioned immediately after the intro text block in the page content.  
- On click, navigates directly to `{{ site.baseurl }}/portfolio/`.  
- Serves as the primary action on the home page.

**Constraints / Notes:**  
- Only one primary CTA is used on the home page.  
- Button-like appearance, hover states, and spacing are implemented in `assets/css/custom.css`.

#### Layout

**Desktop / large screens:**  
- The home page stacks elements vertically in this order:
  1. **Global Header** (site-wide header with nav links and site title).  
  2. **Banner Region** (`banner_image`, `banner_title`, `banner_subtitle`).  
  3. **Intro Text Block** (Markdown content from `index.md`).  
  4. **Primary Call-to-Action** linking to the portfolio list page.

**Mobile / small screens:**  
- Elements appear in the same order as on desktop:
  1. Global Header.  
  2. Banner Region.  
  3. Intro Text Block.  
  4. Primary Call-to-Action.  
- Vertical spacing, text sizing, and banner scaling are controlled via `assets/css/custom.css` to keep the layout readable and consistent with other pages.

### Portfolio List Page Overview

#### Main Elements

**Main elements of the portfolio list page include:**
- **Banner Region (`portfolio/index.md`)**  
  – Full-width banner at the top of the portfolio list page, displaying the banner image, title, and subtitle.
- **Page Header Text (`portfolio/index.md`)**  
  – Full-width introductory block directly **below the banner**, displaying the page lead text.
- **Project Card Grid**  
  – Responsive grid of uniformly styled project cards, each showing the project hero image, title, and summary.

**Front Matter Content (`portfolio/index.md`):** 
- `layout`: Must be set to `portfolio-list-page`.  
- `title`: Page title (i.e., `Portfolio`) used for metadata (browser tab, SEO).
- `description`: Short one-line description for the portfolio list page; used for the `<meta name="description">` tag.
- `banner_image`: Path to the banner image used in the shared banner component.
- `banner_title`: Text title (i.e., `Portfolio`) displayed in the banner.  
- `banner_subtitle`: Short supporting line shown inside the banner under the title.
- `page_lead`: Short introductory paragraph rendered below the banner, describing the portfolio list page.
- `projects:`: Array of project slugs determining which projects to show and their order.
- Example front matter:
  ```yaml
  ---
  layout: portfolio-list-page
  title: "Portfolio"
  banner_image: /assets/images/portfolio-list-banner.png
  banner_title: "Portfolio"
  banner_subtitle: "Open-source research instruments, behavioral platforms, and supporting hardware"
  page_lead: "A collection of open-source research instruments, behavioral platforms, and supporting hardware developed across neuroscience and biomedical engineering projects. Each entry links to a detailed project page with full narrative, images, and a 3D model."
  projects:
    - nc4touch-behavioral-apparatus
    - omniroute-maze-system
    - instantaneous-cue-rotation-arena
  ---
  ```

#### Page Header Text

**Component:**  
- Full-width introductory block rendered **below the banner** on the portfolio list page.
- *Rendered as the header/lead region in `_layouts/portfolio-list-page.html`, optionally wrapped with `_includes/section.html` for consistent spacing.*

**Data source:**  
- `portfolio/index.md` front matter: `page_lead`.

**Behavior:**  
- Renders as a full-width lead paragraph **between** the banner and the project card grid.  
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
- The **entire card is clickable**, linking to `{{ site.baseurl }}/portfolio/projects/<slug>/`.  
- Subtle hover and active states provide visual feedback (gentle lift or shadow change on hover; slight depress on click).

**Constraints / Notes:**  
- Card dimensions, spacing, typography, and hover states are controlled via `assets/css/custom.css` for a cohesive presentation across all projects.  
- Thumbnail aspect ratio is kept consistent so the grid remains visually balanced.

#### Layout

**Desktop / large screens:**  
- The page stacks elements vertically in this order:
  1. **Banner Region**
     - `banner_image` as the background/visual.
     - `banner_title` as the primary heading.
     - `banner_subtitle` as the supporting line beneath the title.
  2. **Page Header Text**
     - `page_lead` rendered as a descriptive paragraph below the banner.
  3. **Project Card Grid**
     - Cards arranged in multiple columns (e.g., 2–4, depending on viewport width).
     - Cards maintain consistent aspect ratio, spacing, and typography across the grid.

**Mobile / small screens:**  
- All elements stack vertically in this order:
  1. Banner Region (image with `banner_title` and `banner_subtitle` stacked)
  2. Page Header Text (`page_lead` as a full-width intro block)
  3. Project Card Grid
     - Grid collapses to fewer columns as the viewport narrows, eventually to a single column on very small screens.
     - Vertical spacing and padding are preserved so cards remain readable and visually distinct.

**Layout Notes:**  
- Overall layout, spacing, and responsive breakpoints are handled via `assets/css/custom.css` to keep the portfolio list visually consistent with project detail pages and other site components.

### Project Detail Page Overview

#### Main Elements

**Main elements of the project detail page include:**
- **Image-Viewer (media carousel):** 
  - Full-width media strip at the top of the project detail page.
  - Displays the primary render and secondary images via a carousel/thumbnail interface.
- **3D-Viewer (window):** 
  - Right-aligned, fixed-width panel positioned below the image-viewer. 
  - Renders the single `.glb` model associated with the project.
- **Project Detail Content (`portfolio/projects/<slug>/index.md`):** 
  - The full structured Markdown (front matter + content body) for the project. 
  - All text on the project detail page (both columns) is derived from this file.
- **Independence of components:**  
  - The image-viewer and 3D-viewer are independent in implementation. The image-viewer handles all image media, and the 3D-viewer handles the single model.  
  - Their behavior and rendering do not affect how the Markdown content is authored.

#### Media Image-Viewer Media Carousel

**Component:** 
- Peeking media carousel for render and photo images, implemented as a **custom CSS scroll-snap carousel** with lightweight vanilla-JS controls.
- *Markup for the carousel is defined in `_layouts/project-detail-page.html` as the full-width media strip at the top of the page.*

**Data source:**  
- The carousel loads all images listed in the `images:` field of the project’s front matter (`portfolio/projects/<slug>/index.md`).  
- Images **must** be shown in the order they are listed in the front matter.  
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
- All JavaScript behavior for the carousel (scrolling, arrows, thumbnails) lives in a small inline `<script>` block at the bottom of `_layouts/project-detail-page.html` (no separate JS bundle is used for V1).

#### 3D Model Viewer Window

**Component:**  
- Single 3D-viewer window implemented with one `<model-viewer>` element in the right column of the project detail page.
- *The `<model-viewer>` element is rendered in the right column of `_layouts/project-detail-page.html`.*

**Data source:**  
- The viewer uses the `model_src` field in the project’s front matter (`portfolio/projects/<slug>/index.md`).  
- `model_src` is a path **relative to the project folder** pointing to the `.glb` file in that project’s local `models/` subfolder.  
  - Example front matter: `model_src: "models/nc4touch-behavioral-apparatus.glb"`  
  - Example corresponding filesystem path:  
    `portfolio/projects/nc4touch-behavioral-apparatus/models/nc4touch-behavioral-apparatus.glb`  
- Per-model viewer fields in front matter:
  - `model_camera_orbit`: String passed to `<model-viewer>` `camera-orbit` (e.g., `"auto auto auto"` or `"45deg 75deg 2.5m"`).
  - `model_camera_target`: String passed to `<model-viewer>` `camera-target` (e.g., `"auto auto auto"` or `"0m 0.5m 0m"`).
  - `model_fov`: String passed to `<model-viewer>` `field-of-view` (e.g., `"auto"` or `"45deg"`).

**Behavior:**  
- On page load, `<model-viewer>` autoloads the `.glb` file referenced by `model_src`.  
- Provides basic interactive controls (orbit, zoom, pan) using `<model-viewer>`’s built-in functionality.  
- Initializes the camera to a sensible default view on load.

**Constraints:**  
- Exactly one `.glb` file per project is supported.  
- The `.glb` file **must** reside under the project’s `models/` subfolder.  
- Maximum file size: ≤ 50 MB.
- The `<model-viewer>` web component script is loaded once in the `<head>` of `_layouts/default.html` from the official CDN (e.g., via a `<script type="module" src="…model-viewer.min.js"></script>` tag) so it is available on all pages that need it.

#### Project Detail Content

**Component:**  
- Includes header and text for the project detail page.
- *Injected by `_layouts/project-detail-page.html` as the main Markdown content region (both columns), using the project’s `index.md` front matter and body.*

**Front Matter Content (`portfolio/projects/<slug>/index.md`):**  
- It includes the following fields:
  - `title`: Full project title shown on the card and project detail page. Rendered as the first element in the left column on the project detail page.
  - `summary`: One-line summary used for the project card on the portfolio list page and directly beneath the title on the project detail page.
  - `description`: One-sentence description used for the page’s `<meta name="description">` tag.
  - `hero`: Path (relative to the project folder) to the hero image file in that project’s `images/` subfolder.
    - Example: `images/render_1.png`.
    - This image is used as the project card thumbnail on the portfolio list page.
    - The value of `hero` **must** exactly match the `src` of one of the entries in the `images` array.
    - The hero image does not need to be first in the `images` list; it is selected solely by matching `hero` to an `images.src` value.
  - `model_src`: Path (relative to the project folder) to the `.glb` file in that project’s `models/` subfolder.
    - Example: `models/nc4touch-behavioral-apparatus.glb`.
    - This file is loaded into the 3D-viewer window on the project detail page.
  - `model_camera_orbit`: String passed to `<model-viewer>` `camera-orbit`.
    - Example values include `"auto auto auto"` or an explicit orbit such as `"45deg 75deg 2.5m"`.
  - `model_camera_target`: String passed to `<model-viewer>` `camera-target`.
    - Example values include `"auto auto auto"` or a specific target such as `"0m 0.5m 0m"`.
  - `model_fov`: String passed to `<model-viewer>` `field-of-view`.
    - Example values include `"auto"` or a specific FOV such as `"45deg"`.
  - `images`: List of supporting render or photo entries, each with:
    - `src`: Path to the `.png` file, relative to the project folder, typically in that project’s `images/` subfolder.
      - Used by the image-viewer media carousel at the top of the project detail page.
    - `caption`: One-line description for context and accessibility.
      - This field is used as the source of the `<img>` `alt` text for the image-viewer.
      - Not visually rendered in V1
- Example front matter:
  ```yaml
  ---
  title: "NC4Touch Behavioral Apparatus"
  summary: "An open-source, modular behavioral apparatus for rodent cognitive experiments."
  description: "An open-source, modular behavioral apparatus for rodent cognitive experiments."
  hero: "images/render_1.png"
  model_src: "models/nc4touch-behavioral-apparatus.glb"
  model_camera_orbit: "auto auto auto"
  model_camera_target: "auto auto auto"
  model_fov: "auto"
  images:
    - src: "images/render_1.png"
      caption: "Isometric view of the NC4Touch apparatus."
    - src: "images/photo_1.png"
      caption: "Photograph of the assembled apparatus in the lab."
  ---
  ```

**Markdown Content Sections (`portfolio/projects/<slug>/index.md`):**  
- All narrative content for a project is authored in the Markdown body directly after the front matter in `index.md`.  
- The content body is wrapped in a structural container that groups sections into two content blocks. The project detail layout (`_layouts/project-detail-page.html`) renders these as the main content region.
- Structure in `index.md`:
  - Parent wrapper: `<div class="content-groups">`
  - Inside it, two content groups:
    - `<div class="content-group content-group-primary" markdown="1">` — primary content sections  
    - `<div class="content-group content-group-secondary" markdown="1">` — secondary content sections  
- Each section is a normal Markdown heading and body inside one of these content groups.
- **Primary content sections (in order):**
  - `Description`
  - `Validation & Performance`
  - `Materials & Fabrication`
  - `Release`
  - `References`
- **Secondary content sections (in order):**
  - `Role & Contributions`
  - `Highlights & Key Specs`
  - `Deployment & Status`
  - `Licensing`
- Headings:
  - Use normal Markdown syntax (`#`, `##`, `###`).
  - Visual styles (sizes, spacing, hierarchy) are controlled globally in `assets/css/custom.css`.
- **Minimal example content body (after front matter):**
  ```markdown
  <div class="content-groups">
  <div class="content-group content-group-primary" markdown="1">
  ## Description
  ...
  ## References
  </div>
  <div class="content-group content-group-secondary" markdown="1">
  ## Role & Contributions
  ...
  ## Licensing
  ...
  </div>
  </div>
  ```

#### Layout

**Desktop**
- Image-viewer media carousel spans the full content width at the top.
- Directly beneath the image-viewer, the page uses a **two-column layout**:
  - **Left column:**
    - `title` (from front matter)
    - `summary` (from front matter)
    - Primary content sections (from content body)
  - **Right column:**
    - 3D-viewer at the top
    - Secondary content sections (from content body)

**Mobile / small screens**
- On smaller screens, all elements stack vertically in this order:
  1. Image-viewer (media carousel)
  2. 3D-viewer (window)
  3. Left-column narrative block:
      - `title` (from front matter)
      - `summary` (from front matter)
      - Primary content sections (from content body)
  4. Right-column narrative block:
      - Secondary content sections (from content body)

**Layout Notes**
- The DOM order matches the mobile stacking order above.
- The desktop layout is achieved purely via CSS (grid/flex) positioning of the left and right column containers.

## IMPLEMENTATION STATUS
*A concise overview of what currently exists in the site and how the core pieces are structured.*

### Structure & Content
*Overall site foundation, routing, and project content.*

**Done:**
- Jekyll site scaffolded with `index.md` as the home page (minimal content for V1).
- Portfolio section in place (portfolio list and project-specific routes wired up as defined in the Site Map above).
- Standardized project folder pattern established (`images/`, `models/`, `index.md`).
- All professional project folders added with full image sets, model files, and `index.md` content.
- Portfolio index configured with project slugs listed in the intended display order.

**To Do:**
- Only minor content tweaks and copy refinements as needed.

### Layouts & Includes
*Templates responsible for rendering pages and reusable components.*

**Done:**
- Layout and include structure defined in this README (names, responsibilities, and how they should work together).

**To Do:**
- Implement the core layouts for the base page shell, portfolio list view, and project detail view.
- Implement the includes for reusable sections and project grids/cards.

### Styling & Components
*Global styles and UI behavior.*

**Done:**
- Global styling approach defined in this README (single main stylesheet, shared patterns for layout and components).

**To Do:**
- Implement global styles in `assets/css/custom.css`.
- Add responsive behavior and visual styling for the header, banner, portfolio cards, image viewer, and project detail layout.

# assets\css\custom.css
/* =========================================================
   1. Design tokens (colors, typography, spacing, layout)
   ========================================================= */

:root {
  /* Typography */
  --ff-body: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
             "Helvetica Neue", Arial, sans-serif;
  --ff-heading: var(--ff-body);

  /* Colors */
  --color-bg: #f7f5f1;            /* page background */
  --color-surface: #ffffff;       /* cards, sections, header */
  --color-border-subtle: #e3dfd7; /* light borders & dividers */

  --color-text: #222222;          /* main text */
  --color-text-muted: #666666;    /* secondary text */
  --color-accent: #2b5f8a;        /* links, key highlights */
  --color-accent-soft: #eef3f9;   /* soft accent background for tags/badges */

  /* Shadows */
  --shadow-card: 0 4px 12px rgba(0, 0, 0, 0.04);      /* default card shadow */
  --shadow-card-hover: 0 10px 28px rgba(0, 0, 0, 0.10);

  /* Spacing scale */
  --space-1: 0.5rem;
  --space-2: 1rem;
  --space-3: 1.5rem;
  --space-4: 2rem;
  --space-5: 3rem;

  /* Layout */
  --max-width-content: 960px;
  --header-height: 56px;
  --page-banner-height: 280px;

  /* Radii */
  --radius-sm: 4px;
  --radius-md: 8px;
}

/* Breakpoints (for reference in comments)
   - Small:  < 768px
   - Medium: 768px–1023px
   - Large:  >= 1024px
*/

/* =========================================================
   2. Base / reset styles
   ========================================================= */

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
  background-color: var(--color-bg);
  color: var(--color-text);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

/* Make images responsive by default */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Typography */
h1,
h2,
h3,
h4 {
  font-family: var(--ff-heading);
  font-weight: 600;
  color: var(--color-text);
  margin-top: var(--space-3);
  margin-bottom: var(--space-2);
  line-height: 1.2;
}

h1 {
  font-size: 2.1rem;
}

h2 {
  font-size: 1.6rem;
}

h3 {
  font-size: 1.25rem;
}

h4 {
  font-size: 1.05rem;
}

p {
  margin-top: 0;
  margin-bottom: var(--space-2);
}

ul,
ol {
  margin-top: 0;
  margin-bottom: var(--space-2);
  padding-left: 1.5rem;
}

li + li {
  margin-top: 0.25rem;
}

/* Links */
a {
  color: var(--color-accent);
  text-decoration: none;
}

a:hover,
a:focus {
  text-decoration: underline;
}

/* Code / pre */
code {
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
    "Courier New", monospace;
  font-size: 0.95em;
}

/* =========================================================
   3. Layout wrappers & global structure
   ========================================================= */

.site-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Primary content wrapper inside layouts */
.site-wrapper {
  max-width: var(--max-width-content);
  margin: 0 auto;
  padding-inline: var(--space-2);
}

/* Main content area (used inside default layout) */
.site-main {
  flex: 1 0 auto;
  padding-top: var(--space-4);
  padding-bottom: var(--space-5);
}

/* Optional footer */
.site-footer {
  flex-shrink: 0;
  padding: var(--space-3) var(--space-2);
  border-top: 1px solid var(--color-border-subtle);
  font-size: 0.9rem;
  color: var(--color-text-muted);
}

/* =========================================================
   4. Global header / navigation
   ========================================================= */

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  background-color: var(--color-surface);
  border-bottom: 1px solid var(--color-border-subtle);
  height: var(--header-height);
}

.site-header-inner {
  max-width: var(--max-width-content);
  margin: 0 auto;
  padding-inline: var(--space-2);
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Left: site title (name) */
.site-title {
  font-weight: 600;
  font-size: 1rem;
  color: var(--color-text);
}

/* Right: nav links */
.site-nav {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.site-nav a {
  font-size: 0.95rem;
  color: var(--color-text);
}

.site-nav a:hover,
.site-nav a:focus {
  color: var(--color-accent);
  text-decoration: none;
}

/* Mobile header stacking */
@media (max-width: 640px) {
  .site-header-inner {
    flex-direction: column;
    justify-content: center;
    gap: 0.25rem;
  }

  .site-header {
    height: auto;
    padding-block: var(--space-1);
  }
}

/* =========================================================
   5. Shared page banner (home + portfolio list)
   ========================================================= */

/* Banner wrapper rendered by layouts when banner_image is present */
.page-banner {
  position: relative;
  height: var(--page-banner-height);
  background-color: var(--color-border-subtle);
  color: var(--color-text);
  overflow: hidden;
}

/* Banner background image applied inline as background-image style
   on an inner div for better control. */
.page-banner-bg {
  position: absolute;
  inset: 0;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  filter: brightness(0.9);
}

/* Overlay to soften the image slightly */
.page-banner-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 0.85),
    rgba(255, 255, 255, 0.95)
  );
}

/* Banner content (title + subtitle) */
.page-banner-content {
  position: relative;
  z-index: 1;
  height: 100%;
}

.page-banner-inner {
  max-width: var(--max-width-content);
  margin: 0 auto;
  padding-inline: var(--space-2);
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.page-banner-title {
  font-size: 1.8rem;
  margin: 0 0 0.25rem 0;
}

.page-banner-subtitle {
  font-size: 1rem;
  margin: 0;
  color: var(--color-text-muted);
}

/* =========================================================
   6. Generic section include (.section.html)
   ========================================================= */

.section {
  padding-block: var(--space-4);
}

.section--tight {
  padding-block: var(--space-3);
}

.section--flush-top {
  padding-top: 0;
}

.section--flush-bottom {
  padding-bottom: 0;
}

.section-inner {
  max-width: var(--max-width-content);
  margin: 0 auto;
  padding-inline: var(--space-2);
}

/* Use for muted / alternate background sections if needed */
.section--surface {
  background-color: var(--color-surface);
}

/* =========================================================
   7. Home / generic content
   ========================================================= */

.page-lead {
  font-size: 1.05rem;
  color: var(--color-text-muted);
  max-width: 40rem;
}

/* Simple primary link-like button (e.g., "View Portfolio") */
.button-link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.45rem 0.9rem;
  font-size: 0.95rem;
  border-radius: var(--radius-sm);
  background-color: var(--color-accent);
  color: #ffffff;
  text-decoration: none;
  border: 1px solid transparent;
}

.button-link:hover,
.button-link:focus {
  text-decoration: none;
  background-color: #234b6c; /* slightly darker accent */
}

/* =========================================================
   8. Portfolio list page: project grid & cards
   ========================================================= */

/* Lead text on portfolio list page */
.portfolio-lead {
  margin-bottom: var(--space-3);
  color: var(--color-text-muted);
}

/* Project grid container */
.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: var(--space-3);
  align-items: stretch;
}

/* Individual project card (wrapper) */
.project-card {
  display: flex;
  flex-direction: column;
  background-color: var(--color-surface);
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border-subtle);
  box-shadow: var(--shadow-card);
  overflow: hidden;
  text-decoration: none; /* in case card is an <a> */
  color: inherit;
  transform-origin: center;
  transition:
    transform 140ms ease-out,
    box-shadow 140ms ease-out,
    border-color 140ms ease-out,
    background-color 140ms ease-out;
}

/* Hero image at the top of the card */
.project-card-image {
  position: relative;
  overflow: hidden;
}

.project-card-image img {
  width: 100%;
  height: auto;
  display: block;
  transition:
    transform 160ms ease-out,
    filter 160ms ease-out;
}

/* Card body (title + summary) */
.project-card-body {
  padding: var(--space-2);
}

.project-card-title {
  font-size: 1.05rem;
  font-weight: 600;
  margin: 0 0 0.35rem 0;
  color: var(--color-text);
}

.project-card-summary {
  font-size: 0.95rem;
  margin: 0;
  color: var(--color-text-muted);
}

/* Hover state: lift, slight scale, stronger shadow, image focus */
.project-card:hover,
.project-card:focus-within {
  transform: translateY(-2px) scale(1.01);
  box-shadow: var(--shadow-card-hover);
  border-color: rgba(0, 0, 0, 0.06);
  background-color: #ffffff;
}

.project-card:hover .project-card-image img,
.project-card:focus-within .project-card-image img {
  transform: scale(1.02);
  filter: brightness(1.05);
}

/* Ensure title link (if used) doesn't add underline on hover */
.project-card-title a {
  color: inherit;
  text-decoration: none;
}

.project-card-title a:hover,
.project-card-title a:focus {
  text-decoration: underline;
}

/* =========================================================
   9. Project detail layout (2-column + content)
   ========================================================= */

/* Overall detail page wrapper */
.project-detail {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

/* Media section (image viewer full-width above the grid) */
.project-media-section {
  margin-bottom: var(--space-3);
}

/* Core grid:
   - Desktop: 2 columns
       main  | model
       main  | aside
   - Mobile: stacked in logical reading order:
       model → main → aside
*/
.project-layout {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(0, 1fr);
  grid-template-areas:
    "main model"
    "main aside";
  gap: var(--space-4);
  align-items: flex-start;
}

/* Legacy column wrappers:
   - Used as semantic containers in the layout markup.
   - We flatten them with display: contents so their children
     can become the real grid items (title/summary + content groups).
*/
.project-main-column,
.project-aside-column {
  display: contents;
  min-width: 0;
}

/* Title and summary:
   - Visually part of the left "main" column.
   - They share the same grid-area as the primary content group,
     so on desktop they sit above it; on mobile they stack between
     the model and secondary content.
*/
.project-title {
  grid-area: main;
  font-size: 1.8rem;
  margin-top: 0;
  margin-bottom: 0.35rem;
}

.project-summary {
  grid-area: main;
  font-size: 1.05rem;
  color: var(--color-text-muted);
  margin-top: 0;
  margin-bottom: var(--space-3);
}

/* Content groups inside the Markdown body:
   - .content-groups is a structural wrapper inserted by authoring.
   - We use display: contents so its children (primary/secondary)
     can participate directly in the grid as distinct areas.
*/
.content-groups {
  display: contents;
}

/* Optional shared styling hook for any content-group wrapper */
.content-group {
  /* no layout rules here on purpose; treat as a semantic hook */
}

/* Primary narrative group:
   - Left column (main) under the title + summary.
   - Shares grid-area: main with the header elements above.
*/
.content-group-primary {
  grid-area: main;
  min-width: 0;
}

/* Secondary narrative group:
   - Right column (aside) beneath the 3D model on desktop.
*/
.content-group-secondary {
  grid-area: aside;
  min-width: 0;
}

/* Generic spacing between narrative sections inside each group */
.project-content-section + .project-content-section {
  margin-top: var(--space-3);
}

/* Small screens: stack in logical order:
   model → main (title + summary + primary) → aside (secondary)
*/
@media (max-width: 767px) {
  .project-layout {
    grid-template-columns: 1fr;
    grid-template-areas:
      "model"
      "main"
      "aside";
    gap: var(--space-3);
  }
}

/* Medium screens: allow columns with slightly different ratio
   and a tighter gap, but keep the same area mapping */
@media (min-width: 768px) and (max-width: 1023px) {
  .project-layout {
    grid-template-columns: minmax(0, 3fr) minmax(0, 2fr);
    gap: var(--space-3);
  }
}

/* =========================================================
   10. Image viewer (banner carousel on project detail)
   ========================================================= */

/* Outer container */
.image-viewer {
  background-color: var(--color-surface);
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border-subtle);
  box-shadow: var(--shadow-card);
  padding: var(--space-2);
}

/* Main area: arrows + scrollable track */
.image-viewer-main {
  position: relative;
}

/* Scrollable horizontal track */
.image-viewer-track {
  display: flex;
  gap: var(--space-1);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  padding-bottom: var(--space-1);
  margin-bottom: var(--space-1);
}

/* Hide default scrollbar (where supported) for cleaner look */
.image-viewer-track::-webkit-scrollbar {
  height: 6px;
}

.image-viewer-track::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.15);
  border-radius: 999px;
}

/* Individual slides */
.image-slide {
  flex: 0 0 100%;
  scroll-snap-align: center;
  position: relative;
  border-radius: var(--radius-sm);
  overflow: hidden;
  aspect-ratio: 16 / 9; /* adjust if you prefer a different frame shape */
}

.image-slide img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
}

/* Navigation arrows (visual style only; JS hooks will wire behavior) */
.image-viewer-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  border: none;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 999px;
  width: 32px;
  height: 32px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
  cursor: pointer;
}

.image-viewer-arrow--prev {
  left: var(--space-1);
}

.image-viewer-arrow--next {
  right: var(--space-1);
}

.image-viewer-arrow-icon {
  font-size: 1rem;
}

/* Thumbnail strip */
.image-viewer-thumbnails {
  display: flex;
  gap: var(--space-1);
  overflow-x: auto;
}

.image-viewer-thumb {
  width: 72px;
  height: 48px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  border: 1px solid transparent;
  cursor: pointer;
  flex-shrink: 0;
}

.image-viewer-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Active thumbnail state (set via JS) */
.image-viewer-thumb--active {
  border-color: var(--color-accent);
}

/* Smaller screens: let slides be slightly narrower than viewport for breathing room */
@media (max-width: 767px) {
  .image-slide {
    flex-basis: 92%;
  }
}

/* =========================================================
   11. 3D viewer panel (<model-viewer>)
   ========================================================= */

.model-viewer-panel {
  grid-area: model;
  background-color: var(--color-surface);
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border-subtle);
  box-shadow: var(--shadow-card);
  padding: var(--space-2);
}

/* Title above the 3D viewer, if used */
.model-viewer-title {
  font-size: 1rem;
  font-weight: 600;
  margin-top: 0;
  margin-bottom: var(--space-2);
}

/* Make the <model-viewer> element a responsive box */
model-viewer {
  width: 100%;
  aspect-ratio: 4 / 3;
  max-height: 480px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  background-color: #e5e5e5; /* neutral fallback while model loads */
}

/* =========================================================
   12. Utility classes & responsive tweaks
   ========================================================= */

/* Utility for muted text */
.text-muted {
  color: var(--color-text-muted);
}

/* Utility for slightly smaller text */
.text-small {
  font-size: 0.9rem;
}

/* Stack vertical spacing in generic content blocks */
.stack > * + * {
  margin-top: var(--space-2);
}

/* On very small screens, reduce padding slightly */
@media (max-width: 480px) {
  .site-wrapper,
  .section-inner {
    padding-inline: var(--space-1);
  }

  .site-main {
    padding-top: var(--space-3);
    padding-bottom: var(--space-4);
  }
}

/* =========================================================
   13. Reduced motion preferences
   ========================================================= */

@media (prefers-reduced-motion: reduce) {
  * {
    scroll-behavior: auto !important;
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
  }
}

# _layouts\default.html

---
---
<!--
  DEFAULT LAYOUT
  This file defines the global HTML structure shared by all pages:
  - <html>, <head>, <body>
  - Metadata (title, description)
  - Global styles/scripts
  - Header + navigation
  - Optional banner
  - Footer
  Child layouts only supply content for {{ content }} inside <main>.
-->

<!DOCTYPE html>
<html lang="{{ site.lang | default: 'en' }}">
  <head>
    <!-- Meta: charset + responsive viewport -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Page <title> construction -->
    {% if page.title %}
      <title>{{ page.title | escape }} | {{ site.title | escape }}</title>
    {% else %}
      <title>{{ site.title | escape }}</title>
    {% endif %}

    <!-- Meta description: prefer page.description, fallback to site.description -->
    {% if page.description %}
      <meta name="description" content="{{ page.description | escape }}">
    {% elsif site.description %}
      <meta name="description" content="{{ site.description | escape }}">
    {% endif %}

    <!-- Global stylesheet -->
    <link rel="stylesheet" href="{{ site.baseurl }}/assets/css/custom.css">

    <!-- Global <model-viewer> web component (loaded once per site) -->
    <script
      type="module"
      src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js">
    </script>
  </head>

  <body class="site-page">
    <!-- ======================================== -->
    <!-- GLOBAL HEADER + PRIMARY NAVIGATION       -->
    <!-- ======================================== -->
    <header class="site-header">
      <div class="site-header-inner">

        <!-- Site title: always links to homepage -->
        <a class="site-title" href="{{ site.baseurl }}/">
          {{ site.title }}
        </a>

        <!-- Primary navigation links -->
        <nav class="site-nav" aria-label="Primary">
          <a href="{{ site.baseurl }}/portfolio/">Portfolio</a>
          <a href="{{ site.baseurl }}/docs/CV.pdf">CV</a>
          <a href="{{ site.baseurl }}/docs/Resume.pdf">Resume</a>
        </nav>

      </div>
    </header>

    <!-- ======================================== -->
    <!-- OPTIONAL PAGE BANNER                     -->
    <!-- Renders only if page.banner_image exists -->
    <!-- ======================================== -->
    {% if page.banner_image %}
      <section class="page-banner">

        <!-- Banner background image -->
        <div
          class="page-banner-bg"
          style="background-image: url('{{ site.baseurl }}{{ page.banner_image }}');">
        </div>

        <!-- Dark overlay to improve legibility -->
        <div class="page-banner-overlay"></div>

        <!-- Foreground banner content -->
        <div class="page-banner-content">
          <div class="page-banner-inner">

            <!-- Banner title (serves as page H1)
                If banner_title is provided, use it.
                Otherwise, fall back to the page's main title.
                This ensures every banner has a meaningful H1. -->
            {% if page.banner_title %}
              <h1 class="page-banner-title">{{ page.banner_title }}</h1>
            {% else %}
              <h1 class="page-banner-title">{{ page.title }}</h1>
            {% endif %}

            <!-- Optional subtitle -->
            {% if page.banner_subtitle %}
              <p class="page-banner-subtitle">{{ page.banner_subtitle }}</p>
            {% endif %}

          </div>
        </div>

      </section>
    {% endif %}

    <!-- ======================================== -->
    <!-- MAIN CONTENT AREA                        -->
    <!-- Child layouts provide all markup inside  -->
    <!-- {{ content }} (wrapped in .site-wrapper) -->
    <!-- ======================================== -->
    <main class="site-main" role="main">
      <div class="site-wrapper">
        {{ content }}
      </div>
    </main>

    <!-- ======================================== -->
    <!-- GLOBAL FOOTER                            -->
    <!-- ======================================== -->
    <footer class="site-footer">
      <div class="site-wrapper">
        <small>
          &copy; {{ site.time | date: "%Y" }} {{ site.title }}.
        </small>
      </div>
    </footer>

  </body>
</html>

# _layouts\portfolio-list-page.html

---
layout: default
---

<!--
  PORTFOLIO LIST PAGE LAYOUT
  ------------------------------------------------
  This file provides the page-level structure for
  the portfolio index. It is rendered inside the
  global default.html layout and outputs only the
  content meant for the {{ content }} region.

  This layout avoids global elements (header, footer,
  banner, wrappers) and delegates project resolution
  and card rendering to the included grid/templates.
-->

<!-- ========================================= -->
<!-- LEAD SECTION                              -->
<!-- Optional introductory text under banner   -->
<!-- ========================================= -->
{% if page.page_lead %}
  {% capture portfolio_lead_content %}
    <div class="portfolio-lead">
      {{ page.page_lead | markdownify }}
    </div>
  {% endcapture %}
  {% include section.html content=portfolio_lead_content %}
{% endif %}


<!-- ========================================= -->
<!-- PROJECT GRID SECTION                      -->
<!-- Main portfolio listing area               -->
<!-- ========================================= -->
{% if page.projects and page.projects.size > 0 %}
  {% capture portfolio_grid_content %}
    {% include project-grid.html projects=page.projects %}
  {% endcapture %}
  {% include section.html class="section--surface" content=portfolio_grid_content %}
{% endif %}

# _layouts\project-detail-page.html

---
layout: default
---

<!--
  PROJECT DETAIL LAYOUT
  Renders the project detail page under the default layout shell.
  Responsibilities:
  - Full-width image-viewer media carousel at the top.
  - 3D <model-viewer> panel in the right column.
  - Two-column narrative layout driven by .content-groups in Markdown.
-->

<div class="project-detail">

  <!-- ======================================== -->
  <!-- MEDIA STRIP: IMAGE-VIEWER CAROUSEL       -->
  <!-- ======================================== -->
  {% if page.images and page.images.size > 0 %}
    <section class="project-media-section">
      <div class="image-viewer" data-image-viewer>
        <div class="image-viewer-main">

          {% assign image_count = page.images | size %}

          <!-- Navigation arrows (only if multiple images) -->
          {% if image_count > 1 %}
            <button
              class="image-viewer-arrow image-viewer-arrow--prev"
              type="button"
              aria-label="Previous image">
              <span class="image-viewer-arrow-icon">&#10094;</span>
            </button>

            <button
              class="image-viewer-arrow image-viewer-arrow--next"
              type="button"
              aria-label="Next image">
              <span class="image-viewer-arrow-icon">&#10095;</span>
            </button>
          {% endif %}

          <!-- Scrollable track of main slides -->
          <div class="image-viewer-track" data-image-viewer-track>
            {% for image in page.images %}
              {% assign image_src = image.src %}
              {% assign image_alt = image.caption | default: page.title %}

              <div class="image-slide" data-image-index="{{ forloop.index0 }}">
                <img
                  src="{{ site.baseurl }}{{ page.dir }}{{ image_src }}"
                  alt="{{ image_alt }}"
                  {% unless forloop.first %}loading="lazy"{% endunless %}>
              </div>
            {% endfor %}
          </div>
        </div>

        <!-- Thumbnail strip (only if multiple images) -->
        {% if image_count > 1 %}
          <div class="image-viewer-thumbnails" data-image-viewer-thumbnails>
            {% for image in page.images %}
              {% assign thumb_src = image.src %}

              <button
                class="image-viewer-thumb{% if forloop.first %} image-viewer-thumb--active{% endif %}"
                type="button"
                data-image-index="{{ forloop.index0 }}"
                aria-label="View image {{ forloop.index }} of {{ image_count }}">
                <img
                  src="{{ site.baseurl }}{{ page.dir }}{{ thumb_src }}"
                  alt="">
              </button>
            {% endfor %}
          </div>
        {% endif %}
      </div>
    </section>
  {% endif %}

  <!-- ======================================== -->
  <!-- MAIN PROJECT LAYOUT (2-COLUMN GRID)      -->
  <!-- ======================================== -->
  <div class="project-layout">

    <!-- Right column: 3D model viewer panel (grid-area: model) -->
    <div class="project-aside-column">
      {% if page.model_src %}
        <div class="model-viewer-panel">
          <model-viewer
            src="{{ site.baseurl }}{{ page.dir }}{{ page.model_src }}"
            {% if page.model_camera_orbit %}camera-orbit="{{ page.model_camera_orbit }}"{% endif %}
            {% if page.model_camera_target %}camera-target="{{ page.model_camera_target }}"{% endif %}
            {% if page.model_fov %}field-of-view="{{ page.model_fov }}"{% endif %}
            aria-label="{{ page.title | escape }} 3D model"
            autoplay
            camera-controls
            interaction-prompt="auto">
          </model-viewer>
        </div>
      {% endif %}
    </div>

    <!-- Left column: title, summary, and primary/secondary content groups -->
    <div class="project-main-column">

      <!-- Project title (page H1 when no banner is present) -->
      {% unless page.banner_image %}
        {% if page.title %}
          <h1 class="project-title">{{ page.title }}</h1>
        {% endif %}
      {% endunless %}

      <!-- Project summary (short one-line description) -->
      {% if page.summary %}
        <p class="project-summary">{{ page.summary }}</p>
      {% endif %}

      <!-- Structured Markdown body:
           - Expects .content-groups wrapper with:
             .content-group-primary (primary narrative)
             .content-group-secondary (secondary narrative)
           - CSS uses display: contents + grid-area to route
             these groups into the left/right regions. -->
      {{ content }}
    </div>

  </div>

</div>

<!-- ========================================== -->
<!-- IMAGE-VIEWER BEHAVIOR (LIGHTWEIGHT JS)    -->
<!-- ========================================== -->
<script>
  (function () {
    var viewer = document.querySelector('[data-image-viewer]');
    if (!viewer) return;

    var track = viewer.querySelector('[data-image-viewer-track]');
    if (!track) return;

    var slides = Array.prototype.slice.call(
      track.querySelectorAll('.image-slide')
    );
    if (!slides.length) return;

    var thumbsContainer = viewer.querySelector('[data-image-viewer-thumbnails]');
    var thumbs = thumbsContainer
      ? Array.prototype.slice.call(
          thumbsContainer.querySelectorAll('.image-viewer-thumb')
        )
      : [];

    var prevButton = viewer.querySelector('.image-viewer-arrow--prev');
    var nextButton = viewer.querySelector('.image-viewer-arrow--next');

    var activeIndex = 0;

    function clampIndex(index) {
      if (index < 0) return 0;
      if (index >= slides.length) return slides.length - 1;
      return index;
    }

    function setActive(index, options) {
      index = clampIndex(index);
      if (index === activeIndex) return;
      activeIndex = index;

      var slide = slides[activeIndex];
      if (slide && slide.scrollIntoView) {
        try {
          slide.scrollIntoView({
            behavior: (options && options.behavior) || 'smooth',
            block: 'nearest',
            inline: 'center'
          });
        } catch (e) {
          // Older browsers may not support options; fall back to default.
          slide.scrollIntoView();
        }
      }

      // Update active thumbnail state
      if (thumbs.length) {
        thumbs.forEach(function (thumb, i) {
          if (i === activeIndex) {
            thumb.classList.add('image-viewer-thumb--active');
          } else {
            thumb.classList.remove('image-viewer-thumb--active');
          }
        });
      }
    }

    function handleArrow(delta) {
      setActive(activeIndex + delta);
    }

    if (prevButton) {
      prevButton.addEventListener('click', function () {
        handleArrow(-1);
      });
    }

    if (nextButton) {
      nextButton.addEventListener('click', function () {
        handleArrow(1);
      });
    }

    if (thumbs.length) {
      thumbs.forEach(function (thumb) {
        thumb.addEventListener('click', function () {
          var indexAttr = thumb.getAttribute('data-image-index');
          var index = parseInt(indexAttr, 10);
          if (!isNaN(index)) {
            setActive(index, { behavior: 'smooth' });
          }
        });
      });
    }

    // Initialize state so the first thumbnail is synced with the first slide
    setActive(0, { behavior: 'auto' });
  })();
</script>
