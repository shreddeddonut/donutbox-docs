#!/usr/bin/env bash
# Extract a filename without its extension, and the extension on its own.
filepath="/path/to/archive.tar.gz"

# Basename without the final extension
name="${filepath##*/}"          # archive.tar.gz
name_no_ext="${name%.*}"        # archive.tar

# Just the final extension
ext="${name##*.}"               # gz

echo "name:        $name"
echo "name_no_ext: $name_no_ext"
echo "ext:         $ext"
