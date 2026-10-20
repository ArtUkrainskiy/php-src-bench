# Paired comparison of two variants of run-proto.sh: per pass, B/A of the runs in the same pass
# (pass k = the k-th run of each variant); prints medians of A and B and median/min/max of B/A - 1.
import json, sys, statistics as st
def load(f):
    out = []
    for l in open(f):
        r = json.loads(l); w = r['wrk']; cw = r['cpu_window']; n = w['requests']
        dbg = 'blog-pg' if r['db'] == 'pgsql' else 'blog-mysql'
        out.append({'stack': cw['stack'] / n * 1000, 'db': cw[dbg] / n * 1000, 'sum': (cw['stack'] + cw[dbg]) / n * 1000,
                    'p99': w['p99_us'] / 1000, 'non2xx': w['non2xx'], 'errors': w['errors'], 'n': n})
    return out
a, b = load(sys.argv[1]), load(sys.argv[2])
assert len(a) == len(b), (len(a), len(b))
print(f"passes={len(a)} requests/run={a[0]['n']} non2xx A={[x['non2xx'] for x in a]} B={[x['non2xx'] for x in b]} errors A={sum(x['errors'] for x in a)} B={sum(x['errors'] for x in b)}")
for k in ('stack', 'db', 'sum', 'p99'):
    r = [y[k] / x[k] - 1 for x, y in zip(a, b)]
    print(f"{k:5} A={st.median(x[k] for x in a):.3f} B={st.median(y[k] for y in b):.3f} B/A-1 median={st.median(r)*100:+.1f}% range={min(r)*100:+.1f}..{max(r)*100:+.1f}%")
