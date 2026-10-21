# Reads `SHOW STATS` of PgBouncer (psql -A -F' ' -P footer=off, with the header line) on stdin and prints the
# counters of database drupal that drupal-run.sh records: transactions, Parse messages from clients and Parse sent
# to PostgreSQL.
import sys

lines = [line.split() for line in sys.stdin if line.strip()]
head = lines[0] if lines and lines[0][0] == 'database' else None
for f in lines:
    if f[0] == 'drupal' and head:
        row = dict(zip(head, f, strict=True))
        for k in ('total_xact_count', 'total_client_parse_count', 'total_server_parse_count'):
            print('bouncer', k.removeprefix('total_').removesuffix('_count'), row[k])
