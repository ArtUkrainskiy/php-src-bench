#!/bin/bash
# Cycles and instructions per call for pairs of builds (master, change),
# PASSES alternating passes per case, one fresh series. Pinned to CPU $CPU.
#   CPU=2 PASSES=5 [CASES='a b'] ./pairs-run.sh out.txt name:base:change [name:base:change ...]
# Output lines: <name> <base|change> <case> <cycles> <instructions>
B=${BENCH_BUILDS:?set BENCH_BUILDS to the directory with the builds}
CPU=${CPU:-2}
PASSES=${PASSES:-5}
PREFIX=${PREFIX-}
out=$1; shift
cd "$(dirname "$0")"
: > "$out"
count() {
	taskset -c "$CPU" timeout 20 perf stat -x, -e cycles,instructions "$B/$PREFIX$1/sapi/cli/php" -n cases.php "$2" "$3" 2>&1 |
		awk -F, '$3 ~ /cpu_atom/ {next} $3 ~ /(^|\/)cycles\/?$/ {c=$1} $3 ~ /(^|\/)instructions\/?$/ {i=$1} END {print c, i}'
}
for g in "$@"; do
	IFS=: read -r name base change <<<"$g"
	for c in ${CASES:-$(timeout 30 "$B/$PREFIX$base/sapi/cli/php" -n cases.php list)}; do
		ns=$(taskset -c "$CPU" timeout 10 "$B/$PREFIX$base/sapi/cli/php" -n cases.php "$c" | awk '{print $2}')
		n=$(python3 -c "print(max(20, int(${NSCALE:-5e7} / $ns)))")
		for ((r = 1; r <= PASSES; r++)); do
			if (( r % 2 )); then L="$base:base $change:change"; else L="$change:change $base:base"; fi
			for x in $L; do
				b=${x%%:*}; role=${x##*:}
				read -r c0 i0 < <(count "$b" "$c" 0)
				read -r c1 i1 < <(count "$b" "$c" "$n")
				echo "$name $role $c $(( (c1 - c0) / n )) $(( (i1 - i0) / n ))" >> "$out"
			done
		done
	done
done
