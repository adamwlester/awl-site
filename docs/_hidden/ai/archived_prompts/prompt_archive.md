# 1: (Copilot) Scaffolding

You are operating in the root of my website repo.

Task:
Inside the existing folder `portfolio/projects/`, create one folder for each of the following slugs:

- roller-bearing-cable-guide
- dual-bundle-electrode-drive
- silicon-probe-microdrive-housing
- fischer-344-rat-model
- wireless-mobile-feeder-robot
- adjustable-aluminum-projector-mount
- two-axis-feeder-gantry
- nc4gate-automatable-gate-module
- track-mounted-feeder-cart
- instantaneous-cue-rotation-arena
- omniroute-maze-system
- nc4touch-behavioral-apparatus

For EACH of these project folders, do the following:
1. Ensure there is an `images/` subfolder.
2. Ensure there is a `models/` subfolder.
3. Create an empty `index.md` file directly inside the project folder (alongside `images` and `models`), if it does not already exist.

Constraints / guardrails:
- Only modify the `portfolio/projects/` directory and its subfolders.
- Do NOT rename or delete any existing files or folders.
- If any of these folders, subfolders, or `index.md` files already exist, leave their existing contents as-is.
- Use relative paths from the repo root, not absolute system paths.

When you’re done, show me the final directory tree for `portfolio/projects/`.

# 2: (ChatGPT) Random

I think you have it.

Now, can you rewrite this section, being careful to use the terms we have established. Get the elements and layout clear. What I want is for you to write out what I have already in a normal out of code block response and bold the parts you think need to be changed. Then explain why.


Review my makdwown up to this point. I need to start adding to the "Project List Page Overview" section. Please take a look at the wireframe and see if you can parse the details of what I am after for this page. We want to use a similar structure to "Project Detail Page Overview" but it should be easier to outline this page.

# 3: (ChatGPT) Markdown conversion for index.md

You are transforming project markdown files into the new portfolio website format.  
Below is the COMPLETE specification of how every project file must be transformed.  
After reading this, you will summarize your understanding.  
AFTER the summary, you will wait for me to provide the original markdown to transform.  
When I provide the original markdown, you will output ONLY the final transformed file in a single fenced code block.

---

# ️REFERENCE EXAMPLES (OLD → NEW)

## OLD FORMAT (NC4touch example)
<<< OLD_NC4TOUCH_MARKDOWN_HERE >>>

## NEW FORMAT (NC4touch example)
<<< NEW_NC4TOUCH_MARKDOWN_HERE >>>

Use these examples to infer formatting conventions, indentation, list behavior, heading style, and section flow.  
BUT ALWAYS follow the explicit rules given below if the example and rules differ.

---

# ️REQUIRED TRANSFORMATION RULES

## 1. FRONT MATTER CONSTRUCTION
Generate a YAML front matter block at the top of the file:

```yaml
---
layout: project-detail-page
title: "<Project Title>"
summary: "<One-sentence summary previously under ## Summary>"
hero: "images/render_1.png"
model: "models/<slug>.glb"
images:
  - src: "<image filename>"
    caption: "<caption text>"
  - ...
---
