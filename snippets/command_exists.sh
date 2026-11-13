#!/usr/bin/env bash
# Check whether a command exists without relying on `which` (not always present).
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Usage
if command_exists jq; then
    echo "jq is installed"
else
    echo "jq is missing"
fi
