#!/usr/bin/env python3
"""Offline local documentation/provenance checks; no hardware or external-link claims."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'!?\[[^\]\n]*\]\((<[^>]+>|[^)\n]+)\)')
REQUIRED = [
    'AGENTS.md', 'README.md', 'docs/README.md', 'docs/project/requirements.md',
    'docs/architecture/system.md', 'docs/development/startup.md',
    'docs/development/worktrees.md', 'docs/development/testing.md',
    'contracts/README.md', 'firmware/motion-stm32/README.md',
    'firmware/esp-cam/README.md', 'firmware/manual-c3/README.md',
    'server/README.md', 'ai/README.md', 'web/README.md',
    'docs/development/error-documentation.md', 'docs/errors/README.md',
    '.github/ISSUE_TEMPLATE/error-session.md',
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchors(text):
    result = set()
    counts = {}
    for line in text.splitlines():
        if not re.match(r'^#{1,6}\s', line):
            continue
        heading = re.sub(r'^#{1,6}\s+|\s+#+\s*$', '', line).strip().lower()
        heading = re.sub(r'[^\w\- ]', '', heading).replace(' ', '-')
        count = counts.get(heading, 0)
        counts[heading] = count + 1
        result.add(heading if not count else f'{heading}-{count}')
    return result


def check():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f'Missing entry point: {name}')
    paths = []
    for name in ['README.md', 'AGENTS.md']:
        paths.append(ROOT / name)
    for directory in ['docs', 'contracts', 'firmware', 'server', 'ai', 'web', '.github', 'tests']:
        paths.extend((ROOT / directory).rglob('*.md'))
    # Historical bodies and supplied writing skills preserve original context/relative links.
    paths.extend((ROOT / 'resources').glob('*/README.md'))
    paths.append(ROOT / 'resources/AGENTS.md')
    checked_links = 0
    for path in paths:
        if not path.is_file():
            continue
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for match in LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith('<'):
                target = target[1:-1]
            # Markdown's optional quoted title is separate from the URL.
            target = re.split(r'\s+["\']', target, maxsplit=1)[0]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            checked_links += 1
            if not dest.exists():
                errors.append(f'{path.relative_to(ROOT)}: broken local link {target}')
            elif parsed.fragment and dest.suffix == '.md':
                if unquote(parsed.fragment) not in anchors(dest.read_text()):
                    errors.append(f'{path.relative_to(ROOT)}: broken heading {target}')

    originals = json.loads((ROOT / 'resources/sources.json').read_text())
    for source in originals:
        path = ROOT / source['path']
        if not path.exists() or digest(path) != source['sha256']:
            errors.append(f'Original school source changed/missing: {source["path"]}')

    manifest = json.loads((ROOT / 'docs/development/migration-manifest.json').read_text())
    for entry in manifest['entries']:
        for name in entry['destinations']:
            if not (ROOT / name).is_file():
                errors.append(f'Migration destination missing: {name}')
        if entry['action'] in ['preserved', 'archived-and-replaced']:
            if digest(ROOT / entry['destinations'][0]) != entry['original_sha256']:
                errors.append(f'Historical bytes changed: {entry["old"]}')

    audit = json.loads((ROOT / 'docs/project/source-audit.json').read_text())
    for source in audit['live_sources']:
        path = ROOT / source['snapshot']
        if not path.exists() or digest(path) != source['sha256']:
            errors.append(f'Source snapshot changed/missing: {source["snapshot"]}')

    schemas = list((ROOT / 'contracts').rglob('*.schema.json'))
    for path in schemas:
        schema = json.loads(path.read_text())
        if schema.get('x-status') != 'proposed' or not schema.get('x-owner'):
            errors.append(f'Schema approval/owner missing: {path.relative_to(ROOT)}')
    for message in errors:
        print(message, file=sys.stderr)
    if errors:
        return 1
    print(f'PASS: {len(paths)} Markdown files; {checked_links} local links; '
          f'{len(originals)} school originals; {len(manifest["entries"])} migration entries; '
          f'{len(audit["live_sources"])} source snapshots; {len(schemas)} proposed schemas')
    return 0


if __name__ == '__main__':
    raise SystemExit(check())
