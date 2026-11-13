#!/bin/bash
# Series for php-src #25243: master vs the PR (and optional variants), N rounds, build order alternates every round, CPU 15.
# Needs perf, /usr/bin/time and, for the ORM rows, doctrine/orm with its dependencies in ./orm.
# Output: one CSV line per run in $OUT: round,cc,build,script,args,mem_limit,rc,rss_kib,cycles,instructions,<result>
# Variables: BUILDS_DIR, BUILDS, CCS, N, OUT, ORM, CPU, EVENTS, LIMIT, CASES_OVERRIDE (see README).
set -u
cd "$(dirname "$0")" || exit 1
# PHP builds: $BUILDS_DIR/gc-<build>-<cc>/sapi/cli/php, e.g. builds/gc-master-gcc15
B=${BUILDS_DIR:-$PWD/builds}
N=${N:-5}
CCS=${CCS:-gcc15}
OUT=${OUT:-series.csv}
BUILDS=${BUILDS:-master 25243}
ORM=${ORM:-1}
CPU=${CPU:-15}
# perf event names; on hybrid Intel use EVENTS=cpu_core/cycles/,cpu_core/instructions/
EVENTS=${EVENTS:-cycles,instructions}
CASES=(
	"mem.php pairs 200000 1" "mem.php pairs 200000 4" "mem.php pairs 200000 16"
	"mem.php pairs 1000000 1" "mem.php pairs 1000000 4" "mem.php pairs 1000000 16"
	"mem.php dtor 200000 0" "mem.php dtor 1000000 0" "mem.php dtor 200000 4"
	"mem.php pairs 70000 0" "mem.php pairs 80000 0" "mem.php pairs 90000 0" "mem.php pairs 160000 0"
	"synth.php nolive" "synth.php live200k" "synth.php live1m"
)
# memory_limit just above the master peak of the dtor case (php_peak 162 MiB), below the PR peak (174 MiB)
LIMIT=${LIMIT:-168M}
[ -n "${CASES_OVERRIDE:-}" ] && eval "CASES=($CASES_OVERRIDE)"
LIMITED=("mem.php pairs 200000 4" "mem.php dtor 200000 4")

# Refuse to append to an old series and check the setup before the first run.
[ -e "$OUT" ] && { echo "$OUT exists, pick another OUT" >&2; exit 1; }
for cc in $CCS; do for b in $BUILDS; do
	[ -x "$B/gc-$b-$cc/sapi/cli/php" ] || { echo "missing $B/gc-$b-$cc/sapi/cli/php" >&2; exit 1; }
done; done
taskset -c "$CPU" true || { echo "cannot pin to CPU $CPU" >&2; exit 1; }
perf stat -x, -e "$EVENTS" true 2>&1 | grep -q 'cycles' || { echo "perf stat cannot count $EVENTS (kernel.perf_event_paranoid?)" >&2; exit 1; }
if [ "$ORM" = 1 ] && [ ! -x orm/vendor/bin/phpunit ]; then echo "orm/vendor/bin/phpunit missing (or set ORM=0)" >&2; exit 1; fi

one() { # round cc build limit script args...
	local r=$1 cc=$2 b=$3 lim=$4; shift 4
	local php=$B/gc-$b-$cc/sapi/cli/php tmp
	tmp=$(mktemp -p .)
	trap 'rm -f "$tmp" "$tmp".*' RETURN
	/usr/bin/time -f 'rss_kib=%M' -o "$tmp.time" \
		perf stat -x, -e "$EVENTS" -o "$tmp.perf" \
		timeout 600 taskset -c "$CPU" "$php" -n -d memory_limit="$lim" "$@" > "$tmp.out" 2>&1
	local rc=$? rss cyc ins res
	rss=$(grep -o 'rss_kib=[0-9]*' "$tmp.time" | cut -d= -f2)
	cyc=$(grep -E ',(cpu_core/)?cycles/?,' "$tmp.perf" | cut -d, -f1)
	ins=$(grep -E ',(cpu_core/)?instructions/?,' "$tmp.perf" | cut -d, -f1)
	res=$(grep -o 'RESULT.*\|time .*' "$tmp.out" | head -1 | tr ' ' ';')
	grep -q 'Allowed memory size' "$tmp.out" && res="FATAL_memory_limit"
	echo "$r,$cc,$b,$1,$(echo "${*:2}" | tr ' ' ':'),$lim,$rc,$rss,$cyc,$ins,$res" >> "$OUT"
}

for r in $(seq 1 "$N"); do
	for cc in $CCS; do
		if (( r % 2 )); then order="$BUILDS"; else order=$(echo $BUILDS | tr " " "\n" | tac | tr "\n" " "); fi
		for c in "${CASES[@]}"; do
			# $c is split into script and arguments on purpose
			for b in $order; do one "$r" "$cc" "$b" -1 $c; done
		done
		for c in "${LIMITED[@]}"; do
			for b in $order; do one "$r" "$cc" "$b" "$LIMIT" $c; done
		done
		for b in $order; do
			[ "$ORM" = 1 ] || continue
			php=$B/gc-$b-$cc/sapi/cli/php
			/usr/bin/time -f 'rss_kib=%M' -o orm.time perf stat -x, -e "$EVENTS" -o orm.perf \
				timeout 1800 taskset -c "$CPU" "$php" -n -d memory_limit=-1 -d auto_prepend_file="$PWD/gcstat.php" \
				orm/vendor/bin/phpunit -c orm/phpunit.xml.dist --no-progress > orm.out 2> orm.err
			rc=$?
			echo "$r,$cc,$b,orm,phpunit,-1,$rc,$(grep -o '[0-9]*$' orm.time),$(grep -E ',(cpu_core/)?cycles/?,' orm.perf | cut -d, -f1),$(grep -E ',(cpu_core/)?instructions/?,' orm.perf | cut -d, -f1),$(grep GCSTAT orm.err | tail -1 | tr ' ' ';');$(grep -E '^(OK|Tests:)' orm.out | tail -1 | tr ' ,' ';;')" >> "$OUT"
		done
		rm -f orm.time orm.perf orm.out orm.err
		echo "round $r/$N $cc done $(date +%T)" >&2
	done
done
