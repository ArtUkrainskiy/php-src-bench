#!/usr/bin/env python3
"""Run each frozen case in fresh paired processes, then separate native counter suites."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--out', type=Path, required=True)
p.add_argument('--cpu', type=int, required=True)
p.add_argument('--compilers', required=True, help='build suffixes, e.g. gcc13,clang20')
p.add_argument('--master', default='master', help='build prefix')
p.add_argument('--candidate', default='compact', help='build prefix')
p.add_argument('--family', choices=['core', 'extensions'], default='core')
p.add_argument('--bench', type=Path, help='optional private extension-enabled runner')
p.add_argument('--wait-idle', type=int, default=120)
p.add_argument('--smoke', action='store_true', help='one case/compiler, tiny elapsed and counter runs')
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
bench = (a.bench or root.parents[1] / 'bench').resolve()
a.out = a.out.resolve()
a.out.mkdir(parents=True, exist_ok=True)
index = json.loads((root / 'corpus/index.json').read_text())
ccs = a.compilers.split(',')
suites = []
for entry in index['suites']:
    if (entry['family'] == 'core') != (a.family == 'core'):
        continue
    cases = json.loads((root / 'corpus' / entry['file']).read_text())['cases']
    suites.append(dict(name=entry['name'], path=str(root / 'suites' / (entry['name'] + '.php')),
                       stage='extensions' if entry['family'] != 'core' else 'controls' if entry['control_only'] else 'product',
                       cases=[c['name'] + ' @ ' + c['input'] for c in cases if c['benchmark']]))
controls = []
byname = {s['name']: s for s in suites}
for name in ['moderation-long', 'substr-count', 'mbstring', 'intl-ascii']:
    if name in byname:controls.append((byname[name], byname[name]['cases'][0], a.master))
for name, prefix in [('replace', 'str_replace/en/repeated @'),
                     ('documents-repeated', 'documents/repeated/str_replace/23 @')]:
    if name in byname:
        s = byname[name]
        controls.append((s, next(k for k in s['cases'] if k.startswith(prefix)), a.candidate))
jobs = []
for when in ['before', 'cases', 'after']:
    if when != 'cases':
        for cc in ccs:
            for i, (suite, key, build) in enumerate(controls):
                jobs.append(dict(tag=f'aa-{when}-{i}-{cc}', suite=suite['path'], key=key,
                                 a=build + '-' + cc, b=build + '-' + cc))
    else:
        for stage in ['product', 'controls', 'extensions']:
            for s in suites:
                if s['stage'] != stage:continue
                for i, key in enumerate(s['cases']):
                    for cc in ccs:
                        jobs.append(dict(tag=f'{s["name"]}-{i}-{cc}', suite=s['path'], key=key,
                                         a=a.master + '-' + cc, b=a.candidate + '-' + cc))
if a.smoke:jobs = [dict(tag='smoke-' + cc, suite=suites[0]['path'], key=suites[0]['cases'][0],
                      a=a.master + '-' + cc, b=a.candidate + '-' + cc) for cc in ccs]
builds_dir = Path(os.environ.get('BENCH_BUILDS', root.parents[1].parent / 'php-builds')).resolve()
build_hashes = {name: hashlib.sha256((builds_dir / name / 'sapi/cli/php').read_bytes()).hexdigest()
                for name in {j[side] for j in jobs for side in ['a', 'b']}}
runner_hashes = {str(f.relative_to(bench.parent)): hashlib.sha256(f.read_bytes()).hexdigest()
                 for f in [bench, *sorted((bench.parent / 'lib').glob('*.php'))]}
module_hashes = {}
module_map = bench.parent / 'modules-map.json'
if module_map.exists():
    runner_hashes['modules-map.json'] = hashlib.sha256(module_map.read_bytes()).hexdigest()
    for directory in set(json.loads(module_map.read_text()).values()):
        for name in ['mbstring.so', 'intl.so']:
            f = Path(directory) / name
            module_hashes[str(f)] = hashlib.sha256(f.read_bytes()).hexdigest()
plan = dict(jobs=jobs, cpu=a.cpu, smoke=a.smoke, wait_idle=a.wait_idle,
            bench=str(bench), master=a.master, candidate=a.candidate, build_hashes=build_hashes,
            runner_hashes=runner_hashes, module_hashes=module_hashes,
            corpus_index_sha256=hashlib.sha256((root / 'corpus/index.json').read_bytes()).hexdigest())
planfile = a.out / 'plan.json'
if planfile.exists():assert json.loads(planfile.read_text()) == plan
else:planfile.write_text(json.dumps(plan, indent=2) + '\n')
env = {**os.environ, 'NO_COLOR': '1'}
for i, job in enumerate(jobs, 1):
    target = a.out / (job['tag'] + '.json')
    if target.exists():continue
    raw = a.out / 'raw' / job['tag']; raw.mkdir(parents=True, exist_ok=True)
    assert not list(raw.glob('*.json')), 'Retained incomplete run; inspect before resuming: ' + str(raw)
    env['BENCH_RESULTS'] = str(raw)
    cmd = [str(bench), 'run', job['suite'], '--a', job['a'], '--b', job['b'], '--cpu', str(a.cpu),
           '--filter', '^' + re.escape(job['key']) + '$', '--rounds', '1' if a.smoke else '5',
           '--samples', '1' if a.smoke else '5', '--target-ms', '10' if a.smoke else '200',
           '--warmup-ms', '10' if a.smoke else '500', '--wait-idle', str(a.wait_idle)]
    print(f'{i}/{len(jobs)} {job["tag"]} START', flush=True)
    log = a.out / (job['tag'] + '.log')
    with log.open('w') as stream:subprocess.run(cmd, env=env, stdout=stream, stderr=subprocess.STDOUT, check=True)
    files = list(raw.glob('*.json')); assert len(files) == 1
    record = json.loads(files[0].read_text()); case = record['cases'][job['key']]
    for field in ['input_hash', 'output_hash']:
        assert len(case['sides']['A'][field]) == 1
        assert case['sides']['A'][field] == case['sides']['B'][field]
    assert 'measuring anyway' not in log.read_text(), 'Disturbed run retained: ' + str(log)
    target.write_bytes(files[0].read_bytes())
    print(f'{i}/{len(jobs)} {job["tag"]} DONE', flush=True)
for suite in suites[:1] if a.smoke else suites:
    target = a.out / ('counters-' + suite['name'] + '.json')
    log = a.out / ('counters-' + suite['name'] + '.log')
    if target.exists() and json.loads(target.read_text())['complete']:
        record = json.loads(target.read_text())
        assert not record['warnings'] and not record['marks']
        assert log.exists() and 'measuring anyway' not in log.read_text(), 'Disturbed run retained: ' + str(log)
        continue
    cmd = [str(bench), 'compare']
    if target.exists():cmd += ['--resume', str(target)]
    else:
        cmd += [suite['path'], *[cc + '=' + a.master + '-' + cc + ':' + a.candidate + '-' + cc for cc in ccs],
                '--cpu', str(a.cpu), '--passes', '1' if a.smoke else '5', '--target-ms', '10' if a.smoke else '50',
                '--wait-idle', str(a.wait_idle), '--out', str(target)]
        if a.smoke:cmd += ['--filter', '^' + re.escape(suite['cases'][0]) + '$']
    print('COUNTERS ' + suite['name'] + ' START', flush=True)
    with log.open('a') as stream:subprocess.run(cmd, env=env, stdout=stream, stderr=subprocess.STDOUT, check=True)
    record = json.loads(target.read_text())
    assert record['complete'] and not record['warnings'] and not record['marks']
    assert 'measuring anyway' not in log.read_text(), 'Disturbed run retained: ' + str(log)
    print('COUNTERS ' + suite['name'] + ' DONE', flush=True)
(a.out / 'complete').write_text('PASS\n')
