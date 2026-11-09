#!/usr/bin/env python3
"""256-byte slice: at most 33 short inputs and one count-baseline control."""
import argparse
from pathlib import Path

import study

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=['smoke', 'pilot', 'run', 'counters'])
    parser.add_argument('--environment', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--cpu', type=int, required=True)
    parser.add_argument('--sibling', type=int, required=True)
    args = parser.parse_args()
    collector = study.Collector(args)
    assert study.sha(Path(__file__)) == collector.plan['schedule_sha256']
    if args.phase == 'smoke':
        for op in study.OPS:
            for n in [1, 48]:
                collector.execute(study.make_case(op, n, 256), 'check', f'smoke-{op}-{n}')
            print('PASS', op, flush=True)
        return
    if args.phase == 'pilot':
        collector.measure(study.make_case('any', 1, 256), 'pilot')
        return
    if args.phase == 'counters':
        collector.counters()
        return
    all_rows = {}
    for op in study.OPS:
        rows = {}
        for n in collector.plan['initial_dictionary_sizes']:
            rows[n] = collector.measure(study.make_case(op, n, 256), '256-byte:initial-grid')
        # One extra point per operation, only between a non-win and a confirmed win.
        gaps = []
        for mode in ['prepared', 'oneshot']:
            for low, high in zip(sorted(rows), sorted(rows)[1:]):
                inside = [n for n in collector.plan['dictionary_sizes'] if low < n < high and n not in rows]
                if inside and rows[low]['scopes'][mode]['state'] != 'win' and rows[high]['scopes'][mode]['state'] == 'win':
                    gaps.append((len(inside), inside[(len(inside) - 1) // 2]))
        if gaps:
            n = max(gaps)[1]
            rows[n] = collector.measure(study.make_case(op, n, 256), '256-byte:boundary-refinement')
        all_rows[op] = rows
    for condition in ['early', 'middle', 'late']:
        collector.measure(study.make_case('any', 48, 256, condition=condition), '256-byte:presence-control')
    for op, rows in all_rows.items():
        winners = [(n, r) for n, r in rows.items() if r['scopes']['prepared']['state'] == 'win']
        if winners:
            n, _ = min(winners)
            collector.measure(study.make_case(op, n, 256, background='comments'), '256-byte:second-background')
    collector.measure(study.make_case('count', 48, 4096), 'count-baseline:4KiB-crosscheck')
    study.save(args.output / 'time-done.json', {'inputs': len(collector.selection), 'fingerprint': collector.fingerprint})
    print('256-byte timing complete:', len(collector.selection), 'inputs', flush=True)


if __name__ == '__main__':
    main()
