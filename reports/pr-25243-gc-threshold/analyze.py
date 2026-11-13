#!/usr/bin/env python3
"""Summarizes a series CSV written by series.sh: one row per case, compiler and memory limit.

Usage: analyze.py <series.csv> [build]   (build defaults to 25243; it is compared with master)

Change = median over rounds of (build / master in the same round) - 1; brackets show min..max of these ratios.
Metrics: wall time (the script's own timer), cycles and instructions (perf stat), peak RSS (/usr/bin/time).
A run that failed (non-zero exit) without a memory limit is skipped; runs that hit memory_limit are
counted in the fatal column, and their time, cycles and instructions are not compared.
"""
import csv
import re
import statistics
import sys
from collections import defaultdict

PR = sys.argv[2] if len(sys.argv) > 2 else '25243'
rows = defaultdict(dict)  # (case, cc, limit) -> round -> build -> fields
order = []
for r in csv.reader(open(sys.argv[1])):
    rnd, cc, build, script, args, limit, rc, rss, cyc, ins = r[:10]
    res = ','.join(r[10:])
    fatal = 'FATAL' in res
    if int(rc) != 0 and not fatal:
        print(f'skipped failed run: {r[:7]}', file=sys.stderr)
        continue
    case = args.replace(':', ' ') if script == 'mem.php' else ('orm' if script == 'orm' else args)
    key = (case, cc, limit)
    if key not in order:
        order.append(key)
    m = re.search(r'time[=;]+([0-9.]+)', res) or re.search(r'wall;([0-9.]+)', res)
    t = re.search(r'threshold[=;]+([0-9]+)', res)
    rows[key].setdefault(rnd, {})[build] = {
        'fatal': fatal,
        'rss': int(rss) / 1024,
        'cyc': None if fatal or not cyc.isdigit() else int(cyc),
        'ins': None if fatal or not ins.isdigit() else int(ins),
        'time': float(m.group(1)) if m and not fatal else None,
        'thr': t.group(1) if t else '—',
    }


def change(key, metric):
    ratios, base = [], []
    for b in rows[key].values():
        if 'master' in b and PR in b and b['master'][metric] and b[PR][metric]:
            ratios.append(b[PR][metric] / b['master'][metric])
            base.append(b['master'][metric])
    if not ratios:
        return '—', '—', 0
    fmt = {'time': '{:.3f}', 'rss': '{:.0f}', 'cyc': '{:.2f}', 'ins': '{:.2f}'}[metric]
    scale = 1e9 if metric in ('cyc', 'ins') else 1
    med = statistics.median(ratios) - 1
    return (fmt.format(statistics.median(base) / scale),
            f'{med * 100:+.1f}% ({(min(ratios) - 1) * 100:+.1f}…{(max(ratios) - 1) * 100:+.1f})', len(ratios))


print(f'{PR} against master; change = median of per-round ratios, brackets = min…max\n')
print(f'| case | cc | memory_limit | pairs | time master, s | time {PR} | cycles master, G | cycles {PR} '
      f'| instructions {PR} | RSS master, MiB | RSS {PR} | threshold master/{PR} | fatal master/{PR} |')
print('|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|')
for key in order:
    case, cc, limit = key
    tm, tc, n = change(key, 'time')
    cm, cc_, _ = change(key, 'cyc')
    _, ic, _ = change(key, 'ins')
    rm, rc, nr = change(key, 'rss')
    fm = sum(b['master']['fatal'] for b in rows[key].values() if 'master' in b)
    fp = sum(b[PR]['fatal'] for b in rows[key].values() if PR in b)
    thm = next((b['master']['thr'] for b in rows[key].values() if 'master' in b), '—')
    thp = next((b[PR]['thr'] for b in rows[key].values() if PR in b), '—')
    print(f'| {case} | {cc} | {limit} | {max(n, nr)} | {tm} | {tc} | {cm} | {cc_} | {ic} | {rm} | {rc} | {thm}/{thp} | {fm}/{fp} |')
