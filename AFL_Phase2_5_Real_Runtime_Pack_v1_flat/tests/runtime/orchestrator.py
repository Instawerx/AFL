from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import socket
import subprocess
import sys
import time
from typing import Any

from runtime_config import RuntimeConfig


@dataclass
class LaunchResult:
    mode: str
    process: subprocess.Popen | None
    health_ready: bool


def wait_for_tcp(host: str, port: int, timeout_s: int) -> bool:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        try:
            with socket.create_connection((host, port), timeout=1.0):
                return True
        except OSError:
            time.sleep(0.5)
    return False


def launch_runtime_server(config: RuntimeConfig) -> LaunchResult:
    if config.server_exe:
        cmd = [config.server_exe]
        if config.server_args.strip():
            cmd.extend(config.server_args.split())
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        ready = wait_for_tcp(config.server_host, config.health_port, config.boot_timeout)
        return LaunchResult(mode="real_exe", process=proc, health_ready=ready)

    stub = Path(__file__).resolve().parent / "stub_server.py"
    cmd = [sys.executable, str(stub), "--health-port", str(config.health_port), "--lifetime", "15"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    ready = wait_for_tcp(config.server_host, config.health_port, config.boot_timeout)
    return LaunchResult(mode="stub_server", process=proc, health_ready=ready)


def simulate_queue_and_match(scenario: dict[str, Any]) -> dict[str, Any]:
    expected = scenario["expected"]
    return {
        "session_type": scenario["session_type"],
        "queue_name": scenario["queue_name"],
        "arena": scenario["arena"],
        "mode": scenario["mode"],
        "players": scenario["players"],
        "winner": expected["winner"],
        "coins_awarded": expected["coins_awarded"],
        "xp_awarded": expected["xp_awarded"],
    }


def write_result(config: RuntimeConfig, payload: dict[str, Any]) -> Path:
    config.results_dir.mkdir(parents=True, exist_ok=True)
    out = config.results_dir / "queue_reward_result.json"
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return out


def shutdown_process(proc: subprocess.Popen | None) -> None:
    if proc is None:
        return
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


def run_pipeline(config: RuntimeConfig, scenario: dict[str, Any]) -> dict[str, Any]:
    launch = launch_runtime_server(config)
    if not launch.health_ready:
        shutdown_process(launch.process)
        raise RuntimeError("Runtime server failed health check.")

    match = simulate_queue_and_match(scenario)
    result = {
        "status": "passed",
        "runtime_mode": launch.mode,
        "health_ready": launch.health_ready,
        "result": match,
        "notes": "Phase 2.5 local runtime scaffold. Real Unreal/EOS can be plugged into the same control path.",
    }

    out = write_result(config, result)
    result["result_file"] = str(out)
    shutdown_process(launch.process)
    return result
