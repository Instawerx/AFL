from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class LobbyResult:
    ready: bool
    players: List[str]
    teams: dict[str, str]


def build_lobby(players: list[str], min_players: int = 2) -> LobbyResult:
    if len(players) < min_players:
        return LobbyResult(ready=False, players=players, teams={})

    teams: dict[str, str] = {}
    for idx, player in enumerate(players):
        teams[player] = "A" if idx % 2 == 0 else "B"

    return LobbyResult(ready=True, players=players, teams=teams)
