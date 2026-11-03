#!/usr/bin/env python3
"""Pure construction, retained memory and direct reuse checks for the length series."""
import argparse
import datetime
import fcntl
import hashlib
import json
import math
import statistics as st
import subprocess
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def ticks(cpu):
    values = next(row for row in Path('/proc/stat').read_text().splitlines()
                  if row.startswith(f'cpu{cpu} ')).split()[1:9]
    values = list(map(int, values))
    return sum(values), values[3] + values[4]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['smoke', 'run'])
    parser.add_argument('--run-root', type=Path, required=True)
    parser.add_argument('--gcc-build', type=Path, required=True)
    parser.add_argument('--clang-build', type=Path)
    parser.add_argument('--cpu', type=int, required=True)
    parser.add_argument('--sibling', type=int, required=True)
    args = parser.parse_args()
    run = args.run_root.resolve()
    builds = {'gcc15': args.gcc_build.resolve()}
    if args.clang_build:
        builds['clang21'] = args.clang_build.resolve()
    full = args.command == 'run'
    assert not full or len(builds) == 2
    names = ['length/prepare.php', 'length/harness.php', 'supplements/definitions.php',
             'supplements/batch.php', 'length/additional.py']
    pins = {name: digest(REPORT / name) for name in names}
    with (run / ('additional-' + args.command + '.lock')).open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with Path(f'/tmp/php-bench-multi-pattern-cpu-{args.cpu}.lock').open('a') as cpu_lock:
            fcntl.flock(cpu_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            execute(args, run, builds, pins)


def execute(args, run, builds, pins):
    full = args.command == 'run'
    corpus = REPORT / '../../corpus/multi-pattern-length'
    index = read(corpus / 'index.json')
    cases = {case['id']: case for name, sha in index['suite_sha256'].items()
             for case in read(corpus / name)['cases'] if digest(corpus / name) == sha}
    assert len(cases) == 24
    sequence = 0
    directory = run / ('additional-raw' if full else 'additional-smoke-raw')
    assert not directory.exists(), 'Use a fresh supplemental directory'
    directory.mkdir()
    passes, warmup, sample = (15, 250_000_000, round(1e9 / 15)) if full else (1, 1_000_000, 10_000_000)

    def call(cc, helper, config, mutation=False):
        nonlocal sequence
        for name, sha in pins.items():
            assert digest(REPORT / name) == sha, name
        sequence += 1
        path = directory / f'{sequence:05}-{cc}.json'
        save(path, config)
        module = run / (('data-length-' if full else 'smoke-') + cc) / 'strmatch.so'
        command = ['taskset', '-c', str(args.cpu), str(builds[cc] / 'sapi/cli/php'), '-n', '-d',
                   'extension=' + str(module), '-d', 'pcre.jit=1', str(REPORT / helper), str(path)]
        before = ticks(args.sibling)
        try:
            process = subprocess.run(command, text=True, capture_output=True, timeout=120, check=False)
        except subprocess.TimeoutExpired as error:
            for stream in ['stdout', 'stderr']:
                value = getattr(error, stream) or b''
                if isinstance(value, bytes):
                    value = value.decode(errors='replace')
                path.with_suffix('.' + stream).write_text(value)
            raise
        after = ticks(args.sibling)
        path.with_suffix('.stdout').write_text(process.stdout)
        path.with_suffix('.stderr').write_text(process.stderr)
        if mutation:
            assert process.returncode and 'mismatch' in (process.stdout + process.stderr).lower()
            return {'mutation_caught': True, 'raw': str(path.relative_to(run))}
        assert process.returncode == 0 and not process.stderr, (process.stdout, process.stderr)
        total = after[0] - before[0]
        activity = None if total <= 0 else 100 * (1 - (after[1] - before[1]) / total)
        assert activity is None or activity <= 5, ('SMT sibling busy', activity)
        data = json.loads(process.stdout)
        return {'result': data, 'raw': str(path.relative_to(run)), 'sibling_busy_percent': activity}

    config_base = {'passes': passes, 'warmup_ns': warmup, 'sample_ns': sample}
    if not full:
        records = []
        for n in [1, 2]:
            for kind in ['Matcher', 'Replacer']:
                dictionary = list(cases['length.unique.mixed.512']['jobs'][0]['dictionary'])[:n]
                if kind == 'Replacer':
                    dictionary = {key: 'replacement' for key in dictionary}
                for mode in ['memory', 'time', 'aa']:
                    records.append(call('gcc15', 'length/prepare.php',
                                        {**config_base, 'dictionary': dictionary, 'class': kind, 'mode': mode}))
            for operation in ['any', 'unique', 'replace']:
                name = 'length.any.absent.128' if operation == 'any' else f'length.{operation}.mixed.512'
                case = cases[name]
                records.append(call('gcc15', 'length/harness.php',
                                    {**config_base, 'case': case, 'lifecycle': 'worker',
                                     'methods': case['methods'], 'mode': 'check'}))
                records.append(call('gcc15', 'length/harness.php',
                                    {**config_base, 'case': case, 'lifecycle': 'worker',
                                     'methods': case['methods'], 'mode': 'check', 'mutation': True}, True))
                config = {**config_base, 'case': case, 'batch_size': n,
                          'methods': case['methods'], 'mode': 'check'}
                records.append(call('gcc15', 'supplements/batch.php', config))
                config['mode'] = 'time'
                records.append(call('gcc15', 'supplements/batch.php', config))
            case = cases['length.any.absent.128']
            records.append(call('gcc15', 'supplements/batch.php',
                                {**config_base, 'case': case, 'batch_size': n, 'methods': ['matcher'],
                                 'mode': 'check', 'mutation': True}, True))
        save(run / 'additional-smoke.json', {'status': 'PASS', 'pins': pins, 'records': records})
        print('ADDITIONAL SMOKE N1/N2, THREE RESULT MUTATIONS AND BATCH MUTATION PASS', flush=True)
        return
    assert read(run / 'additional-smoke.json')['pins'] == pins, 'Smoke must match frozen helpers'
    dictionaries = []
    catalog = read(REPORT / 'memory/glossary-catalog.json')['replacements']
    for size in read(REPORT / 'memory/index.json')['sizes']:
        mapping = dict(list(catalog.items())[:size])
        dictionaries.extend([('support', size, 'Matcher', list(mapping)), ('support', size, 'Replacer', mapping)])
    dictionaries.append(('moderation', 128, 'Matcher', cases['length.any.absent.128']['jobs'][0]['dictionary']))
    for cc in builds:
        main = read(run / f'data-length-{cc}/results.json')
        assert main['metadata']['corpus_index_sha256'] == digest(corpus / 'index.json')
        assert main['metadata']['harness_sha256'] == pins['length/harness.php']
        assert main['metadata']['source_revision'] == '287aaab7fb729d3a8e91c6fd35224c4359c343e3'
        assert main['status'] == 'complete' and len(main['rows']) == 24
        for name, expected in [('php_sha256', builds[cc] / 'sapi/cli/php'),
                               ('module_sha256', run / f'data-length-{cc}/strmatch.so')]:
            assert main['metadata'][name] == digest(expected), name
        metadata = {'main_metadata': main['metadata'], 'pins': pins,
                    'measured_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    'constructor_scope': 'Warm new-only interval; release separately timed; adjacent hrtime cost included.',
                    'passes': passes, 'warmup_ns': warmup, 'sample_ns': sample,
                    'catalog_sha256': digest(REPORT / 'memory/glossary-catalog.json')}
        controls = []

        def aa(stage):
            config = {**config_base, 'dictionary': dictionaries[8][3], 'class': 'Matcher', 'mode': 'aa'}
            timed = call(cc, 'length/prepare.php', config)
            values = timed['result']['constructor_ns']
            ratio = st.median([b / a for a, b in zip(values['a'], values['b'])])
            assert abs(ratio - 1) <= .02, ('Constructor A/A', ratio)
            controls.append({'stage': stage, 'kind': 'constructor', 'median_ratio': ratio, **timed})
            case = cases['length.unique.mixed.512']
            config = {**config_base, 'case': case, 'batch_size': 8, 'methods': {'a': 'matcher', 'b': 'matcher'}, 'mode': 'time'}
            timed = call(cc, 'supplements/batch.php', config)
            values = timed['result']['ns_per_batch']
            ratio = st.median([b / a for a, b in zip(values['a'], values['b'])])
            assert abs(ratio - 1) <= .02, ('Batch A/A', ratio)
            controls.append({'stage': stage, 'kind': 'batch', 'median_ratio': ratio, **timed})
            save(run / f'additional-aa-{cc}.json', controls)

        aa('before')
        rows = []
        for family, size, kind, dictionary in dictionaries:
            config = {**config_base, 'dictionary': dictionary, 'class': kind, 'mode': 'memory'}
            snapshots = [call(cc, 'length/prepare.php', config) for _ in range(5)]
            assert all(row['result'] == snapshots[0]['result'] for row in snapshots)
            config['mode'] = 'time'
            timed = call(cc, 'length/prepare.php', config)
            assert timed['result']['sink'] == timed['result']['iterations'] * passes
            rows.append({'family': family, 'size': size, 'class': kind, 'memory': snapshots, 'time': timed})
            save(run / f'build-cost-{cc}.json', {'status': 'running', 'metadata': metadata, 'rows': rows})
            print('BUILD', cc, family, size, kind, flush=True)
        save(run / f'build-cost-{cc}.json', {'status': 'complete', 'metadata': metadata, 'rows': rows})
        costs = {(r['family'], r['class']): r for r in rows if r['size'] == 128}
        models, batches = [], []
        for row in main['rows']:
            case = cases[row['case']]
            candidate = 'replacer' if case['operation'] == 'replace' else 'matcher'
            kind = 'Replacer' if candidate == 'replacer' else 'Matcher'
            family = 'moderation' if case['operation'] == 'any' else 'support'
            cost = costs[family, kind]['time']['result']
            preparation = st.median([a + b for a, b in zip(cost['constructor_ns'], cost['release_ns'])])
            queries = row['time']['ns_per_job']
            alternatives = {}
            for method in row['methods']:
                if method == candidate:
                    continue
                gap = st.median(queries[method]) - st.median(queries[candidate])
                saving = st.median([1 - b / a for a, b in zip(queries[method], queries[candidate])])
                estimate = math.floor(preparation / gap) + 1 if gap > 0 and saving >= .02 else None
                alternatives[method] = {'gap_ns': gap, 'saving_fraction': saving,
                                        'estimated_calls': estimate,
                                        'status': 'slower' if gap <= 0 else 'close' if saving < .02 else 'estimate'}
            models.append({'case': case['id'], 'candidate': candidate, 'prepare_release_ns': preparation,
                           'alternatives': alternatives})
            if case['length_study']['match'] not in ['absent', 'mixed']:
                continue
            if case['length_study']['bytes'] == 65536:
                continue
            estimates = [v['estimated_calls'] for v in alternatives.values() if v['estimated_calls']]
            points = {1}
            for estimate in estimates:
                points.update([max(1, math.floor(estimate * .75)), min(4096, math.ceil(estimate * 1.25))])
            models[-1]['direct_points'] = sorted(point for point in points if point <= 4096)
            models[-1]['direct_scope'] = 'capped_at_4096' if any(value > 4096 for value in estimates) else 'selected_near_estimates'
            for count in sorted(points):
                if count > 4096:
                    continue
                config = {**config_base, 'case': case, 'batch_size': count,
                          'methods': case['methods'], 'mode': 'check'}
                checked = call(cc, 'supplements/batch.php', config)
                config['mode'] = 'time'
                timed = call(cc, 'supplements/batch.php', config)
                output_sum = sum(len(doc['expected']['text'].encode()) if case['operation'] == 'replace'
                                 else len(doc['expected']) if isinstance(doc['expected'], list)
                                 else int(doc['expected']) for job in case['jobs'] for doc in job['documents'])
                expected_sink = sum(n * count // len(case['jobs']) * output_sum
                                    for n in timed['result']['iterations'].values()) * passes
                assert timed['result']['sink'] == expected_sink
                batches.append({'case': case['id'], 'calls': count, 'check': checked, 'time': timed})
                save(run / f'length-payback-{cc}.json', {'status': 'running', 'metadata': metadata,
                                                       'models': models, 'batches': batches})
                print('BATCH', cc, case['id'], count, flush=True)
        aa('after')
        save(run / f'length-payback-{cc}.json', {'status': 'complete', 'metadata': metadata,
                                               'models': models, 'batches': batches})
    (run / 'ADDITIONAL_COMPLETE').write_text('PASS\n')
    print('ADDITIONAL COMPLETE', flush=True)


if __name__ == '__main__':
    main()
