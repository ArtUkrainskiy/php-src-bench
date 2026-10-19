#!/usr/bin/env python3
# Medians and per-pass ratios from measure.sh result files.
#   aggregate.py results-*.txt
import re, sys, statistics as st
for path in sys.argv[1:]:
    rows = {}
    rps = {}
    cyc = {}
    ins = {}
    for line in open(path):
        m = re.match(r'pass (\d+) (\S+) statistics (on|off): \d+ requests, ([\d.]+) req/s.* ([\d.]+) ms CPU per request(?:, (\d+) cycles, (\d+) instructions)?', line)
        if m:
            p, b, s, r, c = int(m[1]), m[2], m[3], float(m[4]), float(m[5])
            rows.setdefault((b, s), {})[p] = c
            rps.setdefault((b, s), {})[p] = r
            if m[6]:
                cyc.setdefault((b, s), {})[p] = int(m[6])
                ins.setdefault((b, s), {})[p] = int(m[7])
    print(f'== {path}')
    for k, v in sorted(rows.items()):
        vals = [v[p] for p in sorted(v)]
        print(f'{k[0]:22} {k[1]:3}  median {st.median(vals):.4f} ms  [{min(vals):.4f}–{max(vals):.4f}]  req/s median {st.median(rps[k].values()):.0f}  passes {len(vals)}')
    for name, d in (('cycles', cyc), ('instructions', ins)):
        for k, v in sorted(d.items()):
            vals = list(v.values())
            print(f'{k[0]:22} {k[1]:3}  {name} per request median {st.median(vals):.0f}  [{min(vals)}–{max(vals)}]')
    def ratio(d, a, b):
        r = [d[a][p] / d[b][p] for p in d[a] if p in d[b]]
        return f'{(st.median(r) - 1) * 100:+.1f}% [{(min(r) - 1) * 100:+.1f}…{(max(r) - 1) * 100:+.1f}]'
    M = next(b for b, _ in rows if 'master' in b)
    A = next(b for b, _ in rows if 'master' not in b)
    for name, d in (('cpu', rows), ('cycles', cyc), ('instructions', ins)):
        if not d:
            continue
        print(f'[{name}] patch on  / master on :', ratio(d, (A, 'on'), (M, 'on')))
        print(f'[{name}] master on / master off:', ratio(d, (M, 'on'), (M, 'off')))
        print(f'[{name}] patch on  / patch off :', ratio(d, (A, 'on'), (A, 'off')))
        print(f'[{name}] patch on  / master off:', ratio(d, (A, 'on'), (M, 'off')))
        print(f'[{name}] patch off / master off:', ratio(d, (A, 'off'), (M, 'off')))
