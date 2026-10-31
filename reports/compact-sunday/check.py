#!/usr/bin/env python3
"""Independently check the published metrics against the archived native records."""
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import re
import statistics
import tarfile

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'manifest.json').read_text())
metrics = json.loads((ROOT / 'metrics.json').read_text())
assert len(metrics) == manifest['elapsed_pairs'] == 44
assert len({r['source'] for r in metrics}) == 44

def close(actual, expected):
    assert math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-8), (actual, expected)

def normalized(value):
    if isinstance(value, dict):
        return {k: normalized(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normalized(v) for v in value]
    if isinstance(value, str):
        return re.sub(r'/(?:tmp|home)/[^\s"\\)]+', lambda m: '<recorded-path>/' + Path(m[0]).name, value)
    return value

with tarfile.open(ROOT / 'data/native.tar.gz') as archive:
    def raw(name):
        return archive.extractfile(name).read()

    counters = {}
    for folder, filename in [('amd', 'amd-cycles.json'), ('intel-counters', 'intel-cycles.json'), ('early31', 'early31-cycles.json')]:
        data = json.loads(raw(folder + '/cycles.json'))
        assert data['complete'] and not data['warnings'] and not data['marks']
        assert data['config']['passes'] == 5 and data['config']['target_ms'] == 50
        assert json.loads((ROOT / filename).read_text()) == normalized(data)
        suite = ROOT / ('early31-suite.php' if folder == 'early31' else 'suite.php')
        frozen_suite = suite.read_bytes()
        if folder != 'early31':
            # Only the relative require path changes when moving the measured suite to reports/.
            frozen_suite = frozen_suite.replace(b"'/../../suites/substr-product.php'", b"'/../../../suites/substr-product.php'")
        assert hashlib.sha1(frozen_suite).hexdigest() == data['sources']['suite']
        for key, file in [('harness', 'lib/harness.php'), ('corpus', 'lib/Corpus.php')]:
            assert hashlib.sha1((ROOT.parents[1] / file).read_bytes()).hexdigest() == data['sources'][key]
        values = defaultdict(lambda: defaultdict(list))
        fingerprints = json.loads(raw(('amd' if folder == 'early31' else folder) + '/builds.json'))
        for name, build in data['builds'].items():
            assert build['sha1'] == fingerprints[name]['sha1']
            assert build['build']['commit'] == fingerprints[name]['commit']
            assert not build['info']['debug'] and build['build']['profile'] == 'docker'
        for group, side, key, cycles, instructions, empty_cycles, empty_instructions in data['rows']:
            n = data['cases'][key]['n']
            values[group, key][side].append(((cycles - empty_cycles) / n, (instructions - empty_instructions) / n))
        for (group, key), sides in values.items():
            x, y = sides['a'], sides['b']
            assert len(x) == len(y) == 5
            counters[filename, group, key] = {
                'a': statistics.median(v[0] for v in x), 'b': statistics.median(v[0] for v in y),
                'ai': statistics.median(v[1] for v in x), 'bi': statistics.median(v[1] for v in y),
                'delta': 100 * (statistics.median(b[0] / a[0] for a, b in zip(x, y)) - 1),
            }

    for row in metrics:
        payload = raw(row['source'])
        assert hashlib.sha256(payload).hexdigest() == manifest['raw_sha256'][row['source']]
        data = json.loads(payload)
        assert (data['config']['rounds'], data['config']['samples'], data['config']['target_ms'], data['config']['warmup_ms']) == (1, 10, 1000, 3000)
        case = data['cases'][row['case']]
        assert row['bytes'] == case['input_len']
        assert row['aa'] == (data['sides']['A']['name'] == data['sides']['B']['name'])
        builds = json.loads(raw('amd/builds.json'))
        for side, field in [('A', 'a'), ('B', 'b')]:
            meta = data['sides'][side]['build']
            expected = manifest['base'] if side == 'A' or row['aa'] else manifest['head']
            assert meta['commit'] == expected and not meta['debug'] and not meta['snapshot']
            assert meta == builds[data['sides'][side]['name']]['metadata']
            result = case['sides'][side]
            assert len(result['rounds']) == 1 and len(result['rounds'][0]) == 10
            loop = statistics.median(result['loop_ns'])
            samples = [v - loop for v in result['rounds'][0]]
            close(row[field + '_ns'], statistics.median(samples))
            close(row[field + '_min'], min(samples))
            close(row[field + '_max'], max(samples))
        close(row['delta_time'], 100 * (row['b_ns'] / row['a_ns'] - 1))
        assert case['sides']['A']['input_hash'] == case['sides']['B']['input_hash']
        assert case['sides']['A']['output_hash'] == case['sides']['B']['output_hash']
        assert row['idle_wait_timeout'] == ('measuring anyway' in raw(row['log']).decode())
        if row['aa']:
            assert row['cycles'] is None
        else:
            filename = 'early31-cycles.json' if row['source'].startswith('early31/') else 'amd-cycles.json'
            for key, value in counters[filename, row['compiler'], row['case']].items():
                close(row['cycles'][key], value)

text = (ROOT / 'verify/standalone.c').read_text()
begin = text.index('static zend_always_inline void zend_memnstr_ex_pre(')
end = text.index('static zend_always_inline const char *', begin)
assert hashlib.sha256(text[begin:end].encode()).hexdigest() == json.loads((ROOT / 'data/c-validation.json').read_text())['source_sha256']
summary = json.loads((ROOT / 'data/php-validation-summary.json').read_text())
assert len(summary) == 9
with tarfile.open(ROOT / 'data/php-validation.tar.gz') as archive:
    for row in summary:
        log = archive.extractfile(row['log']).read().decode()
        for key, label in [('total', 'Number of tests'), ('passed', 'Tests passed'), ('skipped', 'Tests skipped'), ('failed', 'Tests failed'), ('warned', 'Tests warned')]:
            assert int(re.search(re.escape(label) + r'\s*:\s*(\d+)', log)[1]) == row[key]
        assert row['failed'] == row['warned'] == 0
print('PASS: 44 elapsed records, three five-pass counter series, fingerprints, matching-code hash and nine PHPT logs')
