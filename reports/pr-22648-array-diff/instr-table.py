#!/usr/bin/env python3
# Extra instructions per call relative to master (median of the change runs minus median of the
# master runs), lowest and highest over the four compilers, for each variant.
#   instr-table.py DATA 'pr:PR,peek:...' 'case=label' ...
import collections, statistics as st, sys
data, variants, rows = sys.argv[1], [v.split(":", 1) for v in sys.argv[2].split(",")], [r.split("=", 1) for r in sys.argv[3:]]
d = collections.defaultdict(list)
for line in open(data):
    g, role, case, cyc, ins = line.split()
    d[(g, role, case)].append(int(ins))
def fmt(x):
    x = round(x) if abs(x) < 100 else (round(x, -1) if abs(x) < 1000 else round(x, -2))
    s = f"{abs(int(x)):,}"
    return "0" if x == 0 else ("+" if x > 0 else "−") + s
print("| call | " + " | ".join(n for _, n in variants) + " |")
print("|---|" + "--:|" * len(variants))
for case, label in rows:
    cells = []
    for v, _ in variants:
        ds = [st.median(d[(f"{c}-{v}", "change", case)]) - st.median(d[(f"{c}-{v}", "base", case)]) for c in ("g13", "g14", "c18", "c20")]
        lo, hi = min(ds), max(ds)
        cells.append(fmt(lo) if fmt(lo) == fmt(hi) else f"{fmt(lo)} … {fmt(hi)}")
    print(f"| {label} | " + " | ".join(cells) + " |")
