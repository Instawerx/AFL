# AFL Phase 2 Execution Pack v1

This pack starts **Phase 2: Real System Execution** for AFL.

It adds:

- Unreal BuildGraph runner script
- EOS preflight runner
- Queue → match → reward harness runner
- Runtime config example
- A real Python harness for dry-run and config validation
- A starter scenario file
- A GitHub Actions workflow for runtime checks
- Phase 2 execution plan

## Intended use

1. Copy this pack into repo root.
2. Edit `build/config/runtime.env.example` into your real local env file.
3. Run:
   - `powershell -ExecutionPolicy Bypass -File .\build\scripts\run_eos_preflight.ps1 -RepoRoot .`
   - `powershell -ExecutionPolicy Bypass -File .\build\scripts\run_unreal_buildgraph.ps1 -RepoRoot .`
   - `powershell -ExecutionPolicy Bypass -File .\build\scripts\run_queue_reward_harness.ps1 -RepoRoot . -Scenario .\tests\runtime\scenarios\quickmatch_reward.yaml`

## Notes

This pack does **not** pretend to ship a working Unreal dedicated server or real EOS backend by itself.
It gives you a clean execution scaffold, real scripts, real config validation, and a repeatable harness so the repo can progress from document state into runtime state.
