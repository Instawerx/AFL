# Phase 16 — BP_AFL_RuntimeBridge Graph

## Goal
Continuously poll AFL JSON artifacts and dispatch updates to widgets and spectator control.

## Blueprint Class
- Class: `BP_AFL_RuntimeBridge`
- Parent: `Actor`

## Variables
- `RuntimeFolder` (String) = `artifacts/unreal_runtime`
- `PollIntervalSeconds` (Float) = `0.25`
- `CachedWidgetBindingMap` (String / JSON text)
- `CachedCameraBindingManifest` (String / JSON text)
- `CachedRuntimeManifest` (String / JSON text)
- `SpectatorControllerRef` (Object Reference: `BP_AFL_SpectatorController`)

## Event Graph
1. **Event BeginPlay**
   - Set Timer by Event
   - Time = `PollIntervalSeconds`
   - Looping = true
   - Bound event = `PollRuntimeArtifacts`

2. **Custom Event: PollRuntimeArtifacts**
   - Call `LoadJsonFile` for:
     - `widget_binding_map.json`
     - `camera_binding_manifest.json`
     - `demo_scene_runtime_manifest.json`
   - Compare loaded strings to cached strings
   - If changed:
     - Update cached values
     - Call `DispatchWidgetAndCameraState`

3. **Custom Event: DispatchWidgetAndCameraState**
   - If `SpectatorControllerRef` invalid:
     - Get Player Controller 0
     - Cast to `BP_AFL_SpectatorController`
     - Set `SpectatorControllerRef`
   - Call:
     - `ApplyWidgetBindingMap(CachedWidgetBindingMap)`
     - `ApplyCameraManifest(CachedCameraBindingManifest)`
     - `ApplyRuntimeManifest(CachedRuntimeManifest)`
