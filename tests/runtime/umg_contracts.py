from __future__ import annotations

from typing import Any

def build_umg_scoreboard(scoreboard_contract: dict[str, Any]) -> dict[str, Any]:
    return {"widget_name": "WBP_AFL_Scoreboard", "data": scoreboard_contract}

def build_umg_lower_thirds(lower_contract: dict[str, Any]) -> dict[str, Any]:
    return {"widget_name": "WBP_AFL_LowerThirdStack", "data": lower_contract}

def build_umg_announcer(announcer_contract: dict[str, Any]) -> dict[str, Any]:
    return {"widget_name": "WBP_AFL_AnnouncerBanner", "data": announcer_contract}

def build_umg_phase(phase_contract: dict[str, Any]) -> dict[str, Any]:
    return {"widget_name": "WBP_AFL_MatchPhase", "data": phase_contract}
