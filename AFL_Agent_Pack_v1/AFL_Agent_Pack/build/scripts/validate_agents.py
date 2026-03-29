#!/usr/bin/env python3
from pathlib import Path
import sys


def resolve_root() -> Path:
    cwd = Path.cwd().resolve()
    script_root = Path(__file__).resolve().parents[2]
    cwd_has_layout = (cwd / 'agents').is_dir() and (cwd / 'skills').is_dir()
    return cwd if cwd_has_layout else script_root

try:
    import yaml
except ImportError:
    print('PyYAML is required for validate_agents.py. Install with: pip install pyyaml')
    raise SystemExit(2)

REQUIRED_FRONTMATTER_KEYS = {
    'id', 'name', 'version', 'status', 'primary_domains', 'allowed_paths',
    'protected_paths', 'inputs', 'outputs', 'handoff_targets', 'kpis', 'system_prompt'
}

def parse_frontmatter(path: Path):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        raise ValueError('missing YAML frontmatter start')
    try:
        _, body = text.split('---\n', 1)
        fm_text, _rest = body.split('\n---\n', 1)
    except ValueError:
        raise ValueError('malformed YAML frontmatter block')
    data = yaml.safe_load(fm_text)
    if not isinstance(data, dict):
        raise ValueError('frontmatter did not parse to mapping')
    return data

def main() -> int:
    root = resolve_root()
    registry_path = root / 'agents' / 'registry.yaml'
    if not registry_path.exists():
        print('Missing agents/registry.yaml')
        return 1

    registry = yaml.safe_load(registry_path.read_text(encoding='utf-8'))
    if not isinstance(registry, dict) or 'agents' not in registry:
        print("registry.yaml missing top-level 'agents'")
        return 1

    errors = []
    registry_ids = set()
    for entry in registry['agents']:
        agent_id = entry.get('id')
        agent_file = entry.get('file')
        if not agent_id or not agent_file:
            errors.append('registry entry missing id or file')
            continue
        registry_ids.add(agent_id)
        full_path = root / agent_file
        if not full_path.exists():
            errors.append(f'registry points to missing file: {agent_file}')
            continue
        try:
            fm = parse_frontmatter(full_path)
        except Exception as exc:
            errors.append(f'{agent_file}: {exc}')
            continue

        missing = REQUIRED_FRONTMATTER_KEYS - set(fm.keys())
        if missing:
            errors.append(f"{agent_file}: missing frontmatter keys: {', '.join(sorted(missing))}")

        if fm.get('id') != agent_id:
            errors.append(f'{agent_file}: frontmatter id does not match registry id')

    agent_files = list((root / 'agents').glob('*.md'))
    file_ids = set()
    for path in agent_files:
        try:
            fm = parse_frontmatter(path)
            file_ids.add(fm.get('id'))
        except Exception as exc:
            errors.append(f'{path.relative_to(root)}: {exc}')

    orphan_ids = sorted(x for x in file_ids if x and x not in registry_ids)
    for oid in orphan_ids:
        errors.append(f'agent file id not present in registry: {oid}')

    if errors:
        print('Agent validation failed:')
        for err in errors:
            print(f' - {err}')
        return 1

    print('Agent validation passed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
