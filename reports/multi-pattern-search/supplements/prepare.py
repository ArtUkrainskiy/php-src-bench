#!/usr/bin/env python3
"""Copy frozen PHP helpers into RUN_ROOT and smoke-test batches and constructors.

Requires RUN_ROOT, PHP_BUILD_GCC15, BENCH_CPU and four complete main series.
Uses the GCC product module from that run. Smoke output is separate from timing
captures. Existing prepared helpers/markers are refused, never overwritten.
"""

import hashlib
import json
import os
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPORT = HERE.parent
RUN = Path(os.environ['RUN_ROOT']).resolve()
CPU = int(os.environ['BENCH_CPU'])
PHP = Path(os.environ['PHP_BUILD_GCC15']) / 'sapi/cli/php'
NAMES = ['batch.php', 'construction.php', 'definitions.php', 'order-harness.php']
assert all(not (RUN / name).exists() for name in NAMES + ['SUPPLEMENTS_SMOKE_COMPLETE'])
assert (HERE / 'definitions.php').read_bytes() == (REPORT / 'harness.php').read_bytes().split(b'\ntry {\n', 1)[
    0
] + b'\n'
for cc in ['gcc15', 'clang21']:
    for stem, count in [('product', 92), ('size', 158)]:
        data = json.loads((RUN / f'data-{stem}-{cc}/results.json').read_text())
        assert data['status'] == 'complete' and len(data['rows']) == count
for name in NAMES:
    with (RUN / name).open('xb') as target:
        target.write((HERE / name).read_bytes())
command = ['taskset', '-c', str(CPU), str(PHP), '-n', '-d', 'extension=' + str(RUN / 'data-product-gcc15/strmatch.so')]
index = json.loads((REPORT / '../../corpus/multi-pattern-product/index.json').read_text())
cases = [
    case
    for filename in index['suite_sha256']
    for case in json.loads((REPORT / '../../corpus/multi-pattern-product' / filename).read_text())['cases']
]
case = next(case for case in cases if case['id'] == 'moderation.en.clean')
records = []


def call(helper, config, mutation=False):
    path = RUN / 'supplement-smoke.json'
    path.write_text(json.dumps(config))
    process = subprocess.run(
        [*command, str(RUN / helper), str(path)], capture_output=True, text=True, timeout=15, check=False
    )
    if mutation:
        assert process.returncode and 'Batch output mismatch' in process.stdout + process.stderr
        return {'mutation_caught': True}
    assert process.returncode == 0 and not process.stderr, (process.stdout, process.stderr)
    return json.loads(process.stdout)


for count in [1, 2]:
    config = {
        'case': case,
        'batch_size': count,
        'methods': case['methods'],
        'mode': 'check',
        'warmup_ns': 1_000_000,
        'sample_ns': 10_000_000,
        'passes': 1,
    }
    records.append(call('batch.php', config))
    config['mode'] = 'time'
    records.append(call('batch.php', config))
config.update(mode='check', mutation=True)
records.append(call('batch.php', config, True))
for kind in ['Matcher', 'Replacer']:
    config = {
        'family': str(REPORT / 'memory/glossary-catalog'),
        'size': 1,
        'class': kind,
        'passes': 1,
        'warmup_ns': 1_000_000,
        'sample_ns': 10_000_000,
    }
    for mode in ['check', 'first', 'time', 'aa']:
        config['mode'] = mode
        records.append(call('construction.php', config))
manifest = {name: hashlib.sha256((RUN / name).read_bytes()).hexdigest() for name in NAMES}
(RUN / 'supplement-smoke-results.json').write_text(json.dumps(records, indent=2) + '\n')
(RUN / 'supplement-smoke-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
(RUN / 'SUPPLEMENTS_SMOKE_COMPLETE').write_text('PASS\n')
(RUN / 'MATRIX_COMPLETE').write_text('PASS\n')
print('BATCH N1/N2, MUTATION, CONSTRUCTION N1 PASS')
