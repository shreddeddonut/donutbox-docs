#!/usr/bin/env bash
# Show the largest directories under a path, human-readable.
# Usage: disk-usage.sh [path] [depth]
set -euo pipefail

path="${1:-.}"
depth="${2:-1}"

if ! command -v du >/dev/null 2>&1; then
    echo "du not found" >&2
    exit 1
fi

du -h --max-depth="$depth" "$path" 2>/dev/null | sort -hr | head -20
