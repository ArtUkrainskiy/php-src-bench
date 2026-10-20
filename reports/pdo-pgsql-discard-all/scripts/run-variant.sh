#!/bin/bash
# Runs in harness/ of web-request-cost at commit afd7ea6 (https://github.com/ArtUkrainskiy/web-request-cost).
# PHP stacks on PostgreSQL with PHP 8.5.11 as built by harness/stack/build-php.sh (base) and with another build of
# the same script (variant, PROTO_DIR), at a fixed 2000 req/s over 48 connections (C=50). Base and variant
# alternate within each pass, in reverse order on even passes. VIA_BOUNCER=1 puts PgBouncer in front of PostgreSQL.
#   PROTO_DIR=<build dir with php85-fpm and php85-zts> [VIA_BOUNCER=1] STACKS=fpm PASSES=5 ./run-variant.sh
# The defaults are the settings of the report (15 s warm-up, 20 s window).
set -e
H=$(cd "$(dirname "$0")" && pwd)
cd "$H"
g=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor /sys/devices/system/cpu/cpu0/cpufreq/energy_performance_preference /sys/devices/system/cpu/cpufreq/boost | paste -sd/)
[ "$g" = performance/performance/1 ] || { echo "governor $g, the series ran on performance/performance/1" >&2; exit 1; }
export STACK_CPUS=8-11,24-27 LOAD_CPUS=6-7,22-23 WARMUP=${WARMUP:-15} DURATION=${DURATION:-20}
: "${PROTO_DIR:?set PROTO_DIR}"
OUTDIR=$H/results/variant-$(date +%Y%m%d-%H%M)
mkdir -p "$OUTDIR"
LOG=$OUTDIR/run.log
variant() {   # stack base|proto
	local s=$1 v=$2 extra=()
	[ "$v" = proto ] && extra=(PHP_BUILD=$PROTO_DIR/php85-fpm PHP_ZTS_BUILD=$PROTO_DIR/php85-zts)
	if env "${extra[@]}" STMT_CACHE=0 OUT="$OUTDIR/$s-$v.jsonl" RATES=2000 bash "$H/sweep.sh" "$s" pgsql 50 > /dev/null 2> "$OUTDIR/last.err"; then
		echo "$(date +%T) $s $v ok" | tee -a "$LOG"
	else
		echo "$(date +%T) $s $v REJECTED: $(tail -c 300 "$OUTDIR/last.err" | tr '\n' ' ')" | tee -a "$LOG"
	fi
}
echo "start $(date -Is) passes=${PASSES:-5} stacks=${STACKS:-fpm} variant $(sha256sum "$PROTO_DIR/php85-fpm/sapi/cli/php" | cut -c1-16)" | tee "$LOG"
for pass in $(seq 1 "${PASSES:-5}"); do
	echo "pass $pass" >> "$LOG"
	if [ $((pass % 2)) = 1 ]; then order="base proto"; else order="proto base"; fi
	for s in ${STACKS:-fpm}; do
		for c in $order; do variant "$s" "$c"; done
	done
done
echo "done $(date -Is)" | tee -a "$LOG"
