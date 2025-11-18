# HUMAN NOTES

### Random
^#[ ]\S+

### List of project slugs
nc4touch-behavioral-apparatus
omniroute-maze-system
instantaneous-cue-rotation-arena
track-mounted-feeder-cart
nc4gate-automatable-gate-module
two-axis-feeder-gantry
adjustable-aluminum-projector-mount
wireless-mobile-feeder-robot
silicon-probe-microdrive-housing
dual-bundle-electrode-drive
fischer-344-rat-model
roller-bearing-cable-guide

#### Personal projects
modular-rolling-tool-wall
hidden-drawer-nightstand
adjustable-tv-easel-stand
foldable-adjustable-painting-easel


### 3D Model Conversion

**SolidWorks SLDPRT/SLDASM → STEP AP214 using SolidWorks Assistant**
- Export SolidWorks parts/assemblies as STEP AP214 (`.step`) **with these STEP options**:
  - File format: `STEP`
  - Output as: `Solid / Surface geometry`
  - Set STEP configuration data: `OFF`
  - Export face/edge properties: `ON`
  - Split periodic faces: `ON`
  - Export 3D curve features: `ON`
  - Output coordinate system: `Default`

**Convert STEP to glTF (.glb) using CAD Assistant:**
- Open STEP in **CAD Assistant** (no special import options; use defaults).
- In CAD Assistant, **Save As → glTF 2.0 (Binary .glb)** with:
  - Format: `glTF 2.0` → `Binary (.glb)`
  - Units: `From source` (millimeters from STEP)
  - Transformation format: `Compact`
  - Node name format: `InstanceOrProduct`
  - Mesh name format: `Product`
  - Export UV for elements without texture maps: `OFF`
  - Merge faces within the same part: `ON`
  - Merge faces within 16-bit indices limit: `ON`

**(Optional) Make faces transparent in Blender 4.3.2:**
- Import the `.glb` into Blender: **File → Import → glTF 2.0 (.glb/.gltf)**
- Select each object that should be semi-transparent:
  - In **Material Properties → Surface → Principled BSDF**, lower **Alpha** from `1.0` to `0.1` (or desired value)
  - In **Material Properties → Settings → Surface**, set **Render Method** to `Blended`
- Export back to `.glb`: **File → Export → glTF 2.0** with:
  - **Format:** `glTF Binary (.glb)`
  - **Include → Data:** uncheck `Cameras` and `Punctual Lights`
  - **Compression:** check `Compression` (keep the default numeric values)
  - **Animation:** uncheck `Animation`

## Styling

### Font Stack Options (Personal Notes)

Two recommended approaches for defining global typography in `assets/css/custom.css`. These declarations go inside a top-level `:root` block and are used to set the default fonts for the entire site.

#### Option A — System UI Sans-Serif (Fast + Clean)
Uses native OS fonts (San Francisco, Segoe UI, Roboto) for a modern, high-performance look. No webfonts to load.
```css
:root {
  --ff-body: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --ff-heading: var(--ff-body);
}
```
Context:
This mirrors the stack used on the reference site and provides excellent readability with zero load time. Ideal default choice for a technical portfolio.

#### Option B — Inter Webfont Heading (More Designed)
Loads the Inter font for headings and uses it throughout via cascading fallbacks.
```css
:root {
  --ff-heading: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --ff-body: var(--ff-heading);
}
```
Context:
Inter is a polished, modern sans-serif with strong legibility. This adds a more refined visual tone but requires importing a webfont (minor performance cost).

## To Do

Files & directories to add before enabling GitHub Pages:

1. _config.yml
   - Minimal Jekyll config with:
     - url: "https://adamwlester.github.io"
     - baseurl: "/awl-site"  (or current repo name)
     - exclude: [.github/, .vscode/, README.md, etc.]

2. _layouts/default.html
   - Base HTML shell with global header, {{ content }}, and link to assets/css/custom.css.

3. _layouts/portfolio-list-page.html
   - Front matter: layout: default
   - Simple wrapper around {{ content }}.

4. _layouts/project-detail-page.html
   - Front matter: layout: default
   - Simple wrapper around {{ content }}.

5. _includes/section.html
   - Simple section wrapper stub.

6. _includes/project-grid.html
   - Basic stub container for project grid.

7. _includes/project-card.html
   - Basic stub container for individual project cards.

8. assets/css/custom.css
   - Minimal base stylesheet (just enough to avoid a broken layout).

9. docs/
   - Add CV.pdf and Resume.pdf *if* linked from the header; otherwise skip or remove links.

10. Front matter checks (edits only):
    - index.md → layout: default, title: "Home"
    - portfolio/index.md → layout: portfolio-list-page, title: "Portfolio"
    - each project’s index.md → layout: project-detail-page

