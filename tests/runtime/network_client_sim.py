from __future__ import annotations

import argparse
import json
import socket
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install with: python -m pip install pyyaml")
    sys.exit(2)


def send_json(conn: socket.socket, payload: dict) -> None:
    conn.sendall(json.dumps(payload).encode("utf-8") + b"\n")


def recv_json(conn: socket.socket) -> dict:
    data = b""
    while b"\n" not in data:
        chunk = conn.recv(4096)
        if not chunk:
            break
        data += chunk
    line = data.split(b"\n", 1)[0]
    return json.loads(line.decode("utf-8"))


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("Scenario must load as a mapping.")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL network client simulator")
    parser.add_argument("--scenario", required=True)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9007)
    args = parser.parse_args()

    scenario = load_yaml(Path(args.scenario))
    players = scenario.get("players", [])
    if len(players) < 2:
        raise SystemExit("Scenario must include at least 2 players.")

    for player in players:
        with socket.create_connection((args.host, args.port), timeout=5) as conn:
            send_json(conn, {"type": "join", "player_id": player})
            _ = recv_json(conn)
            send_json(conn, {"type": "ready", "player_id": player})
            update = recv_json(conn)
            print(json.dumps({"player": player, "update_type": update.get("type"), "state": update.get("session", {}).get("state")}, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
