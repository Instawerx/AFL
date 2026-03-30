from __future__ import annotations
import argparse, json
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser(description="AFL Unreal execution bundle index builder")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    payload = {
        "phase": 16,
        "bundle_name": "AFL_Unreal_Execution_Bundle",
        "documents": [
            "docs/phase16_bp_runtime_bridge_graph.md",
            "docs/phase16_bp_spectator_controller_graph.md",
            "docs/phase16_umg_widget_layouts.md",
            "docs/phase16_sequencer_camera_setup.md",
            "docs/phase16_level_bootflow.md",
            "docs/phase16_json_polling_runtime.md",
            "docs/phase16_validation_checklist.md",
        ],
        "goal": "Implement the AFL investor demo directly inside Unreal using Lyra-compatible patterns.",
    }

    (out / "unreal_execution_bundle_index.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Unreal execution bundle index written: {out / 'unreal_execution_bundle_index.json'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
