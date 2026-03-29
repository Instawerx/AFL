from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Literal


SessionType = Literal["PublicCompetitive", "PrivateLobby", "SkillsChallenge", "SpectatorOnly", "InternalTest"]


@dataclass
class PlayerSessionEntry:
    player_id: str
    team: str | None = None
    connected: bool = True


@dataclass
class MatchSession:
    session_type: SessionType
    queue_name: str
    arena: str
    mode: str
    players: List[PlayerSessionEntry] = field(default_factory=list)
    session_id: str | None = None
    state: str = "created"
