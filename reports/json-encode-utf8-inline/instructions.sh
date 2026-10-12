#!/bin/bash
# Instructions per json_encode() call for each case and build: perf stat over N calls minus
# the same process with 0 calls. N is set from the first build's ns/call (~50 ms per run).
#   ./instr3.sh build...
B="${BENCH_BUILDS:-$(cd "$(dirname "$0")/../../.." && pwd)/php-builds}"
count() { taskset -c 2 timeout 20 perf stat -x, -e instructions "$B/json-$1/sapi/cli/php" -n cases.php "$2" "$3" 2>&1 | command grep cpu_core | cut -d, -f1; }
for c in $(timeout 5 "$B/json-$1/sapi/cli/php" -n cases.php list); do
	ns=$(taskset -c 2 timeout 10 "$B/json-$1/sapi/cli/php" -n cases.php "$c" | awk '{print $2}')
	n=$(python3 -c "print(max(20, int(5e7 / $ns)))")
	line="$c"
	for b in "$@"; do
		i0=$(count "$b" "$c" 0); i1=$(count "$b" "$c" "$n")
		line="$line $(( (i1 - i0) / n ))"
	done
	echo "$line"
done
