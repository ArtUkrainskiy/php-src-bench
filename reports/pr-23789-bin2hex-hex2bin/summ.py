#!/usr/bin/env python3
# Median cycles ratio [range of passes] / instructions ratio per case and group.
#   summ.py file.txt [file.txt ...]
import collections, statistics as st, sys
for f in sys.argv[1:]:
    d = collections.defaultdict(lambda: collections.defaultdict(lambda: {'base': [], 'change': []}))
    ins = collections.defaultdict(lambda: collections.defaultdict(lambda: {'base': [], 'change': []}))
    names = []
    for l in open(f):
        n, r, c, cy, i = l.split()
        if n not in names:
            names.append(n)
        d[c][n][r].append(int(cy))
        ins[c][n][r].append(int(i))
    print('==', f)
    print(f"{'case':30}" + ''.join(f"{n:>24}" for n in names))
    for c in d:
        row = f"{c:30}"
        for n in names:
            b = st.median(d[c][n]['base'])
            ch = sorted(x / b for x in d[c][n]['change'])
            ir = st.median(ins[c][n]['change']) / st.median(ins[c][n]['base'])
            row += f"{st.median(ch):6.2f} [{ch[0]:.2f}-{ch[-1]:.2f}] {ir:5.2f}"
        print(row)
