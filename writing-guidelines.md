# Writing Guidelines

Rules for adding content to donutbox.dev. Keep it consistent, keep it useful.

## Every page

1. **Start from `template.md`.** Copy it, fill it in, don't invent a new structure.
2. **Frontmatter is mandatory.** `title`, `description`, `tags`, `date`. The
   description is used for SEO meta tags and the llms.txt index — make it one
   clear line, no trailing period.
3. **Tag everything.** Tags power the /tags/ index. Use 2-4 per page. Common
   tags: `bash`, `python`, `git`, `cli`, `selfhosted`, `productivity`, `macos`,
   `linux`, `windows`.
4. **One-line descriptions.** If it needs more than one line, it's not a
   description, it's the page body.

## Code

5. **Keep code in real files, include it.** Use the snippets plugin so code
   lives in one place and renders everywhere:
   ```text
   --8<-- "snippets/<name>.sh"
   ```
   Don't paste code into markdown and let it drift.
6. **Real, tested code only.** If it's here, it runs. No pseudocode, no
   half-finished examples.

## Content rules

7. **No personal setup.** This is a public site. No IPs, no hostnames, no
   references to personal infrastructure, no private details.
8. **Generic and useful.** Snippets, scripts, tools and apps that anyone could
   use. If it only makes sense to one person, it doesn't belong here.
9. **No fluff.** No "in today's fast-paced world". State what it is, show it,
   move on.

## Adding a page

10. Create the file under the right section: `docs/snippets/`, `docs/scripts/`,
    `docs/tools/`, or `docs/apps/`.
11. Add it to the nav in `mkdocs.yml` if it's a new section page. Individual
    entries don't need nav entries — they're reached from the section index.
12. Build locally before pushing: `.venv/bin/mkdocs build`. Fix warnings, then
    commit.
