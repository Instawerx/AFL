import json, argparse
from pathlib import Path

def load(p): return json.loads(Path(p).read_text())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--broadcast-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    b = Path(args.broadcast_dir)
    o = Path(args.output_dir)
    o.mkdir(parents=True, exist_ok=True)

    scoreboard = load(b/"scoreboard_packet.json")
    lower = load(b/"lower_thirds.json")
    announcer = load(b/"announcer_feed.json")
    cameras = load(b/"camera_packets.json")
    director = load(b/"match_director_state.json")

    ui = {
        "ui_mode": "spectator_demo",
        "scoreboard": scoreboard,
        "lower_thirds": lower,
        "announcer": announcer,
        "camera_packets": cameras,
        "phase": director.get("phase"),
        "winner": director.get("winner")
    }

    (o/"spectator_ui_state.json").write_text(json.dumps(ui, indent=2))
    print("HUD bridge built")

if __name__ == "__main__":
    main()
