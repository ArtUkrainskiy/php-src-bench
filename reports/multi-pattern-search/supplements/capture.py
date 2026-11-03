#!/usr/bin/env python3
"""Audit supplemental records against their raw subprocess output, then export portable data."""

import argparse
import hashlib
import importlib.util
import json
import re
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    run = args.directory.resolve()
    for name in ['MATRIX_COMPLETE', 'SUPPLEMENTS_COMPLETE']:
        assert (run / name).read_text().strip() == 'PASS', name
    assert not (run / 'failure.json').exists() and not (run / 'failure-post.json').exists()
    spec = importlib.util.spec_from_file_location('primary_capture', REPORT / 'capture.py')
    primary = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(primary)
    cases = {}
    for stem, corpus in [('product', 'multi-pattern-product'), ('size', 'multi-pattern-scaling')]:
        root = REPORT / '../../corpus' / corpus
        index = read(root / 'index.json')
        for filename, expected in index['suite_sha256'].items():
            assert digest(root / filename) == expected
            for case in read(root / filename)['cases']:
                cases[stem, case['id']] = case
    audit = []
    for compiler in ['gcc15', 'clang21']:
        main_data = {stem: read(run / f'data-{stem}-{compiler}' / 'results.json') for stem in ['product', 'size']}
        main_rows = {
            (stem, row['case'], row['lifecycle']): row for stem, data in main_data.items() for row in data['rows']
        }
        meta = main_data['product']['metadata']
        roots = primary.path_roots(meta, '${RUN_ROOT}')
        roots[str(run)] = '${RUN_ROOT}'
        memory_path = run / f'memory-{compiler}.json'
        memory = read(memory_path)
        assert memory['status'] == 'complete' and len(memory['rows']) == 44
        assert all(len(row['samples']) == 5 for row in memory['rows'])
        for key in ['php_sha256', 'module_sha256', 'source_revision', 'source_sha256']:
            assert memory['metadata'][key] == meta[key], key
        memory_target = REPORT / 'data' / f'memory-{compiler}.json'
        memory_target.write_text(json.dumps(primary.public(memory, roots), ensure_ascii=False, indent=2) + '\n')
        audit.append(
            {
                'series': 'memory',
                'compiler': compiler,
                'rows': 44,
                'source_result_sha256': digest(memory_path),
                'export_sha256': digest(memory_target),
                'verified_raw_subprocess_outputs': 0,
                'scope': 'Five fresh-process samples per row embedded in the memory result; no separate raw stdout archive.',
            }
        )
        for filename, target in [
            ('order-confirmation', 'order'),
            ('constructors', 'preparation'),
            ('amortization-model', 'payback-model'),
            ('amortization-batches', 'payback-batches'),
        ]:
            path = run / f'{filename}-{compiler}.json'
            data = read(path)
            assert data['status'] == 'complete'
            assert data['metadata']['main_metadata']['module_sha256'] == meta['module_sha256']
            assert data['metadata']['main_metadata']['source_revision'] == meta['source_revision']
            verified = set()

            def visit(value, parent=None, key=None, verified=verified):
                if isinstance(value, list):
                    return [visit(item) for item in value]
                if not isinstance(value, dict):
                    return value
                if 'raw_config' in value:
                    source = run / value['raw_config']
                    output = source.with_name(source.stem + '-output.json')
                    stdout = source.with_name(source.stem + '-stdout.txt')
                    stderr = source.with_name(source.stem + '-stderr.txt')
                    raw = read(output)
                    assert json.loads(stdout.read_text()) == raw and not stderr.read_text()
                    expected = value.get('result')
                    if expected is None:
                        expected = parent[{'raw': 'time', 'check_raw': 'check', 'warm_raw': 'warm_build_release'}[key]]
                    assert raw == expected, value['raw_config']
                    verified.add(str(source.relative_to(run)))
                    exported = {k: visit(v, value, k) for k, v in value.items() if k != 'raw_config'}
                    exported['capture_config_sha256'] = digest(source)
                    exported['capture_stdout_sha256'] = digest(stdout)
                    return exported
                return {k: visit(v, value, k) for k, v in value.items()}

            exported = visit(data)
            for row in data['rows']:
                if target == 'order':
                    original = main_rows[row['corpus'], row['case'], row['lifecycle']]
                    assert row['original_time'] == original['time']
                if target == 'payback-batches':
                    case = cases[row['corpus'], row['case']]
                    cycle_sink = 0
                    for job in case['jobs']:
                        for document in job['documents']:
                            value = document['expected']
                            cycle_sink += (
                                len(value['text'].encode())
                                if case['operation'] == 'replace'
                                else len(value)
                                if isinstance(value, list)
                                else int(value)
                            )
                    passes = data['metadata']['passes']
                    expected = 0
                    for iterations in row['time']['iterations'].values():
                        assert iterations * row['batch_size'] % len(case['jobs']) == 0
                        expected += cycle_sink * iterations * row['batch_size'] // len(case['jobs'])
                    assert row['time']['sink'] == passes * expected
            exported = primary.public(exported, roots)
            text = json.dumps(exported, ensure_ascii=False, indent=2) + '\n'
            assert not re.search(r'/home/|CLionProjects', text)
            target_path = REPORT / 'data' / f'{target}-{compiler}.json'
            target_path.write_text(text)
            audit.append(
                {
                    'series': target,
                    'compiler': compiler,
                    'rows': len(data['rows']),
                    'source_result_sha256': digest(path),
                    'verified_raw_subprocess_outputs': len(verified),
                    'export_sha256': digest(target_path),
                }
            )
    (REPORT / 'data/supplement-capture-audit.json').write_text(json.dumps(audit, indent=2) + '\n')
    print(
        'SUPPLEMENT CAPTURE PASS',
        sum(row['verified_raw_subprocess_outputs'] for row in audit),
        'raw outputs verified; original comparisons and batch sinks checked',
    )


if __name__ == '__main__':
    main()
