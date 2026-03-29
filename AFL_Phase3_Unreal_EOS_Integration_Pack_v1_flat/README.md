# AFL Phase 3 Unreal + EOS Integration Pack v1

This pack upgrades AFL from a local runtime scaffold into a structured Unreal + EOS integration layer.

Included:

- `tests/runtime/eos_adapter.py`
- `tests/runtime/reward_service.py`
- `tests/runtime/result_contract.py`
- `tests/runtime/unreal_server_adapter.py`
- `tests/runtime/session_models.py`
- `build/scripts/run_local_unreal_runtime.ps1`
- `build/scripts/run_eos_session_smoke.ps1`
- `tests/runtime/scenarios/eos_quickmatch_smoke.yaml`
- `.github/workflows/phase3-eos-runtime.yml`
- `docs/phase3_unreal_eos_integration.md`

## What this pack does

It provides:

- a real EOS config + preflight adapter
- a real result contract schema validator
- a reward calculation service boundary
- a local Unreal server adapter
- a session model used by the runtime harness
- PowerShell entrypoints for Unreal runtime and EOS smoke checks

## What this pack does not claim

It does not claim to ship:
- production EOS credentials
- finished Unreal match code
- production reward APIs
- anti-cheat or live ops infrastructure

This is a clean integration layer for your current repo.
