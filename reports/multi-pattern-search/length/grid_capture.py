#!/usr/bin/env python3
"""Audit exact saved 4 KiB inputs, main perf corrections and one-shot stdout before export."""

import argparse
import hashlib
import importlib.util
import json
import statistics as st
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent
CORPUS = REPORT / '../../corpus/multi-pattern-4k'


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def same(left, right):
    return json.dumps(left, ensure_ascii=False) == json.dumps(right, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_root', type=Path)
    args = parser.parse_args()
    run = args.run_root.resolve()
    assert (run / 'GRID_COMPLETE').read_text().strip() == 'PASS'
    assert (run / 'SMOKE_COMPLETE').read_text().strip() == 'PASS'
    assert not (run / 'failure.json').exists()
    spec = importlib.util.spec_from_file_location('primary', REPORT / 'capture.py')
    primary = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(primary)
    cases = {
        case['id']: case
        for name in read(CORPUS / 'index.json')['suite_sha256']
        for case in read(CORPUS / name)['cases']
    }
    assert len(cases) == 18
    exports, audits = {}, []
    for cc in ['gcc15', 'clang21']:
        files, audit = primary.capture(
            run, 'multi-pattern-4k', 'grid', cc, REPORT / 'length/harness.php', REPORT / 'length/measure.py'
        )
        exports.update({'grid-' + name.removeprefix('size-'): value for name, value in files.items()})
        value = read(run / f'oneshot-data-grid-{cc}.json')
        assert value['status'] == 'complete'
        main_data = read(run / f'data-grid-{cc}/results.json')
        assert digest(run / f'data-grid-{cc}/strmatch.so') == main_data['metadata']['module_sha256']
        assert value['metadata']['main_metadata'] == main_data['metadata']
        pins = value['metadata']['pins']
        assert set(pins) == {
            'length/grid.py',
            'length/measure.py',
            'length/harness.php',
            'supplements/batch.php',
            'supplements/definitions.php',
        }
        assert all(digest(REPORT / name) == sha for name, sha in pins.items())
        protocol = value['metadata']['protocol']
        assert protocol == {'passes': 15, 'warmup_ns': 250_000_000, 'sample_ns': round(1e9 / 15)}
        assert len(value['rows']) == len(cases)
        assert {row['case'] for row in value['rows']} == set(cases)
        assert len(value['aa']) == 4 and not value['mutations']
        roots = primary.path_roots(main_data['metadata'], '${RUN_ROOT}')
        roots[str(run)] = '${RUN_ROOT}'
        verified = set()

        def visit(item, protocol=protocol, verified=verified):
            if isinstance(item, list):
                return [visit(v) for v in item]
            if not isinstance(item, dict):
                return item
            if 'raw' in item:
                path = run / item['raw']
                config = read(path)
                case = cases[config['case']['id']]
                assert same(config['case'], case), 'Changed raw case'
                assert all(config[key] == expected for key, expected in protocol.items())
                assert config['batch_size'] == 1 and not config.get('mutation', False)
                assert config['mode'] in ['time', 'check']
                candidate = 'replacer' if case['operation'] == 'replace' else 'matcher'
                assert config['methods'] == case['methods'] or config['methods'] == {'a': candidate, 'b': candidate}
                assert same(read(path.with_suffix('.stdout')), item['result']), 'Changed raw stdout'
                assert not path.with_suffix('.stderr').read_text()
                busy = item['sibling_busy_percent']
                assert busy is None or busy <= 5
                result = item['result']
                if config['mode'] == 'check':
                    assert result == {'checks': len(case['jobs']) * len(config['methods'])}
                else:
                    assert set(result['ns_per_batch']) == set(config['methods'])
                    assert set(result['iterations']) == set(config['methods'])
                    assert all(len(samples) == 15 for samples in result['ns_per_batch'].values())
                    assert all(n > 0 and n % 4 == 0 for n in result['iterations'].values())
                    per_cycle = sum(
                        len(doc['expected']['text'].encode())
                        if case['operation'] == 'replace'
                        else int(doc['expected'])
                        for job in case['jobs']
                        for doc in job['documents']
                    )
                    assert result['sink'] == sum(result['iterations'].values()) // 4 * per_cycle * 15
                verified.add(item['raw'])
                return {
                    'result': result,
                    'sibling_busy_percent': busy,
                    'config_sha256': digest(path),
                    'stdout_sha256': digest(path.with_suffix('.stdout')),
                }
            return {key: visit(v) for key, v in item.items()}

        clean = visit(value)
        for control in value['aa']:
            samples = control['time']['result']['ns_per_batch']
            ratio = st.median([b / a for a, b in zip(samples['a'], samples['b'])])
            assert ratio == control['median_ratio'] and abs(ratio - 1) <= 0.02
        for row in value['rows']:
            assert row['calls'] == 1
            for key, mode in [('time', 'time'), ('check', 'check')]:
                config = read(run / row[key]['raw'])
                assert config['case']['id'] == row['case'] and config['mode'] == mode
        assert verified == {str(path.relative_to(run)) for path in (run / f'batch-data-grid-{cc}').glob('*.json')}
        exports[f'grid-oneshot-{cc}.json'] = primary.public(clean, roots)
        audit['one_shot_raw_outputs_verified'] = len(verified)
        audit['one_shot_rows'] = len(value['rows'])
        audits.append(audit)
    exports['grid-capture-audit.json'] = audits
    for name, value in exports.items():
        (REPORT / 'data' / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    print(
        'GRID CAPTURE PASS',
        sum(a['corrected_counter_samples_verified'] for a in audits),
        'corrected counters;',
        sum(a['one_shot_raw_outputs_verified'] for a in audits),
        'one-shot raw outputs',
    )


if __name__ == '__main__':
    main()
