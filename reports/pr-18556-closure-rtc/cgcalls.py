#!/usr/bin/env python3
"""cgcalls.py <a.cg> <b.cg> <requests> <regex> — per-request calls and inclusive Ir of functions matching regex:
(b - a) / requests, summed over all call sites. Plus per-request program total."""
import re, sys

def parse(path):
    names = {}
    calls = {}   # callee -> [calls, inclusive Ir]
    total = 0
    cfn = None
    pending = None
    def name(tok):
        m = re.match(r'\((\d+)\)(?:\s+(.*))?', tok)
        if not m:
            return tok
        if m.group(2):
            names[m.group(1)] = m.group(2)
        return names.get(m.group(1), tok)
    with open(path) as f:
        for line in f:
            if line.startswith('cfn='):
                cfn = name(line[4:].strip())
            elif line.startswith('calls='):
                pending = int(line[6:].split()[0])
            elif pending is not None and line[:1].isdigit() or (pending is not None and line[:1] in '+-*'):
                parts = line.split()
                ir = int(parts[1]) if len(parts) > 1 else 0
                c = calls.setdefault(cfn, [0, 0])
                c[0] += pending
                c[1] += ir
                pending = None
            elif line.startswith('fn='):
                name(line[3:].strip())
            elif line.startswith('summary:') or line.startswith('totals:'):
                total = int(line.split()[1])
    return calls, total

a, ta = parse(sys.argv[1])
b, tb = parse(sys.argv[2])
n = int(sys.argv[3])
rx = re.compile(sys.argv[4])
pt = (tb - ta) / n
print(f'program Ir per request {pt:,.0f}')
for k in sorted(set(a) | set(b)):
    if rx.search(k):
        ca, ia = a.get(k, [0, 0])
        cb, ib = b.get(k, [0, 0])
        dc, di = (cb - ca) / n, (ib - ia) / n
        if dc:
            print(f'{k:60s} calls {dc:8.1f}  incl Ir {di:12,.0f}  {100*di/pt:6.2f}%  per call {di/dc:8.0f}')
