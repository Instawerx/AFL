from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def build_replay_entry(path: Path, payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "file": str(path),
        "match_id": payload.get("match_id", "unknown_match"),
        "session_id": payload.get("session_id", "unknown_session"),
        "winner": payload.get("winner"),
        "session_valid": payload.get("session_valid", True),
        "replayable": "objective_events" in payload,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL replay index builder")
    parser.add_argument("--data-dir", required=True)
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    sessions_dir = data_dir / "sessions"
    out_file = data_dir / "replay_index.json"

    entries = []
    if sessions_dir.exists():
        for file in sorted(sessions_dir.glob("*.json")):
            payload = json.loads(file.read_text(encoding="utf-8"))
            entries.append(build_replay_entry(file, payload))

    out_file.write_text(json.dumps(entries, indent=2), encoding="utf-8")
    print(f"Replay index written: {out_file}")
    print(f"Entries: {len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
