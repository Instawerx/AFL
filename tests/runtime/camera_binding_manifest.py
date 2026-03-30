from __future__ import annotations

from typing import Any

def build_camera_binding_manifest(camera_timeline: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "sequencer_track_name": "AFL_CameraCueTrack",
        "binding_mode": "json_driven",
        "cue_count": len(camera_timeline),
        "cues": camera_timeline,
        "blueprint_hooks": {
            "OnCameraCue": "BP_AFL_SpectatorController::ApplyCameraCue",
            "OnPhaseChanged": "BP_AFL_SpectatorController::ApplyPhaseState",
        },
    }
