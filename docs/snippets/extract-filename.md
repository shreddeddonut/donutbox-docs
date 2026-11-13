---
title: Extract filename without extension
description: Bash parameter expansion to split a filename and its extension
tags:
  - bash
  - cli
date: 2026-08-26
---

# Extract filename without extension

Pure bash parameter expansion to pull a filename apart — no external tools, no
`basename` or `cut` needed.

## The code

```text
--8<-- "snippets/extract_filename.sh"
```

## How to use it

The expansion handles the full path, so you can use it directly on a path
variable:

```bash
name="${filepath##*/}"   # strip everything up to the last slash
name_no_ext="${name%.*}" # strip the last extension
ext="${name##*.}"        # keep only the last extension
```

## Notes

- `##` strips the longest match from the front; `%` strips the shortest from
  the back.
- For `archive.tar.gz`, this gives `archive.tar` and `gz` — the last extension
  only. If you need the first extension too, chain another expansion.
