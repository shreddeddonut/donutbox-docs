---
title: tmux
description: Terminal multiplexer for persistent, split sessions
tags:
  - cli
  - productivity
  - linux
date: 2026-08-26
---

# tmux

A terminal multiplexer. Keeps sessions alive across disconnects, splits the
screen, and lets you detach and reattach to work later.

## Why it's good

- Sessions survive SSH disconnects — your work is still there when you reconnect.
- Split panes and windows without a GUI.
- Scriptable: start named sessions with a command.

## How to use it

```bash
# Start a new session
tmux new -s work

# Detach (Ctrl-b then d)
# List sessions
tmux ls

# Reattach
tmux attach -t work

# Split panes: Ctrl-b % (vertical), Ctrl-b " (horizontal)
```

## Notes

- Prefix is `Ctrl-b` by default.
- `tmux new -s name -d` starts a session in the background.
