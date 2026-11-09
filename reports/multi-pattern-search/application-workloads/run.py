#!/usr/bin/env python3
"""Resumable application-job checks and paired measurements."""
import argparse
import datetime
import fcntl
import hashlib
import json
import math
from pathlib import Path
import statistics
import subprocess
import time

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def cpu_snapshot(cpu):
    fields = next(line for line in Path('/proc/stat').read_text().splitlines()
                  if line.startswith('cpu' + str(cpu) + ' ')).split()[1:9]
    fields = list(map(int, fields))
    return sum(fields), fields[3] + fields[4]


def read_temperature():
    values = []
    for path in Path('/sys/class/thermal').glob('thermal_zone*/temp'):
        try:
            values.append(int(path.read_text()) / 1000)
        except (OSError, ValueError):
            pass
    return values


def config_for(corpus, case):
    return {'case': case, 'dictionary': corpus['dictionaries'][case['dictionary']],
            'documents': {i: (ROOT / corpus['documents'][i]['path']).read_text()
                          for i in case['documents']}}


def summarize(raw):
    samples = raw['result']['ns_per_job']
    medians = {method: statistics.median(values) for method, values in samples.items()}
    alternatives = [m for m in samples if m not in ['native', 'native_aa']]
    reference = min(alternatives, key=lambda m: medians[m])
    aa = 100 * (statistics.median(b / a for a, b in zip(samples['native'], samples['native_aa'])) - 1)
    spreads = {m: max(abs(v / medians[m] - 1) for v in values) for m, values in samples.items()}
    flags = []
    if abs(aa) > 2:
        flags.append('aa-outside-2-percent')
    if raw['sibling_busy_percent'] > 2:
        flags.append('smt-load')
    if raw['cpu_steal_ticks']:
        flags.append('cpu-steal')
    for method in ['native', 'native_aa', reference]:
        if spreads[method] > .05:
            flags.append('spread:' + method)
    paired = [a / b for a, b in zip(samples['native'], samples[reference])]
    return {'reference': reference, 'median_us': {m: v / 1000 for m, v in medians.items()},
            'paired_ratio': statistics.median(paired), 'paired_ratio_min': min(paired),
            'paired_ratio_max': max(paired), 'delta_percent': 100 * (statistics.median(paired) - 1),
            'aa_percent': aa, 'relative_spread': spreads, 'flags': flags, 'qualified': not flags}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=['check', 'pilot', 'time', 'counters'])
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--environment', type=Path, required=True)
    parser.add_argument('--compilers', default='gcc13,gcc14,clang18,clang20')
    parser.add_argument('--cpu', type=int, required=True)
    parser.add_argument('--sibling', type=int, required=True)
    parser.add_argument('--passes', type=int, default=15)
    parser.add_argument('--sample-ms', type=int, default=40)
    parser.add_argument('--warmup-ms', type=int, default=100)
    parser.add_argument('--attempts', type=int, default=2)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    lock = (args.output / '.measurement.lock').open('w')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    environment = json.loads(args.environment.read_text())
    compilers = args.compilers.split(',')
    corpus = json.loads((ROOT / 'corpus.json').read_text())
    for cc in compilers:
        build = environment['compilers'][cc]
        for key in ['php', 'module']:
            if sha(build[key]) != build[key + '_sha256']:
                raise RuntimeError('Build changed: ' + cc + '/' + key)
    for doc in corpus['documents'].values():
        if sha(ROOT / doc['path']) != doc['sha256']:
            raise RuntimeError('Document changed: ' + doc['id'])
    fingerprint = hashlib.sha256((sha(ROOT / 'corpus.json') + sha(ROOT / 'harness.php') + sha(__file__)
        + sha(args.environment) + str([args.passes, args.sample_ms, args.warmup_ms, args.cpu, args.sibling])).encode()).hexdigest()
    run_manifest = args.output / 'measurement-identity.json'
    identity = {'fingerprint': fingerprint, 'corpus_sha256': sha(ROOT / 'corpus.json'),
                'harness_sha256': sha(ROOT / 'harness.php'), 'runner_sha256': sha(__file__), 'environment_sha256': sha(args.environment),
                'passes': args.passes, 'sample_ms': args.sample_ms, 'warmup_ms': args.warmup_ms,
                'cpu': args.cpu, 'smt_sibling': args.sibling, 'compilers': compilers}
    if run_manifest.exists() and json.loads(run_manifest.read_text())['fingerprint'] != fingerprint:
        raise RuntimeError('Measurement identity changed; choose a new output directory')
    write(run_manifest, identity)
    captures = args.output / 'captures'
    captures.mkdir(exist_ok=True)

    def execute(cc, case, scope, mode, tag, methods=None, iterations=0, mutation=False):
        build = environment['compilers'][cc]
        config = config_for(corpus, case)
        config.update(mode=mode, scope=scope, methods=methods or {m: m for m in case['methods']},
                      passes=args.passes, sample_ns=args.sample_ms * 1000000,
                      warmup_ns=args.warmup_ms * 1000000, iterations=iterations, mutation=mutation)
        if mode == 'time':
            config['methods']['native_aa'] = 'native'
        path = captures / (tag + '.config.json')
        write(path, config)
        command = ['taskset', '-c', str(args.cpu), build['php'], '-n', '-d', 'pcre.jit=1',
                   '-d', 'opcache.enable_cli=0', '-d', 'opcache.jit=0',
                   '-d', 'extension=' + build['module'], str(ROOT / 'harness.php'), str(path)]
        if mode == 'perf':
            command = ['perf', 'stat', '-x', ';', '-e',
                       'cpu_core/cycles/u,cpu_core/instructions/u,context-switches,cpu-migrations', '--'] + command
        first = cpu_snapshot(args.sibling)
        cpu_before = Path('/proc/stat').read_text().splitlines()[0].split()
        temperatures = read_temperature()
        start = time.monotonic()
        result = subprocess.run(command, capture_output=True, text=True, timeout=180)
        elapsed = time.monotonic() - start
        last = cpu_snapshot(args.sibling)
        cpu_after = Path('/proc/stat').read_text().splitlines()[0].split()
        ticks = last[0] - first[0]
        busy = 100 * (1 - (last[1] - first[1]) / ticks) if ticks else 0.0
        record = {'compiler': cc, 'case': case['id'], 'scope': scope, 'mode': mode,
                  'fingerprint': fingerprint, 'returncode': result.returncode, 'elapsed_s': elapsed,
                  'sibling_busy_percent': busy, 'sibling_observation_ticks': ticks,
                  'cpu_steal_ticks': int(cpu_after[8]) - int(cpu_before[8]),
                  'temperature_before_c': temperatures, 'temperature_after_c': read_temperature(),
                  'stdout': result.stdout, 'stderr': result.stderr, 'command': command,
                  'timestamp_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
        if result.returncode == 0:
            record['result'] = json.loads(result.stdout)
        write(captures / (tag + '.json'), record)
        return record

    cases = corpus['cases']
    if args.phase == 'check':
        total = 0
        for cc in compilers:
            checks = 0
            for case in cases:
                result = execute(cc, case, case['modes'][0], 'check', 'check-' + cc + '-' + case['id'])
                if result['returncode']:
                    raise RuntimeError(result['stderr'])
                checks += result['result']['checks']
            mutation = execute(cc, cases[0], cases[0]['modes'][0], 'check', 'mutation-' + cc, mutation=True)
            if not mutation['returncode']:
                raise RuntimeError('Mutation was not detected')
            total += checks
            print(cc, 'PASS', checks, 'comparisons; mutation detected', flush=True)
        write(args.output / 'checks.json', {'status': 'PASS', 'comparisons': total,
              'cases_per_compiler': len(cases), 'fingerprint': fingerprint, 'compilers': compilers,
              'mutation_detected': True})
        return
    checks = json.loads((args.output / 'checks.json').read_text())
    if checks['fingerprint'] != fingerprint or any(cc not in checks['compilers'] for cc in compilers):
        raise RuntimeError('Correctness checks do not cover this measurement identity')
    points = [(cc, case, scope) for cc in compilers for case in cases for scope in case['modes']]
    if args.phase == 'pilot':
        wanted = {next(c['id'] for c in cases if c['family'] == family and 'batch_size' not in c)
                  for family in ['validation', 'references', 'rewrite', 'email']}
        points = [p for p in points if p[0] == compilers[0] and p[1]['id'] in wanted]
    started = time.monotonic()
    if args.phase in ['time', 'pilot']:
        for index, (cc, case, scope) in enumerate(points):
            tag = cc + '-' + case['id'] + '-' + scope
            target = args.output / ('pilot' if args.phase == 'pilot' else 'timings') / (tag + '.json')
            if target.exists():
                if json.loads(target.read_text())['fingerprint'] != fingerprint:
                    raise RuntimeError('Stale checkpoint')
                continue
            attempts, chosen = [], None
            for attempt in range(1, args.attempts + 1):
                record = execute(cc, case, scope, 'time', args.phase + '-' + tag + '-a' + str(attempt))
                if record['returncode']:
                    raise RuntimeError(record['stderr'])
                summary = summarize(record)
                entry = {**summary, 'raw': args.phase + '-' + tag + '-a' + str(attempt) + '.json'}
                attempts.append(entry)
                chosen = chosen or entry
                if summary['qualified']:
                    chosen = entry
                    break
            final = {**chosen, 'compiler': cc, 'case': case['id'], 'scope': scope,
                     'fingerprint': fingerprint, 'attempts': attempts}
            write(target, final)
            status = {'phase': args.phase, 'completed': index + 1, 'total': len(points),
                      'compiler': cc, 'case': case['id'], 'scope': scope, 'flags': chosen['flags'],
                      'elapsed_s': time.monotonic() - started,
                      'updated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
            write(args.output / 'status.json', status)
            print(index + 1, '/', len(points), cc, case['id'], scope,
                  'quality=' + ('PASS' if chosen['qualified'] else ','.join(chosen['flags'])), flush=True)
        write(args.output / (args.phase + '-done.json'), {'status': 'complete', 'points': len(points),
              'elapsed_s': time.monotonic() - started, 'fingerprint': fingerprint})
        return

    for index, (cc, case, scope) in enumerate(points):
        tag = cc + '-' + case['id'] + '-' + scope
        target = args.output / 'counters' / (tag + '.json')
        if target.exists():
            continue
        timing = json.loads((args.output / 'timings' / (tag + '.json')).read_text())
        methods = {}
        for method in case['methods']:
            n = max(1, min(1000000, math.ceil(30000 / timing['median_us'][method])))
            pairs = []
            for round_index in range(5):
                raw = {}
                for count in ([0, n] if round_index % 2 == 0 else [n, 0]):
                    capture = execute(cc, case, scope, 'perf',
                        'perf-' + tag + '-' + method + '-r' + str(round_index) + '-n' + str(count),
                        methods={method: method}, iterations=count)
                    if capture['returncode']:
                        raise RuntimeError(capture['stderr'])
                    counts = {}
                    available = True
                    for line in capture['stderr'].splitlines():
                        fields = line.split(';')
                        if len(fields) > 2 and fields[2] in ['cpu_core/cycles/u', 'cpu_core/instructions/u', 'context-switches', 'cpu-migrations']:
                            try:
                                counts[fields[2]] = float(fields[0])
                            except ValueError:
                                available = False
                            if len(fields) > 4 and fields[4] and float(fields[4]) < 99:
                                available = False
                    raw[count] = {'counts': counts, 'available': available,
                                  'sibling_busy_percent': capture['sibling_busy_percent']}
                events = ['cpu_core/cycles/u', 'cpu_core/instructions/u']
                corrected = {event: (raw[n]['counts'].get(event, -1) - raw[0]['counts'].get(event, -1)) / n for event in events}
                valid = all(value > 0 for value in corrected.values()) and all(
                    v['available'] and v['sibling_busy_percent'] <= 2 and all(event in v['counts'] for event in events)
                    for v in raw.values())
                pairs.append({'per_job': corrected, 'valid': valid, 'raw': raw})
            methods[method] = {'iterations': n, 'pairs': pairs, 'qualified': all(p['valid'] for p in pairs),
                               'median': {event: statistics.median(p['per_job'][event] for p in pairs) for event in events}}
        write(target, {'compiler': cc, 'case': case['id'], 'scope': scope,
                       'fingerprint': fingerprint, 'methods': methods})
        write(args.output / 'counter-status.json', {'completed': index + 1, 'total': len(points),
              'compiler': cc, 'case': case['id'], 'scope': scope,
              'updated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()})
        print('counters', index + 1, '/', len(points), cc, case['id'], scope, flush=True)
    write(args.output / 'counters-done.json', {'status': 'complete', 'points': len(points), 'fingerprint': fingerprint})


if __name__ == '__main__':
    main()
