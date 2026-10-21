#!/bin/bash
# One measurement: the site of setup.sh on one PHP build and one PDO mode, as one JSON line on stdout (record.py).
# Containers, on the CPU lists of cpus.sh: nginx 1.30.5 + PHP-FPM of the build (pm static, 8 children), and
# PgBouncer if BOUNCER=1; PostgreSQL (drupal-bench-pg, from setup.sh); JMeter (8 editors, editors.jmx).
# The database is restored from drupal_tpl, then 200 warm-up URLs (make-urls.py seed 7) run, then the measured list.
# Over the measured part it records the CPU time of the containers' cgroups (cgroup v2, Docker's systemd driver),
# PostgreSQL's transactions, PgBouncer's counters, Drupal's log entries (watchdog) and the busy time of the other CPUs.
# Build base2 is build-base under another name (the A/A control).
#   [BOUNCER=1] [SKIP_GOVERNOR_CHECK=1] ./drupal-run.sh <build: base|base2|v3> <emulated|emulated-persistent|native|native-persistent> <label> <urls.csv>
set -e
cd "$(dirname "$0")"
. ./cpus.sh
build=$1 mode=$2 label=$3 urls=$4
[ "$build" = base2 ] && ln -sfn build-base build-base2
php=$PWD/build-$build/php85-fpm
[ -x "$php/sapi/fpm/php-fpm" ] || { echo "no build $php" >&2; exit 1; }
runtime=drupal-runtime:$(. /etc/os-release && echo "$VERSION_ID")
# the runs used governor performance, energy_performance_preference performance and boost on (amd-pstate);
# other CPU drivers lack some of these files: check the settings by hand and set SKIP_GOVERNOR_CHECK=1
if [ "${SKIP_GOVERNOR_CHECK:-0}" != 1 ]; then
	g=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor /sys/devices/system/cpu/cpu0/cpufreq/energy_performance_preference /sys/devices/system/cpu/cpufreq/boost | paste -sd/)
	[ "$g" = performance/performance/1 ] || { echo "governor/EPP/boost $g, the runs used performance/performance/1 (SKIP_GOVERNOR_CHECK=1 skips this check)" >&2; exit 1; }
fi
bouncer=$([ "${BOUNCER:-0}" = 1 ] && echo 1 || echo 0)
run=$PWD/runs/$label
rm -rf "$run" && mkdir -p "$run" && chmod 777 "$run" # the containers write their logs here
docker stop drupal-bench-fpm drupal-bench-nginx drupal-bench-bouncer >/dev/null 2>&1 || true
P="docker exec drupal-bench-pg psql -U drupal -d postgres -tAq"
$P -c "DROP DATABASE IF EXISTS drupal WITH (FORCE)" -c "CREATE DATABASE drupal TEMPLATE drupal_tpl" -c "CHECKPOINT" >/dev/null
{
	cat "$php/php.ini-production"
	printf '%s\n' opcache.memory_consumption=128 opcache.interned_strings_buffer=8 opcache.max_accelerated_files=10000 \
		opcache.revalidate_freq=60 memory_limit=256M error_log=/run/d/php-error.log
} > "$run/php.ini"
printf '%s\n' '[global]' 'error_log = /run/d/fpm.log' 'daemonize = no' '[drupal]' 'listen = 0.0.0.0:9000' \
	'pm = static' 'pm.max_children = 8' 'clear_env = yes' "env[BENCH_PDO] = $mode" > "$run/php-fpm.conf"
if [ "$bouncer" = 1 ]; then
	printf '%s\n' 'env[BENCH_DB_HOST] = drupal-bench-bouncer' 'env[BENCH_DB_PORT] = 6432' >> "$run/php-fpm.conf"
	printf '%s\n' '[databases]' 'drupal = host=drupal-bench-pg port=5432 dbname=drupal' '[pgbouncer]' \
		'listen_addr = 0.0.0.0' 'listen_port = 6432' 'auth_type = scram-sha-256' 'auth_file = /run/d/userlist.txt' \
		'admin_users = drupal' 'pool_mode = transaction' 'default_pool_size = 8' 'max_client_conn = 1000' \
		'max_prepared_statements = 200' 'logfile = /run/d/pgbouncer.log' > "$run/pgbouncer.ini"
	echo '"drupal" "drupal"' > "$run/userlist.txt"
	docker run -d --rm --name drupal-bench-bouncer --network drupal-bench --cpuset-cpus "$CPUS_STACK" -u "$(id -u)" \
		-v "$run:/run/d" "$runtime" pgbouncer /run/d/pgbouncer.ini >/dev/null
fi
cat > "$run/nginx.conf" <<'EOF'
worker_processes 2;
events { worker_connections 4096; }
http {
	access_log off;
	server {
		listen 80;
		location / {
			fastcgi_pass drupal-bench-fpm:9000;
			include fastcgi_params;
			fastcgi_param SCRIPT_FILENAME /app/web/index.php;
			fastcgi_param SCRIPT_NAME /index.php;
		}
	}
}
EOF
docker run -d --rm --name drupal-bench-fpm --network drupal-bench --cpuset-cpus "$CPUS_STACK" -u "$(id -u)" \
	-v "$php:$php:ro" -v "$PWD/app:/app" -v "$run:/run/d" "$runtime" \
	"$php/sapi/fpm/php-fpm" -c /run/d/php.ini -y /run/d/php-fpm.conf >/dev/null
docker run -d --rm --name drupal-bench-nginx --network drupal-bench --cpuset-cpus "$CPUS_STACK" -p 127.0.0.1:58090:80 \
	-v "$run/nginx.conf:/etc/nginx/nginx.conf:ro" \
	nginx@sha256:9bf97bd7714f5e24c1ccd545ecb9eb5435cb6d109c97cebb15e7e455e0239edb >/dev/null # nginx:1.30.5
timeout 120 bash -c 'until curl -s -o /dev/null -f http://127.0.0.1:58090/user/login; do sleep 1; done' ||
	{ echo "the site did not answer within 120 s" >&2; exit 1; }
jm() { # urls file, name; editors.jmx reads ./urls.csv and ./nids.csv (from setup.sh) of this directory
	cp "$1" urls.csv
	docker run --rm --network host --cpuset-cpus "$CPUS_JMETER" -v "$PWD:/w" -w /w \
		alpine/jmeter@sha256:4fa9671e144e73d0cfb79c861c14f2d0d0f2a999d213ed49e92a55a050b4e8e8 \
		-n -t editors.jmx -Jport=58090 -Jthreads=8 -Jout="runs/$label/$2.jtl" > "$run/jmeter-$2.log" 2>&1 # alpine/jmeter:5.6.3
}
python3 make-urls.py 200 7 > "$run/warm.csv"
jm "$run/warm.csv" warm
groups="drupal-bench-fpm drupal-bench-nginx drupal-bench-pg"
[ "$bouncer" = 1 ] && groups="$groups drupal-bench-bouncer"
cpu_snap() {
	for c in $groups; do
		echo "cpu $c $(awk '/^usage_usec/{print $2}' "/sys/fs/cgroup/system.slice/docker-$(docker inspect -f '{{.Id}}' "$c").scope/cpu.stat")"
	done
	grep '^cpu[0-9]' /proc/stat
}
# PostgreSQL flushes the statistics of an idle backend every 10 s (persistent connections stay idle between
# requests), so the database counters are read after 11 s without load, outside the measured interval
db_snap() {
	sleep 11
	echo "xact $(docker exec drupal-bench-pg psql -U drupal -d drupal -tAqc "SELECT xact_commit + xact_rollback FROM pg_stat_database WHERE datname = 'drupal'")"
	docker exec drupal-bench-pg psql -U drupal -d drupal -tAqc "SELECT 'watchdog ' || severity || ' ' || count(*) FROM watchdog GROUP BY severity"
	if [ "$bouncer" = 1 ]; then
		docker exec -e PGPASSWORD=drupal drupal-bench-pg psql -h drupal-bench-bouncer -p 6432 -U drupal -d pgbouncer -A -F' ' -P footer=off \
			-c 'SHOW STATS' | python3 bouncer-stats.py
	fi
}
db_snap > "$run/before.txt"; cpu_snap >> "$run/before.txt"; t0=$(date +%s.%N)
jm "$urls" measure
t1=$(date +%s.%N); cpu_snap > "$run/after.txt"; db_snap >> "$run/after.txt"
# stop the containers of the run; PostgreSQL keeps running
# shellcheck disable=SC2086 # the container names are separate words
docker stop ${groups/drupal-bench-pg/} >/dev/null
python3 record.py "$label" "$build" "$mode" "$bouncer" "$run" "$t0" "$t1" "$(sha256sum "$php/sapi/fpm/php-fpm" | cut -c1-16)"
