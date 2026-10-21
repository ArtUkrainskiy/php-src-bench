# The JSON line of one drupal-run.sh measurement, from runs/<label>/{before,after}.txt and measure.jtl.
# Fields ("per URL" = divided by the number of page requests of the measured list, 2000):
#   label            p<pass>-<build>-<mode>; build (base, base2, v3), mode (emulated, emulated-persistent, native,
#                    native-persistent), pgbouncer (true when PHP connected through PgBouncer)
#   php_fpm_sha256   first 16 hex digits of the sha256 of the php-fpm binary
#   start, seconds   Unix time of the start of the measured part, and its length
#   urls, samples    page requests, and all JMeter samples (pages plus logins and the comment form and post)
#   comments         comments posted; codes = samples by HTTP status; failed = samples JMeter marked failed
#   cpu_ms           CPU time per URL in ms of each container: fpm (PHP-FPM), nginx, pg (PostgreSQL), bouncer
#                    (PgBouncer); the logins and comments of the run are part of this work
#   cpu_total_ms     the sum of cpu_ms
#   xact_per_url     PostgreSQL transactions (xact_commit + xact_rollback of pg_stat_database) per URL
#   bouncer          PgBouncer's SHOW STATS per URL: xact (client transactions), client_parse (prepares sent by
#                    PHP), server_parse (prepares PgBouncer sent to PostgreSQL); empty without PgBouncer
#   watchdog_new     Drupal log entries written during the run, by severity (0 emergency .. 4 warning .. 7 debug)
#   other_cpus_busy  busy fraction of the CPUs outside the lists of cpus.sh
#   p50_ms, p99_ms   latency of the page requests
#   python3 record.py <label> <build> <mode> <bouncer 0|1> <run dir> <t0> <t1> <php-fpm sha256 prefix>
import csv
import json
import os
import sys

label, build, mode, bouncer, run, t0, t1, sha = sys.argv[1:]


def cpu_list(text):  # '8-11,24-27' -> {8, 9, 10, 11, 24, 25, 26, 27}
    cpus = set()
    for part in text.split(','):
        lo, _, hi = part.partition('-')
        cpus.update(range(int(lo), int(hi or lo) + 1))
    return cpus


USED = set().union(*(cpu_list(os.environ[v]) for v in ('CPUS_STACK', 'CPUS_PG', 'CPUS_JMETER')))  # from cpus.sh


def snap(name):
    d = {'cpu': {}, 'watchdog': {}, 'bouncer': {}, 'stat': {}}
    with open(f'{run}/{name}.txt') as fh:
        lines = fh.read().splitlines()
    for line in lines:
        f = line.split()
        if f[0] == 'cpu':
            d['cpu'][f[1].removeprefix('drupal-bench-')] = int(f[2])
        elif f[0] == 'xact':
            d['xact'] = int(f[1])
        elif f[0] == 'watchdog':
            d['watchdog'][int(f[1])] = int(f[2])
        elif f[0] == 'bouncer':
            d['bouncer'][f[1]] = int(f[2])
        elif f[0].startswith('cpu'):
            v = list(map(int, f[1:]))
            d['stat'][int(f[0][3:])] = (sum(v) - v[3] - v[4], sum(v))  # busy, total (idle and iowait are not busy)
    return d


a, b = snap('before'), snap('after')
with open(f'{run}/measure.jtl') as fh:
    rows = list(csv.DictReader(fh))
pages = [r for r in rows if r['label'] == 'page']
n = len(pages)
el = sorted(int(r['elapsed']) for r in pages)
other = [c for c in b['stat'] if c not in USED]
busy = sum(b['stat'][c][0] - a['stat'][c][0] for c in other)
total = sum(b['stat'][c][1] - a['stat'][c][1] for c in other)
cpu = {k: (b['cpu'][k] - a['cpu'][k]) / 1000 / n for k in b['cpu']}
print(
    json.dumps(
        {
            'label': label,
            'build': build,
            'mode': mode,
            'pgbouncer': bouncer == '1',
            'php_fpm_sha256': sha,
            'start': float(t0),
            'seconds': round(float(t1) - float(t0), 1),
            'urls': n,
            'samples': len(rows),
            'comments': sum(r['label'] == 'comment post' for r in rows),
            'codes': {c: sum(r['responseCode'] == c for r in rows) for c in sorted({r['responseCode'] for r in rows})},
            'failed': sum(r['success'] != 'true' for r in rows),
            'cpu_ms': cpu,
            'cpu_total_ms': sum(cpu.values()),
            'xact_per_url': (b['xact'] - a['xact']) / n,
            'bouncer': {k: (b['bouncer'][k] - a['bouncer'].get(k, 0)) / n for k in b['bouncer']},
            'watchdog_new': {
                s: c - a['watchdog'].get(s, 0) for s, c in b['watchdog'].items() if c != a['watchdog'].get(s, 0)
            },
            'other_cpus_busy': round(busy / total, 4) if total else None,
            'p50_ms': el[n // 2],
            'p99_ms': el[int(n * 0.99)],
        }
    )
)
