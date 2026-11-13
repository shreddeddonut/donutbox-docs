---
title: fzf
description: Command-line fuzzy finder for files, history, and more
tags:
  - cli
  - productivity
  - linux
date: 2026-08-26
---

# fzf

A general-purpose command-line fuzzy finder. Type a few characters, get a
filtered list, pick with the arrow keys. Transforms how you use the terminal.

## Why it's good

- Fuzzy-matches anything you pipe into it — files, history, processes, git branches.
- Integrates with your shell: `Ctrl-R` for history, `Ctrl-T` for files.
- Tiny, fast, and scriptable.

## How to use it

```bash
# Find a file interactively
find . -type f | fzf

# Pick a git branch
git branch | fzf

# Search shell history
history | fzf

# Use the selected result in a command
vim "$(find . -type f | fzf)"
```

## Notes

- Install: `apt install fzf`, `brew install fzf`.
- Add `eval "$(fzf --zsh)"` (or `--bash`) to your shell rc for the keybindings.
