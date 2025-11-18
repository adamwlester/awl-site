### 1. Repo structure comment for `index.md` and portfolio-related files

**Existing text to replace:**

`index.md # homepage (**site root**) -> minimal landing + link to /portfolio/`  
`│ ├── project-grid.html # include for the **portfolio project grid** on /portfolio/`  
`│ ├── portfolio-list-page.html # layout for the **portfolio list page** (/portfolio/)`

```markdown
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
```

* * *

### 2. Layout responsibilities for `portfolio-list-page.html`

**Existing text to replace:**

`-` _layouts/portfolio-list-page.html`

* Specializes the layout for `/portfolio/`: shared banner, page lead/intro text, and the project card grid.`
    

```markdown
- `_layouts/portfolio-list-page.html`  
  - Specializes the layout for the portfolio list page (`{{ site.baseurl }}/portfolio/`): shared banner, page lead/intro text, and the project card grid.
```

* * *

### 3. Home page main elements – CTA target

**Existing text to replace:**

`- **Primary Call-to-Action (CTA):** – Prominent link or button that routes users to` /portfolio/`.`

```markdown
- **Primary Call-to-Action (CTA):**  
  – Prominent link or button that routes users to the portfolio list page (`{{ site.baseurl }}/portfolio/`).
```

* * *

### 4. Home page CTA – data source example link

**Existing text to replace:**

`- Markdown link in` index.md`pointing to`/portfolio/`, for example:

* `[View Portfolio](/portfolio/)`
    
* Optionally annotated with a class (e.g., `{: .button }`) for button styling.`
    

```markdown
- Markdown link in `index.md` pointing to the portfolio list page via `{{ site.baseurl }}`, for example:  
  - `[View Portfolio]({{ site.baseurl }}/portfolio/)`  
  - Optionally annotated with a class (e.g., `{: .button }`) for button styling.
```

* * *

### 5. Home page layout description – CTA target

**Existing text to replace:**

`4. **Primary Call-to-Action** linking to` /portfolio/`.`

```markdown
4. **Primary Call-to-Action** linking to the portfolio list page (`{{ site.baseurl }}/portfolio/`).
```

* * *

### 6. Project card grid behavior – card link target

**Existing text to replace:**

`- The **entire card is clickable**, linking to` /portfolio/projects/<slug>/`.`

```markdown
- The **entire card is clickable**, linking to `{{ site.baseurl }}/portfolio/projects/<slug>/`.
```

* * *

### 7. Implementation status – portfolio routes summary

**Existing text to replace:**

`- Portfolio section in place (`/portfolio/`) with project-specific routes under` portfolio/projects/<slug>/`.`

```markdown
- Portfolio section in place (portfolio list at `{{ site.baseurl }}/portfolio/` with project-specific routes under `{{ site.baseurl }}/portfolio/projects/<slug>/`).
```

* * *

These changes keep your README conceptually aligned with the earlier “use `{{ site.baseurl }}` for internal links” rule and match how the site will actually resolve under `/awl-site` on GitHub Pages.