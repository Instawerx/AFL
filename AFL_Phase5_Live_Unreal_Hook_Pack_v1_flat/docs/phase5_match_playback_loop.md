# AFL Phase 5 — Match Playback Loop

## Purpose

Replay recorded match event streams and rebuild official AFL match results + rewards.

## Why this matters

This gives AFL:
- repeatable playback validation
- post-match verification
- replay-driven debugging
- deterministic reward validation

## Current path

recorded event file -> playback timeline -> match result -> reward result
