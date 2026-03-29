#!/usr/bin/env python3
from pathlib import Path
import re
import sys


def resolve_root() -> Path:
    cwd = Path.cwd().resolve()
    script_root = Path(__file__).resolve().parents[2]
    cwd_has_layout = (cwd / 'agents').is_dir() and (cwd / 'skills').is_dir()
    return cwd if cwd_has_layout else script_root

KEBAB_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*\.md$')
PY_RE = re.compile(r'^[a-z0-9_]+\.py$')
YML_RE = re.compile(r'^[a-z0-9][a-z0-9._-]*\.yml$')

def check_dir(path: Path, pattern, label: str):
    errors = []
    if not path.exists():
        return errors
    for item in path.iterdir():
        if item.is_file():
            if item.suffix == '.md' and label in {'agents', 'skills', 'templates'}:
                if not pattern.match(item.name):
                    errors.append(f'{label}: invalid markdown filename {item.name}')
            elif item.suffix == '.py' and label == 'scripts':
                if not pattern.match(item.name):
                    errors.append(f'{label}: invalid python filename {item.name}')
            elif item.suffix == '.yml' and label == 'workflows':
                if not pattern.match(item.name):
                    errors.append(f'{label}: invalid workflow filename {item.name}')
    return errors

def main() -> int:
    root = resolve_root()
    errors = []
    errors += check_dir(root / 'agents', KEBAB_RE, 'agents')
    errors += check_dir(root / 'skills', KEBAB_RE, 'skills')
    errors += check_dir(root / 'templates', KEBAB_RE, 'templates')
    errors += check_dir(root / 'build' / 'scripts', PY_RE, 'scripts')
    errors += check_dir(root / '.github' / 'workflows', YML_RE, 'workflows')

    if errors:
        print('Naming validation failed:')
        for err in errors:
            print(f' - {err}')
        return 1

    print('Naming validation passed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
