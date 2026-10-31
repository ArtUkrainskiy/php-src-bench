#!/usr/bin/env python3
"""Independently check elapsed arithmetic and source identities against raw evidence."""
from collections import defaultdict
import hashlib
import json
import re
from pathlib import Path
import statistics as st
import tarfile

root = Path(__file__).resolve().parent
metrics = json.loads((root / 'metrics.json').read_text())
manifest = json.loads((root / 'manifest.json').read_text())
assert not manifest['partial'] and len(metrics) == manifest['metrics'] == 113
assert len(manifest['files']) == 113
expected = {'base': 'ef99f4248f1450c39fb86fd7fd6f24c49b8d11eb',
            'product-guard': 'ca89fb5fb96399ed730cacb12d948025f83c4e6e',
            'review-no-gram4': 'fa81a3379208e6f4b6d80f1cd0f7b7689cec1d20',
            'review-scalar': 'db4d3f65c6924674ec909466be40c6e735f88b85'}
hashes = {}
counts = defaultdict(int)
provenance = json.loads((root / 'binary-provenance.json').read_text())
for name, sha1 in {
    'base-gcc15': '4e30c09b37e7eb9323290291d44a4199adba941d',
    'product-guard-gcc15': '993cfd6d6cda982e07601a21e4e506f86505e0cc',
    'base-clang21': 'cd4ae15f5317a58cb41793e47a2d240d8953533d',
    'product-guard-clang21': '19d8b71be35ac88be6e5ae14e029e9a34faa922c',
}.items():
    assert provenance[name]['sha1'] == sha1, 'Frozen control binary changed'
with tarfile.open(root / 'native.tar.gz') as archive:
    assert len(archive.getnames()) == len(set(archive.getnames()))
    for row in metrics:
        name = row['source']
        raw = archive.extractfile(name).read()
        assert hashlib.sha256(raw).hexdigest() == manifest['files'][name], name
        data = json.loads(raw)
        log = archive.extractfile(name[:-5] + '.log').read().decode()
        assert row['idle_wait_timeout'] == ('measuring anyway' in log)
        cfg = data['config']
        assert cfg['rounds'] == 4 and cfg['samples'] == 1
        assert cfg['warmup_ms'] == cfg['target_ms'] == 1000 and cfg['cpu'] == 15
        key = row['case']
        assert list(data['cases']) == [key]
        case = data['cases'][key]
        for side, prefix in [('A', 'a'), ('B', 'b')]:
            build_name = row[prefix]
            build_prefix = build_name.rsplit('-', 1)[0]
            assert data['sides'][side]['build']['commit'] == expected[build_prefix]
            assert not data['sides'][side]['build']['debug']
            assert data['sides'][side]['build']['profile'] == 'docker'
            values = case['sides'][side]
            times = [sample - st.median(values['loop_ns']) for rr in values['rounds'] for sample in rr]
            median = st.median(times)
            assert abs(median - row[prefix + '_ns']) < 1e-8
            spread = 1.4826 * st.median(abs(t - median) for t in times) / median * 100
            assert abs(spread - row[prefix + '_spread']) < 1e-8
            identity = (values['input_hash'], values['output_hash'])
            assert key not in hashes or hashes[key] == identity, (name, key)
            hashes[key] = identity
        delta = 100 * (row['b_ns'] / row['a_ns'] - 1)
        assert abs(delta - row['delta_time']) < 1e-8
        assert abs(100 * (row['b_instructions'] / row['a_instructions'] - 1) - row['delta_instructions']) < 1e-8
        counts[row['comparison']] += 1
    for name in ['cycles.json', 'extra-cycles.json']:
        original = json.loads(archive.extractfile(name).read())
        original['machine_warnings'] = [re.sub(r'/tmp/php[-_][^/\s]+/tools/bench', 'bench', v) for v in original['machine_warnings']]
        assert original == json.loads((root / name).read_text())
assert len(hashes) == 26 and counts['aa'] == 8
for path in [root / 'cycles.json', root / 'extra-cycles.json']:
    data = json.loads(path.read_text())
    assert data['complete'] and not data['warnings'] and not data['marks']
    for name, build in data['builds'].items():
        assert build['sha1'] == provenance[name]['sha1']
    values = defaultdict(lambda: defaultdict(list))
    for group, side, key, bc, bi, ec, ei in data['rows']:
        values[group, key][side].append((bc - ec) / data['cases'][key]['n'])
    for row in metrics:
        group = row['comparison'] + '-' + row['compiler']
        key = row['case']
        if (group, key) not in values: continue
        a, b = (values[group, key][s] for s in ['a', 'b'])
        assert len(a) == len(b) == 3
        c = row['cycles']
        assert abs(c['a'] - st.median(a)) < 1e-8
        assert abs(c['b'] - st.median(b)) < 1e-8
        assert abs(c['delta'] - 100 * (st.median(bb / aa for aa, bb in zip(a, b)) - 1)) < 1e-8
print('Verified 113 elapsed pairs, 26 timed inputs, source identities, outputs and separate cycle arithmetic')

for path in sorted((root / 'cycle-views').glob('*.json')):
    view = json.loads(path.read_text())
    parent = json.loads((root / view['presentation_view']['source']).read_text())
    names = set(view['presentation_view']['selected_groups'])
    assert view['groups'] == [g for g in parent['groups'] if g['name'] in names]
    assert view['rows'] == [r for r in parent['rows'] if r[0] in names]
    assert view['cases'] == parent['cases'] and view['builds'] == parent['builds']
assert len(list((root / 'cycle-views').glob('*.json'))) == 6
print('Verified six counter presentation views; numeric rows unchanged')
