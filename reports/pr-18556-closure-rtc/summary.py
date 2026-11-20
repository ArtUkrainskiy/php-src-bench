#!/usr/bin/env python3
"""summary.py <dir>: one line per <name>.sum: median of the per-pass B/A ratios of cycles (min..max) and of
instructions, as percent change (negative = B is faster), plus the mean cycles per request of A."""
import glob, os, statistics, sys

for path in sorted(glob.glob(os.path.join(sys.argv[1], '*.sum'))):
    cyc, ins, a = [], [], []
    for line in open(path):
        f = line.split()
        if len(f) < 12 or f[0] != 'pass':
            continue
        a.append(float(f[3])); cyc.append(float(f[9])); ins.append(float(f[11]))
    if not cyc:
        continue
    pct = lambda r: (r - 1) * 100
    print(f'{os.path.basename(path)[:-4]:34s} A {statistics.mean(a):12,.0f} cyc/req  cycles {pct(statistics.median(cyc)):+6.2f}% '
          f'({pct(min(cyc)):+.2f}..{pct(max(cyc)):+.2f})  instructions {pct(statistics.median(ins)):+6.2f}%  passes {len(cyc)}')
