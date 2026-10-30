#!/usr/bin/env python3
"""Reproduce the warmed one-second series with the unchanged native benchmark harness."""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--bench-root', type=Path, required=True)
p.add_argument('--builds', type=Path, required=True)
p.add_argument('--out', type=Path, required=True)
p.add_argument('--cpu', type=int, required=True)
p.add_argument('--orchestrator-cpu', type=int, required=True)
p.add_argument('--full', action='store_true')
p.add_argument('--primary-only', action='store_true', help='measure the 76 owned primary cases, without public document snapshots')
p.add_argument('--base-commit', default='ef99f4248f1450c39fb86fd7fd6f24c49b8d11eb')
p.add_argument('--candidate-commit', default='ca89fb5fb96399ed730cacb12d948025f83c4e6e')
a = p.parse_args()
a.out.mkdir(parents=True, exist_ok=True)
runs = a.out / 'runs'
runs.mkdir(exist_ok=True)
suite = a.bench_root / 'reports/substr-adaptive-search/suite.php'
env = {**os.environ, 'BENCH_BUILDS': str(a.builds), 'BENCH_RESULTS': str(runs),
       'BENCH_PHP': str(a.builds / 'base-gcc15/sapi/cli/php'), 'NO_COLOR': '1'}
ccs = ['gcc15', 'clang21']
baseline = a.base_commit
control = a.candidate_commit
keys = ['banlist12/en/post/early', 'banlist12/hi/post/early', 'banlist12/en/post/clean',
        'parse-http/small', 'banlist12/ru/thread/clean', 'render-template/4k']
frozen = json.loads((a.bench_root / 'reports/substr-adaptive-search/data/corpus-manifest.json').read_text())
corpus = Path(os.environ.get('SUBSTR_PRODUCT_CORPUS', str(a.bench_root / 'corpus/substr-product/generated')))
actual = json.loads((corpus / 'manifest.json').read_text())
actual_cases = {case['id']: case for case in actual['cases']}
primary_cases = set(json.loads((a.bench_root / 'reports/substr-adaptive-search/data/primary-cases.json').read_text()))
for case in frozen['cases']:
    if not a.full or a.primary_only:
        if case['id'] not in primary_cases:
            continue
    assert case['id'] in actual_cases and actual_cases[case['id']]['code'] == case['code'], case['id']
    name = case['input']
    path = corpus / 'inputs' / (name + '.txt')
    assert hashlib.sha256(path.read_bytes()).hexdigest() == frozen['inputs'][name]['sha256'], name
pattern = '^(?:' + '|'.join(re.escape(k) for k in keys) + ') @ '
events = json.loads((a.out / 'events.json').read_text()) if (a.out / 'events.json').exists() else []
fingerprints = {}
for cc in ccs:
    for prefix, commit in [('base-', baseline), ('product-guard-', control)]:
        name = prefix + cc
        folder = a.builds / name
        meta = json.loads((folder / '.bench-build.json').read_text())
        assert meta['commit'] == commit and not meta['debug'] and not meta['snapshot']
        assert meta['profile'] == 'docker'
        fingerprints[name] = {'commit': commit, 'binary_sha1': hashlib.sha1((folder / 'sapi/cli/php').read_bytes()).hexdigest()}
        reference = json.loads((a.builds / ('base-' + cc) / '.bench-build.json').read_text())
        for field in ['cc', 'configure', 'cflags_user', 'ldflags', 'profile']:
            assert meta[field] == reference[field], (name, field)
fp = a.out / 'build-fingerprints.json'
if fp.exists():
    assert json.loads(fp.read_text()) == fingerprints, 'Binaries changed since the previous part'
fp.write_text(json.dumps(fingerprints, indent=2) + '\n')


def run(name, cc, bprefix, samples, target, warmup, filter_pattern, perf=False):
    path = a.out / (name + '.json')
    if path.exists():
        d = json.loads(path.read_text())
        assert d['config']['samples'] == samples and d['config']['target_ms'] == target
        assert d['config']['warmup_ms'] == warmup
        assert d['config']['filter'] == filter_pattern and d['config']['rounds'] == 4
        assert d['sides']['A']['name'] == 'base-' + cc and d['sides']['B']['name'] == bprefix + cc
        return d
    print(name, 'started', flush=True)
    start = time.time()
    before = set(runs.glob('*.json'))
    cmd = ['taskset', '-c', str(a.orchestrator_cpu), str(a.bench_root / 'bench'), 'run', str(suite),
           '--a', 'base-' + cc, '--b', bprefix + cc, '--cpu', str(a.cpu), '--rounds', '4',
           '--samples', str(samples), '--target-ms', str(target), '--warmup-ms', str(warmup),
           '--wait-idle', '300']
    if filter_pattern:
        cmd += ['--filter', filter_pattern]
    if perf:
        cmd += ['--perf']
    with (a.out / (name + '.log')).open('w') as log:
        subprocess.run(cmd, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
    added = set(runs.glob('*.json')) - before
    assert len(added) == 1
    raw = added.pop()
    d = json.loads(raw.read_text())
    assert d['sides']['A']['build']['commit'] == baseline
    assert d['sides']['B']['build']['commit'] == (baseline if bprefix == 'base-' else control)
    for case in d['cases'].values():
        x, y = case['sides']['A'], case['sides']['B']
        assert x['input_hash'] == y['input_hash'] and x['output_hash'] == y['output_hash']
    path.write_bytes(raw.read_bytes())
    events.append({'name': name, 'seconds': time.time() - start})
    (a.out / 'events.json').write_text(json.dumps(events, indent=2) + '\n')
    print(name, 'complete', round(time.time() - start), 's', flush=True)
    return d


for cc in ccs:
    run(cc + '-aa-50ms', cc, 'base-', 7, 50, 10, pattern)
    run(cc + '-aa-1sec', cc, 'base-', 1, 1000, 1000, pattern)
print('One-second pilot complete', flush=True)

if a.full or a.primary_only:
    listing = json.loads(subprocess.check_output(['taskset', '-c', str(a.cpu),
        str(a.builds / 'base-gcc15/sapi/cli/php'), '-n', str(a.bench_root / 'lib/harness.php'),
        str(suite), json.dumps({'mode': 'list', 'filter': None})], text=True))
    all_keys = [c['id'] for c in listing['cases']]
    # Preserve the established primary product set first, then cover the remainder.
    primary = set(json.loads((a.bench_root / 'reports/substr-adaptive-search/data/primary-cases.json').read_text()))
    assert len(primary) == 76 and primary <= set(all_keys)
    order = [k for k in all_keys if k in primary]
    if not a.primary_only:
        order += [k for k in all_keys if k not in primary]
    total = 76 if a.primary_only else 233
    assert len(order) == len(set(order)) == total
    (a.out / 'full-order.json').write_text(json.dumps(order, indent=2) + '\n')
    aggregate = {}
    parts = {cc: [] for cc in ccs}
    for index, key in enumerate(order, 1):
        exact = '^' + re.escape(key).replace(r'\#', '#') + '$'
        for cc in ccs:
            name = f'{cc}-case{index:03d}-1sec'
            d = run(name, cc, 'product-guard-', 1, 1000, 1000, exact, True)
            assert list(d['cases']) == [key]
            parts[cc].append(name + '.json')
            if cc not in aggregate:
                aggregate[cc] = copy.deepcopy(d)
                aggregate[cc]['cases'] = {}
                aggregate[cc]['config']['filter'] = None
                aggregate[cc]['elapsed_s'] = 0
            combined = aggregate[cc]
            combined['cases'].update(d['cases'])
            combined['elapsed_s'] += d['elapsed_s']
            combined['seconds_series'] = {'complete': index == total, 'total_cases': total,
                'completed_cases': index, 'native_parts': parts[cc],
                'elapsed_s_semantics': 'sum of native per-case series durations'}
            target_path = a.out / (cc + f'-full{total}-1sec.json')
            temporary = target_path.with_suffix('.json.tmp')
            temporary.write_text(json.dumps(combined, indent=2) + '\n')
            temporary.replace(target_path)
            print(cc, 'corpus progress', index, f'/ {total}:', key, flush=True)
    print('One-second product corpus complete', flush=True)
