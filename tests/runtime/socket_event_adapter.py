from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SocketAdapterConfig:
    host: str = "127.0.0.1"
    port: int = 8899


def get_socket_stub_description() -> dict:
    return {
        "status": "stub",
        "message": "Socket mode is intentionally stubbed in Phase 4. File mode is the active path.",
        "future_transport": "tcp_or_websocket",
    }
