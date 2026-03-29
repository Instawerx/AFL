from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
from typing import Dict


def _load_env_file(path: Path) -> Dict[str, str]:
    data: Dict[str, str] = {}
    if not path.exists():
        return data
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip()
    return data


@dataclass
class RuntimeConfig:
    server_exe: str | None
    server_args: str
    server_host: str
    server_port: int
    health_port: int
    boot_timeout: int
    results_dir: Path
    log_dir: Path

    @classmethod
    def from_env(cls, env_file: str | None = None) -> "RuntimeConfig":
        overrides: Dict[str, str] = {}
        if env_file:
            overrides = _load_env_file(Path(env_file))

        def get(name: str, default: str = "") -> str:
            return os.getenv(name, overrides.get(name, default))

        return cls(
            server_exe=get("AFL_SERVER_EXE") or None,
            server_args=get("AFL_SERVER_ARGS", ""),
            server_host=get("AFL_SERVER_HOST", "127.0.0.1"),
            server_port=int(get("AFL_SERVER_PORT", "7777")),
            health_port=int(get("AFL_HEALTH_PORT", "7788")),
            boot_timeout=int(get("AFL_SERVER_BOOT_TIMEOUT", "25")),
            results_dir=Path(get("AFL_RESULTS_DIR", "artifacts/runtime")),
            log_dir=Path(get("AFL_LOG_DIR", "artifacts/logs")),
        )
