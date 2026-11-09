#!/usr/bin/env python3
"""Bounded adaptive measurements of prepared and one-shot literal operations."""
import argparse
import datetime
import fcntl
import gzip
import hashlib
import json
import math
from pathlib import Path
import statistics
import subprocess
import time

ROOT = Path(__file__).resolve().parent
NATIVE = ['prepared', 'prepared_aa', 'oneshot', 'oneshot_aa']
OPS = {'any': 'Matcher::matches()', 'unique': 'Matcher::getMatchedKeywords()',
       'count': 'Matcher::countMatches()', 'all': 'Matcher::matchAll()', 'replace': 'Replacer::replace()'}


def read(path):
    return json.loads(path.read_text())


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hits(subject, keys):
    result = []
    for key in keys:
        offset = 0
        needle = key.encode()
        while True:
            offset = subject.find(needle, offset)
            if offset < 0:
                break
            result.append({'offset': offset, 'length': len(needle), 'keyword': key})
            offset += 1
    return sorted(result, key=lambda h: (h['offset'], h['length']))


def rewritten(subject, mapping, occurrences):
    cursor, parts = 0, []
    for hit in sorted(occurrences, key=lambda h: (h['offset'], -h['length'])):
        if hit['offset'] < cursor:
            continue
        parts += [subject[cursor:hit['offset']], mapping[hit['keyword']].encode()]
        cursor = hit['offset'] + hit['length']
    return b''.join(parts + [subject[cursor:]]).decode()


def make_case(op, n, size, background='technical', condition=None):
    plan = read(ROOT / 'plan.json')
    dictionary = read(ROOT / 'dictionary.json')
    keys = dictionary['keys'][:n]
    mapping = {k: dictionary['replacements'][k] for k in keys}
    condition = condition or ('absent' if op == 'any' else 'single')
    subject = (ROOT / plan['backgrounds'][background]['file']).read_bytes()[:size]
    assert len(subject) == size and not hits(subject, dictionary['keys'])
    if condition != 'absent':
        key = plan['positive_key'] if condition == 'single' else plan['presence_control_key']
        assert key in keys
        needle = key.encode()
        offset = 8 if condition == 'early' else size - len(needle) - 8 if condition == 'late' else (size - len(needle)) // 2
        subject = subject[:offset - 1] + b' ' + needle + b' ' + subject[offset + len(needle) + 1:]
    found = hits(subject, keys)
    assert len(found) == (0 if condition == 'absent' else 1)
    expected = {'any': lambda: bool(found), 'unique': lambda: list(dict.fromkeys(h['keyword'] for h in found)),
                'count': lambda: len(found), 'all': lambda: found,
                'replace': lambda: rewritten(subject, mapping, found)}[op]()
    methods = ['native', 'string_loop', 'preg_literal', 'preg_trie']
    if op == 'any':
        methods += ['contains_loop']
        if n == 1:
            methods += ['single_contains']
    if op == 'unique' and n == 1:
        methods += ['single_unique']
    if op == 'replace':
        methods = ['native', 'strtr', 'preg_literal_callback', 'preg_trie_callback']
        sequential = subject.decode()
        for key in sorted(keys, key=len, reverse=True):
            sequential = sequential.replace(key, mapping[key])
        if sequential == expected:
            methods += ['str_replace']
    case_id = f'{background}.{op}.n{n}.b{size}.{condition}'
    return {'id': case_id, 'operation': op, 'policy': 'case-sensitive', 'documents': ['subject'],
            'modes': ['prepared', 'oneshot'], 'methods': methods, 'expected': {'subject': expected},
            'keys': n, 'bytes': size, 'background': background, 'condition': condition,
            'occurrences': len(found), 'unique_matched_keys': len({h['keyword'] for h in found}),
            'first_offset': found[0]['offset'] if found else None,
            'dictionary': {'keys': keys, 'replacements': mapping}, 'subject': subject.decode(),
            'subject_sha256': hashlib.sha256(subject).hexdigest()}


def cpu_snapshot(cpu):
    values = list(map(int, next(line for line in Path('/proc/stat').read_text().splitlines()
                     if line.startswith(f'cpu{cpu} ')).split()[1:9]))
    return sum(values), values[3] + values[4]


def method_name(method, op):
    names = {'string_loop': 'strpos() loop', 'contains_loop': 'str_contains() loop',
             'single_contains': 'str_contains()', 'single_unique': 'strpos() + result list',
             'strtr': 'strtr()', 'str_replace': 'str_replace()',
             'preg_literal_callback': 'preg_replace_callback() [literal]',
             'preg_trie_callback': 'preg_replace_callback() [prefix]'}
    if method in ['prepared', 'oneshot']:
        return OPS[op] + ' ' + method
    if method in ['preg_literal', 'preg_trie']:
        return ('preg_match()' if op == 'any' else 'preg_match_all()') + (' [prefix]' if method == 'preg_trie' else ' [literal]')
    return names.get(method, method)


class Collector:
    def __init__(self, args):
        self.args = args
        self.out = args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.lock = (self.out / '.lock').open('w')
        fcntl.flock(self.lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        self.plan = read(ROOT / 'plan.json')
        self.environment = read(args.environment)
        self.build = self.environment['compilers']['gcc14']
        for key in ['php', 'module']:
            assert sha(Path(self.build[key])) == self.build[key + '_sha256'], key
        for background in self.plan['backgrounds'].values():
            assert sha(ROOT / background['file']) == background['sha256']
        assert sha(ROOT / 'dictionary.json') == self.plan['dictionary_sha256']
        self.identity = {'files': {f: sha(ROOT / f) for f in ['plan.json', 'dictionary.json', 'harness.php', 'study.py']},
                         'environment_sha256': sha(args.environment), 'cpu': args.cpu, 'sibling': args.sibling,
                         'compiler': 'gcc14'}
        self.fingerprint = hashlib.sha256(json.dumps(self.identity, sort_keys=True).encode()).hexdigest()
        self.identity['fingerprint'] = self.fingerprint
        manifest = self.out / 'identity.json'
        if manifest.exists():
            assert read(manifest) == self.identity, 'Changed measurement identity'
        save(manifest, self.identity)
        self.selection = read(self.out / 'selection.json') if (self.out / 'selection.json').exists() else []

    def execute(self, case, mode, tag, methods=None, iterations=0, mutation=False):
        config = {'case': {k: v for k, v in case.items() if k not in ['dictionary', 'subject']},
                  'dictionary': case['dictionary'], 'documents': {'subject': case['subject']},
                  'mode': mode, 'scope': 'prepared', 'passes': self.plan['passes'],
                  'sample_ns': self.plan['sample_ms'] * 1000000,
                  'warmup_ns': self.plan['warmup_ms'] * 1000000, 'iterations': iterations, 'mutation': mutation,
                  'methods': methods or {**{label: 'native' for label in NATIVE},
                                        **{m: m for m in case['methods'] if m != 'native'}},
                  'method_scopes': {label: ('oneshot' if label.startswith('oneshot') else 'prepared') for label in NATIVE}}
        path = self.out / 'captures' / (tag + '.config.json')
        save(path, config)
        cmd = [self.build['php'], '-n', '-d', 'pcre.jit=1', '-d', 'opcache.enable_cli=0',
               '-d', 'opcache.jit=0', '-d', 'extension=' + self.build['module'], str(ROOT / 'harness.php'), str(path)]
        if mode == 'perf':
            cmd = ['perf', 'stat', '-x', ';', '-e', 'cpu_core/cycles/u,cpu_core/instructions/u,context-switches,cpu-migrations', '--'] + cmd
        cmd = ['taskset', '-c', str(self.args.cpu)] + cmd
        first = cpu_snapshot(self.args.sibling)
        steal = int(Path('/proc/stat').read_text().splitlines()[0].split()[8])
        start = time.monotonic()
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10 if mode == 'check' else 180)
        last = cpu_snapshot(self.args.sibling)
        ticks = last[0] - first[0]
        raw = {'fingerprint': self.fingerprint, 'case': case['id'], 'mode': mode,
               'elapsed_s': time.monotonic() - start, 'sibling_busy_percent': 100 * (1 - (last[1] - first[1]) / ticks) if ticks else 0,
               'sibling_ticks': ticks, 'cpu_steal_ticks': int(Path('/proc/stat').read_text().splitlines()[0].split()[8]) - steal,
               'returncode': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr,
               'timestamp_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
        if result.returncode == 0:
            raw['result'] = json.loads(result.stdout)
        save(self.out / 'captures' / (tag + '.json'), raw)
        if result.returncode and not mutation:
            raise RuntimeError(result.stderr)
        return raw

    def summarize(self, raw):
        samples = raw['result']['ns_per_job']
        medians = {m: statistics.median(v) / 1000 for m, v in samples.items()}
        ref = min((m for m in samples if m not in NATIVE), key=lambda m: medians[m])
        spread = {m: max(abs(v / statistics.median(values) - 1) for v in values) for m, values in samples.items()}
        scopes = {}
        for mode in ['prepared', 'oneshot']:
            paired = [a / b for a, b in zip(samples[mode], samples[ref])]
            aa = statistics.median(b / a for a, b in zip(samples[mode], samples[mode + '_aa']))
            flags = []
            if abs(aa - 1) > .02:
                flags += ['A/A']
            if raw['sibling_busy_percent'] > 2:
                flags += ['SMT load']
            if raw['cpu_steal_ticks']:
                flags += ['CPU steal']
            flags += ['spread:' + m for m in [mode, mode + '_aa', ref] if spread[m] > .05]
            ratio = statistics.median(paired)
            state = 'flagged' if flags else 'win' if ratio < .98 and max(paired) < 1 else 'loss' if ratio > 1.02 and min(paired) > 1 else 'close'
            scopes[mode] = {'qualified': not flags, 'flags': flags, 'aa_percent': 100 * (aa - 1),
                            'paired_ratio': ratio, 'paired_min': min(paired), 'paired_max': max(paired), 'state': state}
        return {'reference': ref, 'median_us': medians, 'spread': spread, 'scopes': scopes}

    def measure(self, case, reason):
        target = self.out / 'timings' / (case['id'] + '.json')
        if target.exists():
            row = read(target)
            assert row['fingerprint'] == self.fingerprint
            return row
        assert len(self.selection) < self.plan['max_measured_inputs'], 'Measurement budget exhausted'
        if not any(x['case'] == case['id'] for x in self.selection):
            self.selection.append({'case': case['id'], 'reason': reason})
            save(self.out / 'selection.json', self.selection)
        save(self.out / 'inputs' / (case['id'] + '.json'), case)
        checked = self.execute(case, 'check', 'check-' + case['id'])
        if not (self.out / 'mutation.json').exists():
            wrong = self.execute(case, 'check', 'mutation', mutation=True)
            assert wrong['returncode'] != 0, 'Wrong expected output was accepted'
            save(self.out / 'mutation.json', {'detected': True})
        deadline = time.monotonic() + 120
        while True:
            before = [cpu_snapshot(cpu) for cpu in [self.args.cpu, self.args.sibling]]
            time.sleep(.5)
            after = [cpu_snapshot(cpu) for cpu in [self.args.cpu, self.args.sibling]]
            busy = [100 * (1 - (b[1] - a[1]) / (b[0] - a[0])) if b[0] > a[0] else 0 for a, b in zip(before, after)]
            if busy[0] <= 20 + 1e-9 and busy[1] <= 2 + 1e-9:
                break
            if time.monotonic() > deadline:
                raise RuntimeError('Measured CPU or SMT sibling did not become idle within 120 seconds')
        attempts = []
        for attempt in range(self.plan['attempts']):
            tag = case['id'] + '-a' + str(attempt + 1)
            raw = self.execute(case, 'time', tag)
            summary = self.summarize(raw)
            attempts.append({**summary, 'capture': tag + '.json'})
            if all(v['qualified'] for v in summary['scopes'].values()):
                break
        chosen = next((r for r in attempts if all(v['qualified'] for v in r['scopes'].values())), attempts[0])
        row = {**chosen, 'fingerprint': self.fingerprint, 'case': case, 'attempts': attempts,
               'correctness_comparisons': checked['result']['checks']}
        save(target, row)
        save(self.out / 'status.json', {'phase': 'time', 'completed_inputs': len(list((self.out / 'timings').glob('*.json'))),
                                      'case': case['id'], 'reason': reason})
        print(len(self.selection), case['id'], {m: v['state'] for m, v in row['scopes'].items()}, flush=True)
        return row

    def run(self):
        results = {}
        for axis in ['keys', 'length']:
            grid = self.plan['dictionary_sizes'] if axis == 'keys' else self.plan['subject_sizes']
            for op in self.plan['operations']:
                values = {}
                for value in [grid[0], grid[-1]]:
                    values[value] = self.measure(make_case(op, value if axis == 'keys' else 48,
                                                          4096 if axis == 'keys' else value), axis + ':endpoint')
                for iteration in range(self.plan['refinements_per_axis_operation']):
                    candidates = []
                    modes = ['prepared', 'oneshot'] if axis == 'keys' else ['oneshot']
                    measured = sorted(values)
                    for mode in modes:
                        for low, high in zip(measured, measured[1:]):
                            inside = [x for x in grid if low < x < high and x not in values]
                            if inside and values[low]['scopes'][mode]['state'] != 'win' and values[high]['scopes'][mode]['state'] == 'win':
                                candidates.append((len(inside), inside[(len(inside) - 1) // 2]))
                    if candidates:
                        value = max(candidates)[1]
                    else:
                        remaining = [x for x in grid if x not in values]
                        if not remaining:
                            break
                        # Probe untested interior points even when endpoints have the same winner.
                        value = remaining[len(remaining) // 2]
                    values[value] = self.measure(make_case(op, value if axis == 'keys' else 48,
                                                          4096 if axis == 'keys' else value), axis + ':refinement-' + str(iteration + 1))
                results[(axis, op)] = values
        presence = results[('length', 'any')]
        winning = [size for size, row in presence.items() if row['scopes']['oneshot']['state'] == 'win']
        control_size = min(winning) if winning else max(presence)
        for condition in ['early', 'middle', 'late']:
            self.measure(make_case('any', 48, control_size, condition=condition), 'presence-position-control')
        for op in self.plan['operations']:
            for axis, mode in [('keys', 'prepared'), ('length', 'oneshot')]:
                winners = [(value, row) for value, row in results[(axis, op)].items() if row['scopes'][mode]['state'] == 'win']
                if winners:
                    _, row = min(winners)
                    case = row['case']
                    self.measure(make_case(op, case['keys'], case['bytes'], background='comments', condition=case['condition']),
                                 'second-background:' + axis + ':' + mode)
        save(self.out / 'time-done.json', {'inputs': len(self.selection), 'fingerprint': self.fingerprint})

    def counters(self):
        assert (self.out / 'time-done.json').exists()
        for index, selected in enumerate(self.selection):
            row = read(self.out / 'timings' / (selected['case'] + '.json'))
            case = row['case']
            path = self.out / 'counters' / (case['id'] + '.json')
            if path.exists():
                continue
            methods = {}
            for method in [m for m in row['median_us'] if not m.endswith('_aa')]:
                count = max(1, min(1000000, math.ceil(30000 / row['median_us'][method])))
                pairs = []
                for repeat in range(5):
                    observations = {}
                    for n in ([0, count] if repeat % 2 == 0 else [count, 0]):
                        capture = self.execute(case, 'perf', f'perf-{case["id"]}-{method}-r{repeat}-n{n}',
                                               methods={method: 'native' if method in NATIVE else method}, iterations=n)
                        counts, available = {}, True
                        for line in capture['stderr'].splitlines():
                            fields = line.split(';')
                            if len(fields) > 2 and fields[2] in ['cpu_core/cycles/u', 'cpu_core/instructions/u']:
                                try:
                                    counts[fields[2]] = float(fields[0])
                                    available &= not fields[4] or float(fields[4]) >= 99
                                except (ValueError, IndexError):
                                    available = False
                        observations[n] = {'counts': counts, 'available': available,
                                           'sibling_busy_percent': capture['sibling_busy_percent']}
                    events = ['cpu_core/cycles/u', 'cpu_core/instructions/u']
                    corrected = {e: (observations[count]['counts'].get(e, -1) - observations[0]['counts'].get(e, -1)) / count for e in events}
                    valid = all(v > 0 for v in corrected.values()) and all(x['available'] and x['sibling_busy_percent'] <= 2
                            and all(e in x['counts'] for e in events) for x in observations.values())
                    pairs.append({'valid': valid, 'per_job': corrected, 'raw': observations})
                methods[method] = {'qualified': all(x['valid'] for x in pairs), 'pairs': pairs,
                                   'median': {e: statistics.median(x['per_job'][e] for x in pairs) for e in events}}
            save(path, {'case': case['id'], 'fingerprint': self.fingerprint, 'methods': methods})
            print('counters', index + 1, '/', len(self.selection), case['id'], flush=True)
        save(self.out / 'counters-done.json', {'inputs': len(self.selection), 'fingerprint': self.fingerprint})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=['smoke', 'pilot', 'run', 'counters'])
    parser.add_argument('--environment', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--cpu', type=int, required=True)
    parser.add_argument('--sibling', type=int, required=True)
    args = parser.parse_args()
    collector = Collector(args)
    if args.phase == 'smoke':
        for op in OPS:
            for n, size in [(1, 128), (48, 65536)]:
                case = make_case(op, n, size)
                collector.execute(case, 'check', f'smoke-{op}-{n}')
            print('PASS', op, flush=True)
        return
    if args.phase == 'pilot':
        collector.measure(make_case('any', 1, 128), 'pilot')
        return
    collector.run() if args.phase == 'run' else collector.counters()


if __name__ == '__main__':
    main()
