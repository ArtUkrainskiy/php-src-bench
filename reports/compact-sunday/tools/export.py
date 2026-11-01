#!/usr/bin/env python3
"""Export completed capture directories; retain observations and normalize private paths."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

p = argparse.ArgumentParser(description=__doc__, epilog=(
    'Original capture layout: protocol.json, events.json, reference-builds.json, fixture-files.json; '
    'one <event.tag>.json per event; counters-*.json; replication/{plan.json,events.json,<job.tag>.json}; '
    'optional modules.json and counter-validation/. The portable measure.py writes a different '
    'layout; retain those new experiments separately rather than importing them here.'))
p.add_argument('--amd', type=Path, required=True)
p.add_argument('--intel', type=Path, required=True)
p.add_argument('--extensions', type=Path, required=True)
p.add_argument('--report', type=Path, default=Path(__file__).resolve().parents[1])
p.add_argument('--source', type=Path, required=True, help='candidate php-src checkout, read only')
a = p.parse_args()
out = a.report / 'data'
(out / 'counters').mkdir(parents=True, exist_ok=True)
provenance = []
metadata = {'format': 1, 'captures': {}}


def normalize(value):
    if isinstance(value, dict):
        return {key: normalize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize(item) for item in value]
    if not isinstance(value, str):
        return value
    if value.endswith('/replication/legacy-prefix.php'):
        return 'reports/compact-sunday/suites/prefix-default-offset.php'
    value = re.sub(r'/[^\s\"]*/(?:fixtures/suites|extension-suites)/([^/\s\"]+\.php)',
                   r'reports/compact-sunday/suites/\1', value)
    value = re.sub(r'/[^\s\"]*/builds/(compact-[^/\s\"]+)/sapi/cli/php',
                   r'BUILD_DIR/\1/sapi/cli/php', value)
    return re.sub(r'/(?:home|tmp)/[^\s\"]+',
                  lambda match: 'CAPTURE_PATH/' + Path(match.group()).name, value)


def read(root, name):
    source = root / name
    provenance.append({'capture': root.name, 'file': str(name),
                       'captured_sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
    return json.loads(source.read_text())


def write(name, data):
    (out / name).write_text(json.dumps(normalize(data), ensure_ascii=False, indent=2) + '\n')


for label, root in [('amd', a.amd), ('intel', a.intel), ('intel-extensions', a.extensions)]:
    assert (root / 'complete').read_text().strip() == 'PASS'
    assert (root / 'replication/complete').read_text().strip() == 'PASS'
    plan = read(root, 'protocol.json')
    events = read(root, 'events.json')
    assert len(events) == len(plan['jobs'])
    builds = read(root, 'reference-builds.json')
    modules = read(root, 'modules.json') if (root / 'modules.json').exists() else None
    metadata['captures'][label] = {'builds': builds, 'modules': modules,
                                    'fixture_hashes': read(root, 'fixture-files.json'),
                                    'protocol': {k: v for k, v in plan.items() if k != 'jobs'}}
    if (root / 'replication/legacy-prefix.php').exists():
        source = root / 'replication/legacy-prefix.php'
        (a.report / 'suites/prefix-default-offset.php').write_bytes(source.read_bytes())
        metadata['supplemental_suite'] = {'file': 'suites/prefix-default-offset.php',
                                           'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                                           'scope': 'Two additional diagnostic comparisons; outside the 205-case corpus'}
    records = []
    for event in events:
        raw = read(root, event['tag'] + '.json')
        assert raw['config']['rounds'] == 5 and raw['config']['samples'] == 5
        assert raw['config']['warmup_ms'] == 500 and raw['config']['target_ms'] == 200
        assert list(raw['cases']) == [event['case']]
        record = {k: raw[k] for k in ['format', 'date', 'suite', 'config', 'env', 'cases']}
        record['builds'] = {side: raw['sides'][side]['name'] for side in ['A', 'B']}
        record['event'] = event
        records.append(record)
    write('elapsed-' + label + '.json', records)
    jobs = read(root, 'replication/plan.json')
    assert len(jobs) == len(read(root, 'replication/events.json'))
    repeated = []
    for job in jobs:
        raw = read(root, 'replication/' + job['tag'] + '.json')
        record = {k: raw[k] for k in ['format', 'date', 'suite', 'config', 'env', 'cases']}
        record['builds'] = {side: raw['sides'][side]['name'] for side in ['A', 'B']}
        record['job'] = job
        repeated.append(record)
    write('repeats-' + label + '.json', repeated)
    for source in sorted(root.glob('counters-*.json')):
        native = read(root, source.name)
        assert native['complete'] and not native['warnings'] and not native['marks']
        write('counters/' + label + '-' + source.name.removeprefix('counters-'), native)
    if (root / 'counter-quality.json').exists():
        quality = read(root, 'counter-quality.json')
        quality['exported_source'] = 'counters/intel-extensions-mbstring.json'
        quality['exported_validation'] = 'counters/intel-extensions-aa-validation.json'
        write('counter-quality.json', quality)
        native = read(root, 'counter-validation/aa2-mb-strstr-zh-absent.json')
        assert native['complete'] and not native['warnings'] and not native['marks']
        write('counters/intel-extensions-aa-validation.json', native)
# The saved corpus, rather than the optional generator, defines the measured inputs.
for capture in metadata['captures'].values():
    for name, digest in capture['fixture_hashes'].items():
        if name.startswith('corpus/') and name != 'corpus/README.md':
            assert hashlib.sha256((a.report / name).read_bytes()).hexdigest() == digest, name
def git(*args):
    return subprocess.check_output(['git', '-C', str(a.source), *args], text=True).strip()

measured = metadata['captures']['amd']['builds']['compact-head-gcc15']['metadata']['commit']
master = metadata['captures']['amd']['builds']['compact-base-gcc15']['metadata']['commit']
assert git('rev-parse', measured + '^{tree}') == git('rev-parse', 'HEAD^{tree}')
metadata['measured_tree'] = {'master': master, 'measured_candidate': measured,
                             'branch_candidate': git('rev-parse', 'HEAD'),
                             'candidate_tree': git('rev-parse', 'HEAD^{tree}'),
                             'identical_source_tree': True}
write('metadata.json', metadata)
write('provenance.json', provenance)
manifest = {str(f.relative_to(out)): hashlib.sha256(f.read_bytes()).hexdigest()
            for f in sorted(out.rglob('*.json')) if f.name != 'sha256.json'}
write('sha256.json', manifest)
print(json.dumps({'captures': 3, 'observations': 1206, 'files': len(manifest)}))
