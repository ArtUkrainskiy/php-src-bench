#!/usr/bin/env python3
"""Runs benchmark cells on one CPU: output checks, then rounds of fresh processes, then rechecks.

    python3 tools/run.py --out <dir> --cpu 15 --sibling 31 --php gcc15=<php> --php clang21=<php> <cell.json>...

Every (cell, compiler) gets one `verify` run and `--processes` timing processes; process k of a cell runs
in round k, so processes of one cell are spread over the whole queue. Results are written as they finish;
rerunning the same command resumes. Cells whose processes disagree or whose A/A check fails get
`--recheck` more processes.
"""
import argparse
import datetime
import json
import os
import statistics
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INI = ['-n', '-d', 'memory_limit=-1', '-d', 'opcache.enable_cli=1', '-d', 'opcache.file_update_protection=0',
       '-d', 'opcache.jit=disable', '-d', 'pcre.jit=1']


def cpu_ticks(cpu):
    for line in Path('/proc/stat').read_text().splitlines():
        if line.startswith(f'cpu{cpu} '):
            fields = list(map(int, line.split()[1:9]))
            return sum(fields), fields[3] + fields[4]
    raise SystemExit(f'cpu{cpu} not found')


def busy(before, after):
    total = after[0] - before[0]
    return 100 * (1 - (after[1] - before[1]) / total) if total else 0.0


def wait_idle(cpus, limit=5.0, patience=30.0):
    """Waits until every CPU in `cpus` is at most `limit` percent busy over 250 ms; returns the last reading."""
    started = time.monotonic()
    while True:
        before = [cpu_ticks(c) for c in cpus]
        time.sleep(0.25)
        reading = [busy(b, cpu_ticks(c)) for b, c in zip(before, cpus)]
        if max(reading) <= limit or time.monotonic() - started > patience:
            return reading, max(reading) > limit


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value) + '\n')
    tmp.replace(path)


def run(args, php, cell, extra):
    cmd = ['taskset', '-c', str(args.cpu), php, *INI, str(ROOT / 'tools/bench.php'), str(cell), *extra]
    idle, waited = wait_idle([args.cpu, args.sibling])
    sibling_before, steal_before = cpu_ticks(args.sibling), Path('/proc/stat').read_text().split()[8]
    started = time.monotonic()
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)
    record = {'elapsed_s': round(time.monotonic() - started, 3), 'idle_before': idle, 'idle_timeout': waited,
              'sibling_busy': busy(sibling_before, cpu_ticks(args.sibling)),
              'steal_ticks': int(Path('/proc/stat').read_text().split()[8]) - int(steal_before),
              'cpu': args.cpu, 'sibling': args.sibling,
              'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')}
    if result.returncode:
        raise SystemExit(f'{cell}: {result.stderr.strip()[-2000:]}')
    record['result'] = json.loads(result.stdout)
    return record


def flagged(records, aa_limit=1.5, spread_limit=2.0):
    """True when any mode has |A/A| above aa_limit or a native/reference ratio spread above spread_limit."""
    for mode in records[0]['result']['samples']:
        ratios, aas = [], []
        for rec in records:
            raw = rec['result']['samples'][mode]
            samples = {m: [t - o for t, o in zip(v, raw['noop'])] for m, v in raw.items() if m != 'noop'}
            medians = {m: statistics.median(v) for m, v in samples.items()}
            reference = min((m for m in medians if m not in ('native', 'native_aa')), key=medians.get)
            ratios.append(statistics.median(a / b for a, b in zip(samples['native'], samples[reference])))
            aas.append(100 * (statistics.median(b / a for a, b in zip(samples['native'], samples['native_aa'])) - 1))
        if max(abs(a) for a in aas) > aa_limit or 100 * (max(ratios) / min(ratios) - 1) > spread_limit:
            return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cells', nargs='+', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--cpu', type=int, required=True)
    parser.add_argument('--sibling', type=int, required=True)
    parser.add_argument('--php', action='append', required=True, help='<label>=<php binary>')
    parser.add_argument('--processes', type=int, default=3)
    parser.add_argument('--recheck', type=int, default=2)
    parser.add_argument('--passes', type=int, default=5)
    args = parser.parse_args()
    phps = dict(item.split('=', 1) for item in args.php)
    cells = [c.resolve() for c in args.cells]
    key = lambda cell: f'{cell.parent.name}/{cell.stem}'
    total = len(cells) * len(phps)
    save(args.out / 'run.json', {'argv': sys.argv[1:], 'ini': INI, 'pid': os.getpid(),
                                 'php': {label: subprocess.run([php, '-v'], capture_output=True, text=True).stdout.splitlines()[0]
                                         for label, php in phps.items()}})

    for i, cell in enumerate(cells):
        for label, php in phps.items():
            target = args.out / 'verify' / label / f'{key(cell)}.json'
            if not target.exists():
                save(target, run(args, php, cell, ['verify']))
        print(f'verify {i + 1}/{len(cells)} {key(cell)}', flush=True)

    def timing(cell, label, process):
        target = args.out / 'time' / label / key(cell) / f'p{process}.json'
        if target.exists():
            return json.loads(target.read_text())
        methods = json.loads((args.out / 'verify' / label / f'{key(cell)}.json').read_text())['result']['eligible']
        # Every process measures the same text blocks; processes differ only in placement and timing noise.
        record = run(args, phps[label], cell, ['time', str(args.passes), '0', ','.join(methods)])
        save(target, record)
        return record

    for process in range(1, args.processes + 1):
        done = 0
        for cell in cells:
            for label in phps:
                timing(cell, label, process)
                done += 1
                if done % 20 == 0 or done == total:
                    print(f'process {process}/{args.processes}: {done}/{total}', flush=True)
    rechecked = 0
    for cell in cells:
        for label in phps:
            records = [timing(cell, label, p) for p in range(1, args.processes + 1)]
            if flagged(records):
                rechecked += 1
                for p in range(args.processes + 1, args.processes + args.recheck + 1):
                    timing(cell, label, p)
    save(args.out / 'done.json', {'cells': len(cells), 'compilers': list(phps), 'rechecked': rechecked,
                                  'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')})
    print(f'done: {len(cells)} cells, {rechecked} (cell, compiler) pairs rechecked', flush=True)


if __name__ == '__main__':
    main()
