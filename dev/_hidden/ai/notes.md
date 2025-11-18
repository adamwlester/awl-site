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