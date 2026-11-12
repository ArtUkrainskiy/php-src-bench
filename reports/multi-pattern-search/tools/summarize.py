#!/usr/bin/env python3
"""Reduces raw timing processes to one record per (cell, compiler, mode).

    python3 tools/summarize.py <run dir> [<run dir>...] --out data/results.json

Every sample has the same pass's empty-call time ("noop": loop, closure call, result accounting)
subtracted first. Per process: the median over passes of each method, and the median over passes of
native/reference.
Reference: the existing method whose per-process medians have the lowest median. Reported values are
medians over processes; `spread` is the max/min ratio of the per-process native/reference values.
"""
import argparse
import json
import statistics as st
from pathlib import Path

AA_LIMIT, SPREAD_LIMIT, NOOP_SHARE_LIMIT = 1.5, 2.0, 30.0
PREEMPT_RATE = 20  # involuntary context switches per second of the process; the timer tick alone gives 5-12
# Replacement methods that are right only on some texts: str_replace() rescans its own output, PCRE in
# dictionary order may pick a shorter key, and several patterns in turn rescan the output. The bench.php that
# produced data/results.json also timed them; they never count as the reference.
NOT_UNIVERSAL = {'str_replace_input', 'str_replace_longest', 'pcre_input', 'pcre_input_512', 'pcre_input_1024',
                 'pcre_input_constant', 'pcre_prefix_512', 'pcre_prefix_1024'}


def universal(cell, method):
    return not ('replace' in cell.split('/')[1].split('.') and method in NOT_UNIVERSAL)


def summarize(cell, compiler, records, verify, cpu):
    out = []
    for mode in records[0]['result']['samples']:
        per = []
        for r in records:
            raw = r['result']['samples'][mode]
            per.append({m: [t - o for t, o in zip(v, raw['noop'])] for m, v in raw.items() if m != 'noop'})
        noop_ns = st.median(st.median(r['result']['samples'][mode]['noop']) for r in records)
        # A method left untimed in some process was estimated >5x slower than the best there; it cannot be the reference.
        common = {m for m in set.intersection(*(set(s) for s in per)) if universal(cell, m)}
        per = [{m: v for m, v in s.items() if m in common} for s in per]
        medians = {m: [st.median(s[m]) for s in per] for m in per[0]}
        existing = {m: st.median(v) for m, v in medians.items() if m not in ('native', 'native_aa')}
        reference = min(existing, key=existing.get)
        ratios = [st.median(a / b for a, b in zip(s['native'], s[reference])) for s in per]
        aas = [100 * (st.median(b / a for a, b in zip(s['native'], s['native_aa'])) - 1) for s in per]
        raw = [r['result']['samples'][mode] for r in records]
        raw_ratio = st.median(st.median(a / b for a, b in zip(s['native'], s[reference])) for s in raw)
        noop_share = 100 * noop_ns / st.median(st.median(s['native']) for s in raw)
        ratio = st.median(ratios)
        spread = 100 * (max(ratios) / min(ratios) - 1)
        flags = []
        if max(abs(a) for a in aas) > AA_LIMIT:
            flags.append('aa')
        if spread > SPREAD_LIMIT:
            flags.append('spread')
        if any(r['sibling_busy'] > 2 or r['steal_ticks'] or r.get('idle_timeout') for r in records):
            flags.append('load')
        if any(r['result'].get('involuntary_switches', 0) > PREEMPT_RATE * r['elapsed_s'] for r in records):
            flags.append('preempted')
        if noop_share > NOOP_SHARE_LIMIT or min(min(s['native']) for s in per) <= 0:
            flags.append('noop')
        out.append({'cell': cell, 'compiler': compiler, 'mode': mode, 'cpu': cpu, 'processes': len(records),
                    'native_us': st.median(medians['native']) / 1000, 'reference': reference,
                    'reference_us': existing[reference] / 1000,
                    'methods_us': {m: v / 1000 for m, v in existing.items()},
                    'ratio': ratio, 'change_percent': 100 * (ratio - 1), 'ratio_min': min(ratios), 'ratio_max': max(ratios),
                    'spread_percent': spread, 'aa_percent': st.median(aas), 'aa_max_percent': max(aas, key=abs),
                    'noop_ns': noop_ns, 'noop_share_percent': noop_share,
                    'change_without_noop_percent': 100 * (raw_ratio - 1),
                    'calls_per_pass': records[0]['result']['calls'][mode], 'passes': records[0]['result']['passes'][mode],
                    'untimed': {m: st.median(r['result']['per_call_estimate_ns'][mode][m] for r in records) / 1000
                                for m in sorted(set(records[0]['result']['methods']) - common - {'native'}) if universal(cell, m)},
                    'flags': flags, 'excluded': verify['excluded'], 'texts': records[0]['result']['texts']})
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('runs', nargs='+', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    results = []
    for run in args.runs:
        if not (run / 'done.json').exists():
            raise SystemExit(f'{run}: no done.json, the series has not finished')
        for compiler_dir in sorted((run / 'time').iterdir()):
            for cell_dir in sorted(p for p in compiler_dir.glob('*/*') if p.is_dir()):
                records = [json.loads(p.read_text()) for p in sorted(cell_dir.glob('p*.json'))]
                cell = f'{cell_dir.parent.name}/{cell_dir.name}'
                verify = json.loads((run / 'verify' / compiler_dir.name / f'{cell}.json').read_text())['result']
                results += summarize(cell, compiler_dir.name, records, verify, records[0]['cpu'])
    keys = [(r['cell'], r['compiler'], r['mode']) for r in results]
    if len(set(keys)) != len(keys):
        raise SystemExit('the same cell, compiler and mode in more than one run')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(results, indent=1) + '\n')
    flagged = [r for r in results if r['flags']]
    print(f'{len(results)} records, {len(flagged)} flagged')
    for r in flagged:
        print('  ', r['cell'], r['compiler'], r['mode'], r['flags'], f"spread {r['spread_percent']:.1f}% aa {r['aa_max_percent']:+.1f}%")


if __name__ == '__main__':
    main()
