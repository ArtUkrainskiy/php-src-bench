#!/usr/bin/env python3
"""Build a history chart of php-src's benchmark CI results (php/benchmarking-data) for the
last N master commits: an SVG with one panel per benchmark and a list of the largest steps."""
import json, os, sys, datetime

S = os.path.dirname(os.path.abspath(__file__))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
DATA = os.path.join(S, 'bdata')
NAMES = ['Zend/bench.php', 'Zend/bench.php JIT', 'Symfony Demo 2.2.3', 'Symfony Demo 2.2.3 JIT',
         'Wordpress 6.2', 'Wordpress 6.2 JIT']

# master history, newest first
log = []
for line in open(os.path.join(S, 'master_log.txt')):
    sha, ts, subj = line.rstrip('\n').split(' ', 2)
    log.append((sha, int(ts), subj))

rows = []
for sha, ts, subj in log:
    p = os.path.join(DATA, sha[:2], sha, 'summary.json')
    if not os.path.exists(p):
        continue
    try:
        d = json.load(open(p))
    except Exception:
        continue
    vals = {k: int(d[k]['instructions']) for k in NAMES if k in d}
    if len(vals) < len(NAMES):
        continue
    rows.append((sha, ts, subj, vals))
    if len(rows) >= N:
        break
rows.reverse()  # oldest first
print(f'{len(rows)} master commits with results, {datetime.date.fromtimestamp(rows[0][1])} .. {datetime.date.fromtimestamp(rows[-1][1])}')

# steps between consecutive benchmarked commits
steps = []
for i in range(1, len(rows)):
    for k in NAMES:
        a, b = rows[i-1][3][k], rows[i][3][k]
        steps.append(((b - a) / a * 100, k, rows[i][0][:10], rows[i][2]))
noise = sorted(abs(s[0]) for s in steps)
print(f'|delta| percentiles over {len(steps)} steps: p50 {noise[len(noise)//2]:.3f}%  p90 {noise[int(len(noise)*.9)]:.3f}%  p99 {noise[int(len(noise)*.99)]:.3f}%')
print('\nlargest steps:')
for d, k, sha, subj in sorted(steps, key=lambda s: -abs(s[0]))[:20]:
    print(f'  {d:+7.2f}%  {k:24s} {sha} {subj[:70]}')

# SVG: every panel in percent relative to the median of its series, same scale everywhere
import statistics
W, H, PADL, PADR, TOP = 1400, 200, 70, 30, 30
YMIN, YMAX = (-float(sys.argv[2]), float(sys.argv[2])) if len(sys.argv) > 2 else (-2.5, 2.5)
panels = len(NAMES)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H*panels+TOP}" font-family="sans-serif" font-size="12">',
       '<rect width="100%" height="100%" fill="white"/>']
def X(i): return PADL + i * (W - PADL - PADR) / max(1, len(rows) - 1)
for pi, k in enumerate(NAMES):
    ys = [r[3][k] for r in rows]
    med = statistics.median(ys)
    pct = [(v - med) / med * 100 for v in ys]
    y0 = pi * H + TOP
    plot_h = H - 50
    def Y(p): return y0 + plot_h - (min(max(p, YMIN), YMAX) - YMIN) / (YMAX - YMIN) * plot_h
    svg.append(f'<text x="{PADL}" y="{y0-8}" font-weight="bold">{k}</text>'
               f'<text x="{PADL+260}" y="{y0-8}" fill="#555">median {med/1e6:,.1f}M instructions per request; range {min(pct):+.2f}% .. {max(pct):+.2f}%</text>')
    g = YMIN
    while g <= YMAX + 1e-9:
        col = '#999' if abs(g) < 1e-9 else '#e5e5e5'
        svg.append(f'<line x1="{PADL}" y1="{Y(g):.1f}" x2="{W-PADR}" y2="{Y(g):.1f}" stroke="{col}"/>')
        svg.append(f'<text x="{PADL-6}" y="{Y(g)+4:.1f}" text-anchor="end" fill="#666" font-size="11">{g:+.1f}%</text>')
        g += 0.5 if YMAX <= 3 else (1 if YMAX <= 8 else 5)
    pts = ' '.join(f'{X(i):.1f},{Y(p):.1f}' for i, p in enumerate(pct))
    svg.append(f'<polyline points="{pts}" fill="none" stroke="#1f77b4" stroke-width="1.2"/>')
    last = None; last_label_x = -1000
    for i, r in enumerate(rows):
        if len(rows) > 1000:
            m = datetime.date.fromtimestamp(r[1]).strftime('%Y-%m'); wk = m
        else:
            m = datetime.date.fromtimestamp(r[1]).strftime('%Y-%m-%d'); wk = datetime.date.fromtimestamp(r[1]).isocalendar()[1]
        if wk != last:
            last = wk
            svg.append(f'<line x1="{X(i):.1f}" y1="{y0}" x2="{X(i):.1f}" y2="{y0+plot_h}" stroke="#f3f3f3"/>')
            if pi == 0 or True:
                if 'last_label_x' not in dir() or X(i) - last_label_x >= 58 or i == 0:
                    svg.append(f'<text x="{X(i)+2:.1f}" y="{y0+plot_h+14}" fill="#888" font-size="10">{m}</text>')
                    last_label_x = X(i)
    last_label_x = -1000
svg.append('</svg>')
out = os.path.join(S, f'bench_history_{N}.svg')
open(out, 'w').write('\n'.join(svg))
print('\nwrote', out)
