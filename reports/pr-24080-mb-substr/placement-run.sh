#!/bin/bash
# Branch misses and top-down slots per call for the rows without the flag, master against a change (GCC 13.3).
#   CPU=2 ./placement-run.sh out.txt g13-base g13-fix
# Each count: N calls minus 0 calls, divided by N; three alternating passes.
B=${BENCH_BUILDS:?set BENCH_BUILDS to the directory with the builds}
CPU=${CPU:-2}
out=$1; base=$2; change=$3
cd "$(dirname "$0")"
: > "$out"
E=cpu_core/cycles/,cpu_core/instructions/,cpu_core/branch-misses/,cpu_core/slots/,cpu_core/topdown-fe-bound/,cpu_core/topdown-bad-spec/
count() {
	taskset -c "$CPU" timeout 30 perf stat -x, -e "$E" "$B/mb-$1/sapi/cli/php" -n cases.php "$2" "$3" 2>&1 |
		awk -F, '$3 ~ /cpu_core/ {gsub(/cpu_core\/|\//, "", $3); printf "%s=%s ", $3, $1} END {print ""}'
}
for c in head10@en-title-plain mid20@en-1k-plain mid20@zh-1k-plain; do
	n=${N:-200000}
	for r in 1 2 3; do
		if (( r % 2 )); then L="$base $change"; else L="$change $base"; fi
		for b in $L; do
			z=$(count "$b" "$c" 0); w=$(count "$b" "$c" "$n")
			python3 -c '
import sys
z = dict(x.split("=") for x in sys.argv[1].split())
w = dict(x.split("=") for x in sys.argv[2].split())
print(sys.argv[3], sys.argv[4], " ".join("%s=%.1f" % (k, (int(w[k]) - int(z[k])) / int(sys.argv[5])) for k in w))
' "$z" "$w" "$c" "$b" "$n" >> "$out"
		done
	done
done
