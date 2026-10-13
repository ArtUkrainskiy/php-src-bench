#!/usr/bin/env python3
# Per case: range over compilers of the median cycles ratio and of the instructions ratio to master.
#   ranges.py data.txt group[,group...] [cases-regex]
import collections, math, re, statistics as st, sys
def r2(x):
    """Two decimals, half up (1.125 -> 1.13)."""
    return f"{math.floor(x * 100 + 0.5) / 100:.2f}"

d = collections.defaultdict(lambda: collections.defaultdict(lambda: {'base': [], 'change': []}))
for l in open(sys.argv[1]):
    n, r, c, cy, i = l.split()
    d[c][n][r].append((int(cy), int(i)))
groups = sys.argv[2].split(',')
rx = re.compile(sys.argv[3] if len(sys.argv) > 3 else '.')
for c in d:
    if not rx.search(c):
        continue
    cyc, ins = [], []
    for g in groups:
        b, ch = d[c][g]['base'], d[c][g]['change']
        cyc.append(st.median(x[0] for x in ch) / st.median(x[0] for x in b))
        ins.append(st.median(x[1] for x in ch) / st.median(x[1] for x in b))
    print(f"{c:22} cycles {r2(min(cyc))}–{r2(max(cyc))}  instr {r2(min(ins))}–{r2(max(ins))}")
