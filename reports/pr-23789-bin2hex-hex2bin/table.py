#!/usr/bin/env python3
# Markdown table: master cycles per call (GCC 13), cycles ratio per compiler [range of passes], instructions ratio range.
#   table.py data.txt g13,g14,c18,c20
import collections, math, statistics as st, sys
def r2(x):
    """Two decimals, half up (1.125 -> 1.13)."""
    return f"{math.floor(x * 100 + 0.5) / 100:.2f}"

d = collections.defaultdict(lambda: collections.defaultdict(lambda: {'base': [], 'change': []}))
for l in open(sys.argv[1]):
    n, r, c, cy, i = l.split()
    d[c][n][r].append((int(cy), int(i)))
gs = sys.argv[2].split(',')
names = {'g13': 'GCC 13.3', 'g14': 'GCC 14.2', 'c18': 'clang 18.1', 'c20': 'clang 20.1'}
print('| case | master, cycles (GCC 13) | ' + ' | '.join(names.get(g.rstrip('t'), g) for g in gs) + ' | instructions |')
print('|---|--:|' + '--:|' * len(gs) + '--:|')
for c in d:
    b0 = st.median(x[0] for x in d[c][gs[0]]['base'])
    cells, ins = [], []
    for g in gs:
        b = st.median(x[0] for x in d[c][g]['base'])
        rs = sorted(x[0] / b for x in d[c][g]['change'])
        cells.append(f"{r2(st.median(rs))} [{r2(rs[0])}–{r2(rs[-1])}]")
        ins.append(st.median(x[1] for x in d[c][g]['change']) / st.median(x[1] for x in d[c][g]['base']))
    print(f"| {c} | {b0:,.0f} | " + ' | '.join(cells) + f" | {r2(min(ins))}–{r2(max(ins))} |")
