# AFL Build/Test Scaffold Pack v1

This pack adds the first executable build/test scaffold for the AFL automation repo.

## Included
- `build/buildgraph/AFL_BuildGraph.xml`
- `build/scripts/run_fast_validation.ps1`
- `build/scripts/run_packaged_smoke.ps1`
- `build/scripts/run_queue_reward_test.ps1`
- `templates/workflow-template.md`

## Intent
This is a real scaffold, not a fake completed pipeline.

It does three useful things now:

1. Runs the Python validators already present in your AFL repo.
2. Provides a valid BuildGraph pipeline shape for Unreal integration.
3. Establishes the package/smoke and queue/reward test entry points.

## What you still need to wire
- Unreal Engine install path
- Actual `AFL.uproject`
- EOS online shell
- Gauntlet/runtime test harness
- Packaged executable launch assertions
- Reward verification hooks

## First use
Run:

```powershell
python .\build\scripts\validate_repo.py
python .\build\scripts\validate_agents.py
python .\build\scripts\validate_naming.py
powershell -ExecutionPolicy Bypass -File .\build\scripts\run_fast_validation.ps1 -RepoRoot .
```

## Unreal integration
Once `AFL.uproject` exists, update:

- `UERoot`
- `ProjectPath`

inside `build/buildgraph/AFL_BuildGraph.xml`
