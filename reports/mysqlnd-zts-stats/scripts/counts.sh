#!/bin/bash
# Do the global mysqlnd statistics count every request under concurrency?
# Sends exactly K requests (curl --parallel, 50 at a time) to FrankenPHP with 16 threads, statistics on,
# and compares the change of the global counters (mysqli_get_client_stats()) with K.
#   ./counts.sh [build ...]      (K=50000)
set -e
cd "$(dirname "$0")"
APP_CPUS=${APP_CPUS:-8-11,24-27} LOAD_CPUS=${LOAD_CPUS:-6-7,22-23} DB_CPUS=${DB_CPUS:-0-5,16-21}
THREADS=${THREADS:-16} K=${K:-50000}
REPRO=$(cd ../repro && pwd)
BUILDS=("$@"); [ ${#BUILDS[@]} = 0 ] && BUILDS=(php-master-b7256ee-mysqli php-atomic-f5b2623-mysqli php-mutant-racy-mysqli)
OUT=$PWD/counts-$(date +%Y%m%d-%H%M).txt
W=$PWD/work
mkdir -p "$W/app" "$W/ini-on"
cp "$REPRO/index.php" "$W/app/index.php"
echo '<?php foreach (mysqli_get_client_stats() as $k => $v) echo "$k $v\n";' > "$W/app/stats.php"
echo 'mysqlnd.collect_statistics=1' > "$W/ini-on/php.ini"
sed "s/num_threads [0-9]*/num_threads $THREADS/; s/num [0-9]*$/num $THREADS/" "$W/Caddyfile" > "$W/Caddyfile.counts"
for i in $(seq 1 "$K"); do printf 'url = "http://127.0.0.1:8080/"\noutput = /dev/null\n'; done > "$W/urls.cfg"
log() { echo "$@" | tee -a "$OUT"; }
stats() { curl -fs http://127.0.0.1:8080/stats.php | LC_ALL=C sort; }

ss -ltn | command grep -q -E ':(3307|8080) ' && { echo 'port 3307 or 8080 is busy' >&2; exit 1; }
docker rm -f repro-mysql >/dev/null 2>&1 || true
docker run -d --name repro-mysql --network host --cpuset-cpus "$DB_CPUS" -e MYSQL_ROOT_PASSWORD=pw -e MYSQL_DATABASE=test \
	-v "$REPRO/init.sql:/docker-entrypoint-initdb.d/init.sql:ro" mysql:8.4.11 --port=3307 --mysqlx=OFF >/dev/null
trap 'docker rm -f repro-mysql >/dev/null 2>&1 || true' EXIT
timeout 120 bash -c "until docker exec repro-mysql mysql -h127.0.0.1 -P3307 -uroot -ppw test -e 'SELECT COUNT(*) FROM t' >/dev/null 2>&1; do read -t 1 <> <(:) || true; done" \
	|| { echo 'MySQL did not start' >&2; exit 1; }
log "counts $(date -Is) threads=$THREADS K=$K"

for b in "${BUILDS[@]}"; do
	PHPRC=$W/ini-on taskset -c "$APP_CPUS" "./$b/frankenphp" run --config "$W/Caddyfile.counts" > "$W/frankenphp.log" 2>&1 &
	fpid=$!
	timeout 60 bash -c 'until curl -fs http://127.0.0.1:8080/ >/dev/null; do read -t 1 <> <(:) || true; done' \
		|| { echo "$b did not answer 200" >&2; kill "$fpid"; exit 1; }
	stats > "$W/s0-$b.txt"
	[ -s "$W/s0-$b.txt" ] || { echo "$b: no statistics from mysqli_get_client_stats()" >&2; kill "$fpid"; exit 1; }
	codes=$(taskset -c "$LOAD_CPUS" curl -s --parallel --parallel-max 50 -K "$W/urls.cfg" -w '%{http_code}\n' | sort | uniq -c | tr '\n' ' ')
	stats > "$W/s1-$b.txt"
	kill "$fpid"
	wait "$fpid" || true
	log "$b: responses: $codes"
	LC_ALL=C join "$W/s0-$b.txt" "$W/s1-$b.txt" | awk -v k="$K" '$3 != $2 { d = $3 - $2; printf "  %-45s %12d  per request %.4f\n", $1, d, d / k }' \
		| command grep -E 'rows_fetched_from_server_normal|rows_buffered_from_client_normal|com_query|result_set_queries|connect_success|packets_received_rset_row|non_result_set|rows_fetched_from_client' | tee -a "$OUT"
done
