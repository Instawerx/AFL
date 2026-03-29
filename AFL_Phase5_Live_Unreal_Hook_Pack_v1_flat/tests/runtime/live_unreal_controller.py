from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class LiveHookConfig:
    watch_dir: Path
    output_dir: Path
    mode: str = "file_watch"


def describe_controller(config: LiveHookConfig) -> dict:
    return {
        "mode": config.mode,
        "watch_dir": str(config.watch_dir),
        "output_dir": str(config.output_dir),
        "status": "ready",
    }
