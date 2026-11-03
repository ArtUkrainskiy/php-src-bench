#!/usr/bin/env python3
"""Measure saved 4 KiB dictionary/position cases and directly timed one-operation lifetimes."""

import argparse
import datetime
import fcntl
import hashlib
import json
import os
import statistics as st
import subprocess
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent
CORPUS = REPORT / '../../corpus/multi-pattern-4k'
REVISION = '287aaab7fb729d3a8e91c6fd35224c4359c343e3'


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def ticks(cpu):
    values = list(
        map(
            int,
            next(line for line in Path('/proc/stat').read_text().splitlines() if line.startswith(f'cpu{cpu} ')).split()[
                1:9
            ],
        )
    )
    return sum(values), values[3] + values[4]


def cases():
    index = read(CORPUS / 'index.json')
    result = []
    for name, expected in index['suite_sha256'].items():
        assert digest(CORPUS / name) == expected, name
        result.extend(read(CORPUS / name)['cases'])
    assert len(result) == 18
    return result


def run_batches(args, tag, build, smoke, pins):
    mode = 'smoke' if smoke else 'data-grid'
    main_dir = args.run_root / f'{mode}-{tag}'
    main = read(main_dir / 'results.json')
    metadata = main['metadata']
    assert main['status'] == ('smoke-pass' if smoke else 'complete')
    assert metadata['source_revision'] == REVISION
    assert metadata['source_sha256']['strmatch.c'] == 'adafc9cb67a435523811b540734c7d51fc4f7ff1edf3aabd5f7b94c4cf19e254'
    assert metadata['php_sha256'] == digest(build / 'sapi/cli/php')
    assert metadata['module_sha256'] == digest(main_dir / 'strmatch.so')
    raw = args.run_root / f'batch-{mode}-{tag}'
    raw.mkdir()
    sequence = 0
    protocol = {
        'passes': 1 if smoke else 15,
        'warmup_ns': 1_000_000 if smoke else 250_000_000,
        'sample_ns': 10_000_000 if smoke else round(1e9 / 15),
    }
    all_cases = cases()
    selected = (
        [case for case in all_cases if case['id'] in ['grid.any.absent.8', 'grid.replace.mixed.8']]
        if smoke
        else all_cases
    )
    output = {
        'status': 'running',
        'metadata': {'main_metadata': metadata, 'pins': pins, 'protocol': protocol},
        'rows': [],
        'aa': [],
        'mutations': [],
    }

    def call(helper, config, mutation=False):
        nonlocal sequence
        assert all(digest(REPORT / name) == expected for name, expected in pins.items())
        sequence += 1
        path = raw / f'{sequence:05}.json'
        save(path, {**protocol, **config})
        command = [
            'taskset',
            '-c',
            str(args.cpu),
            str(build / 'sapi/cli/php'),
            '-n',
            '-d',
            'pcre.jit=1',
            '-d',
            'opcache.enable_cli=0',
            '-d',
            'opcache.jit=0',
            '-d',
            'extension=' + str(main_dir / 'strmatch.so'),
            str(REPORT / helper),
            str(path),
        ]
        before = ticks(args.sibling)
        process = subprocess.run(command, text=True, capture_output=True, timeout=120, check=False)
        after = ticks(args.sibling)
        path.with_suffix('.stdout').write_text(process.stdout)
        path.with_suffix('.stderr').write_text(process.stderr)
        if mutation:
            assert process.returncode and 'mismatch' in (process.stdout + process.stderr).lower()
            return {'raw': str(path.relative_to(args.run_root)), 'caught': True}
        assert process.returncode == 0 and not process.stderr, (process.stdout, process.stderr)
        total = after[0] - before[0]
        busy = None if total == 0 else 100 * (1 - (after[1] - before[1]) / total)
        assert busy is None or busy <= 5, ('SMT sibling busy', busy)
        return {
            'raw': str(path.relative_to(args.run_root)),
            'result': json.loads(process.stdout),
            'sibling_busy_percent': busy,
        }

    def aa(stage):
        for identifier, candidate in [('grid.any.absent.128', 'matcher'), ('grid.replace.mixed.128', 'replacer')]:
            case = next(c for c in all_cases if c['id'] == identifier)
            result = call(
                'supplements/batch.php',
                {'case': case, 'methods': {'a': candidate, 'b': candidate}, 'batch_size': 1, 'mode': 'time'},
            )
            values = result['result']['ns_per_batch']
            ratio = st.median([b / a for a, b in zip(values['a'], values['b'])])
            assert smoke or abs(ratio - 1) <= 0.02, ('One-shot A/A', ratio)
            output['aa'].append({'stage': stage, 'case': identifier, 'median_ratio': ratio, 'time': result})
            print('ONE-SHOT AA', tag, stage, identifier, f'{(ratio - 1) * 100:+.2f}%', flush=True)

    with Path(f'/tmp/php-bench-multi-pattern-cpu-{args.cpu}.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        aa('before')
        for case in selected:
            for count in [1, 2] if smoke else [1]:
                config = {'case': case, 'methods': case['methods'], 'batch_size': count}
                check = call('supplements/batch.php', {**config, 'mode': 'check'})
                timed = call('supplements/batch.php', {**config, 'mode': 'time'})
                result = timed['result']
                expected = sum(
                    len(doc['expected']['text'].encode()) if case['operation'] == 'replace' else int(doc['expected'])
                    for job in case['jobs']
                    for doc in job['documents']
                )
                assert all(n % 4 == 0 for n in result['iterations'].values())
                assert result['sink'] == sum(result['iterations'].values()) // 4 * count * expected * protocol['passes']
                output['rows'].append({'case': case['id'], 'calls': count, 'check': check, 'time': timed})
            if smoke:
                candidate = 'matcher' if case['operation'] == 'any' else 'replacer'
                result = call(
                    'length/harness.php',
                    {'case': case, 'methods': [candidate], 'mode': 'check', 'lifecycle': 'worker', 'mutation': True},
                    mutation=True,
                )
                output['mutations'].append(result)
            save(args.run_root / f'oneshot-{mode}-{tag}.json', output)
            print('ONE-SHOT', tag, case['id'], flush=True)
        aa('after')
    output['status'] = 'smoke-pass' if smoke else 'complete'
    save(args.run_root / f'oneshot-{mode}-{tag}.json', output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['smoke', 'run'])
    parser.add_argument('--run-root', type=Path, required=True)
    parser.add_argument('--gcc-build', type=Path, required=True)
    parser.add_argument('--clang-build', type=Path, required=True)
    parser.add_argument('--gcc', default='gcc')
    parser.add_argument('--clang', default='clang')
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--cpu', type=int, required=True)
    parser.add_argument('--sibling', type=int, required=True)
    args = parser.parse_args()
    args.run_root = args.run_root.resolve()
    args.run_root.mkdir(exist_ok=True, parents=True)
    smoke = args.command == 'smoke'
    names = [
        'length/grid.py',
        'length/measure.py',
        'length/harness.php',
        'supplements/batch.php',
        'supplements/definitions.php',
    ]
    pins = {name: digest(REPORT / name) for name in names}
    state = {'pid': os.getpid(), 'started': datetime.datetime.now(datetime.UTC).isoformat(), 'pins': pins}
    try:
        with (args.run_root / 'coordinator.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            for tag, compiler, build in [
                ('gcc15', args.gcc, args.gcc_build),
                ('clang21', args.clang, args.clang_build),
            ]:
                build = build.resolve()
                if not smoke:
                    assert read(args.run_root / f'oneshot-smoke-{tag}.json')['metadata']['pins'] == pins
                state.update(compiler=tag, phase='prepared', updated=datetime.datetime.now(datetime.UTC).isoformat())
                save(args.run_root / 'status.json', state)
                command = [
                    'python3',
                    REPORT / 'length/measure.py',
                    'smoke' if smoke else 'run',
                    '--php-build',
                    build,
                    '--cc',
                    compiler,
                    '--source',
                    args.source,
                    '--source-revision',
                    REVISION,
                    '--cpu',
                    str(args.cpu),
                    '--corpus',
                    CORPUS,
                    '--output',
                    args.run_root / f'{"smoke" if smoke else "data-grid"}-{tag}',
                ]
                if smoke:
                    command.extend(
                        ['--filter', 'grid.any.absent.8', '--passes', '1', '--sample', '.01', '--warmup', '.001']
                    )
                log = args.run_root / f'{args.command}-{tag}.log'
                with log.open('x') as stream:
                    result = subprocess.run(
                        list(map(str, command)), stdout=stream, stderr=subprocess.STDOUT, check=False
                    )
                assert result.returncode == 0, log
                state['phase'] = 'one-shot'
                save(args.run_root / 'status.json', state)
                run_batches(args, tag, build, smoke, pins)
            state.update(phase='complete', finished=datetime.datetime.now(datetime.UTC).isoformat())
            save(args.run_root / 'status.json', state)
            (args.run_root / ('SMOKE_COMPLETE' if smoke else 'GRID_COMPLETE')).write_text('PASS\n')
            print('GRID', args.command.upper(), 'COMPLETE', flush=True)
    except BaseException as error:
        save(args.run_root / 'failure.json', {**state, 'error': repr(error)})
        raise


if __name__ == '__main__':
    main()
