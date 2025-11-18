You are transforming project markdown files into the new portfolio website format.  
Below is the COMPLETE specification of how every project file must be transformed.  
After reading this, you will summarize your understanding.  
AFTER the summary, you will wait for me to provide the original markdown to transform.  
When I provide the original markdown, you will output ONLY the final transformed file in a single fenced code block.

---

# ️REFERENCE EXAMPLES (OLD → NEW)

I am providing two files along with this prompt:

- **index_old.md** — the original NC4touch markdown (OLD FORMAT)
- **index_new.md** — the transformed NC4touch markdown (NEW FORMAT)

Use **index_old.md** and **index_new.md** together to infer formatting conventions, indentation, list behavior, heading style, and section flow.

HOWEVER:  
**If the examples differ from the explicit rules in this prompt, the explicit rules always override.**

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
- For images:
  - Extract them from the “### Image Files” section of the old markdown.
  - Each original filename like `render_01.png` must become:
    ```yaml
    - src: "images/render_01.png"
      caption: "<original caption text>"
    ```
  - In other words: **prepend `images/` to the original filename** to form `src`, but do not otherwise change the filename.
  - Preserve the original caption text exactly.
  - Preserve the original order of the image entries.
---
```

Rules:

* **title** = the original H1 (e.g., `# NC4touch Behavioral Apparatus`)
    
* **summary** = the text that previously appeared under `## Summary`
    
* **hero** is always `"hero.png"`
    
* **model** must be `"models/<slug>.glb"` (slug is the folder name; I will tell you the slug when sending each file OR it is obvious from context)
    
* For images:
    
    * Extract them from the “### Image Files” section of the old markdown.
        
    * Convert each into a front matter object:
        
        ```yaml
        - src: "<filename>"
          caption: "<caption>"
        ```
        
    * Preserve order.
        
    * Do not rewrite filenames or captions.
        
* **Do NOT include any other fields.**
    

The entire front matter block must appear between `---` lines with no extra spacing.

**Note about slugs**
You can generate the slug from the project title by lowercasing it and replacing spaces with hyphens. For example, "NC4touch Behavioral Apparatus" becomes "nc4touch-behavioral-apparatus".

* * *

️2. BODY TRANSFORMATION RULES
=============================

A. Remove the following from the body entirely:
----------------------------------------------

* Remove the single H1 title line only, e.g. a line that looks like:
  `# NC4touch Behavioral Apparatus`
  - Do NOT remove any content that follows it.
* Remove the entire `## Summary` section (the `## Summary` heading and all of its content).

B. Preserve the following section exactly (no renaming):
--------------------------------------------------------

You MUST preserve the following section and its subsections in the body as is:

* `## Included files`
* `### Image Files`
* `### 3D Model Files`

Rules:

* Do NOT remove, rename, or reorder these headings.
* You MAY read the entries under `### Image Files` to build the front matter `images:` list, but:
  * Keep all lines under `## Included files`, `### Image Files`, and `### 3D Model Files` in the body.
  * Do NOT delete, rewrite, or simplify them after copying their information.
* The only allowed change is minor indentation/spacing normalization if needed for valid Markdown.
    

C. Required body section order (exact headings):
------------------------------------------------

1. `## Description`
    
2. `## Role & Contributions`
    
3. `## Highlights & Key Specs`
    
4. `## Materials & Fabrication`
    
5. `## Validation & Performance`
    
6. `## Deployment & Status`
    
7. `## Included files` (if present)
    
8. `## Release`
    
9. `## References`
    

If any section is missing in the original file:

* Create the header.
    
* Leave it empty with a placeholder bullet: `- (content not provided)`.
    

D. Bullet restructuring rules (critical):
-----------------------------------------

For these sections only:

* `## Highlights & Key Specs`
* `## Materials & Fabrication`
* `## Validation & Performance`
* `## Deployment & Status`

You MUST:

* Convert any inline bullets into **one bullet per line**.
* Split semi-colon–separated clauses into **separate top-level bullets**.
* When a bullet begins with a bold label like `- **Development:** ...` or `- **Status:** ...`:
  * Turn the label into a bold heading on its own line, for example:

    ```markdown
    **Development:**  
    Completed, Sep 2023–Nov 2024  
    ```

  * If the original bullet has text after the label (e.g. `- **Development:** completed, Sep 2023–Nov 2024`), move that text to its own line directly under the bold label (not as a bullet), preserving wording and punctuation.
  * If the original bullet has nested bullets (e.g. `- **Deployment:**` followed by indented `-` items), keep those nested bullets directly under the bold label, preserving their order and text:

    ```markdown
    **Deployment:**  
    - NC4 Lab, University of British Columbia (2 studies, 4 rigs)  
    - Snyder Lab, University of British Columbia (1 study, 2 rigs)  
    ```

  * If the text after the label contains semicolons, split it into multiple bullets under that label, one clause per bullet.
* Preserve wording exactly except for breaking clauses into bullets and moving label text to its own line.
* Never combine sentences.
* Do not alter grammar or rewrite text.
* Do not end any bullets with periods unless they were originally present.
* Do capitalize the first letter of each bullet, including those you generate from semi-colon–separated clauses.
    

E. Headings
-----------

* All headings must use Markdown `##`.
    
* Do not alter capitalization of required section names.
    
* Do not insert extra commentary, explanations, or blank sections.
    
* After **every** `##` heading, insert exactly **one blank line** before any content.
  
  Correct:
  ```markdown
  ## Deployment & Status

  **Development:**  
  Completed, Jan 2018–Feb 2018
  ```
  Incorrect:
  ```markdown
  ## Deployment & Status
  **Development:**  
  Completed, Jan 2018–Feb 2018
  ```

* * *

️3. OUTPUT RULES (CRITICAL)
===========================

When I provide a project’s original markdown in the next message:

**You will output ONLY the complete transformed `index.md` in a single triple-backtick fenced code block.**

No commentary, no reasoning, no explanations. Only the file.

* * *

️YOUR NEXT ACTION
=================

1. **Summarize your understanding of the transformation rules.**
    
2. **Then wait for me to provide the original markdown input.**  
    Do NOT transform anything yet.
    