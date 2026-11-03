#!/usr/bin/env python3
"""Audit the fixed-length matrix and construction/batch raw output before importing."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_root', type=Path)
    args = parser.parse_args()
    run = args.run_root.resolve()
    assert (run / 'ADDITIONAL_COMPLETE').read_text().strip() == 'PASS'
    assert not (run / 'failure.json').exists()
    spec = importlib.util.spec_from_file_location('primary', REPORT / 'capture.py')
    primary = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(primary)
    exports, audit = {}, []
    cases = {}
    corpus = REPORT / '../../corpus/multi-pattern-length'
    index = read(corpus / 'index.json')
    for filename, expected in index['suite_sha256'].items():
        assert digest(corpus / filename) == expected
        for case in read(corpus / filename)['cases']:
            cases[case['id']] = case
    catalog = read(REPORT / 'memory/glossary-catalog.json')['replacements']
    dictionary_sizes = read(REPORT / 'memory/index.json')['sizes']
    expected_dictionaries = []
    for count in dictionary_sizes:
        mapping = dict(list(catalog.items())[:count])
        expected_dictionaries += [('Matcher', list(mapping)), ('Replacer', mapping)]
    expected_dictionaries.append(('Matcher', cases['length.any.absent.128']['jobs'][0]['dictionary']))

    def same(left, right):
        return json.dumps(left, ensure_ascii=False) == json.dumps(right, ensure_ascii=False)

    def check_config(config):
        assert config['passes'] == 15 and config['warmup_ns'] == 250_000_000
        assert config['sample_ns'] == round(1e9 / 15)
        assert not config.get('mutation', False)
        if 'case' in config:
            case = cases[config['case']['id']]
            assert same(config['case'], case), 'Changed raw case'
            assert config['methods'] == case['methods'] or config['methods'] == {'a': 'matcher', 'b': 'matcher'}
            assert 1 <= config['batch_size'] <= 4096
            assert config['mode'] in ['check', 'time']
        else:
            assert config['mode'] in ['memory', 'time', 'aa']
            assert any(
                config['class'] == kind and same(config['dictionary'], dictionary)
                for kind, dictionary in expected_dictionaries
            ), 'Changed raw dictionary'

    for cc in ['gcc15', 'clang21']:
        files, counters = primary.capture(
            run, 'multi-pattern-length', 'length', cc, REPORT / 'length/harness.php', REPORT / 'length/measure.py'
        )
        exports.update({'length-' + name.removeprefix('size-'): value for name, value in files.items()})
        audit.append(counters)
        main_data = read(run / f'data-length-{cc}/results.json')
        metadata = main_data['metadata']
        roots = primary.path_roots(metadata, '${RUN_ROOT}')
        roots[str(run)] = '${RUN_ROOT}'
        verified = set()

        def visit(value, verified=verified):
            if isinstance(value, list):
                return [visit(item) for item in value]
            if not isinstance(value, dict):
                return value
            if 'raw' in value:
                path = run / value['raw']
                check_config(read(path))
                assert json.loads(path.with_suffix('.stdout').read_text()) == value['result']
                assert not path.with_suffix('.stderr').read_text()
                verified.add(value['raw'])
                return {
                    **{key: visit(item) for key, item in value.items() if key != 'raw'},
                    'capture_config_sha256': digest(path),
                    'capture_stdout_sha256': digest(path.with_suffix('.stdout')),
                }
            return {key: visit(item) for key, item in value.items()}

        for filename in ['build-cost', 'length-payback', 'additional-aa']:
            data = read(run / f'{filename}-{cc}.json')
            if filename != 'additional-aa':
                assert data['status'] == 'complete'
                assert data['metadata']['main_metadata'] == metadata
                assert data['metadata']['passes'] == 15
                for name, expected in data['metadata']['pins'].items():
                    assert digest(REPORT / name) == expected, name
            if filename == 'build-cost':
                assert len(data['rows']) == 23
                for row in data['rows']:
                    assert len(row['memory']) == 5
                    assert all(sample['result'] == row['memory'][0]['result'] for sample in row['memory'])
                    expected = (
                        cases['length.any.absent.128']['jobs'][0]['dictionary']
                        if row['family'] == 'moderation'
                        else dict(list(catalog.items())[: row['size']])
                    )
                    if row['class'] == 'Matcher' and isinstance(expected, dict):
                        expected = list(expected)
                    for entry in row['memory'] + [row['time']]:
                        config = read(run / entry['raw'])
                        assert config['class'] == row['class'] and same(config['dictionary'], expected)
                        assert config['mode'] == ('time' if entry is row['time'] else 'memory')
                    result = row['time']['result']
                    assert result['sink'] == result['iterations'] * 15
                    assert len(result['constructor_ns']) == len(result['release_ns']) == 15
            elif filename == 'length-payback':
                assert len(data['models']) == 24
                for row in data['batches']:
                    case = cases[row['case']]
                    for label, mode in [('check', 'check'), ('time', 'time')]:
                        config = read(run / row[label]['raw'])
                        assert same(config['case'], case) and config['batch_size'] == row['calls']
                        assert config['methods'] == case['methods'] and config['mode'] == mode
                    total = sum(
                        len(doc['expected']['text'].encode())
                        if case['operation'] == 'replace'
                        else len(doc['expected'])
                        if isinstance(doc['expected'], list)
                        else int(doc['expected'])
                        for job in case['jobs']
                        for doc in job['documents']
                    )
                    expected = (
                        sum(
                            n * row['calls'] // len(case['jobs']) * total
                            for n in row['time']['result']['iterations'].values()
                        )
                        * 15
                    )
                    assert row['time']['result']['sink'] == expected
            else:
                assert len(data) == 4
                assert all(abs(row['median_ratio'] - 1) <= 0.02 for row in data)
            exports[f'{filename}-{cc}.json'] = primary.public(visit(data), roots)
        audit.append({'series': 'length-additional', 'compiler': cc, 'raw_subprocess_outputs_verified': len(verified)})
    (REPORT / 'data').mkdir(exist_ok=True)
    for name, value in exports.items():
        text = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
        assert '/home/' not in text and 'CLionProjects' not in text
        (REPORT / 'data' / name).write_text(text)
    (REPORT / 'data/length-capture-audit.json').write_text(json.dumps(audit, indent=2) + '\n')
    print(
        'LENGTH CAPTURE PASS',
        sum(row.get('corrected_counter_samples_verified', 0) for row in audit),
        'corrected counters;',
        sum(row.get('raw_subprocess_outputs_verified', 0) for row in audit),
        'supplemental raw outputs',
    )


if __name__ == '__main__':
    main()
