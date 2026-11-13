---
title: Disk usage checker
description: Show the largest directories under a path, human-readable
tags:
  - bash
  - cli
  - linux
date: 2026-08-26
---

# Disk usage checker

Shows the largest directories under a path, sorted by size, human-readable.

## The code

```text
--8<-- "scripts/disk-usage.sh"
```

## How to use it

```bash
./disk-usage.sh /var/log 2
```

Prints the top 20 largest directories at the given depth.

## Notes

- Uses `du -h --max-depth` and `sort -hr`, so it needs GNU coreutils (Linux).
- `set -euo pipefail` makes it fail fast on errors.
