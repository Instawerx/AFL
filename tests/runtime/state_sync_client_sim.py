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
    return json.loads(line.decode("utf-8")) if line else {}


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("Scenario must load as a mapping.")
    return data


def wait_for_state(conn: socket.socket, expected_state: str, max_reads: int = 10) -> dict:
    last = {}
    for _ in range(max_reads):
        snapshot = recv_json(conn)
        if snapshot:
            last = snapshot
            state = snapshot.get("state", {}).get("state")
            if state == expected_state:
                return snapshot
    return last


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL state sync client simulator")
    parser.add_argument("--scenario", required=True)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9018)
    args = parser.parse_args()

    scenario = load_yaml(Path(args.scenario))
    players = scenario.get("players", [])
    winner = scenario.get("expected", {}).get("winner", players[0] if players else "player_alpha")

    conns = []
    try:
        for player in players:
            conn = socket.create_connection((args.host, args.port), timeout=5)
            conns.append((player, conn))
            send_json(conn, {"type": "join", "player_id": player})
            _ = recv_json(conn)

        for player, conn in conns:
            send_json(conn, {"type": "ready", "player_id": player})

        # wait until one client sees match_live
        live_snapshot = wait_for_state(conns[0][1], "match_live")

        # winner performs objective and capture completion
        for player, conn in conns:
            if player == winner:
                send_json(conn, {"type": "objective_enter", "player_id": player})
                _ = recv_json(conn)
                send_json(conn, {"type": "capture_complete", "player_id": player})
                completed_snapshot = wait_for_state(conn, "completed")
                print(json.dumps({
                    "winner_action_by": player,
                    "live_state": live_snapshot.get("state", {}).get("state"),
                    "server_state": completed_snapshot.get("state", {}).get("state"),
                    "winner": completed_snapshot.get("state", {}).get("winner"),
                }, indent=2))
                break
    finally:
        for _, conn in conns:
            try:
                conn.close()
            except OSError:
                pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
