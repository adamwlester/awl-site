_layouts\portfolio-list-page.html questions:

2. **Use of `_includes/section.html` on the portfolio page**
   - **Question:** For the content under the banner on `/portfolio/`, should we:
     - (a) Wrap both page_lead and the project grid in a single section.
     - (b) Use two sections: one for page_lead, one for the project grid.
     - (c) Not use `section.html` at all (just rely on `.site-wrapper` directly).
     - (d) Use some other custom pattern.
   - **Answer:** (b) Two sections (lead + grid)
   - **Rationale:** This keeps implementation very simple but gives you maximum visual and layout flexibility (e.g., putting the grid in a `.section--surface` band) while aligning with the idea of `section.html` as a generic section wrapper described in the README and supported by the CSS.

3. **Section include API (`_includes/section.html` parameters)**
   - **Question:** How should layouts pass options to `section.html`?
     - (a) Pass CSS classes directly, e.g. `{% include section.html class="section--tight section--flush-top" %}`.
     - (b) Pass a semantic `variant` string that `section.html` maps to classes internally.
     - (c) Use no parameters; all sections share the same style and spacing.
     - (d) Use some other parameter scheme.
   - **Answer:** (a) Pass CSS classes directly
   - **Rationale:** Direct classes are easy to understand, closely match the existing CSS modifiers (`.section--surface`, `.section--tight`, etc.), and avoid the added indirection and complexity of a custom “variant mapping” layer, while still being flexible for future tweaks.

4. **Source of project metadata in `_includes/project-grid.html`**
   - **Question:** Given `projects: [slugs]` in `portfolio/index.md`, how should we find the corresponding project pages?
     - (a) Treat them as normal pages and look up by folder/dir (`/portfolio/projects/<slug>/`).
     - (b) Move projects into a Jekyll collection (e.g., `collections: [projects]`) and use `site.projects`.
     - (c) Implement (a) now but structure the code so it’s easy to switch to a collection later.
     - (d) Use some other data source strategy.
   - **Answer:** (c) Use page lookups now but encapsulate logic for easy migration
   - **Rationale:** The README and current structure already assume projects live as normal pages under `/portfolio/projects/<slug>/`, so page-based lookup is the most natural fit; wrapping this logic in one place keeps complexity low while making it easy to switch to a collection later if you ever need that.

5. **Behavior when a slug cannot be resolved or required fields are missing**
   - **Question:** If `projects:` includes a slug with no corresponding page, or a project is missing `hero` or `summary`, should we:
     - (a) Fail silently and skip that project card.
     - (b) Render a minimal fallback card (e.g., title only or “Coming soon”).
     - (c) Fail loudly in the HTML (visible warnings, possibly gated by `jekyll.environment`).
     - (d) Use a different approach.
   - **Answer:** (a) Skip card, ideally with a non-visible hint (HTML comment) for debugging
   - **Rationale:** Skipping invalid cards keeps the live UX clean and avoids broken-looking placeholders, while adding a simple HTML comment (or similar) in the markup gives you a low-friction way to spot and debug issues without adding significant template complexity.

6. **Alt text for project card hero images**
   - **Question:** What should be used for the `<img alt="…">` in project cards?
     - (a) Use the project title as alt text.
     - (b) Use the project summary as alt text.
     - (c) Treat the card hero as decorative and set `alt=""`.
     - (d) Plan a dedicated `hero_alt` field in front matter, with title/summary as fallback.
   - **Answer:** (c) Treat card heroes as decorative (`alt=""`)
   - **Rationale:** The card already exposes the project title and summary in text, so the image doesn’t convey essential extra meaning; making it decorative avoids redundant, noisy screen reader output and is the simplest approach that still aligns with accessibility best practices.

7. **Heading / semantics in the main content area**
   - **Question:** Given that the banner already shows `banner_title` (“Portfolio”), what heading structure should we use in the content below?
     - (a) No additional `<h1>` in the main content; the banner title is the page’s H1.
     - (b) Add a modest `<h1>` in the main content that duplicates the page title.
     - (c) Some other arrangement (e.g., use `h2`/`h3` in content only).
   - **Answer:** (a) Treat the banner’s `banner_title` as the sole H1
   - **Rationale:** The README treats the banner title as the primary page heading, and duplicating it as a second H1 in the content would be semantically redundant; relying on the banner for H1 and using `h2`/`h3` in the body keeps the structure clean and predictable.

8. **Single section vs visually distinct band for the project grid**
   - **Question:** Visually, should the lead and grid share one neutral background, or should the grid sit on its own “surface” band?
     - (a) Lead and grid share the same neutral background in one section.
     - (b) Lead on default background; grid in a `.section--surface` band (or similar) for contrast.
   - **Answer:** (b) Use a `.section--surface` band for the grid
   - **Rationale:** Giving the grid its own surface band helps it read as a dedicated “portfolio area,” makes good use of the `.section--surface` pattern already defined in CSS, and adds visual clarity without significantly increasing layout or template complexity.



_layouts\project-detail-page.html questions:

1. Primary vs secondary content handling  
   - **Question:** How should the Markdown body map into left/right columns?  
   - **Options:**  
     - (a) Keep README pattern: use `.content-group-primary` / `.content-group-secondary` wrappers in the body, with minimal extra CSS.  
     - (b) Keep existing CSS (`.project-main-column` / `.project-aside-column`) but change the authoring pattern in the README.  
     - (c) Treat Markdown body as only primary; secondary content lives elsewhere (e.g., separate fields).  
     - (d) Something else (custom pattern).  
   - **Answer:** (a)  
   - **Rationale:** This aligns directly with the README’s documented authoring model and avoids brittle Liquid tricks to split content. You get a clear, semantic primary/secondary distinction while keeping the implementation focused on CSS styling rather than complex template logic.

2. Where should `{{ content }}` live in the layout?  
   - **Question:** How is the Markdown body physically inserted into the layout?  
   - **Options:**  
     - (a) Place `{{ content }}` only inside the left column.  
     - (b) Split the content across left and right columns in the layout.  
     - (c) Wrap `{{ content }}` once and let CSS + inner wrappers (`content-groups`) handle grouping.  
   - **Answer:** (c)  
   - **Rationale:** A single `{{ content }}` call is the simplest and least fragile from a Jekyll perspective. Letting the authored `.content-groups` wrappers and CSS control layout keeps behavior predictable and consistent with the README.

3. Use of `_includes/section.html` on project pages  
   - **Question:** Should the generic section wrapper be used around the project detail layout?  
   - **Options:**  
     - (a) Wrap the entire project detail page in `section.html`.  
     - (b) Wrap only the media + 2-column block in `section.html`.  
     - (c) Don’t use `section.html` on project pages at all.  
   - **Answer:** (c)  
   - **Rationale:** Project pages already have a dedicated layout vocabulary (`.project-detail`, `.project-layout`, etc.) and carefully tuned spacing. Adding a generic section wrapper risks redundant padding/overlaps, making the system more brittle without clear UX benefit.

4. Optional vs required media fields  
   - **Question:** How should the layout behave if images or model fields are missing?  
   - **Options:**  
     - (a) Assume every project has images and a model; no checks.  
     - (b) Add conditions so the carousel/model hide gracefully if data is missing.  
     - (c) Treat missing media as a hard error to be fixed in content (no defensive code).  
   - **Answer:** (b)  
   - **Rationale:** Light conditional guards preserve page integrity if a field is missing while still nudging you to keep projects complete. This balances robustness with small implementation effort and avoids ugly broken states in the UI.

5. Hero vs image order  
   - **Question:** How should the first slide in the carousel be chosen relative to `hero`?  
   - **Options:**  
     - (a) Carousel strictly follows `images:` order; `hero` is just used in the grid.  
     - (b) Always force the `hero` image to be the first slide in the carousel.  
     - (c) Other rule (e.g., flags on images).  
   - **Answer:** (a)  
   - **Rationale:** Letting `images:` define the canonical order keeps the implementation simple and avoids extra matching/reordering logic. The README already implies the hero is “typically” first, which is easy to maintain as a content convention instead of code.

6. Alt text fallback  
   - **Question:** What should alt text be when explicit alt text isn’t provided?  
   - **Options:**  
     - (a) Fallback to `page.title`.  
     - (b) Use a generic string like “Project image”.  
     - (c) Use empty alt (`""`).  
     - (d) Assume captions always exist and use them.  
   - **Answer:** Hybrid of (a) and (d) — e.g., `image.alt → image.caption → page.title`.  
   - **Rationale:** Layering fallbacks ensures images remain meaningfully described for accessibility even when metadata is incomplete. It’s low-complexity to implement and gives you more informative alt text than a generic string or an empty value.

7. Model viewer behavior  
   - **Question:** How configurable should `<model-viewer>` be from front matter?  
   - **Options:**  
     - (a) Fixed viewer attributes; only `src` + camera params vary per project.  
     - (b) Expose many more attributes to front matter for per-project tuning.  
     - (c) Start with (a) for V1 and expand later if needed.  
   - **Answer:** (c)  
   - **Rationale:** A minimal, fixed configuration keeps behavior consistent and the code easy to reason about, while still giving you control over framing. If you later find a real need for more knobs, optional front-matter fields can be added incrementally without breaking existing pages.

8. 3D viewer labeling  
   - **Question:** How should the 3D viewer be labeled visually?  
   - **Options:**  
     - (a) Include a fixed title label above the viewer (e.g., “3D model”).  
     - (b) Make the label text configurable via front matter.  
     - (c) No title at all.  
   - **Answer:** (a)  
   - **Rationale:** A simple fixed label improves clarity for users and takes advantage of the existing `.model-viewer-title` CSS hook with almost no extra complexity. Making it configurable feels like premature flexibility for a one-person portfolio.

9. Carousel script assumptions  
   - **Question:** How defensive should the JS be for the image viewer?  
   - **Options:**  
     - (a) Assume one viewer and multiple images; minimal checks.  
     - (b) Add basic guards for 0–1 images (hide arrows/thumbnails, skip wiring if no slides).  
     - (c) Add more defensive coding and warnings for various edge cases.  
   - **Answer:** (b)  
   - **Rationale:** Basic guards prevent awkward behavior when there are few or no images while keeping the script small and straightforward. Heavier defensive logic and warnings offer diminishing returns for a tightly controlled, author-only site like this.






1. **Section wrapper strategy for project detail content**  
   - **Question:**  
     a) Wrap the entire project detail content in ONE generic section via section.html  
        (section → section-inner → .project-detail inside).  
     b) Do NOT use section.html here; let .project-detail be the top-level block under .site-wrapper.  
     c) Use multiple sections (e.g., one for the media strip, one for the two-column layout).  
     d) Something else (briefly describe).  
   - **Answer:** (b) Do NOT use `section.html`; let `.project-detail` be the top-level block  
   - **Rationale:** From the earlier project-detail-page decision: project pages already have a dedicated layout vocabulary (`.project-detail`, `.project-layout`, etc.) and carefully tuned spacing. Adding the generic `section.html` wrapper on project pages was explicitly **not** recommended because it risks double-padding and fighting the custom grid, without giving clear UX benefit. That said, confirm this assessment is accurate and still holds with the current state of things.

2. **Data guarantees for V1 projects**  
   - **Question:**  
     a) Assume EVERY project has at least one image in `images:` AND a valid `model_src`.  
     b) Images always exist, but `model_src` may be absent on some projects.  
     c) Both `images` and `model_src` may be absent in some edge cases; layout should degrade gracefully.  
     d) Other (describe your expectations).  
   - **Answer:** (a)  
   - **Rationale:** I have and will make sure all assets are present and formatted correctly.

3. **DOM order inside .project-layout (important for mobile semantics)**  
   - **Question:**  
     a) Enforce DOM order: model-viewer-panel → title/summary/primary (via content-groups) → secondary.  
     b) DOM order: title/summary/primary → secondary → model (relying on CSS for visual order only).  
     c) I’m okay relaxing the “DOM order = mobile visual order” rule if it simplifies implementation.  
     d) Other (describe exactly what you want).  
   - **Answer:** (c or a) Go with C if this notably decreases the likelihood of issues  
   - **Rationale:** A is the ideal but willing to let it go to get this working without issue. More code is ok, but any complexity that veers into semi-uncharted or unpredictable waters should be avoided.

4. **Image-viewer behavior scope for V1**  
   - **Question:**  
     a) Minimal: scrollable track, arrow buttons, active thumb highlight; basic but clean.  
     b) Enhanced: (a) plus keyboard navigation and basic ARIA roles/labels.  
     c) Ultra-minimal: JUST the scrollable track and thumbnails; no arrows/JS for now.  
     d) Other (describe desired behavior).  
   - **Answer:** (b or a)
   - **Rationale:** I would be fine with either. This is one feature I care most about but want to factor in how easy it is to just get working versus trying to pack in all functionality and frontloading ourselves with debugging before system is stable.

5. **Visible captions in the image-viewer**  
   - **Question:**  
     a) Stick to the README: captions are ONLY used for alt text; no visible caption in V1.  
     b) Show a simple text caption below the main slide using `image.caption`.  
     c) Provide a hook (e.g., a visually hidden caption element) to make future caption rendering easy, but don’t show it yet.  
     d) Other (describe). 
   - **Answer:** (a) 
   - **Rationale:**  We can add this support later but not a priority right now.

6. **3D viewer labeling**  
   - **Question:**  
     a) Always show a small label above the viewer (e.g., “3D model” using .model-viewer-title).  
     b) Make the label optional via a front matter field (e.g., `model_title:`); omit if not set.  
     c) Don’t show any label; just the viewer.  
     d) Other (describe).  
   - **Answer:** (c)
   - **Rationale:** We do not need any label for this, at least right now.

7. **Any projects WITHOUT `content-groups`?**  
   - **Question:**  
     a) All project Markdown bodies will follow the documented pattern with `<div class="content-groups">` and both primary/secondary groups.  
     b) A few legacy/experimental projects may not have that wrapper; layout should not break hard if it’s missing.  
     c) Other (describe).  
   - **Answer:** (a) All project Markdown bodies will follow the documented pattern  
   - **Rationale:** The prior “Primary vs secondary content handling” answer explicitly chose to **keep the README pattern** of authoring `.content-group-primary` / `.content-group-secondary` in the Markdown. That assumes you’ll follow this structure for your projects rather than supporting arbitrary/legacy formats.

8. **Anything else you care about for this page’s semantics or accessibility?**  
   - **Question:**  
     (Open-ended: write your priorities, e.g., heading structure, landmark roles, tab order, etc.)  
   - **Answer / Priorities (derived from earlier answers):**  
     - Use the **banner title as the sole H1** when present, as previously decided for the portfolio page; project pages should have a single clear H1 (the project title) and then use `h2`/`h3` for subsections.  
     - Treat **project card hero images as decorative** with `alt=""`, since title and summary are already exposed as text.  
     - Keep the JS **light but robust**: basic guards for 0–1 images, and avoid complex or brittle behavior. Maximize look and features but not at the expense of frontloading ourselves with debugging before system is stable, especially for features that might be tricky but can be easily added in later.






_includes\section.html questions:

1) Root element for _includes/section.html
   - **Question:** What should the root element of `section.html` be?
     - (a) Use a `<section>` element with a base class (e.g., `class="section"`).
     - (b) Use a `<div>` element with a base class (e.g., `class="section"`).
     - (c) Prefer `<section>`, but allow callers to override to `<div>` via a parameter.
     - (d) Something else (describe).
   - **Answer:** (a) Use a `<section>` with a base `"section"` class
   - **Rationale:** Everywhere we’ve discussed this include, we’ve treated it as a *semantic section band* that wraps major page regions (portfolio lead, portfolio grid, future “about” blocks) rather than a generic div. The CSS is class-driven (`.section`, `.section-inner`, modifiers like `.section--surface`), so the choice is mostly about semantics; using `<section class="section …">` matches that intent and keeps the mental model clean without adding any extra complexity.

2) API for classes
   - **Question:** How should classes be applied on the outer wrapper?
     - (a) Every section always has the base `"section"` class; the include MERGES any passed class, so `class="section section--surface"` when you call `class="section--surface"`.
     - (b) Passed class COMPLETELY replaces the base; `section.html` does NOT automatically add `"section"`.
     - (c) Provide two parameters: `base_class` and `modifier_class`; `section.html` assembles them.
     - (d) Another pattern you prefer (describe).
   - **Answer:** (a) Always include `"section"`, merge any passed classes
   - **Rationale:** This lines up with your earlier decision for the section include API: pass CSS classes directly and keep the include thin, with `.section` as the stable base hook and modifiers like `.section--surface` layered on top. Automatically merging `"section"` with any caller-supplied classes keeps all sections opt-in to the same spacing/width system while still letting you add variants per use case.

3) Inner container customization
   - **Question:** How configurable should the `.section-inner` container be?
     - (a) Only the outer wrapper is configurable; inner uses a fixed class (e.g., `"section-inner"`).
     - (b) Allow an optional `inner_class` parameter to append classes to the inner wrapper.
     - (c) Allow both outer and inner classes to be fully controlled by the caller.
     - (d) You have a strong preference to keep the include as minimal as possible (outer only).
   - **Answer:** (a) Fixed `"section-inner"`; only outer configurable
   - **Rationale:** So far, all planned uses of `section.html` (portfolio lead + grid bands, future simple sections) share the same inner behavior: centered, max-width container with consistent vertical rhythm. You’ve consistently favored “thin, generic wrapper + direct class control” without extra abstraction layers. Locking `section-inner` in the include keeps it predictable and leverages the existing CSS, while outer class control is enough to handle visual variants like `.section--surface`.

4) Optional content handling for portfolio list
   - **Question:** For V1, when implementing the portfolio list page, how strict should we be about data presence?
     - (a) Assume `page_lead` and `projects` are always present and non-empty; fail loudly if not.
     - (b) Skip the lead section if `page_lead` is missing/blank, but assume `projects` always exist.
     - (c) Skip both lead and grid gracefully if their data is missing (no visible errors).
     - (d) Another specific rule set (describe how strict you want this to be).
   - **Answer:** (b) Skip lead if missing; assume projects always exist
   - **Rationale:** You’ve already treated `page_lead` as optional “nice to have” text on `/portfolio/`, but the `projects:` list is the entire purpose of the page and you’ve committed to curating it. That matches a minimal-guards posture: treat the grid as required content (you maintain the data), but avoid rendering an empty lead wrapper when `page_lead` is omitted.

5) ID and anchors on sections
   - **Question:** How should IDs for in-page anchors be handled on sections?
     - (a) Add an optional `id=` parameter to `section.html` and apply it to the root wrapper now.
     - (b) Skip ID support for V1; you don’t anticipate in-page anchors.
     - (c) Add ID support only for known cases (e.g., portfolio list grid), not as a generic parameter.
     - (d) Other (describe).
   - **Answer:** Add an optional id= parameter to section.html
   - **Rationale:** It’s basically free in terms of complexity, keeps section.html generic, and gives you future flexibility for “jump to section” links, skip links, or in-page navigation without having to redesign anything later.

6) Accessibility / semantics expectations
   - **Question:** How much accessibility behavior should be baked into `section.html` itself?
     - (a) You want `section.html` to stay “dumb”: no ARIA attributes, no assumptions about headings.
     - (b) You want a light pattern (e.g., optional `aria_label` parameter mapped to `aria-label` on the root).
     - (c) You’d like a stronger pattern tying sections to headings (we’d document how to use it).
     - (d) You’re not sure yet; prefer we keep it minimal and revisit once layouts are in place.
   - **Answer:** (a) Keep `section.html` “dumb”
   - **Rationale:** Your earlier decisions around headings and semantics were focused on *where* the true H1 lives (banner vs body) and keeping images either meaningful or explicitly decorative, not on centralizing ARIA in shared includes. Given that `section.html` is already positioned as a thin layout utility, it’s safer to avoid baking in ARIA or heading rules prematurely and let each layout or page author supply semantics where they actually know the content.



1) Section wrapper element
   How should section.html render its outer wrapper by default?
   a) Always use <section class="section …"> for semantics/landmarks.
   b) Use <section> by default, but allow an override (e.g., include.tag = "div").
   c) Always use <div class="section …"> and keep semantics in the calling layout/Markdown.
   d) Something else (briefly describe).
   - **Answer:** (a) Always use `<section class="section …">`
   - **Rationale:** Everywhere we’ve talked about `section.html`, we’ve been treating it as a “page band” wrapper for major regions (portfolio lead, portfolio grid, future sections), not as a generic div. The CSS is built around `.section` / `.section-inner`, and using a semantic `<section>` for those bands matches how the portfolio page is structured under the banner. There’s no strong need for tag overrides in this site, so a consistent `<section class="section …">` keeps things simple and predictable.

2) Class handling for include.class
   When a caller passes class="section--surface", what do you want the final class attribute to be?
   a) Always prepend the base class: class="section section--surface".
   b) Use exactly the string passed in include.class (no automatic "section" base class).
   c) Prepend "section" by default, but allow an opt-out flag if needed later.
   d) Another convention (describe).
   - **Answer:** (a) Always prepend the base class
   - **Rationale:** Your layouts already assume `.section` is the baseline spacing/width hook, and modifiers like `.section--surface` are layered on top (as in the portfolio grid band). Having `section.html` always output `class="section …"` guarantees all sections get the core layout behavior, while the caller can freely tack on modifiers (`section--surface`, future `section--tight`, etc.). This matches how you’re calling it now on the portfolio page and keeps the include “thin” but safe.

3) Additional attributes
   Do you want section.html to support extra attributes right away?
   a) Yes — support include.id (for id="…") and include.aria_label (for aria-label="…").
   b) Yes — but only id for now (no ARIA attributes yet).
   c) No — keep the include minimal: only class + content, add more later if needed.
   d) Other (describe what attributes you’d like to support).
   - **Answer:** (b) Support `id` now, skip ARIA for V1
   - **Rationale:** We already discussed IDs for anchors: they’re occasionally useful (e.g., linking to `#portfolio-grid` from a button), and adding an optional `id` parameter is almost zero complexity. At the same time, you’ve been clear that `section.html` should stay “dumb” and not hard-code ARIA patterns. So: `include.id` → `id="…"`, but keep ARIA decisions in specific layouts/markup where the context is clearer.

4) page_lead semantics (locking in the decision)
   For page.page_lead on the portfolio list page (and any future pages that use it), what’s the intended long-term behavior?
   a) Treat page_lead as Markdown and always run it through markdownify (current implementation).
   b) Treat page_lead as plain text only (no Markdown rendering).
   c) Allow Markdown but constrain usage (e.g., inline formatting + links only, documented convention).
   d) Something else (explain).
   - **Answer:** (a) Treat `page_lead` as Markdown (markdownify)
   - **Rationale:** You’re already rendering the portfolio lead with `{{ page.page_lead | markdownify }}`, and we explicitly chose Markdown so you can add links and light emphasis without cluttering front matter with HTML. In practice you’ll use it like a short paragraph or two with occasional inline links, which naturally fits “Markdown first; be sensible in authoring” without extra template rules.

5) Behavior when content is missing
   If, for some reason, section.html is called without a meaningful include.content value, what should it do?
   a) Render nothing (no outer wrapper at all if content is blank/nil).
   b) Still render the wrapper but allow it to be empty.
   c) Assume callers will always guard; we don’t add any checks in section.html.
   d) Other (describe your preferred behavior).
   - **Answer:** (c) Assume callers guard; `section.html` doesn’t add checks
   - **Rationale:** On the portfolio page you’re already guarding at the layout level (`{% if page.page_lead %}`, `{% if page.projects and page.projects.size > 0 %}`) before calling `section.html`. That matches your general approach: “assume valid data, add light guards at the layout/template level when it clearly prevents weird output.” Keeping `section.html` as a dumb wrapper (no extra branching) makes it easier to reason about. If someone forgets to guard and passes empty content, the worst case is an empty band that’s immediately obvious and easy to fix.

6) Vertical spacing and adjacency of sections on the portfolio page
   For the combination of lead + grid on /portfolio/, how do you want the spacing between those two sections to feel?
   a) Keep them as two fully separated sections using the default .section padding (current behavior).
   b) Default .section padding for the lead, but tighten the grid section using a modifier (e.g., section--tight).
   c) Visually merge the lead and grid into a single band by using flush modifiers (e.g., section--flush-bottom / section--flush-top).
   d) You’re not sure yet — keep current behavior, but design section.html to support these modifiers cleanly.
   - **Answer:** (a) Keep them as two fully separated sections using the default `.section` padding  
   - **Rationale:** This matches our current layouts, uses the established vertical rhythm provided by `.section`, preserves the visual distinction between the neutral lead band and the surface-styled project grid band, and avoids introducing modifier classes prematurely. It keeps the layout predictable, aligns with our existing aesthetic decisions, and maintains future flexibility if spacing adjustments are ever needed.





1. Card click target
   How should the card markup be structured for clickability?
   a) Make `.project-card` an <a> wrapping the entire card (hero + text).
   b) Use a semantic wrapper (<article> or <div>.project-card) with only the title as an <a>.
   c) Use a wrapper <article> and wrap both hero image and title in a single inner <a>.
   d) Something else (describe).
   - **Answer:** (a) Make `.project-card` an `<a>` wrapping the entire card  
   - **Rationale:** The CSS already treats `.project-card` as a single interactive unit, with hover/active states on the card wrapper and a note that it may be an `<a>`. Making the entire card clickable is consistent with that design, gives a clear, large hit target, and avoids duplicating link targets on both the image and title. It also keeps the DOM simple and predictable for screen readers and keyboard users.

2. Project URL construction
   How should we build the link to each project detail page?
   a) Use the Jekyll URL property: href="{{ site.baseurl }}{{ project.url }}".
   b) Manually construct from the slug: href="{{ site.baseurl }}/portfolio/projects/{{ slug }}/".
   c) Support both via some conditional logic.
   d) You have a different preferred pattern.
   - **Answer:** (a) Use `href="{{ site.baseurl }}{{ project.url }}"`  
   - **Rationale:** Jekyll already computes a stable `url` for each project page based on its folder structure. Using `{{ project.url }}` and prefixing `{{ site.baseurl }}` matches how image/model paths are handled elsewhere and makes the grid resilient to any future changes in folder structure or collection setup. It keeps the slug resolution logic in one place (finding the project page) and lets Jekyll own the final URL format.

3. Required front matter vs. guards
   For V1, can we assume all listed projects have complete front matter (hero, title, summary)?
   a) Yes – assume complete data; no extra guards beyond basic presence checks in layouts.
   b) Mostly yes – but if hero is missing, hide the image block gracefully.
   c) No – please add lightweight guards for missing hero/summary/title.
   d) Other (describe your tolerance for “fail loud” vs “degrade gracefully”).
   - **Answer:** (a) Yes – assume complete data with only light presence checks  
   - **Rationale:** You’ve already committed to keeping all project assets and fields complete for V1 (including images and model fields) and prefer “assume valid data, minimal guards.” For cards, `title`, `summary`, and `hero` are core to the design and authored once in each project’s `index.md`. It’s reasonable to assume they exist for any project listed in `projects:`, with only basic checks (e.g., skip a card entirely if its page cannot be resolved) rather than complex per-field fallback behavior.

4. Hero alt text source
   Where should card hero <img> alt text come from by default?
   a) The caption of the matching image in the project’s `images:` front matter, if found; else fall back to project.title.
   b) Always project.title (ignore image captions).
   c) A dedicated front matter field (e.g., hero_alt) if present; else fall back to (a) or (b).
   d) You’re not sure yet; design card markup so the alt source is easy to change later.
   - **Answer:** (d) Something else: treat the card hero as decorative (`alt=""`)  
   - **Rationale:** For cards, the title and summary already expose the essential information as text, and the hero image acts primarily as a visual cue. You’ve previously chosen to treat card hero images as decorative for accessibility, which avoids redundant, noisy screen reader output. Using `alt=""` is the cleanest implementation and consistent with that prior decision; the template can be written so that swapping to a caption/title-based alt later would be straightforward if you change your mind.

5. Summary length handling
   How should we treat long `summary` text on cards?
   a) Trust author discipline – no truncation logic; render whatever is in `summary`.
   b) Use a purely CSS-based visual clamp (e.g., 2–3 lines) without changing the underlying HTML.
   c) Implement text truncation in Liquid (e.g., `truncatewords`).
   d) Other (describe).
   - **Answer:** (a) Trust author discipline; no truncation in templates  
   - **Rationale:** This is a single-author, tightly controlled site where you manage all front matter. Your general approach is to keep templates simple, assume well-formed content, and add only minimal guards. It’s easy to keep `summary` concise by editing content directly, and adding clamp/truncation logic now would increase complexity for marginal benefit. If summaries ever start to drift long, a future CSS clamp would be the first tool to reach for.

6. Empty or missing `projects:` list
   If `portfolio/index.md` has no `projects:` or an empty list, what should happen?
   a) Render nothing for the grid section (current behavior) – page just shows the lead text.
   b) Render a short “No projects to display yet.” message inside a section.
   c) Treat this as a configuration error and make it visually obvious something is wrong.
   d) Other (describe).
   - **Answer:** (a) Render nothing for the grid section  
   - **Rationale:** The portfolio list page’s primary purpose is to show projects, and you’ve already committed to curating the `projects:` list as part of maintaining the site. Treating an empty list as a content/config issue rather than a user-facing state keeps the UX clean and matches your “minimal guards” philosophy. The existing layout (`if page.projects and page.projects.size > 0`) already implements this behavior: no `projects:` means no grid, only the lead (if any).

7. Future metadata on cards (for V2)
   Do you anticipate wanting extra metadata on project cards (e.g., year, domain tags, repository links)?
   - If yes, which 1–2 fields are most important to reserve visual/structural room for?
   - If no, confirm you want cards to stay strictly “hero image + title + summary” for V1 and likely V2.
   - **Answer:** No — keep cards strictly “hero + title + summary” for V1 and likely V2.
   - **Rationale:** There’s no need to pre-allocate space now. If metadata becomes useful later (e.g., year, tags, repo link), adding a small metadata row in `_includes/project-card.html` is trivial and will only require a small CSS adjustment. Reserving empty structure today would complicate the layout without a clear purpose, whereas adding metadata in V2 is a low-cost, low-risk change.





This was the old version:
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
and the new:
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
  {% capture lead_html %}
    <div class="portfolio-lead">
      {{ page.page_lead | markdownify }}
    </div>
  {% endcapture %}
  {% include section.html content=lead_html %}
{% endif %}

<!-- ========================================= -->
<!-- PROJECT GRID SECTION                      -->
<!-- Main portfolio listing area               -->
<!-- ========================================= -->
{% if page.projects and page.projects.size > 0 %}
<section class="section section--surface">
  <div class="section-inner">
    {% include project-grid.html projects=page.projects %}
  </div>
</section>
{% endif %}