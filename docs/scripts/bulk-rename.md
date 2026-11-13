---
title: Bulk file renamer
description: Python script to rename files in a directory with a simple pattern
tags:
  - python
  - cli
  - linux
date: 2026-08-26
---

# Bulk file renamer

Renames files in a directory, replacing one substring with another. Dry-run by
default so you can see what would change before committing.

## The code

```text
--8<-- "scripts/bulk-rename.py"
```

## How to use it

```bash
# See what would change (dry run)
./bulk-rename.py /path/to/dir "report_" "summary_"

# Actually rename
./bulk-rename.py /path/to/dir "report_" "summary_" --apply
```

## Notes

- Dry-run by default; pass `--apply` to rename.
- Replaces every occurrence of the old substring in each filename.
- Sorts filenames before processing so the output is predictable.
