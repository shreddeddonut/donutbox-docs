---
title: VLC
description: Free, open-source media player that plays almost anything
tags:
  - media
  - video
  - audio
date: 2026-08-26
---

# VLC

A free and open-source media player. Plays nearly every video and audio format
without extra codecs, and doubles as a streaming client and converter.

## Why it's good

- Plays almost anything — codecs are built in, no hunting for downloads.
- Cross-platform: Windows, macOS, Linux, Android, iOS.
- Also streams, records, and converts media.

## How to use it

- Open a file: `vlc file.mp4`.
- Stream a URL: `vlc https://example.com/stream.m3u8`.
- Convert: `vlc input.mp4 --sout '#transcode{vcodec=h264}:standard{mux=mp4,dst=out.mp4}'`.

## Notes

- Free and open source (GPL).
- The command-line interface is powerful for scripting conversions.
