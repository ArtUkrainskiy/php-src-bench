#!/bin/bash
# Mutex acquisitions and futex calls per request in the FrankenPHP container, mysqlnd statistics on and off.
#   sudo ./count-locks.sh            # full run, needs root (uprobes)
#   CHECK=1 ./count-locks.sh         # no root: start containers, resolve PID/libc/symbol, print the bpftrace program, stop
# Same setup as run.sh (image mysqlnd-zts-repro, MySQL 8.4.11, ports 3307/8080). Results: count-locks-<date>.txt next to this script.
set -e
cd "$(dirname "$0")"
APP_CPUS=${APP_CPUS:-8-11,24-27} LOAD_CPUS=${LOAD_CPUS:-6-7,22-23} DB_CPUS=${DB_CPUS:-0-5,16-21}
THREADS=${THREADS:-16} PASSES=${PASSES:-2} DURATION=${DURATION:-10s}
if [ -z "$CHECK" ] && [ "$(id -u)" != 0 ]; then echo 'run with sudo (or CHECK=1 without root)' >&2; exit 1; fi
OUT=$PWD/count-locks-$(date +%Y%m%d-%H%M)${CHECK:+-check}.txt
RAW=$PWD/count-locks-raw
mkdir -p "$RAW"
log() { echo "$@" | tee -a "$OUT"; }

cleanup() { docker rm -f repro-app repro-mysql >/dev/null 2>&1 || true; }
trap cleanup EXIT
cleanup
sed "s/THREADS/$THREADS/g" Caddyfile > Caddyfile.run
echo 'mysqlnd.collect_statistics=0' > off.ini
docker run -d --name repro-mysql --network host --cpuset-cpus "$DB_CPUS" -e MYSQL_ROOT_PASSWORD=pw -e MYSQL_DATABASE=test \
	-v "$PWD/init.sql:/docker-entrypoint-initdb.d/init.sql:ro" mysql:8.4.11 --port=3307 --mysqlx=OFF >/dev/null
timeout 120 bash -c "until docker exec repro-mysql mysql -h127.0.0.1 -P3307 -uroot -ppw test -e 'SELECT COUNT(*) FROM t' >/dev/null 2>&1; do read -t 1 <> <(:) || true; done" \
	|| { echo 'MySQL did not start' >&2; exit 1; }

log "count-locks $(date -Is) host=$(hostname) kernel=$(uname -r) bpftrace=$(bpftrace --version 2>&1)"
log "threads=$THREADS passes=$PASSES duration=$DURATION app_cpus=$APP_CPUS load_cpus=$LOAD_CPUS db_cpus=$DB_CPUS"
log "image $(docker inspect -f '{{.Id}}' mysqlnd-zts-repro)"

for pass in $(seq 1 "$PASSES"); do
	for stats in on off; do
		extra=(); [ $stats = off ] && extra=(-v "$PWD/off.ini:/usr/local/etc/php/conf.d/zz-off.ini:ro")
		docker run -d --name repro-app --network host --cpuset-cpus "$APP_CPUS" -v "$PWD/Caddyfile.run:/etc/frankenphp/Caddyfile:ro" "${extra[@]}" mysqlnd-zts-repro >/dev/null
		timeout 60 bash -c 'until curl -fs http://127.0.0.1:8080/ >/dev/null; do read -t 1 <> <(:) || true; done' \
			|| { echo 'FrankenPHP did not answer 200' >&2; docker logs repro-app 2>&1 | tail -5 >&2; exit 1; }
		pid=$(docker inspect -f '{{.State.Pid}}' repro-app)
		comm=$(cat /proc/$pid/comm)
		[ "$comm" = frankenphp ] || { echo "container PID $pid is '$comm', not frankenphp" >&2; exit 1; }
		inlibc=$(docker exec repro-app awk '$6 ~ /\/libc\.so\.6$/ {print $6; exit}' /proc/1/maps)
		[ -n "$inlibc" ] || { echo "libc of PID $pid not found" >&2; exit 1; }
		libc=/proc/$pid/root$inlibc
		val=$(docker exec repro-app php -r 'echo ini_get("mysqlnd.collect_statistics");')
		taskset -c "$LOAD_CPUS" wrk -t4 -c50 -d5s http://127.0.0.1:8080/ >/dev/null

		prog=$RAW/pass$pass-$stats.bt
		cat > "$prog" <<EOF
uprobe:$libc:pthread_mutex_lock /pid == $pid/ { @locks = count(); @by_mutex[arg0] = count(); @by_caller[usym(*(uint64 *)reg("sp"))] = count(); }
tracepoint:syscalls:sys_enter_futex /pid == $pid/ { @futex = count(); @futex_by_addr[args.uaddr] = count(); }
END { print(@locks); print(@futex); print(@by_mutex, 20); print(@futex_by_addr, 20); print(@by_caller, 25); clear(@locks); clear(@futex); clear(@by_mutex); clear(@futex_by_addr); clear(@by_caller); }
EOF
		if [ -n "$CHECK" ]; then
			log "pass $pass statistics $stats (collect_statistics=$val): PID $pid, libc $libc"
			bpftrace -l "uprobe:$libc:pthread_mutex_lock" 2>&1 | tee -a "$OUT"
			cat "$prog" | tee -a "$OUT"
			docker rm -f repro-app >/dev/null
			exit 0
		fi

		bt=$RAW/pass$pass-$stats.out
		if ! bpftrace --dry-run "$prog" > "$bt.dry" 2>&1; then
			log "bpftrace --dry-run failed, retrying without @by_caller: $(head -3 "$bt.dry" | tr '\n' ' ')"
			sed -i 's/ @by_caller\[usym([^;]*; //; s/ print(@by_caller, 25);//; s/ clear(@by_caller);//' "$prog"
			bpftrace --dry-run "$prog" > "$bt.dry" 2>&1 || { echo 'bpftrace --dry-run failed:' >&2; cat "$bt.dry" >&2; exit 1; }
		fi
		bpftrace "$prog" > "$bt" 2>&1 &
		bpid=$!
		timeout 30 bash -c "until command grep -q '^Attached' '$bt'; do read -t 1 <> <(:) || true; done" \
			|| { echo 'bpftrace did not attach' >&2; cat "$bt" >&2; kill "$bpid"; exit 1; }
		wout=$(taskset -c "$LOAD_CPUS" wrk -t4 -c50 -d"$DURATION" http://127.0.0.1:8080/)
		kill -INT "$bpid"
		wait "$bpid" || true
		n=$(echo "$wout" | awk '/requests in/{print $1}')
		locks=$(awk '/^@locks:/{print $2}' "$bt")
		futex=$(awk '/^@futex:/{print $2}' "$bt")
		log "pass $pass statistics $stats (collect_statistics=$val): $n requests, $(echo "$wout" | awk '/Requests\/sec/{print $2}') req/s under tracing," \
			"$locks mutex locks ($(awk -v a="$locks" -v n="$n" 'BEGIN{printf "%.1f", a / n}') per request)," \
			"$futex futex calls ($(awk -v a="${futex:-0}" -v n="$n" 'BEGIN{printf "%.2f", a / n}') per request)"
		docker rm -f repro-app >/dev/null
	done
done
log "raw bpftrace output: $RAW"
[ -n "$SUDO_USER" ] && chown -R "$SUDO_USER": "$OUT" "$RAW" Caddyfile.run off.ini
