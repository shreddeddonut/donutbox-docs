---
title: Check if a command exists
description: Portable bash check for whether a command is installed
tags:
  - bash
  - cli
date: 2026-08-26
---

# Check if a command exists

A portable way to test whether a command is on the PATH, without relying on
`which` (which isn't always installed).

## The code

```text
--8<-- "snippets/command_exists.sh"
```

## How to use it

Source the function, then call it with the command name:

```bash
if command_exists jq; then
    echo "jq is installed"
fi
```

## Notes

`command -v` is POSIX and works in bash, zsh, and dash. Prefer it over `which`
for portability.
