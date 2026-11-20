#!/usr/bin/env python3
"""cgcallees.py <a.cg> <b.cg> <requests> <fn> — per-request self Ir of <fn> and inclusive Ir of each callee: (b - a) / requests."""
import re, sys
def parse(path, target):
    names = {}; fn = cfn = None; pending = None; self_ir = 0; callees = {}
    def name(tok):
        m = re.match(r'\((\d+)\)(?:\s+(.*))?', tok)
        if not m: return tok
        if m.group(2): names[m.group(1)] = m.group(2)
        return names.get(m.group(1), tok)
    for line in open(path):
        if line.startswith('fn='): fn = name(line[3:].strip()); pending = None
        elif line.startswith('cfn='): cfn = name(line[4:].strip())
        elif line.startswith('calls='): pending = int(line[6:].split()[0])
        elif line[:1].isdigit() or line[:1] in '+-*':
            p = line.split(); ir = int(p[1]) if len(p) > 1 else 0
            if fn == target:
                if pending is not None:
                    c = callees.setdefault(cfn, [0, 0]); c[0] += pending; c[1] += ir
                else:
                    self_ir += ir
            pending = None
    return self_ir, callees
n = int(sys.argv[3]); t = sys.argv[4]
sa, ca = parse(sys.argv[1], t); sb, cb = parse(sys.argv[2], t)
print(f'{t}: self Ir/request {(sb-sa)/n:,.0f}')
for k in sorted(set(ca) | set(cb), key=lambda k: -(cb.get(k,[0,0])[1]-ca.get(k,[0,0])[1])):
    dc = (cb.get(k,[0,0])[0]-ca.get(k,[0,0])[0])/n; di = (cb.get(k,[0,0])[1]-ca.get(k,[0,0])[1])/n
    if dc: print(f'  {k:50s} calls {dc:7.1f} incl Ir {di:10,.0f}  per call {di/dc:6.0f}')
