import json, argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hud-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    hud = Path(args.hud_dir)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    ui = json.loads((hud/"spectator_ui_state.json").read_text())

    payload = {
        "mode": "demo_scene",
        "phase": ui.get("phase"),
        "winner": ui.get("winner"),
        "camera_packets": ui.get("camera_packets")
    }

    (out/"demo_scene_driver_state.json").write_text(json.dumps(payload, indent=2))
    print("Demo scene built")

if __name__ == "__main__":
    main()
