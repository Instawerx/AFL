# AFL Agent Pack v1

This pack is a repo-ready starting point for the Avatar Fight League build system.

It contains:

- A machine-readable agent registry
- 12 AFL-specific expert agent profiles
- 13 grounded implementation skills
- 4 reusable templates
- 3 validation scripts
- 2 GitHub Actions workflows

## Intended placement

Copy these folders into the root of the AFL repository:

- `agents/`
- `skills/`
- `templates/`
- `build/scripts/`
- `.github/workflows/`

## Design rules

- Agents are narrow and production-oriented.
- Protected zones are explicit.
- Skills are operational playbooks, not generic advice.
- Validation scripts are executable and repo-safe.
- Workflows are conservative and do not assume Unreal is installed on GitHub runners.

## Recommended first use

1. Commit the pack.
2. Review `agents/registry.yaml`.
3. Assign the Master Orchestrator as the only planner.
4. Use skills from `skills/` as standard operating procedures.
5. Run:

```bash
python build/scripts/validate_repo.py
python build/scripts/validate_agents.py
python build/scripts/validate_naming.py
```

## Notes

- This pack assumes Unreal content is eventually Perforce-first, while scripts/docs may also be mirrored in Git.
- No agent is allowed to directly change protected authority zones without human review.
- The pack is written for AFL's current scope: Crash Site Omega, Assault Core, EOS session flow, Coins/Tickets/XP, and build automation.
