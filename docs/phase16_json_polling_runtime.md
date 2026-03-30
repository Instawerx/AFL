# Phase 16 — JSON Polling Runtime

## Runtime Folder
- `artifacts/unreal_runtime`

## Watched Files
- `widget_binding_map.json`
- `camera_binding_manifest.json`
- `demo_scene_runtime_manifest.json`

## Polling Strategy
- Timer every `0.25s`
- Load file text
- Compare against cached text
- If changed, dispatch update
