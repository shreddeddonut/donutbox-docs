# donutbox-docs

Project page for [donutbox.dev](https://donutbox.dev) - a quick-reference
library for scripts, handy snippets, and homelab notes. Built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## How it works

- Content lives in `docs/` as plain Markdown
- Pushing to `main` builds the site and deploys it to GitHub Pages
  (see `.github/workflows/deploy.yml`)
- The site is served at `https://donutbox.dev` via Cloudflare DNS

## Adding content

1. **Scripts** - add a page under `docs/scripts/`, e.g. `docs/scripts/my-script.md`.
   Wrap the script in a fenced code block so the copy button works:

   ````markdown
   # My Script

   ```bash
   #!/bin/bash
   echo "hello"
   ```
   ````

2. **Snippets** - same pattern under `docs/snippets/`.

3. **Notes** - same pattern under `docs/notes/`.

4. Add the page to the `nav` section in `mkdocs.yml`, then commit and push.

## Local development

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve   # preview at http://127.0.0.1:8000
.venv/bin/mkdocs build   # static site in site/
```

## Deployment

The GitHub Actions workflow in `.github/workflows/deploy.yml` runs `mkdocs build`
on every push to `main` and uploads the result as a Pages artifact. GitHub Pages
is configured with the "GitHub Actions" build source.

- Custom domain: `donutbox.dev` (via `docs/CNAME`)
- DNS: Cloudflare CNAME `donutbox.dev` -> `shreddeddonut.github.io`
