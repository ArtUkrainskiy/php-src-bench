#!/usr/bin/env python3
"""Two summaries of a bench compare series of suite.php, from the medians over the passes.

1. FETCH_OBJ against FETCH_ASSOC of the same rows in one build: the ratio of the median cycles per call.
   The two cases run at different moments of the series, so this is a ratio of medians, not per pass.
2. What the change saves per row: master minus change, instructions and cycles per call divided by 100 rows.

Usage: gap.py series.json
"""
import collections
import json
import statistics
import sys

ROWS = 100

with open(sys.argv[1]) as f:
    series = json.load(f)
calls = {case: info['n'] for case, info in series['cases'].items()}
per_call = collections.defaultdict(list)
for group, side, case, cyc, ins, empty_cyc, empty_ins in series['rows']:
    per_call[(group, side, case)].append(((cyc - empty_cyc) / calls[case], (ins - empty_ins) / calls[case]))
groups = [g['name'] for g in series['groups'] if g['a'] != g['b']]


def median(group, side, case, i):
    return statistics.median(x[i] for x in per_call[(group, side, case)])


print('FETCH_OBJ against FETCH_ASSOC, cycles')
print(f"{'case':38s} {'compiler':9s} {'master':>7s} {'change':>7s}")
for obj, assoc in [('fetchAll OBJ', 'fetchAll ASSOC'), ('prepared OBJ', 'prepared ASSOC')]:
    for case in sorted(c for c in calls if c.startswith(obj + ' @ ')):
        other = f"{assoc} @ {case.split(' @ ')[1]}"
        if other not in calls:
            continue
        for group in groups:
            cells = [f'{100 * (median(group, side, case, 0) / median(group, side, other, 0) - 1):+4.0f}%' for side in 'ab']
            print(f'{case:38s} {group:9s} {cells[0]:>7s} {cells[1]:>7s}')

print()
print('Saved per row by the change (master minus change)')
print(f"{'case':38s} {'compiler':9s} {'instructions':>12s} {'cycles':>7s}")
for case in sorted(c for c in calls if 'OBJ' in c):
    for group in groups:
        saved = [(median(group, 'a', case, i) - median(group, 'b', case, i)) / ROWS for i in (1, 0)]
        print(f'{case:38s} {group:9s} {saved[0]:12.0f} {saved[1]:7.0f}')
