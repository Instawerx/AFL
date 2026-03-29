from __future__ import annotations

import argparse
import json
import socket
import time
from pathlib import Path

from state_packet_schema import validate_state_packet
from overlay_event_builder import build_overlay_payload


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL UDP state broadcaster")
    parser.add_argument("--port", type=int, default=9120)
    parser.add_argument("--state-file", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--ticks", type=int, default=5)
    args = parser.parse_args()

    state_file = Path(args.state_file)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    state = json.loads(state_file.read_text(encoding="utf-8"))
    packet = {
        "packet_type": "state_snapshot",
        "match_id": state.get("match_id", "unknown_match"),
        "session_id": state.get("session_id", "unknown_session"),
        "tick": int(state.get("tick", 0)),
        "state": state.get("state", "unknown"),
        "winner": state.get("winner"),
        "players": state.get("players", {}),
    }

    problems = validate_state_packet(packet)
    if problems:
        raise SystemExit("\n".join(problems))

    overlay = build_overlay_payload(state)
    (output_dir / "overlay_payload.json").write_text(json.dumps(overlay, indent=2), encoding="utf-8")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(args.ticks):
        packet["tick"] = int(packet["tick"]) + 1
        payload = json.dumps(packet).encode("utf-8")
        sock.sendto(payload, ("127.0.0.1", args.port))
        time.sleep(0.1)
    sock.close()

    (output_dir / "state_packet_seed.json").write_text(json.dumps(packet, indent=2), encoding="utf-8")
    print(f"Broadcasted {args.ticks} packets to UDP port {args.port}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
