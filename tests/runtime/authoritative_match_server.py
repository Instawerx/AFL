from __future__ import annotations

import argparse
import json
import socket
import threading
import time
import uuid
from pathlib import Path
from typing import Any

from state_models import AuthoritativeMatchState, PlayerState
from action_validator import validate_action
from authority_result_emitter import emit_authority_artifacts


def send_json(conn: socket.socket, payload: dict[str, Any]) -> None:
    conn.sendall(json.dumps(payload).encode("utf-8") + b"\n")


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


def build_state() -> AuthoritativeMatchState:
    return AuthoritativeMatchState(
        match_id=f"afl_match_{uuid.uuid4().hex[:10]}",
        session_id=f"afl_session_{uuid.uuid4().hex[:10]}",
        arena="CrashSiteOmega",
        mode="AssaultCore",
    )


def assign_team(index: int) -> str:
    return "A" if index % 2 == 0 else "B"


def update_readiness(state: AuthoritativeMatchState) -> None:
    if len(state.players) >= 2 and all(p.ready for p in state.players.values()):
        state.state = "match_live"


def handle_action(state: AuthoritativeMatchState, payload: dict[str, Any]) -> None:
    problems = validate_action(payload)
    if problems:
        return

    player_id = payload["player_id"]
    action_type = payload["type"]

    if action_type == "join":
        if player_id not in state.players:
            team = assign_team(len(state.players))
            state.players[player_id] = PlayerState(player_id=player_id, team=team)
    elif action_type == "ready":
        if player_id in state.players:
            state.players[player_id].ready = True
            update_readiness(state)
    elif action_type == "objective_enter":
        if player_id in state.players and state.state == "match_live":
            state.players[player_id].objective_control += 1
    elif action_type == "capture_complete":
        if player_id in state.players and state.state == "match_live":
            state.winner = player_id
            state.state = "completed"


def handle_client(conn: socket.socket, state: AuthoritativeMatchState, lock: threading.Lock, peers: list[socket.socket]) -> None:
    try:
        for payload in recv_lines(conn):
            with lock:
                handle_action(state, payload)
                snapshot = {"type": "state_snapshot", "state": state.as_jsonable()}
                dead = []
                for peer in peers:
                    try:
                        send_json(peer, snapshot)
                    except OSError:
                        dead.append(peer)
                for d in dead:
                    if d in peers:
                        peers.remove(d)
    finally:
        try:
            conn.close()
        except OSError:
            pass


def ticker(state: AuthoritativeMatchState, lock: threading.Lock, stop_flag: dict) -> None:
    while not stop_flag["stop"]:
        time.sleep(0.25)
        with lock:
            if state.state in ("match_live", "completed"):
                state.tick += 1
            if state.state == "completed":
                stop_flag["stop"] = True


def main() -> int:
    parser = argparse.ArgumentParser(description="AFL authoritative state sync server")
    parser.add_argument("--port", type=int, default=9018)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--once-complete", action="store_true")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    state = build_state()
    lock = threading.Lock()
    peers: list[socket.socket] = []
    stop_flag = {"stop": False}

    tick_thread = threading.Thread(target=ticker, args=(state, lock, stop_flag), daemon=True)
    tick_thread.start()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", args.port))
    server.listen(8)
    server.settimeout(0.5)

    print(json.dumps({"status": "listening", "port": args.port, "match_id": state.match_id, "session_id": state.session_id}))

    try:
        while not stop_flag["stop"]:
            try:
                conn, _ = server.accept()
            except socket.timeout:
                continue
            peers.append(conn)
            t = threading.Thread(target=handle_client, args=(conn, state, lock, peers), daemon=True)
            t.start()
    finally:
        server.close()

    with lock:
        emit_authority_artifacts(output_dir, state.as_jsonable())

    print(json.dumps({"status": "stopped", "winner": state.winner, "output_dir": str(output_dir)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
