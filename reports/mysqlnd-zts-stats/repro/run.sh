#!/bin/bash
# CPU time of the FrankenPHP container per request, with mysqlnd statistics on (default) and off.
#   APP_CPUS=8-11,24-27 LOAD_CPUS=6-7,22-23 DB_CPUS=0-5,16-21 [THREADS=16] ./run.sh
# Needs Linux with cgroup v2 and the systemd cgroup driver of Docker, wrk, taskset, curl, free ports 3307 and 8080.
set -e
cd "$(dirname "$0")"
: "${APP_CPUS:?}" "${LOAD_CPUS:?}" "${DB_CPUS:?}"
docker rm -f repro-mysql repro-app >/dev/null 2>&1 || true
docker build -q -t mysqlnd-zts-repro . >/dev/null
sed "s/THREADS/${THREADS:-16}/g" Caddyfile > Caddyfile.run
docker run -d --name repro-mysql --network host --cpuset-cpus "$DB_CPUS" -e MYSQL_ROOT_PASSWORD=pw -e MYSQL_DATABASE=test \
	-v "$PWD/init.sql:/docker-entrypoint-initdb.d/init.sql:ro" mysql:8.4.11 --port=3307 --mysqlx=OFF >/dev/null
timeout 120 bash -c "until docker exec repro-mysql mysql -h127.0.0.1 -P3307 -uroot -ppw test -e 'SELECT COUNT(*) FROM t' >/dev/null 2>&1; do read -t 1 <> <(:) || true; done" || { echo 'MySQL did not start' >&2; exit 1; }
echo 'mysqlnd.collect_statistics=0' > off.ini
for pass in $(seq 1 ${PASSES:-3}); do
	for stats in on off; do
		extra=(); [ $stats = off ] && extra=(-v "$PWD/off.ini:/usr/local/etc/php/conf.d/zz-off.ini:ro")
		docker run -d --name repro-app --network host --cpuset-cpus "$APP_CPUS" -v "$PWD/Caddyfile.run:/etc/frankenphp/Caddyfile:ro" "${extra[@]}" mysqlnd-zts-repro >/dev/null
		timeout 60 bash -c 'until curl -fs http://127.0.0.1:8080/ >/dev/null; do read -t 1 <> <(:) || true; done' || { echo 'FrankenPHP did not answer 200' >&2; docker logs repro-app 2>&1 | tail -5 >&2; exit 1; }
		taskset -c "$LOAD_CPUS" wrk -t4 -c50 -d5s http://127.0.0.1:8080/ >/dev/null
		cg=/sys/fs/cgroup/system.slice/docker-$(docker inspect -f '{{.Id}}' repro-app).scope/cpu.stat
		u0=$(awk '/^usage_usec/{print $2}' "$cg")
		out=$(taskset -c "$LOAD_CPUS" wrk -t4 -c50 -d20s http://127.0.0.1:8080/)
		u1=$(awk '/^usage_usec/{print $2}' "$cg")
		n=$(echo "$out" | awk '/requests in/{print $1}')
		echo "threads ${THREADS:-16} pass $pass statistics $stats: $n requests, $(echo "$out" | awk '/Requests\/sec/{print $2}') req/s, $(awk -v u=$((u1 - u0)) -v n="$n" 'BEGIN{printf "%.3f", u / n / 1000}') ms CPU per request"
		docker rm -f repro-app >/dev/null
	done
done
docker rm -f repro-mysql >/dev/null
