from __future__ import annotations

from typing import Any

def build_json_polling_bridge() -> dict[str, Any]:
    return {
        "bridge_mode": "file_polling",
        "poll_interval_seconds": 0.25,
        "runtime_folder": "artifacts/unreal_runtime",
        "watched_files": [
            "widget_binding_map.json",
            "camera_binding_manifest.json",
            "demo_scene_runtime_manifest.json",
        ],
        "unreal_runtime_contract": {
            "bridge_actor": "BP_AFL_RuntimeBridge",
            "load_function": "LoadJsonArtifacts",
            "dispatch_function": "DispatchWidgetAndCameraState",
        },
    }
