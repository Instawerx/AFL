#!/usr/bin/env python3
from pathlib import Path
import sys

REQUIRED_DIRS = [
    "agents",
    "skills",
    "templates",
    "build/scripts",
    ".github/workflows",
]

REQUIRED_FILES = [
    "README.md",
    ".gitignore",
    "agents/registry.yaml",
    "templates/agent-template.md",
    "templates/skill-template.md",
    "templates/workflow-template.md",
    "templates/validation-rule-template.md",
    "build/scripts/validate_repo.py",
    "build/scripts/validate_agents.py",
    "build/scripts/validate_naming.py",
    ".github/workflows/docs-lint.yml",
    ".github/workflows/repo-structure-check.yml",
]

def main() -> int:
    root = Path('.').resolve()
    errors = []
    for d in REQUIRED_DIRS:
        if not (root / d).is_dir():
            errors.append(f"Missing required directory: {d}")
    for f in REQUIRED_FILES:
        if not (root / f).exists():
            errors.append(f"Missing required file: {f}")

    agent_count = len(list((root / 'agents').glob('*.md'))) if (root / 'agents').exists() else 0
    if agent_count < 12:
        errors.append(f"Expected at least 12 agent markdown files, found {agent_count}")

    skill_count = len(list((root / 'skills').glob('*.md'))) if (root / 'skills').exists() else 0
    if skill_count < 10:
        errors.append(f"Expected at least 10 skill markdown files, found {skill_count}")

    if errors:
        print('AFL repo structure validation failed:')
        for err in errors:
            print(f' - {err}')
        return 1

    print('AFL repo structure validation passed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
