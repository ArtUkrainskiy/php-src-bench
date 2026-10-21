# Prints the tables of the report from one drupal-series.sh file (fields: record.py): the checks of all runs, the
# medians of the passes per variant (through PgBouncer also its counters per URL), and the changes between
# variants. A change is the median of the per-pass ratios (variant b against variant a in the same pass) − 1; the
# full table adds their min…max.
#   python3 table.py <direct.jsonl | pgbouncer.jsonl>
import json
import statistics as st
import sys

with open(sys.argv[1]) as f:
    runs = [json.loads(line) for line in f]
bouncer = runs[0]['pgbouncer']
BUILDS = {'base': '8.5.11', 'base2': '8.5.11, A/A copy', 'v3': '8.5.11 + cache'}
MODES = {
    'emulated': 'emulated',
    'emulated-persistent': 'emulated, persistent',
    'native': 'native',
    'native-persistent': 'native, persistent',
}
by = {}  # 'build mode' -> {pass label 'p1': record}
for r in runs:
    by.setdefault(f'{r["build"]} {r["mode"]}', {})[r['label'].split('-')[0]] = r


def value(r, k):
    if k == 'total':
        return r['cpu_total_ms']
    if k in ('fpm', 'pg', 'bouncer'):
        return r['cpu_ms'][k]
    if k.startswith('bouncer_'):
        return r['bouncer'][k.removeprefix('bouncer_')]
    return r[k]  # p50_ms, p99_ms, xact_per_url


def med(variant, k):
    return st.median(value(r, k) for r in by[variant].values())


def ratios(a, b, k):
    return [value(by[b][p], k) / value(by[a][p], k) - 1 for p in by[b] if p in by[a]]


def pct(x):
    s = f'{x * 100:+.1f}%'
    return '0.0%' if s in ('+0.0%', '-0.0%') else s.replace('-', '−')


def name(variant):
    b, m = variant.split()
    return f'{BUILDS[b]} | {MODES[m]}'


def table(head, rows):
    print('| ' + ' | '.join(head) + ' |')
    text = 2 if head[1] == 'PDO mode' else 1
    print('|' + '---|' * text + '---:|' * (len(head) - text))
    for row in rows:
        print('| ' + ' | '.join(row) + ' |')
    print()


codes, failed, warn = {}, 0, 0
for r in runs:
    failed += r['failed']
    warn += sum(c for s, c in r['watchdog_new'].items() if int(s) <= 4)  # severity 0 emergency .. 4 warning
    for c, n in r['codes'].items():
        codes[c] = codes.get(c, 0) + n
print(
    f'{len(runs)} runs; responses by status {codes}; failed samples {failed}; watchdog entries warning or worse {warn}'
)
print()

cpu = ['total', 'fpm', 'pg'] + (['bouncer'] if bouncer else [])
cpu_head = ['total CPU', 'PHP-FPM', 'PostgreSQL'] + (['PgBouncer'] if bouncer else [])
table(
    ['build', 'PDO mode', *cpu_head, 'p50', 'p99'] + ([] if bouncer else ['PostgreSQL transactions per URL']),
    [
        [name(v)]
        + [f'{med(v, k):.1f}' for k in cpu]
        + [f'{med(v, k):.0f} ms' for k in ('p50_ms', 'p99_ms')]
        + ([] if bouncer else [f'{med(v, "xact_per_url"):.1f}'])
        for v in by
    ],
)
if bouncer:
    counters = ['bouncer_xact', 'bouncer_client_parse', 'bouncer_server_parse']
    table(
        ['build', 'PDO mode', 'client transactions', 'prepares sent by PHP', 'prepares sent to PostgreSQL'],
        [[name(v)] + [f'{med(v, k):.2f}' for k in counters] for v in by],
    )

COMPARISONS = [
    ('A/A: the same binary twice', 'base native-persistent', 'base2 native-persistent'),
    ('A/A: the same binary twice', 'base native', 'base2 native'),
    ('native + patch against native, neither persistent', 'base native', 'v3 native'),
    ('native + patch against native, both persistent', 'base native-persistent', 'v3 native-persistent'),
    ('native + patch against emulated, both persistent', 'base emulated-persistent', 'v3 native-persistent'),
    ('native + patch against emulated, neither persistent', 'base emulated', 'v3 native'),
    ('native + patch, persistent, against emulated, not', 'base emulated', 'v3 native-persistent'),
    ('no patch: emulated, persistent against not', 'base emulated', 'base emulated-persistent'),
]
keys = cpu + ['p50_ms']
head = ['comparison', *cpu_head, 'p50']
rows = [(what, a, b) for what, a, b in COMPARISONS if a in by and b in by]
for what, a, b in rows:
    print(f'- {what}: {name(b).replace(" | ", ", ")} against {name(a).replace(" | ", ", ")}')
print()
table(head, [[what] + [pct(st.median(ratios(a, b, k))) for k in keys] for what, a, b in rows])
print('With the min…max of the five per-pass ratios:')
print()
table(
    head,
    [
        [what]
        + [
            f'{pct(st.median(x))} ({pct(min(x)).removesuffix("%")}…{pct(max(x)).removesuffix("%")})'
            for x in (ratios(a, b, k) for k in keys)
        ]
        for what, a, b in rows
    ],
)
