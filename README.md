# WEBSITE OVERVIEW & ROADMAP
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

### Liquid Limitation in GitHub Pages (Jekyll 3)

**GitHub Pages uses `Jekyll 3.10` + `Liquid 4`, with known issue**:
- Avoid this pattern:
    ```liquid
    {% capture x %}
      {% include something.html %}
    {% endcapture %}
    {% include section.html content=x %}
    ```
  - It can trigger a false **“Nesting too deep”** Liquid error.
- Use inline triple-quoted content instead:
    ```liquid
    {% include section.html content="""
      {% include something.html %}
    """ %}
    ```
  - This avoids the Liquid recursion bug while preserving the intended layout.

**Commenting Liquid safely in templates**:
- HTML comments (`<!-- ... -->`) do **not** stop Liquid from executing; any `{% %}` or `{{ }}` inside them will still run.
- Use Liquid comments to hide Liquid syntax completely:
  ```liquid
  {%- comment -%}
    Internal note that can mention {% include %} safely.
  {%- endcomment -%}
  ```
- When you want to show example Liquid code in a comment or docs without executing it, wrap it in `raw`:
  ```liquid
  {% raw %}
    {% include section.html content=lead_html %}
  {% endraw %}
  ```
- General rule: keep Liquid tags out of plain HTML comments; use Liquid `{% comment %}` or `{% raw %}` whenever a comment needs to mention real Liquid code.





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
  hero: "images/hero.png"
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




## LOCAL DEVELOPMENT WORKFLOW
*This section covers how to run the site locally with the same URL behavior as GitHub Pages for fast iteration and reliable path testing.

### Local preview server

Use the `github-pages` gem and Jekyll’s built-in server with a baseurl that matches production:
```bash
bundle exec jekyll serve --livereload --baseurl "/awl-site"
```

**Behavior:**
- Serves the site at: 
  - `http://localhost:4000/awl-site/`
- Uses the same `site.baseurl` (`/awl-site`) as production.
- Automatically reloads pages when layouts, includes, CSS, or content change.

**Why `--baseurl "/awl-site"` matters:**
- Internal links written as `href="{{ site.baseurl }}/portfolio/"` resolve correctly both:
  - Locally:
    - `http://localhost:4000/awl-site/portfolio/`
  - On GitHub Pages:
    - `https://adamwlester.github.io/awl-site/portfolio/`
- Asset paths that rely on `{{ site.baseurl }}` (CSS, images, models, docs) behave exactly as they will in production.
- Any baseurl-related issues (404s, broken links, missing assets) show up locally instead of only after a GitHub Pages deploy.

**Recommended edit → test → deploy loop**
**Develop locally:**
- Start the server once with:  
  ```bash
  bundle exec jekyll serve --livereload --baseurl "/awl-site"
  ```
- Visit: `http://localhost:4000/awl-site/`
- Make changes to layouts, includes, CSS, or Markdown content and verify in the browser as they auto-reload.

**Commit in batches:**
- After fixing a small cluster of issues (links, layout tweaks, copy edits), commit the changes locally.

**Deploy to GitHub Pages:**
- Push to `main` → GitHub Actions runs the **pages build and deployment** workflow.
- Watch the **Actions** tab: when the latest run is green (success), the live site at  
  `https://adamwlester.github.io/awl-site/` is updated.

**Link List:**
- **Local development root**
  - <http://localhost:4000/awl-site/>
- **Local portfolio index**
  - <http://localhost:4000/awl-site/portfolio/>
- **Production site root**
  - <https://adamwlester.github.io/awl-site/>
- **Production portfolio index**
  - <https://adamwlester.github.io/awl-site/portfolio/>




## IMPLEMENTATION STATUS
*Notes for maintaining this section:*
* *Use concise, single-level bullets.*
* *Keep entries in sync with the current repo state.*
* *Prefer present-tense descriptions over historical build steps.*

*A concise overview of what currently exists in the site and how the core pieces are structured.*

### Structure & Content
*Overall site foundation, routing, and project content.*

**Status:**
- Jekyll site scaffolded with `index.md` as the home page.
- Portfolio section routes match the Site Map (`/portfolio/` and `/portfolio/projects/<slug>/`).
- Standardized project folder pattern (`images/`, `models/`, `index.md`) applied across all projects.
- All project folders include full image sets, model files, and `index.md` content.
- Portfolio index front matter lists project slugs in the intended display order.

### Layouts & Includes
*Templates responsible for rendering pages and reusable components.*

**Status:**
- Base layout (`_layouts/default.html`) implemented with global shell, header, banner, and footer.
- Portfolio list layout (`_layouts/portfolio-list-page.html`) implemented with lead + project grid sections.
- Project detail layout (`_layouts/project-detail-page.html`) implemented with media carousel, 3D viewer, and two-column narrative layout.
- Section wrapper include (`_includes/section.html`) implemented for reusable page bands.
- Project grid and card includes (`_includes/project-grid.html`, `_includes/project-card.html`) implemented and wired into the portfolio list page.

### Styling & Components
*Global styles and UI behavior.*

**Status:**
- Global styling implemented in `assets/css/custom.css` (typography, colors, spacing, layout tokens).
- Responsive behavior in place for header, banner, portfolio grid/cards, and project detail layout.
- Image viewer (media carousel) styling implemented and wired to lightweight JS behavior.
- 3D model viewer panel styled and integrated with the global `<model-viewer>` script.

### Local Jekyll Environment Setup

**Installed Components:**  
- **Ruby:** 3.3.10 (x64, via RubyInstaller with MSYS2 toolchain)
- **Bundler:** Installed via RubyGems  
- **MSYS2 + MINGW toolchain:** Installed using option `3` during RubyInstaller setup  
  - Required for native Ruby gem compilation on Windows  
- **Gemfile created** with:
  - `github-pages` gem (GitHub Pages’ locked Jekyll environment, Jekyll 3.10.0)
  - `webrick` (required for Jekyll serving on Ruby 3+)
- **bundle install** completed successfully  
  - Installed Jekyll **3.10.0** (GitHub Pages version)  
  - Installed Liquid **4.0.4**
  - Installed all other GitHub Pages-pinned dependencies

**Jekyll Commands Verified:**
- `bundle exec jekyll build`
- `bundle exec jekyll serve --livereload`
  
**Site Structure Confirmed:**
- All layouts, includes, assets, models, and project folders present
- Portfolio pages routed correctly
- Section include, project grid include, and project card include wired in

**Current Build Status:**
- `bundle exec jekyll serve --livereload` runs without Liquid errors  
- Previous “Nesting too deep” issue resolved by wrapping example `{% include %}` lines in `_includes/section.html` with `{% raw %} ... {% endraw %}` so they are not executed  