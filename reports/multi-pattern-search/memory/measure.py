#!/usr/bin/env python3
"""Measure both prepared classes in five fresh processes per size on a Linux CPU."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--php-build', type=Path, required=True)
    parser.add_argument('--module', type=Path, required=True)
    parser.add_argument('--compiler', choices=['gcc15', 'clang21'], required=True)
    parser.add_argument('--reference-data', type=Path,
                        help='Complete time-series JSON for the exact PHP/module binaries (default: published series)')
    parser.add_argument('--cpu', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Use a new output file')
    if os.environ.get('USE_ZEND_ALLOC') == '0':
        raise SystemExit('USE_ZEND_ALLOC=0 disables the measured counter')
    index = json.loads((ROOT / 'index.json').read_text())
    for name, expected in index['files_sha256'].items():
        assert digest(ROOT / name) == expected, name
    build = json.loads((args.php_build / '.bench-build.json').read_text())
    reference_path = args.reference_data or ROOT.parent / 'data' / f'{args.compiler}.json'
    reference = json.loads(reference_path.read_text())['metadata']
    php = args.php_build / 'sapi/cli/php'
    assert not build['debug'] and build['profile'] == 'docker'
    assert digest(php) == reference['php_sha256'], 'Use the published release PHP binary'
    assert digest(args.module) == reference['module_sha256'], 'Use the published extension binary'
    metadata = {key: reference[key] for key in ['compiler', 'runtime_build', 'source_revision', 'source_sha256',
                                               'php_sha256', 'module_sha256', 'cpu_model']}
    metadata.update({'measured_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                     'cpu': args.cpu, 'repeats': 5, 'metric': 'Zend live allocation bytes, memory_get_usage(false)',
                     'peak': 'memory_get_peak_usage(false), reset immediately before each operation',
                     'index_sha256': digest(ROOT / 'index.json'), 'driver_sha256': digest(__file__),
                     'harness_sha256': digest(ROOT / 'measure.php'), 'one_configuration_per_process': True})
    rows = []
    for family in index['families']:
        for size in index['sizes']:
            for kind in ['Matcher', 'Replacer']:
                samples = []
                for repeat in range(5):
                    command = ['taskset', '-c', str(args.cpu), str(php), '-n', '-d', 'memory_limit=1G',
                               '-d', 'opcache.enable_cli=0', '-d', 'extension=' + str(args.module),
                               str(ROOT / 'measure.php'), str(ROOT / family), str(size), kind]
                    result = subprocess.run(command, text=True, capture_output=True, timeout=30)
                    if result.returncode or result.stderr:
                        raise RuntimeError(f'{family}/{size}/{kind}: {result.stdout}\n{result.stderr}')
                    sample = json.loads(result.stdout)
                    assert sample['size'] == size and sample['class'] == kind
                    assert not sample['runtime']['debug'] and sample['runtime']['zend_allocator']
                    samples.append(sample)
                rows.append({'family': family, 'size': size, 'class': kind, 'samples': samples})
                print(f'{args.compiler}: {family} {size} {kind} PASS', flush=True)
    output = {'status': 'complete', 'metadata': metadata, 'rows': rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation also protects an existing file if another process wrote it.
    with args.output.open('x') as stream:
        stream.write(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print(f'MEMORY COMPLETE: {len(rows)} configurations, {len(rows) * 5} fresh processes', flush=True)


if __name__ == '__main__':
    main()
