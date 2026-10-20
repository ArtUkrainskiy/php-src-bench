# PgBouncer SHOW STATS (database "bench") before and after 2000 requests, per build: differences of the counters.
#   python3 bouncer-counts.py <dir with <build>-before.csv and <build>-after.csv>
import csv, sys, os
d = sys.argv[1]
for n in ('base', 'discard', 'keep', 'plans'):
    h, a = list(csv.reader(open(os.path.join(d, f'{n}-before.csv'))))
    b = list(csv.reader(open(os.path.join(d, f'{n}-after.csv'))))[1]
    x = {k: int(v2) - int(v1) for k, v1, v2 in zip(h, a, b) if k.startswith('total_') and k.endswith('_count')}
    print(f"{n:8} transactions={x['total_xact_count']:6} client_parse={x['total_client_parse_count']:6} "
          f"server_parse={x['total_server_parse_count']:6} bind={x['total_bind_count']:6} "
          f"server_parse_per_request={x['total_server_parse_count'] / 2000:.2f}")
