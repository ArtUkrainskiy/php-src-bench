#!/usr/bin/env python3
"""One >=3s warmup and ten ~1s samples per build/case; separate paired counters."""
import argparse
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
p.add_argument('--lane', choices=['amd', 'intel'], required=True)
p.add_argument('--cpu', type=int, required=True)
p.add_argument('--orchestrator', type=int, required=True)
p.add_argument('--wait-idle', type=int, default=120)
p.add_argument('--counters-only', action='store_true')
a = p.parse_args()
suite = Path(__file__).with_name('suite.php')
a.out.mkdir(parents=True, exist_ok=True)
runs = a.out / 'runs'; runs.mkdir(exist_ok=True)
compilers = ['gcc15', 'clang21'] if a.lane == 'amd' else ['gcc13', 'gcc14', 'clang18', 'clang20']
env = {**os.environ, 'BENCH_BUILDS': str(a.builds), 'BENCH_RESULTS': str(runs),
       'BENCH_PHP': str(a.builds / ('compact-base-' + compilers[0]) / 'sapi/cli/php'), 'NO_COLOR': '1'}
bench = str(a.bench_root / 'bench')
fingerprints = {}
for cc in compilers:
    ref = json.loads((a.builds / ('compact-base-' + cc) / '.bench-build.json').read_text())
    for prefix, commit in [('compact-base-', 'cf1b5771a76a81b455a8677446daf9c46e1781be'), ('compact-head-', '8d7babbc364ffcf28dac9777ce807edc9adbb534')]:
        name = prefix + cc; folder = a.builds / name
        meta = json.loads((folder / '.bench-build.json').read_text())
        assert meta['commit'] == commit and not meta['debug'] and not meta['snapshot']
        for field in ['cc', 'configure', 'cflags_user', 'ldflags', 'profile']: assert meta[field] == ref[field], (name, field)
        raw = (folder / 'sapi/cli/php').read_bytes()
        fingerprints[name] = dict(commit=commit, sha1=hashlib.sha1(raw).hexdigest(), sha256=hashlib.sha256(raw).hexdigest(), metadata=meta)
fp = a.out / 'builds.json'
if fp.exists(): assert json.loads(fp.read_text()) == fingerprints
fp.write_text(json.dumps(fingerprints, indent=2) + '\n')
listing = json.loads(subprocess.check_output([env['BENCH_PHP'], '-n', str(a.bench_root / 'lib/harness.php'), str(suite), '{"mode":"list","filter":null}'], text=True))
all_keys = [c['id'] for c in listing['cases']]
assert len(all_keys) == 26, len(all_keys)
def name(key): return key.split(' @ ')[0]
if a.lane == 'amd':
    keys = [k for k in all_keys if '/thread/' not in k or name(k) in ['banlist12/en/thread/clean', 'banlist12/zh/thread/clean']]
    assert len(keys) == 19
else:
    selected = ['banlist12/en/thread/clean', 'banlist12/zh/thread/clean', 'render-template/4k', 'explode/colon2/4k', 'boundary/31/early', 'boundary/32/early']
    keys = [k for k in all_keys if name(k) in selected]
    assert len(keys) == 6
control = next(k for k in all_keys if name(k) == 'boundary/31/early')
events_file = a.out / 'events.json'
events = json.loads(events_file.read_text()) if events_file.exists() else []
(a.out / 'protocol.json').write_text(json.dumps(dict(lane=a.lane, timed_cases=[] if a.counters_only else keys, counter_cases=all_keys,
    warmup_ms=3000, samples=10, target_ms=1000, rounds=1, elapsed_verdict='descriptive only; one paired round',
    counter_passes=5, counter_target_ms=50), indent=2) + '\n')
def run(tag, cc, key, aa=False):
    output = a.out / (tag + '.json')
    if output.exists(): return
    start = time.time(); before = set(runs.glob('*.json'))
    cmd = ['taskset', '-c', str(a.orchestrator), bench, 'run', str(suite), '--a', 'compact-base-' + cc,
           '--b', ('compact-base-' if aa else 'compact-head-') + cc, '--cpu', str(a.cpu),
           '--rounds', '1', '--samples', '10', '--target-ms', '1000', '--warmup-ms', '3000',
           '--wait-idle', str(a.wait_idle), '--filter', '^' + re.escape(key) + '$']
    print(tag, key, 'started', flush=True)
    with (a.out / (tag + '.log')).open('w') as log:
        subprocess.run(cmd, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
    added = set(runs.glob('*.json')) - before; assert len(added) == 1
    raw = added.pop(); data = json.loads(raw.read_text()); assert list(data['cases']) == [key]
    x, y = (data['cases'][key]['sides'][s] for s in ['A', 'B'])
    assert x['input_hash'] == y['input_hash'] and x['output_hash'] == y['output_hash']
    output.write_bytes(raw.read_bytes())
    events.append(dict(tag=tag, compiler=cc, case=key, aa=aa, seconds=time.time() - start))
    events_file.write_text(json.dumps(events, indent=2) + '\n')
    print(tag, 'complete', round(time.time() - start), 's', flush=True)
if not a.counters_only:
    for cc in compilers: run('aa-before-' + cc, cc, control, True)
    for i, key in enumerate(keys, 1):
        for cc in compilers: run(f'case-{i:02d}-' + cc, cc, key)
        print('PROGRESS', i, '/', len(keys), flush=True)
    for cc in compilers: run('aa-after-' + cc, cc, control, True)
path = a.out / 'cycles.json'
if not path.exists() or not json.loads(path.read_text())['complete']:
    cmd = ['taskset', '-c', str(a.orchestrator), bench, 'compare']
    if path.exists(): cmd += ['--resume', str(path)]
    else: cmd += [str(suite), *[f'{cc}=compact-base-{cc}:compact-head-{cc}' for cc in compilers], '--cpu', str(a.cpu), '--passes', '5', '--target-ms', '50', '--out', str(path), '--wait-idle', str(a.wait_idle)]
    with (a.out / 'cycles.log').open('a') as log: subprocess.run(cmd, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
(a.out / 'complete').write_text('PASS\n')
print('All compact-Sunday measurements complete', flush=True)
