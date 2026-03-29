from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List
import uuid


@dataclass
class SessionRecord:
    session_id: str
    queue_name: str
    session_type: str
    arena: str
    mode: str
    state: str = "created"
    players: List[str] = field(default_factory=list)


class SessionRegistry:
    def __init__(self) -> None:
        self._sessions: Dict[str, SessionRecord] = {}

    def create_session(self, queue_name: str, session_type: str, arena: str, mode: str) -> SessionRecord:
        session_id = f"afl_{uuid.uuid4().hex[:12]}"
        record = SessionRecord(
            session_id=session_id,
            queue_name=queue_name,
            session_type=session_type,
            arena=arena,
            mode=mode,
        )
        self._sessions[session_id] = record
        return record

    def add_player(self, session_id: str, player_id: str) -> None:
        record = self._sessions[session_id]
        if player_id not in record.players:
            record.players.append(player_id)

    def set_state(self, session_id: str, state: str) -> None:
        self._sessions[session_id].state = state

    def export(self) -> list[dict]:
        return [asdict(v) for v in self._sessions.values()]


def self_test() -> int:
    reg = SessionRegistry()
    record = reg.create_session("QuickMatch", "PublicCompetitive", "CrashSiteOmega", "AssaultCore")
    reg.add_player(record.session_id, "player_alpha")
    reg.add_player(record.session_id, "player_beta")
    reg.set_state(record.session_id, "ready")
    print(json.dumps(reg.export(), indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    print("SessionRegistry module loaded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
