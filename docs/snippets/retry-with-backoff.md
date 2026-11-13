---
title: Retry with exponential backoff
description: Python retry helper with exponential backoff and jitter
tags:
  - python
  - cli
date: 2026-08-26
---

# Retry with exponential backoff

A small Python helper that retries a callable with exponential backoff and
jitter. Useful for network calls that fail transiently.

## The code

```text
--8<-- "snippets/retry_with_backoff.py"
```

## How to use it

Pass any callable. It retries up to `attempts` times, doubling the delay each
time and adding jitter to avoid thundering-herd retries:

```python
result = retry_with_backoff(flaky_call, attempts=5)
```

## Notes

- Raises the last exception after all attempts are exhausted.
- Jitter spreads retries so concurrent callers don't all retry at once.
