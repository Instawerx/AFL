from __future__ import annotations

import argparse
import json
import socket
import threading
import uuid
from pathlib import Path
from typing import Any

from network_state_models import SessionState, ConnectedClient


def send_json(conn: socket.socket, payload: dict[str, Any]) -> None:
    message = json.dumps(payload).encode("utf-8") + b"\n"
    conn.sendall(message)


def recv_lines(conn: socket.socket):
    buffer = b""
    while True:
        data = conn.recv(4096)
        if not data:
            break
        buffer += data
        while b"\n" in buffer:
            line, buffer = buffer.split(b"\n", 1)
            if line.strip():
                yield json.loads(line.decode("utf-8"))


def build_default_state() -> SessionState:
    return SessionState(
        session_id=f"afl_net_{uuid.uuid4().hex[:12]}",
        queue_name="QuickMatch",
        session_type="PublicCompetitive",
        arena="CrashSiteOmega",
        mode="AssaultCore",
    )


def assign_teams(state: SessionState) -> None:
    for idx, player_id in enumerate(state.clients.keys()):
        state.clients[player_id].team = "A" if idx % 2 == 0 else "B"


def maybe_advance_state(state: SessionState) -> None:
    if len(state.clients) >= 2 and all(client.ready for client in state.clients.values()):
        assign_teams(state)
        state.state = "match_started"


def handle_client(conn: socket.socket, addr, state: SessionState, lock: threading.Lock, broadcast_targets: list[socket.socket]) -> None:
    try:
        for message in recv_lines(conn):
            with lock:
                msg_type = message.get("type")
                player_id = message.get("player_id", "")
                if msg_type == "join":
                    state.clients[player_id] = ConnectedClient(player_id=player_id, ready=False)
                    if conn not in broadcast_targets:
                        broadcast_targets.append(conn)
                    send_json(conn, {"type": "joined", "session": state.as_jsonable()})
                elif msg_type == "ready":
                    if player_id in state.clients:
                        state.clients[player_id].ready = True
                    maybe_advance_state(state)
                    snapshot = {"type": "session_update", "session": state.as_jsonable()}
                    dead = []
                    for target in broadcast_targets:
                        try:
                            send_json(target, snapshot)
                        except OSError:
                            dead.append(target)
                    for d in dead:
                        if d in broadcast_targets:
                            broadcast_targets.remove(d)
                elif msg_type == "snapshot":
                    send_json(conn, {"type": "session_update", "session": state.as_jsonable()})
    finally:
        try:
            conn.close()
        except OSError:
            pass


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL lightweight TCP session server")
    parser.add_argument("--port", type=int, default=9007)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--once-ready", action="store_true")
    args = parser.parse_args()

    state = build_default_state()
    lock = threading.Lock()
    broadcast_targets: list[socket.socket] = []

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", args.port))
    server.listen(8)
    server.settimeout(0.5)

    print(json.dumps({"status": "listening", "port": args.port, "session_id": state.session_id}))

    try:
        while True:
            try:
                conn, addr = server.accept()
            except socket.timeout:
                with lock:
                    if state.state == "match_started":
                        (out_dir / "network_session_state.json").write_text(json.dumps(state.as_jsonable(), indent=2), encoding="utf-8")
                        if args.once_ready:
                            break
                continue
            t = threading.Thread(target=handle_client, args=(conn, addr, state, lock, broadcast_targets), daemon=True)
            t.start()
    finally:
        server.close()

    (out_dir / "network_session_state.json").write_text(json.dumps(state.as_jsonable(), indent=2), encoding="utf-8")
    print(json.dumps({"status": "stopped", "session_state_file": str(out_dir / "network_session_state.json")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
