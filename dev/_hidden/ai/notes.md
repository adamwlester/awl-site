# High-Level Overview of the Copilot Agent Interface (2025 VS Code)
====================================================================

1. **The Copilot Agent Panel**
------------------------------

This is the sidebar panel where you interact with the agent.  
It has three core modes (top-left dropdown):

### **● Ask**

Freeform chat.  
You give instructions, ask questions, and Copilot responds.  
This is NOT guaranteed to change files—just chat output.

### **● Edit**

You give a request, and Copilot proposes a specific code/workspace change.  
It generates a diff you can apply or modify.  
Think: _“Change this file,” “Refactor this block,” “Add folders,”_ etc.

### **● Plan**

Copilot generates a _multi-step_ plan for a larger task before editing.  
Think: scaffolding a complex directory, renaming components, reorganizing modules.  
You approve steps before execution.

This is closest to “Agent Mode” from the promotional material.

* * *

2. **“Add Content” Button in the Chat Editor**
==============================================

This is **NOT persistent instructions**.

It lets you inject:

* File excerpts
    
* Entire files
    
* Terminal output
    
* Folder trees
    
* Arbitrary text
    

into the chat context _for that one conversation_.  
It does **not** get stored between sessions, and does not behave like system prompts.

Think of it as a way to give Copilot “context snapshots” manually.

* * *

3. **Persistent Instructions**
==============================

Right now, Copilot in VS Code **does not have a true native persistent system prompt** like ChatGPT’s “Customize ChatGPT.”

But you have **two partial systems** that approximate persistence:

* * *

**Option A — Workspace Instructions in VS Code (Copilot Agent)**
----------------------------------------------------------
To generate the workspace-level instruction file used by Copilot:

1. Open the **Command Palette** (`Ctrl+Shift+P`).
2. Run: **Chat: Generate Workspace Instructions File**.
3. VS Code will automatically create the proper instruction file in the correct location for the current workspace.
4. The file becomes the authoritative, persistent set of rules Copilot Agent uses for all chat, plan, and edit operations within this project.

* * *

**Option B — Repository-Level Config Files**
--------------------------------------------

Copilot will automatically consume structured metadata from:

```
.vscode/settings.json
.vscode/copilot-instructions.md
README.md
CONTRIBUTING.md
```

This is an indirect way to give persistent context.

You cannot place “agent instructions” in arbitrary folders and expect VS Code to read them, but README/CONTRIBUTING are often used as soft guidance.

* * *

4. **No Built-in Repo-Wide System Prompt Directory**
====================================================

There is **no** mechanism like:

```
repo/
  .copilot-system/
    instructions.md
```

Copilot does not scan arbitrary directories for instructions.

The only reliable persistent mechanism today is:

### → `.vscode/copilot-instructions.md`

Everything else is temporary or informal.

* * *

5. **How the Agent Uses the Instruction Layers**
================================================

Here is the priority hierarchy (roughly):

1. **Workspace instructions** (persistent; strongest override)
    
2. **File context** (open files, cursor position)
    
3. **Added Content** (manual context injection)
    
4. **Conversation history**
    
5. **Repo structure / README**
    
6. Copilot defaults
    

* * *

6. **How You Should Set Up Persistent Instructions for Your Portfolio Project**
===============================================================================

You want a centralized persistent instruction layer.

Do this:

### Step 1 — Add persistent workspace instructions

From VS Code:

```
Command Palette → "Copilot: Add Workspace Instruction"
```

Inside the file, add something like:

```markdown
# Workspace Instructions

This repo contains my portfolio website. Apply these rules:

- Use the term “scaffold” for creating project directory structures.
- Project pages live under `portfolio/projects/<slug>/`.
- Each project folder must contain:
  - `index.md`
  - `images/`
  - `models/`
- Never delete existing content unless explicitly asked.
- Prefer concise, high-clarity instructions and folder operations.
- Use kebab-case for folder names.
```

### Step 2 — Keep your README aligned

Copilot reads the README as background context.

* * *

7. **How to Use the Agent Modes for Scaffolding**
=================================================

The reliable workflow:

### **Plan → Edit → Apply**

1. In the Copilot Agent, choose **Plan**
    
2. Paste your scaffolding instructions
    
3. Copilot produces a step-by-step plan
    
4. Approve
    
5. Copilot switches to **Edit** mode
    
6. You apply the diff
    

This avoids it doing surprising things and is the recommended workflow for structural changes.

* * *

## Summary (very concise)
======================

* **Persistent prompts:** a real feature exists → `Copilot: Add Workspace Instruction` (writes to `.vscode/copilot-instructions.md`).
    
* **Add Content:** temporary context injection for the current chat.
    
* **Plan / Ask / Edit:**
    
    * **Ask:** normal chat
        
    * **Plan:** generate multi-step approach
        
    * **Edit:** propose file changes
        
* Copilot does **not** scan arbitrary directories for instructions.










Generate the complete `_layouts/default.html` in a single code block.  
Do an excellent job — treat this as a production-ready file, not a draft.

Before writing the file, apply **full contextual reasoning**:

• Use the FINAL, corrected CSS and the FINAL README spec.  
• Respect the exact DOM responsibilities of `default.html`:  
  – HTML shell  
  – <head> with correct title/meta logic  
  – global header and nav  
  – conditional shared banner (only if page.banner_image is present)  
  – main wrapper (`.site-main` → `.site-wrapper` → {{ content }})  
  – optional footer using existing CSS class hooks  
• Use `{{ site.baseurl }}` correctly for ALL asset paths and links.  
• Implement the model-viewer script import ONCE globally in <head>.  
• Do NOT include any project-detail or portfolio-grid logic here — that belongs in their own layouts.  
• Ensure ALL class names match the CSS exactly.

Take a moment to fully internalize the project context before producing output.

If after reasoning you identify any remaining assumptions, resolve them in the most consistent and conservative way that aligns with the README and CSS.

Then output ONLY the final `_layouts/default.html` file inside one fenced code block — no commentary.




Generate the complete `_layouts/portfolio-list-page.html` in a single code block.  
Produce a polished, production-quality file and apply full contextual reasoning before writing anything.

Use ONLY the current project context (README + final CSS + established layout conventions).  
Do not assume or invent behaviors outside that context.

Key expectations for this layout:

• This file uses `layout: default` and outputs only the content that belongs INSIDE the default layout’s {{ content }} region.  
• It must correctly render the portfolio list page’s structure based on front matter fields such as:  
  – title, description  
  – banner_* (handled by default layout)  
  – page_lead  
  – projects: [slugs]

• It must use the existing CSS class hooks exactly as defined (e.g., `.portfolio-lead`, `.section`, `.section-inner`, `.project-grid`, etc.).

• It must not duplicate header, banner, or main wrapper markup — those belong exclusively to `default.html`.

• It must render the project grid via the appropriate include (`project-grid.html`) and pass the project slugs correctly.

• All URLs should be built using `{{ site.baseurl }}` where required.

Before generating output, reason thoroughly about how the CSS, includes, and front matter interact.  
If you encounter any unclear point, resolve it in the simplest and most consistent way aligned with the overall system.

Then output ONLY the final `_layouts/portfolio-list-page.html` inside one fenced code block — no commentary.





Generate the complete `_layouts/project-detail-page.html` in a single code block.  
Produce a production-quality file and apply full contextual reasoning before writing anything.

Work strictly from the current project context (final README, final CSS, and established layout conventions).  
Do not assume or invent behaviors outside that context.

Key expectations for this layout:

• This file must declare `layout: default` and output only the markup that belongs INSIDE the default layout’s {{ content }} region.

• The structure must reflect the project detail page requirements, including:
  – Full-width image viewer at the top (`.project-media-section` containing `.image-viewer`)  
  – A `.project-detail` wrapper containing a `.project-layout` grid  
  – The three direct children of `.project-layout`, in DOM order, matching the CSS expectations:
       1) `.model-viewer-panel`
       2) `.project-main-column`
       3) `.project-aside-column`

• All CSS class names must match the final CSS exactly.  
• All image and model paths must correctly use `{{ site.baseurl }}` and `{{ page.dir }}`.  
• `<model-viewer>` must use the front matter fields (`model`, optional model_* fields) and follow the existing per-project configuration pattern.  
• Render the primary and secondary content groups in a way that aligns with the README and current Markdown conventions, without hardcoding assumptions that conflict with the existing content model.

• This layout must NOT include:  
  – HTML shell  
  – `<head>`  
  – global nav  
  – banner markup  
These belong exclusively to `default.html`.

Before generating output, take time to fully reason about:
  – how the CSS grid dictates DOM order,
  – how the README defines project page content,
  – how images, hero media, and the 3D viewer integrate,
  – how to structure the page so it works cleanly on both desktop and mobile.

If any ambiguity arises, resolve it in the simplest, most consistent way that aligns with the project’s established patterns.

Then output ONLY the final `_layouts/project-detail-page.html` inside one fenced code block — no commentary.
