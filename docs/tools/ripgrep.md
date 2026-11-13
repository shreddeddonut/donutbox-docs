---
title: ripgrep
description: Fast, recursive grep replacement that respects gitignore
tags:
  - cli
  - search
  - linux
date: 2026-08-26
---

# ripgrep

A line-oriented search tool that recursively searches the current directory for
a regex pattern. Faster than `grep -r` and respects `.gitignore` by default.

## Why it's good

- Blazing fast — built on Rust, parallel by default.
- Respects `.gitignore`, so it skips build artifacts and vendored code.
- Smart defaults: skips hidden files and binary files unless you ask.

## How to use it

```bash
# Search for a pattern, showing line numbers
rg "TODO" src/

# Search, ignoring case
rg -i "error" .

# List only filenames that match
rg -l "import" .

# Search a specific file type
rg -t py "def main"
```

## Notes

- Install: `apt install ripgrep`, `brew install ripgrep`, or `cargo install ripgrep`.
- Drop-in replacement for most `grep -r` workflows.
