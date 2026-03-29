# AFL Phase 4 File to Socket Upgrade Path

## Current path

Unreal or simulation emits JSON event files.
AFL ingests those files and builds official match results.

## Later path

Swap transport only:
- file output -> socket transport
- schema remains the same
- result builder remains the same
- reward engine remains the same

## Why this is correct for AFL demo

The current AFL demo is gameplay-first and does not require live arena or real robot transport yet.
