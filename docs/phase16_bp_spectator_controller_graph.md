# Phase 16 — BP_AFL_SpectatorController Graph

## Goal
Own the AFL spectator HUD and camera cue application logic.

## Blueprint Class
- Class: `BP_AFL_SpectatorController`
- Parent: `PlayerController`

## Event BeginPlay
1. Create Widget `WBP_AFL_Scoreboard`
2. Add to Viewport
3. Repeat for:
   - `WBP_AFL_LowerThirdStack`
   - `WBP_AFL_AnnouncerBanner`
   - `WBP_AFL_MatchPhase`

## Functions
- `ApplyWidgetBindingMap(JsonString)`
- `ApplyCameraManifest(JsonString)`
- `ApplyRuntimeManifest(JsonString)`
- `ApplyCameraCue(CueData)`
- `ApplyPhaseState(PhaseName)`
