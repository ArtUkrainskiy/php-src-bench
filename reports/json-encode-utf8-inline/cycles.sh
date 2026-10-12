#!/bin/bash
# Cycles per json_encode() call (perf stat over N calls minus 0 calls), less sensitive to
# frequency changes than ns. Builds alternate forward and backward, 3 passes; prints the
# median ratio to the first build and the spread.
#   ./cycles.sh out.txt build...
B="${BENCH_BUILDS:-$(cd "$(dirname "$0")/../../.." && pwd)/php-builds}"
out=$1; shift
: > "$out"
count() { taskset -c 2 timeout 20 perf stat -x, -e cycles "$B/json-$1/sapi/cli/php" -n cases.php "$2" "$3" 2>&1 | command grep cpu_core | cut -d, -f1; }
fwd=("$@"); rev=(); for ((i=${#fwd[@]}-1; i>=0; i--)); do rev+=("${fwd[i]}"); done
for c in $(timeout 5 "$B/json-$1/sapi/cli/php" -n cases.php list); do
	ns=$(taskset -c 2 timeout 10 "$B/json-$1/sapi/cli/php" -n cases.php "$c" | awk '{print $2}')
	n=$(python3 -c "print(max(20, int(5e7 / $ns)))")
	for r in 1 2 3; do
		if (( r % 2 )); then L=("${fwd[@]}"); else L=("${rev[@]}"); fi
		for b in "${L[@]}"; do
			i0=$(count "$b" "$c" 0); i1=$(count "$b" "$c" "$n")
			echo "$b $c $(( (i1 - i0) / n ))" >> "$out"
		done
	done
done
python3 - "$out" "$@" <<'PY'
import collections, statistics as st, sys
out, base, rest = sys.argv[1], sys.argv[2], sys.argv[3:]
d = collections.defaultdict(lambda: collections.defaultdict(list))
for l in open(out):
    b, c, cy = l.split(); d[c][b].append(int(cy))
for c, v in d.items():
    m = st.median(v[base])
    print(f"{c:28}{m:9.0f} " + ' '.join(f"{st.median(v[b])/m:6.3f}[{(max(v[b])-min(v[b]))/m:.2f}]" for b in rest))
PY
