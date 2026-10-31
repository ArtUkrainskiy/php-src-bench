#!/usr/bin/env python3
"""Finite supplementary experiment: warmed time, instructions, cycles, A/A."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import subprocess
import time

source_dir = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--bench-root', type=Path, required=True)
parser.add_argument('--builds', type=Path, required=True)
parser.add_argument('--out', type=Path, required=True)
parser.add_argument('--cpu', type=int, required=True)
parser.add_argument('--orchestrator-cpu', type=int, required=True)
parser.add_argument('--base-commit', default='ef99f4248f1450c39fb86fd7fd6f24c49b8d11eb')
parser.add_argument('--control-commit', default='ca89fb5fb96399ed730cacb12d948025f83c4e6e')
parser.add_argument('--nogram-commit', default='fa81a3379208e6f4b6d80f1cd0f7b7689cec1d20')
parser.add_argument('--scalar-commit', default='db4d3f65c6924674ec909466be40c6e735f88b85')
parser.add_argument('--smoke', action='store_true')
parser.add_argument('--extra', action='store_true', help='two additional periodic-needle attribution inputs')
parser.add_argument('--confirm', action='store_true', help='one independent repeat of the long early match on each compiler')
args = parser.parse_args()
root = args.out.resolve()
root.mkdir(parents=True, exist_ok=True)
bench_root = args.bench_root.resolve()
builds = args.builds.resolve()
suite = source_dir / ('gram-periodic-suite.php' if args.extra else 'suite.php')
env = {**os.environ, 'BENCH_BUILDS': str(builds), 'BENCH_RESULTS': str(root / 'runs'),
       'BENCH_PHP': str(builds / 'base-gcc15/sapi/cli/php'), 'NO_COLOR': '1'}
bench = str(bench_root / 'bench')
(root / 'runs').mkdir(exist_ok=True)
commits = {'base': args.base_commit,
           'product-guard': args.control_commit,
           'review-no-gram4': args.nogram_commit,
           'review-scalar': args.scalar_commit}
fingerprints = {}
for cc in ['gcc15', 'clang21']:
    for prefix, sha in commits.items():
        name = prefix + '-' + cc
        folder = builds / name
        meta = json.loads((folder / '.bench-build.json').read_text())
        ref = json.loads((builds / ('base-' + cc) / '.bench-build.json').read_text())
        assert meta['commit'] == sha and not meta['debug'] and not meta['snapshot']
        for field in ['cc', 'configure', 'cflags_user', 'ldflags', 'profile']:
            assert meta[field] == ref[field], (name, field)
        fingerprints[name] = dict(commit=sha, binary_sha256=hashlib.sha256((folder / 'sapi/cli/php').read_bytes()).hexdigest(), metadata=meta)
fp = root / 'build-fingerprints.json'
if fp.exists():
    assert json.loads(fp.read_text()) == fingerprints, 'A measured binary changed'
fp.write_text(json.dumps(fingerprints, indent=2) + '\n')
listing = json.loads(subprocess.check_output(['taskset', '-c', str(args.cpu), str(builds / 'base-gcc15/sapi/cli/php'),
    '-n', str(bench_root / 'lib/harness.php'), str(suite), '{"mode":"list","filter":null}'], text=True))
keys = [case['id'] for case in listing['cases']]
assert len(keys) == (2 if args.extra else 36), len(keys)
events_file = root / 'events.json'
events = json.loads(events_file.read_text()) if events_file.exists() else []

def run(name, a, b, key, target=1000):
    output = root / (name + '.json')
    if output.exists():
        data = json.loads(output.read_text())
        assert data['sides']['A']['name'] == a and data['sides']['B']['name'] == b
        return
    before = set((root / 'runs').glob('*.json'))
    cmd = ['taskset', '-c', str(args.orchestrator_cpu), bench, 'run', str(suite), '--a', a, '--b', b,
           '--cpu', str(args.cpu), '--rounds', '4', '--samples', '1', '--target-ms', str(target),
           '--warmup-ms', '1000', '--wait-idle', '120', '--perf', '--filter', '^' + re.escape(key) + '$']
    print(name, key, 'started', flush=True)
    start = time.time()
    with (root / (name + '.log')).open('w') as log:
        subprocess.run(cmd, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
    added = set((root / 'runs').glob('*.json')) - before
    assert len(added) == 1
    raw = added.pop()
    d = json.loads(raw.read_text())
    assert list(d['cases']) == [key]
    x, y = d['cases'][key]['sides'].values()
    assert x['input_hash'] == y['input_hash'] and x['output_hash'] == y['output_hash']
    output.write_bytes(raw.read_bytes())
    events.append(dict(name=name, a=a, b=b, case=key, seconds=time.time() - start))
    events_file.write_text(json.dumps(events, indent=2) + '\n')
    print(name, 'complete', round(time.time() - start), 's', flush=True)

def run_cycles(name, groups):
    path = root / (name + '.json')
    cmd = ['taskset', '-c', str(args.orchestrator_cpu), bench, 'compare']
    if path.exists():
        if json.loads(path.read_text())['complete']:
            return
        cmd += ['--resume', str(path)]
    else:
        cmd += [str(suite), *groups, '--cpu', str(args.cpu), '--passes', '3',
                '--out', str(path), '--wait-idle', '120']
    with (root / (name + '.log')).open('a') as log:
        subprocess.run(cmd, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)

if args.smoke:
    run('smoke-no-gram4-gcc15', 'product-guard-gcc15', 'review-no-gram4-gcc15',
        next(k for k in keys if k.startswith('route/gram/selective/absent ')))
    raise SystemExit(0)

if args.confirm:
    key = next(k for k in keys if k.startswith('route/long/early @ '))
    for cc in ['gcc15', 'clang21']:
        run(f'confirm-stock-native-{cc}-long-early', 'base-' + cc, 'product-guard-' + cc, key)
    (root / 'confirm-complete').write_text('PASS\n')
    raise SystemExit(0)

if args.extra:
    groups = []
    for cc in ['gcc15', 'clang21']:
        for i, key in enumerate(keys):
            run(f'extra-stock-native-{cc}-{i}', 'base-' + cc, 'product-guard-' + cc, key)
            for variant in ['no-gram4', 'scalar']:
                run(f'extra-{variant}-{cc}-{i}', 'product-guard-' + cc, 'review-' + variant + '-' + cc, key)
        groups += [f'nogram-{cc}=product-guard-{cc}:review-no-gram4-{cc}',
                   f'scalar-{cc}=product-guard-{cc}:review-scalar-{cc}',
                   f'stock-{cc}=base-{cc}:product-guard-{cc}']
    run_cycles('extra-cycles', groups)
    (root / 'extra-complete').write_text('PASS\n')
    raise SystemExit(0)

controls = [k for k in keys if any(k.startswith(p) for p in ['banlist12/en/post/early ', 'explode/colon2/4k '])]
assert len(controls) == 2
for cc in ['gcc15', 'clang21']:
    for i, key in enumerate(controls):
        run(f'aa-before-{cc}-{i}', 'product-guard-' + cc, 'product-guard-' + cc, key)
for i, key in enumerate(keys, 1):
    # Interleave compiler and variant, preserving temporal proximity of each A/B pair.
    for cc in ['gcc15', 'clang21']:
        for variant in ['no-gram4', 'scalar']:
            product_control = any(key.startswith(p + ' @ ') for p in [
                'banlist12/en/post/clean', 'banlist12/en/post/early', 'explode/colon2/4k',
                'substr-count/colon2/4k', 'str-replace/colon2/4k', 'render-template/4k'])
            if variant == 'no-gram4':
                relevant = key.startswith(('route/gram/', 'route/twoway/'))
            else:
                relevant = key.startswith(('route/pair/', 'route/gram/', 'route/twoway/', 'route/threshold/'))
            if not (product_control or relevant):
                continue
            run(f'{variant}-{cc}-{i:02d}', 'product-guard-' + cc, 'review-' + variant + '-' + cc, key)
        if key.startswith('route/'):
            run(f'stock-native-{cc}-{i:02d}', 'base-' + cc, 'product-guard-' + cc, key)
    print('CORPUS', i, '/', len(keys), flush=True)
for cc in ['gcc15', 'clang21']:
    for i, key in enumerate(controls):
        run(f'aa-after-{cc}-{i}', 'product-guard-' + cc, 'product-guard-' + cc, key)

groups = []
for cc in ['gcc15', 'clang21']:
    groups += [f'nogram-{cc}=product-guard-{cc}:review-no-gram4-{cc}',
               f'scalar-{cc}=product-guard-{cc}:review-scalar-{cc}',
               f'stock-{cc}=base-{cc}:product-guard-{cc}']
run_cycles('cycles', groups)
(root / 'measurements-complete').write_text(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + '\n')
print('Supplementary measurements complete', flush=True)
