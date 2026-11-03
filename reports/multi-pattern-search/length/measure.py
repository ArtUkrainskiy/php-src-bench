#!/usr/bin/env python3
"""Measure the fixed-length corpus on a pinned Linux CPU; one call processes one document."""
import argparse
import datetime
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import statistics
import subprocess
import time

ROOT = Path(__file__).resolve().parent


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cpu_ticks(cpu):
    line = next(line for line in Path('/proc/stat').read_text().splitlines() if line.startswith(f'cpu{cpu} '))
    ticks = list(map(int, line.split()[1:9]))
    return {'total': sum(ticks), 'idle': ticks[3] + ticks[4]}


def execute(command, timeout=120):
    result = subprocess.run(list(map(str, command)), capture_output=True, text=True, timeout=timeout)
    if result.returncode:
        raise RuntimeError(f'Command failed ({result.returncode}): {command}\n{result.stdout}\n{result.stderr}')
    return result


class Measurement:
    def __init__(self, args):
        self.args = args
        self.output = Path(args.output).resolve()
        self.output.mkdir(parents=True, exist_ok=True)
        self.lock = (self.output / 'run.lock').open('w')
        fcntl.flock(self.lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if (self.output / 'results.json').exists():
            raise RuntimeError('Use a new output directory; results already exist')
        self.cpu_lock = Path(f'/tmp/php-bench-multi-pattern-cpu-{args.cpu}.lock').open('w')
        fcntl.flock(self.cpu_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        self.corpus = Path(args.corpus).resolve()
        self.index = read(self.corpus / 'index.json')
        self.cases = []
        for name, expected in self.index['suite_sha256'].items():
            if digest(self.corpus / name) != expected:
                raise RuntimeError('Corpus hash mismatch: ' + name)
            self.cases.extend(read(self.corpus / name)['cases'])
        if args.filter:
            self.cases = [case for case in self.cases if args.filter in case['id']]
        if not self.cases:
            raise RuntimeError('No cases selected')
        self.build = Path(args.php_build).resolve()
        self.php = self.build / 'sapi/cli/php'
        self.module = self.output / 'strmatch.so'
        self.runtime = read(self.build / '.bench-build.json')
        if self.runtime['debug'] or self.runtime['profile'] != 'docker':
            raise RuntimeError('Use a release docker-profile build')
        if args.cpu not in os.sched_getaffinity(0):
            raise RuntimeError('Unavailable CPU')
        self.source_hashes = {name: digest(Path(args.source) / name) for name in ['strmatch.c', 'php_strmatch.h', 'strmatch_arginfo.h']}
        flags = shlex.split(self.runtime['cflags_user']) + [
            '-std=c11', '-shared', '-fPIC', '-ffp-contract=off', '-fvisibility=hidden', '-DNDEBUG',
            '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-sign-compare',
            '-D_GNU_SOURCE', '-DCOMPILE_DL_STRMATCH=1', '-DZEND_ENABLE_STATIC_TSRMLS_CACHE=1',
        ]
        self.build_command = [args.cc, *flags, *['-I' + str(self.build / part) for part in ['', 'main', 'TSRM', 'Zend']],
                              str(Path(args.source).resolve() / 'strmatch.c'), '-o', str(self.module)]
        execute(self.build_command, timeout=60)
        self.base_command = ['taskset', '-c', str(args.cpu), str(self.php), '-n', '-d', 'pcre.jit=1',
                             '-d', 'opcache.enable_cli=0', '-d', 'opcache.jit=0', '-d', 'extension=' + str(self.module)]
        version = json.loads(execute([*self.base_command, '-r',
            'echo json_encode(["php"=>PHP_VERSION,"debug"=>(bool)PHP_DEBUG,"zts"=>(bool)PHP_ZTS,"extension"=>phpversion("strmatch"),"pcre"=>PCRE_VERSION,"pcre_jit"=>ini_get("pcre.jit")]);']).stdout)
        if version['debug'] or version['extension'] != '0.9-dev':
            raise RuntimeError('Unexpected runtime or extension')
        self.protocol = {'passes': args.passes, 'warmup_ns': int(args.warmup * 1e9),
                         'sample_ns': int(args.sample * 1e9), 'perf_passes': 5, 'perf_target_ns': 80_000_000,
                         'first_requests': 15, 'pcre_cache': 'Warm for main series; separate fresh-process first requests',
                         'counter_method': 'user cycles/instructions for N jobs minus same startup/warmup with zero jobs, divided by N',
                         'wall_method': 'elapsed within process; complete jobs rotated evenly; no empty-loop subtraction',
                         'all_result_types': 'Matcher returns MatchResult objects; native/PCRE return associative arrays; normalization only in output checks',
                         'input_dictionary_sharing': 'Equal per-job dictionaries share one array outside timing; different per-order maps remain distinct'}
        self.metadata = {'started': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                         'compiler': execute([args.cc, '--version']).stdout.splitlines()[0],
                         'cpu': args.cpu, 'host': os.uname().nodename, 'kernel': os.uname().release,
                         'runtime_build': self.runtime, 'version': version, 'php_sha256': digest(self.php),
                         'module_sha256': digest(self.module), 'source_sha256': self.source_hashes, 'source_revision': args.source_revision,
                         'corpus_index_sha256': digest(self.corpus / 'index.json'),
                         'harness_sha256': digest(ROOT / 'harness.php'), 'driver_sha256': digest(__file__),
                         'build_command': self.build_command, 'protocol': self.protocol,
                         'cpu_model': next(line.split(':',1)[1].strip() for line in Path('/proc/cpuinfo').read_text().splitlines() if line.startswith('model name')),
                         'siblings': Path(f'/sys/devices/system/cpu/cpu{args.cpu}/topology/thread_siblings_list').read_text().strip(),
                         'governor': Path(f'/sys/devices/system/cpu/cpu{args.cpu}/cpufreq/scaling_governor').read_text().strip(),
                         'load_before': os.getloadavg(),
                         'boost': Path('/sys/devices/system/cpu/cpufreq/boost').read_text().strip() if Path('/sys/devices/system/cpu/cpufreq/boost').exists() else None}
        self.result = {'metadata': self.metadata, 'checks': [], 'aa': [], 'rows': []}
        self.sequence = 0
        (self.output / 'raw').mkdir(exist_ok=True)
        self.save()

    def save(self):
        write(self.output / 'results.json', self.result)

    def request(self, case, lifecycle, methods, mode, **extra):
        self.sequence += 1
        config = {'case': case, 'lifecycle': lifecycle, 'methods': methods, 'mode': mode,
                  'passes': self.args.passes, 'warmup_ns': self.protocol['warmup_ns'],
                  'sample_ns': self.protocol['sample_ns'], **extra}
        path = self.output / 'raw' / f'{self.sequence:05}-{mode}.json'
        write(path, config)
        command = [*self.base_command, str(ROOT / 'harness.php'), str(path)]
        return command, path

    def call(self, case, lifecycle, methods, mode, **extra):
        command, path = self.request(case, lifecycle, methods, mode, **extra)
        result = execute(command, timeout=120)
        if result.stderr:
            raise RuntimeError(result.stderr)
        output = json.loads(result.stdout)
        write(path.with_name(path.stem + '-output.json'), output)
        return output

    def counter(self, case, lifecycle, method, iterations):
        command, path = self.request(case, lifecycle, [method], 'perf', iterations=iterations)
        result = execute(['perf', 'stat', '-x', ';', '-e', 'cycles:u,instructions:u,context-switches,cpu-migrations', '--', *command])
        path.with_suffix('.perf.txt').write_text(result.stderr)
        values = {}
        for line in result.stderr.splitlines():
            fields = line.split(';')
            if len(fields) > 2 and fields[2] in ['cycles:u', 'instructions:u']:
                values[fields[2]] = float(fields[0])
                if len(fields) > 4 and fields[4] and float(fields[4]) < 99:
                    raise RuntimeError('Multiplexed hardware counters')
        if len(values) != 2:
            raise RuntimeError(result.stderr)
        return values

    def counter_pair(self, case, lifecycle, method, count, repeat):
        values = {}
        for n in ([0, count] if repeat % 2 == 0 else [count, 0]):
            values[n] = self.counter(case, lifecycle, method, n)
        sample = {name: (values[count][name] - values[0][name]) / count for name in values[count]}
        if any(value <= 0 for value in sample.values()):
            raise RuntimeError('Nonpositive corrected counters')
        return sample

    def counters(self, case, lifecycle, method, count):
        return [self.counter_pair(case, lifecycle, method, count, repeat) for repeat in range(self.protocol['perf_passes'])]

    def aa(self, stage):
        choices = [('length.any.absent.128', 'worker', 'matcher'), ('length.replace.mixed.65536', 'worker', 'replacer')]
        for identifier, lifecycle, method in choices:
            case = next((case for case in self.cases if case['id'] == identifier), None)
            if case is None:
                case = self.cases[0]
                lifecycle = case['lifetime']['modes'][0]['id']
                method = case['methods'][0]
            timed = self.call(case, lifecycle, {'a': method, 'b': method}, 'time')
            ratios = [b/a for a,b in zip(timed['ns_per_job']['a'], timed['ns_per_job']['b'])]
            multiple = len(case['jobs'])
            count = max(multiple, math.ceil(timed['iterations']['a'] * 80_000_000 / self.protocol['sample_ns'] / multiple) * multiple)
            counter_samples = {'a': [], 'b': []}
            for repeat in range(self.protocol['perf_passes']):
                for label in (['a', 'b'] if repeat % 2 == 0 else ['b', 'a']):
                    counter_samples[label].append(self.counter_pair(case, lifecycle, method, count, repeat))
            a, b = counter_samples['a'], counter_samples['b']
            item = {'stage': stage, 'case': case['id'], 'lifecycle': lifecycle, 'method': method, 'time': timed,
                    'time_ratios': ratios, 'median_ratio': statistics.median(ratios),
                    'counter_a': a, 'counter_b': b}
            self.result['aa'].append(item)
            self.save()
            print('AA', stage, case['id'], f"{(item['median_ratio']-1)*100:+.2f}%", flush=True)
            if abs(item['median_ratio'] - 1) > 0.02:
                raise RuntimeError('A/A elapsed median outside 2%; inspect environment before continuing')

    def run(self):
        checks = []
        for case in self.cases:
            for mode in case['lifetime']['modes']:
                result = self.call(case, mode['id'], case['methods'], 'check')
                checks.append({'case': case['id'], 'lifecycle': mode['id'], **result})
        self.result['checks'] = checks
        self.save()
        print('CORRECTNESS PASS', sum(item['comparisons'] for item in checks), 'comparisons', flush=True)
        if self.args.command == 'smoke':
            case = self.cases[0]
            mode = case['lifetime']['modes'][0]['id']
            timed = self.call(case, mode, {method: method for method in case['methods']}, 'time')
            for method in case['methods']:
                count = max(len(case['jobs']), timed['iterations'][method])
                self.counters(case, mode, method, count)
            if case['operation'] == 'any' and 'contains_loop' in case['methods']:
                try:
                    self.call(case, mode, ['contains_loop'], 'check', mutation=True)
                except RuntimeError as error:
                    if 'Output mismatch' not in str(error):
                        raise
                    print('MUTATION CAUGHT', flush=True)
                else:
                    raise RuntimeError('Incorrect output was accepted')
            self.result['smoke'] = timed
            self.result['status'] = 'smoke-pass'
            self.save()
            print('SMOKE PASS', flush=True)
            return
        self.aa('before')
        total = sum(len(case['lifetime']['modes']) for case in self.cases)
        done = 0
        start = time.monotonic()
        for case in self.cases:
            for mode in case['lifetime']['modes']:
                lifecycle = mode['id']
                before = time.monotonic()
                siblings = [int(cpu) for cpu in self.metadata['siblings'].split(',') if int(cpu) != self.args.cpu]
                sibling_before = {cpu: cpu_ticks(cpu) for cpu in siblings}
                timed = self.call(case, lifecycle, {method: method for method in case['methods']}, 'time')
                counters = {}
                multiple = len(case['jobs'])
                for method in case['methods']:
                    count = max(multiple, math.ceil(timed['iterations'][method] * 80_000_000 / self.protocol['sample_ns'] / multiple) * multiple)
                    counters[method] = {'iterations': count, 'samples': []}
                for repeat in range(self.protocol['perf_passes']):
                    order = case['methods'] if repeat % 2 == 0 else case['methods'][::-1]
                    for method in order:
                        counters[method]['samples'].append(self.counter_pair(case, lifecycle, method, counters[method]['iterations'], repeat))
                first = {}
                if lifecycle == 'request':
                    for method in case['methods']:
                        if method.startswith('preg_'):
                            first[method] = [self.call(case, lifecycle, [method], 'first', job=i % len(case['jobs']))['ns'] for i in range(15)]
                row = {'case': case['id'], 'title': case['title'], 'kind': case['kind'], 'lifecycle': lifecycle,
                       'methods': case['methods'], 'time': timed, 'counters': counters,
                       'fresh_process_first_request_ns': first,
                       'ns_per_job_median': {method: statistics.median(samples) for method,samples in timed['ns_per_job'].items()},
                       'duration_s': time.monotonic() - before, 'load_after': os.getloadavg()}
                row['sibling_busy_percent'] = {}
                for cpu in siblings:
                    after = cpu_ticks(cpu)
                    total_ticks = after['total'] - sibling_before[cpu]['total']
                    idle_ticks = after['idle'] - sibling_before[cpu]['idle']
                    row['sibling_busy_percent'][str(cpu)] = 100 * (1 - idle_ticks / max(1, total_ticks))
                self.result['rows'].append(row)
                self.save()
                if any(value > 5 for value in row['sibling_busy_percent'].values()):
                    raise RuntimeError('SMT sibling busy above 5%; current row needs remeasurement')
                done += 1
                eta = (time.monotonic()-start)/done*(total-done)
                print(f'DONE {done}/{total} {case["id"]} {lifecycle} {row["duration_s"]:.1f}s ETA {eta/60:.1f}min',flush=True)
        self.aa('after')
        self.result['finished'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        self.result['status'] = 'complete'
        self.save()
        print('COMPLETE', len(self.result['rows']), 'rows', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['smoke','run'])
    parser.add_argument('--php-build', required=True)
    parser.add_argument('--source', required=True)
    parser.add_argument('--source-revision', required=True)
    parser.add_argument('--cc', required=True)
    parser.add_argument('--cpu', required=True, type=int)
    parser.add_argument('--output', required=True)
    parser.add_argument('--corpus', default=str(ROOT.parent.parent.parent / 'corpus/multi-pattern-length'))
    parser.add_argument('--filter', default='')
    parser.add_argument('--passes', type=int, default=15)
    parser.add_argument('--sample', type=float, default=1/15)
    parser.add_argument('--warmup', type=float, default=0.25)
    args = parser.parse_args()
    if args.passes < 1 or args.sample <= 0 or args.warmup < 0:
        parser.error('Invalid timing protocol')
    Measurement(args).run()


if __name__ == '__main__':
    main()
