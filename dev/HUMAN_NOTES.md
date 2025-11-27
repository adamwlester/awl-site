# HUMAN NOTES

### Random
^#[ ]\S+
^##[ ]\S+

### List of project slugs
nc4touch-behavioral-apparatus
omniroute-maze-system
instantaneous-cue-rotation-arena
track-mounted-feeder-cart
nc4gate-automatable-gate-module
two-axis-feeder-gantry
adjustable-projector-mount
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

_config.yml
_assets/css/custom.css
_layouts/default.html
_layouts/portfolio-list-page.html
_layouts/project-detail-page.html
_includes/section.html
_includes/project-grid.html
_includes/project-card.html


## Layout Schematic

======================================================================
DESKTOP LAYOUT (wide screens)
======================================================================

Viewport / page width
┌───────────────────────────────────────────────────────────────────┐
│                      [ IMAGE VIEWER / CAROUSEL ]                  │
│   - Uses front matter: images[] (hero + additional images)        │
│   - Full-width "hero" media band at the top of the project page   │
└───────────────────────────────────────────────────────────────────┘


Two-column project content area
┌───────────────────────────────┬───────────────────────────────────┐
│           LEFT COLUMN         │             RIGHT COLUMN          │
│        (.project-main)        │         (.project-aside)          │
│                               │                                   │
│  ┌─────────────────────────┐  │  ┌─────────────────────────────┐  │
│  │   PROJECT TITLE         │  │  │      [ 3D VIEWER PANEL ]    │  │
│  │   (page.title)          │  │  │   (.model-viewer-panel)     │  │
│  └─────────────────────────┘  │  │  - <model-viewer> element   │  │
│                               │  │  - Uses: model_src,         │  │
│  ┌─────────────────────────┐  │  │          model_camera_*     │  │
│  │   PROJECT SUMMARY       │  │  └─────────────────────────────┘  │
│  │   (page.summary)        │  │                                   │
│  └─────────────────────────┘  │  ┌─────────────────────────────┐  │
│                               │  │   SECONDARY CONTENT         │  │
│  ┌─────────────────────────┐  │  │   (Right-column sections    │  │
│  │   PRIMARY CONTENT       │  │  │    from content body)       │  │
│  │   (Left-column sections │  │  └─────────────────────────────┘  │
│  │    from content body)   │  │                                   │
│  └─────────────────────────┘  │                                   │
│                               │                                   │
└───────────────────────────────┴───────────────────────────────────┘

High-level desktop structure:
- Top band:  full-width image viewer
- Below:     CSS grid with two columns
  - Left:    title + summary + primary narrative sections
  - Right:   3D viewer panel on top, secondary sections below it


======================================================================
MOBILE LAYOUT (narrow screens)
======================================================================

All elements stack vertically in *this* order,
and the DOM order matches this sequence.

┌───────────────────────────────────────────────────────────────────┐
│ [1] IMAGE VIEWER / CAROUSEL                                       │
│     - Full width                                                  │
│     - media from images[]                                         │
└───────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────┐
│ [2] 3D VIEWER PANEL                                               │
│     - .model-viewer-panel                                         │
│     - <model-viewer> using model_src, model_camera_*              │
└───────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────┐
│ [3] LEFT-COLUMN NARRATIVE BLOCK                                   │
│     - PROJECT TITLE (page.title)                                  │
│     - PROJECT SUMMARY (page.summary)                              │
│     - PRIMARY CONTENT SECTIONS (from content body,                │
│       e.g. Description, Design Goals, Implementation, etc.)       │
└───────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────┐
│ [4] RIGHT-COLUMN NARRATIVE BLOCK                                  │
│     - SECONDARY CONTENT SECTIONS (from content body,              │
│       e.g. Role & Contributions, Collaboration, Links, etc.)      │
└───────────────────────────────────────────────────────────────────┘

So in mobile order (top → bottom):

  1. Image viewer (media carousel)
  2. 3D viewer panel
  3. Left narrative (title + summary + primary sections)
  4. Right narrative (secondary sections)

This *same* sequence is the DOM order, and desktop CSS uses a grid to
place:
- Left narrative into the left column,
- 3D viewer + secondary sections into the right column,
while preserving this underlying stacking order for small screens and
assistive tech.


























PROJECT: Adjustable Aluminum Projector Mount
description: "Adjustable aluminum projector mount for precise alignment of short-throw projectors in behavioral arenas."
summary: "Adjustable aluminum projector mount for precise alignment of short-throw projectors in behavioral arenas."


PROJECT: Dual-Bundle Electrode Drive
description: "Split-bundle implant for dual-region tetrode recordings in freely moving rats."
summary: "Split-bundle implant for dual-region tetrode recordings in freely moving rats."


PROJECT: Fischer 344 Rat Model
description: "To-scale 3D model of a Fischer 344 laboratory rat for design planning, visualization, and demonstration of behavioral systems."
summary: "To-scale 3D model of a Fischer 344 laboratory rat for design planning, visualization, and demonstration of behavioral systems."


PROJECT: Instantaneous Cue Rotation Arena
description: "An augmented reality behavioral arena for studying cue-based navigation in freely moving rats."
summary: "An augmented reality behavioral arena for studying cue-based navigation in freely moving rats."


PROJECT: NC4gate Automatable Gate Module
description: "Modular motorized gate system for autonomous control of rodent behavior in maze experiments."
summary: "Modular motorized gate system for autonomous control of rodent behavior in maze experiments."


PROJECT: NC4touch Behavioral Apparatus
description: "Touchscreen-based behavioral apparatus for flexible, high-throughput cognitive testing with mice and rats."
summary: "Touchscreen-based behavioral apparatus for flexible, high-throughput cognitive testing with mice and rats."


PROJECT: Omniroute Maze System
description: "A dynamically reconfigurable rodent maze system that integrates automated route configurations, sensory cue control, and targeted reward delivery."
summary: "A dynamically reconfigurable rodent maze system that integrates automated route configurations, sensory cue control, and targeted reward delivery."


PROJECT: Roller-Bearing Cable Guide
description: "Compact, low-torsion cable guide with a bearing-mounted collet and dual-rail carriage for quiet, low-resistance travel in tethered rodent recordings."
summary: "Compact, low-torsion cable guide with a bearing-mounted collet and dual-rail carriage for quiet, low-resistance travel in tethered rodent recordings."


PROJECT: Silicon Probe Microdrive Housing
description: "Implantable housing for high-density chronic silicon probe recordings in freely moving rats."
summary: "Implantable housing for high-density chronic silicon probe recordings in freely moving rats."


PROJECT: Track-Mounted Feeder Cart
description: "Mobile feeder cart for controlled on-track liquid reinforcement with gated feeder access for rodent circular track experiments"
summary: "Mobile feeder cart for controlled on-track liquid reinforcement with gated feeder access for rodent circular track experiments"


PROJECT: Two-Axis Feeder Gantry
description: "CNC-based gantry system for automated spatially targeted reward delivery in rodent open-field experiments."
summary: "CNC-based gantry system for automated spatially targeted reward delivery in rodent open-field experiments."


PROJECT: Wireless Mobile Feeder Robot
description: "A mobile feeder robot for delivering liquid rewards to rats during circular track experiments"
summary: "A mobile feeder robot for delivering liquid rewards to rats during circular track experiments"






"Omniroute Maze System: rodent maze with fully automatable routes, cues, and reward delivery" 
:contentReference[oaicite:0]{index=0}

"90 × 90 cm rat maze with 60 motorized gates (NC4gate), 4 projectors for floor and gate-face visual cues, XY liquid-reward gantry, real-time 3D tracking, and unified closed-loop control via ROS" 
:contentReference[oaicite:1]{index=1}

"90x90 cm rat maze with 60 addressable gates (NC4gate), projected cues, 3D tracking, XY feeder gantry, and ROS control" 
:contentReference[oaicite:2]{index=2}

"A dynamically reconfigurable rodent maze integrating automated route configuration, projected sensory cues on the maze walls and floor, and spatially targeted reward delivery."
:contentReference[oaicite:3]{index=3}

"An open-source real-world navigation platform that combines dynamically reconfigurable routes via 60 motorized gates, projector-based visual and auditory cues, and an XY reward gantry with real-time 3D tracking and closed-loop control."
:contentReference[oaicite:4]{index=4}


"Modular three-screen touchscreen chamber for high-throughput cognitive testing in mice and rats." 
:contentReference[oaicite:5]{index=5}

"Three 3.5″ 320×480 capacitive touchscreens, automated liquid reward, overhead video, and multi-chamber Raspberry Pi-based real-time closed-loop control." 
:contentReference[oaicite:6]{index=6}

"3-touchscreen chamber for mice and rats with automated reward, overhead video, and multi-chamber Raspberry Pi-based control." 
:contentReference[oaicite:7]{index=7}

"NC4touch Behavioral Apparatus: touchscreen chamber for mouse and rat experiments." 
:contentReference[oaicite:8]{index=8}


"NC4gate Automatable Gate Module: an addressable motorized gate for programmatically configurable rodent mazes" 
:contentReference[oaicite:9]{index=9}

"Compact motorized gate module for autonomous maze configuration and dynamic behavioral control." 
:contentReference[oaicite:10]{index=10}

"Open-source NC4gate modular gate system for autonomous maze control with robust, low-cost hardware and a Python API and Qt GUI enabling control of up to 512 gates." 
:contentReference[oaicite:11]{index=11}


"Instantaneous Cue Rotation (ICR) Arena: augmented-reality rodent behavioral apparatus" 
:contentReference[oaicite:12]{index=12}

"Augmented-reality rodent arena enabling instantaneous rotation of a 360° panorama of visual cues during ongoing circular track navigation." 
:contentReference[oaicite:13]{index=13}

"1.4 m circular track with 68 cm rear-projection walls displaying a 360° cue panorama from 4 short-throw projectors." 
:contentReference[oaicite:14]{index=14}

"An augmented-reality method that remotely and instantaneously rotates all orienting visual cues during ongoing real-world navigation." 
:contentReference[oaicite:15]{index=15}


"Wireless Mobile Feeder Robot: Wireless cart subsystem for the ICR that tracks the rat and delivers liquid reward via a retractable dish." 
:contentReference[oaicite:16]{index=16}

"A mobile feeder robot for delivering liquid rewards to rats during circular track experiments."
:contentReference[oaicite:17]{index=17}

"Tracks rats on a circular track and delivers precisely timed, spatially targeted liquid food rewards." 
:contentReference[oaicite:18]{index=18}


"CNC-based gantry system for automated, spatially targeted liquid reward delivery in the Omniroute maze." 
:contentReference[oaicite:19]{index=19}

"XY gantry for automated spatially targeted reward delivery, developed for the Omniroute." 
:contentReference[oaicite:20]{index=20}


"Servo-gated mobile feeder with IR sensing for automated reward delivery, developed for use in the NC4 rodent VR Dome apparatus." 
:contentReference[oaicite:21]{index=21}

"Mobile feeder cart for controlled on-track liquid reinforcement with gated feeder access for rodent circular track experiments." 
:contentReference[oaicite:22]{index=22}


"Split-bundle implant for dual-region tetrode recordings in freely moving rats." 
:contentReference[oaicite:23]{index=23}

"18-shuttle implantable drive with independent depth control and bundle positioning for dual-site electrode recordings in freely moving rats." 
:contentReference[oaicite:24]{index=24}


"Implantable housing for high-density chronic silicon probe recordings in freely moving rats." 
:contentReference[oaicite:25]{index=25}

"Lightweight 3D-printed implantable housing for chronic silicon probe recordings with integrated Cambridge Neurotech NanoDrive adjustment." 
:contentReference[oaicite:26]{index=26}


"Compact, low-torsion cable guide with a bearing-mounted collet and dual-rail carriage for quiet, low-resistance travel in tethered rodent recordings." 
:contentReference[oaicite:27]{index=27}


"To-scale 3D model of a Fischer 344 laboratory rat for design planning, visualization, and demonstration of behavioral systems." 
:contentReference[oaicite:28]{index=28}


"Adjustable aluminum projector mount for precise alignment of short-throw projectors in behavioral arenas." 
:contentReference[oaicite:29]{index=29}





"I lead the end-to-end design and delivery of research instruments and hardware-software platforms." 
:contentReference[oaicite:30]{index=30}

"I’ve scoped, architected, built, and validated more than ten instruments in active use, including three standalone behavioral systems released as open source." 
:contentReference[oaicite:31]{index=31}

"Full-stack skills for building and deploying research instruments and end-to-end platforms." 
:contentReference[oaicite:32]{index=32}

"Integrated closed-loop research systems, with portfolio links." 
:contentReference[oaicite:33]{index=33}

"Behavioral platforms – fully integrated HW–SW systems for rodent behavioral neuroscience." 
:contentReference[oaicite:34]{index=34}

"Subsystems and instruments developed for real-time behavioral control, electrophysiology, and automated reward delivery."  
(from combined context)
