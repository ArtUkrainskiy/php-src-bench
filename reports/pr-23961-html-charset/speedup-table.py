#!/usr/bin/env python3
"""Comparison table for public texts (PR comments, PR descriptions, php-src-bench reports).

Input: pairs-run.sh output, lines `<group> <base|change> <case> <cycles> <instructions>`.
Output: Markdown table — master's CPU cycles per call (first group) and, per group, the change
in cycles relative to master in percent: "−25%" (fewer cycles, faster), "+4%" (slower), "0%".
The value is the median over passes of (PR cycles / master cycles − 1), rounded half up to a
whole percent. The caption over the table must say "negative = fewer cycles (faster)".

  speedup-table.py [--full] DATA 'g13:GCC 13.3,g14:GCC 14.2,c18:clang 18.1,c20:clang 20.1' \
      'bin2hex-16=`bin2hex()`, 16 bytes' 'hex2bin-16=`hex2bin()`, 32 hex characters' ...

--full adds the range over passes to each cell, "−25% (−26 … −21)", and a last column with the
change in instructions, range over the groups: for the full table of a report.
"""
import collections, math, statistics as st, sys


def num(r):
    v = math.floor((r - 1) * 100 + 0.5)
    return f"+{v}" if v > 0 else (f"−{-v}" if v < 0 else "0")


args = sys.argv[1:]
full = args[0] == "--full"
if full:
    args = args[1:]
data, groups, rows = args[0], [g.split(":", 1) for g in args[1].split(",")], [r.split("=", 1) for r in args[2:]]
cyc = collections.defaultdict(lambda: collections.defaultdict(lambda: {"base": [], "change": []}))
ins = collections.defaultdict(lambda: collections.defaultdict(lambda: {"base": [], "change": []}))
for line in open(data):
    n, role, case, cy, i = line.split()
    cyc[case][n][role].append(int(cy))
    ins[case][n][role].append(int(i))

first = groups[0]
head = f"| call | master, CPU cycles per call ({first[1]}) | " + " | ".join(g[1] for g in groups) + " |"
print(head + (" instructions |" if full else ""))
print("|---|--:|" + "--:|" * len(groups) + ("--:|" if full else ""))
for case, label in rows:
    if case not in cyc:
        sys.exit(f"no case {case} in {data}")
    cells, ir = [], []
    for g, _ in groups:
        b = st.median(cyc[case][g]["base"])
        rs = sorted(x / b for x in cyc[case][g]["change"])
        cell = num(st.median(rs)) + "%"
        if full:
            cell += f" ({num(rs[0])} … {num(rs[-1])})"
        cells.append(cell)
        ir.append(st.median(ins[case][g]["change"]) / st.median(ins[case][g]["base"]))
    line = f"| {label} | {st.median(cyc[case][first[0]]['base']):,.0f} | " + " | ".join(cells) + " |"
    if full:
        lo, hi = num(min(ir)), num(max(ir))
        line += f" {lo}%" + ("" if lo == hi else f" … {hi}%") + " |"
    print(line)
