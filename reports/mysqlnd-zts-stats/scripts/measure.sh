#!/bin/bash
# CPU time per request of FrankenPHP (worker mode) on master and on the patch, mysqlnd statistics on and off.
#   ./measure.sh            (PASSES=5 THREADS=16 DURATION=20s TAG=  PREPARES=emulated|native)
# Workload: the repro of the issue (one prepared SELECT of 20 rows per request, MySQL 8.4.11 in Docker on port 3307).
# FrankenPHP runs natively; CPU = utime+stime of the process (all threads) from /proc/<pid>/stat around the wrk run.
set -e
cd "$(dirname "$0")"
APP_CPUS=${APP_CPUS:-8-11,24-27} LOAD_CPUS=${LOAD_CPUS:-6-7,22-23} DB_CPUS=${DB_CPUS:-0-5,16-21}
THREADS=${THREADS:-16} PASSES=${PASSES:-5} DURATION=${DURATION:-20s}
REPRO=$(cd ../repro && pwd)
read -r -a BUILDS <<< "${BUILDS:-php-master-b7256ee php-atomic-f5b2623}"
PREPARES=${PREPARES:-emulated}
OUT=$PWD/results-$(date +%Y%m%d-%H%M)-t$THREADS${TAG:+-$TAG}.txt
W=$PWD/work
mkdir -p "$W/app" "$W/ini-on" "$W/ini-off"
cp "$REPRO/index.php" "$W/app/index.php"
if [ "$PREPARES" = native ]; then
	sed -i "s|'root', 'pw');|'root', 'pw', [PDO::ATTR_EMULATE_PREPARES => false]);|" "$W/app/index.php"
	command grep -q ATTR_EMULATE_PREPARES "$W/app/index.php" || { echo 'native prepares not set' >&2; exit 1; }
fi
echo '<?php echo ini_get("mysqlnd.collect_statistics"), " ", PHP_VERSION;' > "$W/app/check.php"
echo 'mysqlnd.collect_statistics=1' > "$W/ini-on/php.ini"
echo 'mysqlnd.collect_statistics=0' > "$W/ini-off/php.ini"
cat > "$W/Caddyfile" <<EOF
{
	auto_https off
	frankenphp {
		num_threads $THREADS
		worker {
			file $W/app/index.php
			num $THREADS
		}
	}
}

:8080 {
	root * $W/app
	php_server
}
EOF
log() { echo "$@" | tee -a "$OUT"; }
ss -ltn | command grep -q -E ':(3307|8080) ' && { echo 'port 3307 or 8080 is busy' >&2; exit 1; }

docker rm -f repro-mysql >/dev/null 2>&1 || true
docker run -d --name repro-mysql --network host --cpuset-cpus "$DB_CPUS" -e MYSQL_ROOT_PASSWORD=pw -e MYSQL_DATABASE=test \
	-v "$REPRO/init.sql:/docker-entrypoint-initdb.d/init.sql:ro" mysql:8.4.11 --port=3307 --mysqlx=OFF >/dev/null
trap 'docker rm -f repro-mysql >/dev/null 2>&1 || true' EXIT
timeout 120 bash -c "until docker exec repro-mysql mysql -h127.0.0.1 -P3307 -uroot -ppw test -e 'SELECT COUNT(*) FROM t' >/dev/null 2>&1; do read -t 1 <> <(:) || true; done" \
	|| { echo 'MySQL did not start' >&2; exit 1; }

log "measure $(date -Is) kernel=$(uname -r) governor=$(cat /sys/devices/system/cpu/cpu8/cpufreq/scaling_governor)"
log "prepares=$PREPARES threads=$THREADS passes=$PASSES duration=$DURATION app_cpus=$APP_CPUS load_cpus=$LOAD_CPUS db_cpus=$DB_CPUS"
for b in "${BUILDS[@]}"; do log "$b: $(./$b/sapi/cli/php -v | head -1)"; done
hz=$(getconf CLK_TCK)

for pass in $(seq 1 "$PASSES"); do
	# alternate the order of the variants between passes
	if [ $((pass % 2)) = 1 ]; then order="0:on 1:on 0:off 1:off"; else order="1:off 0:off 1:on 0:on"; fi
	for v in $order; do
		b=${BUILDS[${v%%:*}]} stats=${v##*:}
		PHPRC=$W/ini-$stats taskset -c "$APP_CPUS" "./$b/frankenphp" run --config "$W/Caddyfile" > "$W/frankenphp.log" 2>&1 &
		fpid=$!
		timeout 60 bash -c 'until curl -fs http://127.0.0.1:8080/ >/dev/null; do read -t 1 <> <(:) || true; done' \
			|| { echo "$b did not answer 200" >&2; tail -n 5 "$W/frankenphp.log" >&2; kill "$fpid"; exit 1; }
		[ "$(cat /proc/$fpid/comm)" = frankenphp ] || { echo "PID $fpid is not frankenphp" >&2; kill "$fpid"; exit 1; }
		chk=$(curl -fs http://127.0.0.1:8080/check.php)
		want=$([ $stats = on ] && echo 1 || echo 0)
		[ "${chk%% *}" = "$want" ] || { echo "$b: collect_statistics is '$chk', expected $want" >&2; kill "$fpid"; exit 1; }
		taskset -c "$LOAD_CPUS" wrk -t4 -c50 -d5s http://127.0.0.1:8080/ >/dev/null
		t0=$(awk '{print $14 + $15}' /proc/$fpid/stat)
		wout=$(perf stat -x, -e cycles,instructions -o "$W/perf.csv" -p "$fpid" -- taskset -c "$LOAD_CPUS" wrk -t4 -c50 -d"$DURATION" http://127.0.0.1:8080/)
		t1=$(awk '{print $14 + $15}' /proc/$fpid/stat)
		kill "$fpid"
		wait "$fpid" || true
		n=$(echo "$wout" | awk '/requests in/{print $1}')
		non2xx=$(echo "$wout" | awk '/Non-2xx/{print $NF}')
		log "pass $pass $b statistics $stats: $n requests, $(echo "$wout" | awk '/Requests\/sec/{print $2}') req/s, non-2xx ${non2xx:-0}, ini '$chk'," \
			"$(awk -v t=$((t1 - t0)) -v n="$n" -v hz="$hz" 'BEGIN{printf "%.4f", t / hz / n * 1000}') ms CPU per request," \
			"$(awk -F, -v n="$n" '$3 == "cycles" {c = $1} $3 == "instructions" {i = $1} END {printf "%.0f cycles, %.0f instructions per request", c / n, i / n}' "$W/perf.csv")"
	done
done
