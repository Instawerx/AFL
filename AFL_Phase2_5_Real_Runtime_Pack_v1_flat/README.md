# AFL Phase 2.5 Real Runtime Pack v1

This pack upgrades the AFL runtime harness from a pure dry-run into a real local runtime scaffold.

It adds:

- tests/runtime/orchestrator.py
- tests/runtime/runtime_config.py
- upgraded tests/runtime/queue_reward_harness.py
- build/scripts/run_afl_server.ps1
- updated scenario model
- runtime stub server for local bring-up
- CI workflow for runtime harness

This pack can:

- load runtime config from environment or env file
- start a local server executable or Python stub server
- wait for a TCP health port
- simulate queue -> session -> match -> reward flow
- write structured JSON results to artifacts/runtime

This pack does not pretend to provide:

- a finished Unreal dedicated server
- real EOS session creation
- real production economy writes
- anti-cheat
- real robot telemetry
