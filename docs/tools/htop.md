---
title: htop
description: Interactive process viewer and system monitor
tags:
  - cli
  - monitoring
  - linux
date: 2026-08-26
---

# htop

An interactive process viewer for the terminal. A friendlier, more visual
replacement for `top`.

## Why it's good

- Color-coded CPU, memory, and swap bars at a glance.
- Scroll and search through processes; kill or renice with a keypress.
- Works over SSH with no GUI.

## How to use it

```bash
# Launch
htop

# Inside htop
# F3: search, F5: tree view, F9: kill, F6: sort
```

## Notes

- Install: `apt install htop`, `brew install htop`.
- `htop -d 2` sets the refresh delay in tenths of a second.
