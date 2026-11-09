#!/usr/bin/env python3
"""Measure prepared calls on the complete 4 by 4 input grid."""
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
            collector.execute(study.make_case(op, 8, 128), 'check', 'smoke-' + op)
            print('PASS', op, flush=True)
        return
    if args.phase == 'pilot':
        collector.measure(study.make_case('any', 8, 128), 'pilot')
        return
    if args.phase == 'counters':
        collector.counters()
        return
    rows = []
    for size in collector.plan['subject_sizes']:
        for n in collector.plan['dictionary_sizes']:
            for op in study.OPS:
                rows.append(collector.measure(study.make_case(op, n, size), 'prepared-grid'))
    for op in study.OPS:
        winners = [r for r in rows if r['case']['bytes'] == 128 and r['case']['operation'] == op
                   and r['scopes']['prepared']['state'] == 'win']
        if winners:
            winner = min(winners, key=lambda r:r['case']['keys'])
            collector.measure(study.make_case(op, winner['case']['keys'], 128, 'comments'), '128-byte:second-background')
    study.save(args.output / 'time-done.json', {'inputs': len(collector.selection), 'fingerprint': collector.fingerprint})
    print('Prepared grid timing complete:', len(collector.selection), 'inputs', flush=True)


if __name__ == '__main__':
    main()
