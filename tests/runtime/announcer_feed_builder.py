from __future__ import annotations

from typing import Any


def build_announcer_feed(state: dict[str, Any]) -> list[dict[str, Any]]:
    feed = []
    if state.get("state") == "lobby":
        feed.append({"type": "callout", "text": "Teams are assembling."})
    if state.get("state") == "match_live":
        feed.append({"type": "callout", "text": "Match is live. Objective pressure building."})
    if state.get("winner"):
        feed.append({"type": "callout", "text": f"{state['winner']} has secured the round."})
    return feed
