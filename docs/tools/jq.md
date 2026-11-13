---
title: jq
description: Lightweight command-line JSON processor
tags:
  - cli
  - json
  - linux
date: 2026-08-26
---

# jq

A lightweight and flexible command-line JSON processor. The standard tool for
parsing and transforming JSON in the shell.

## Why it's good

- Parse, filter, and reshape JSON without writing a script.
- Pipes naturally with `curl` and other CLI tools.
- Available everywhere: `apt install jq`, `brew install jq`.

## How to use it

```bash
# Pretty-print JSON
echo '{"a":1,"b":2}' | jq .

# Extract a field
curl -s https://api.example.com/data | jq '.results[0].name'

# Filter an array
jq '.[] | select(.status == "active")' data.json

# Build a new object
jq '{name: .user.name, email: .user.email}' data.json
```

## Notes

- `jq .` pretty-prints; `jq -r` outputs raw strings without quotes.
- Combine with `--arg` to inject shell variables into filters.
