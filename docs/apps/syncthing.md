---
title: Syncthing
description: Continuous, peer-to-peer file synchronization
tags:
  - selfhosted
  - sync
  - privacy
date: 2026-08-26
---

# Syncthing

A continuous file synchronization program. Syncs folders between devices
directly, peer-to-peer, with no cloud intermediary.

## Why it's good

- No central server — devices talk directly, so your data never sits on a
  third-party cloud.
- End-to-end encrypted between devices.
- Open source and free.

## How to use it

- Install on each device you want to sync.
- Add a folder on one device, share it with another device's ID.
- Both devices must be online to sync (or use a relay).

## Notes

- Great for syncing an Obsidian vault, config files, or documents.
- Web UI runs on port 8384 by default.
