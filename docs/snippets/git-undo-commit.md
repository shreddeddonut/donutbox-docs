---
title: Undo the last git commit
description: Soft, mixed, and hard resets to undo the last commit
tags:
  - git
  - cli
date: 2026-08-26
---

# Undo the last git commit

Three ways to undo the most recent commit, depending on whether you want to
keep the changes.

## The code

```text
--8<-- "snippets/git_undo_commit.sh"
```

## How to use it

- **Soft reset** keeps your changes staged — good if you committed too early
  and want to redo the commit.
- **Mixed reset** (the default) keeps your changes but unstages them.
- **Hard reset** discards the changes entirely. Only use it if you're certain.

## Notes

- These only touch the last commit. For older commits, use `git rebase -i` or
  `git revert`.
- If you've already pushed, prefer `git revert` over resetting — rewriting
  pushed history breaks anyone who pulled.
