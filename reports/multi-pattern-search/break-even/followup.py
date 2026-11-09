#!/usr/bin/env python3
"""Bound quality confirmations and remaining gap probes before counters."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import study

ROOT = Path(__file__).resolve().parent


def points(collector):
    result = {p.stem: study.read(p) for p in (collector.out / 'timings').glob('*.json')}
    for p in (collector.out / 'confirmations').glob('*.json'):
        row = study.read(p)
        if all(s['qualified'] for s in row['scopes'].values()):
            result[p.stem] = row
    return list(result.values())


def groups(rows, plan):
    for axis, mode in [('keys', 'prepared'), ('length', 'oneshot')]:
        field = 'keys' if axis == 'keys' else 'bytes'
        grid = plan['dictionary_sizes'] if axis == 'keys' else plan['subject_sizes']
        for op in plan['operations']:
            group = sorted([r for r in rows if r['case']['background'] == 'technical'
                and r['case']['operation'] == op and r['case']['condition'] == ('absent' if op == 'any' else 'single')
                and r['case']['bytes' if axis == 'keys' else 'keys'] == (4096 if axis == 'keys' else 48)], key=lambda r:r['case'][field])
            winners = [r for r in group if r['scopes'][mode]['state'] == 'win']
            upper = winners[0]['case'][field] if winners else grid[-1]
            losers = [r for r in group if r['scopes'][mode]['state'] == 'loss' and r['case'][field] < upper]
            lower = losers[-1]['case'][field] if losers else 0
            yield axis, mode, op, field, grid, group, lower, upper


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--environment', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--cpu', type=int, required=True)
    parser.add_argument('--sibling', type=int, required=True)
    args = parser.parse_args()
    collector = study.Collector(args)
    assert (args.output / 'time-done.json').exists()
    policy = {'max_quality_confirmations': 6, 'max_gap_probes': 4,
              'total_distinct_input_limit': collector.plan['max_measured_inputs'],
              'collector_fingerprint': collector.fingerprint,
              'followup_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'rule': 'First confirm flagged points inside a reported boundary; then probe the widest remaining candidate-grid gap. Never select by fastest observation.'}
    study.save(args.output / 'followup-policy.json', policy)
    attempted = set(p.stem for p in (args.output / 'confirmations').glob('*.json'))
    for _ in range(6 - len(attempted)):
        candidates = []
        for axis, mode, op, field, grid, group, lower, upper in groups(points(collector), collector.plan):
            for row in group:
                if lower < row['case'][field] <= upper and row['scopes'][mode]['state'] == 'flagged' and row['case']['id'] not in attempted:
                    candidates.append(row)
        if not candidates:
            break
        original = candidates[0]
        case = original['case']
        attempted.add(case['id'])
        tag = 'confirmation-' + case['id']
        raw = collector.execute(case, 'time', tag)
        result = collector.summarize(raw)
        row = {**original, **result, 'capture': tag + '.json',
               'attempts': original['attempts'] + [{**result, 'capture': tag + '.json'}],
               'confirmation_policy': 'one additional capture for an uncertain boundary input'}
        study.save(args.output / 'confirmations' / (case['id'] + '.json'), row)
        print('confirmation', case['id'], {m:s['state'] for m,s in result['scopes'].items()}, flush=True)
    def validate_winners():
        for axis, mode, op, field, grid, group, lower, upper in groups(points(collector), collector.plan):
            winner = next((r for r in group if r['scopes'][mode]['state'] == 'win'), None)
            if not winner:
                continue
            c = winner['case']
            other = study.make_case(op, c['keys'], c['bytes'], 'comments', c['condition'])
            if len(collector.selection) >= collector.plan['max_measured_inputs'] and not (args.output / 'timings' / (other['id'] + '.json')).exists():
                continue
            collector.measure(other, 'followup:second-background')
    validate_winners()
    probe_log = study.read(args.output / 'gap-probes.json') if (args.output / 'gap-probes.json').exists() else []
    for _ in range(4 - len(probe_log)):
        if len(collector.selection) + 2 > collector.plan['max_measured_inputs']:
            break
        candidates = []
        for axis, mode, op, field, grid, group, lower, upper in groups(points(collector), collector.plan):
            has_upper = any(r['case'][field] == upper and r['scopes'][mode]['state'] == 'win' for r in group)
            if not lower or not has_upper:
                continue
            measured = {r['case'][field] for r in group}
            remaining = [x for x in grid if lower < x < upper and x not in measured]
            if remaining:
                candidates.append((math.log2(upper / lower), axis, op, remaining[(len(remaining) - 1) // 2]))
        if not candidates:
            break
        _, axis, op, value = max(candidates)
        case = study.make_case(op, value if axis == 'keys' else 48, 4096 if axis == 'keys' else value)
        probe_log.append({'axis': axis, 'operation': op, 'value': value, 'case': case['id']})
        study.save(args.output / 'gap-probes.json', probe_log)
        collector.measure(case, 'followup:widest-boundary-gap')
        validate_winners()
    study.save(args.output / 'time-done.json', {'inputs': len(collector.selection), 'fingerprint': collector.fingerprint,
                                               'bounded_followup': True})
    print('Follow-up complete:',len(collector.selection),'distinct inputs',flush=True)


if __name__ == '__main__':
    main()
