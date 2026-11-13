#!/usr/bin/env python3
"""Bulk-rename files in a directory with a simple pattern.

Usage:
    bulk-rename.py <directory> <old> <new>

Replaces every occurrence of <old> with <new> in each filename.
Dry-run by default; pass --apply to actually rename.
"""
import argparse
import os
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", help="directory to scan")
    parser.add_argument("old", help="substring to replace")
    parser.add_argument("new", help="replacement string")
    parser.add_argument("--apply", action="store_true", help="actually rename (default is dry-run)")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"not a directory: {args.directory}", file=sys.stderr)
        return 1

    renamed = 0
    for name in sorted(os.listdir(args.directory)):
        if args.old not in name:
            continue
        new_name = name.replace(args.old, args.new)
        src = os.path.join(args.directory, name)
        dst = os.path.join(args.directory, new_name)
        print(f"{name} -> {new_name}")
        if args.apply:
            os.rename(src, dst)
        renamed += 1

    print(f"\n{renamed} file(s) matched. "
          f"Run with --apply to rename." if not args.apply else f"\n{renamed} file(s) renamed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
