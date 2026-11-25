#!/usr/bin/env bash
# difftest.sh <reference php> <php>... — runs difftest-chars.php and difftest-random.php (50,000 random formats,
# seed 1) on the reference and on every other binary, and prints the MD5 and the line count of each output.
# The reference is also listed as its own first line. stderr goes into the output, so a crash, a warning or a
# sanitizer report also counts as a difference. A non-zero exit code of a binary counts as a failure too.
# Exits 2 when the reference itself fails, 1 when an output differs or a binary fails, else 0.
# For an ASan build, export USE_ZEND_ALLOC=0 first.
set -u
if (( $# < 2 )); then
	echo "usage: $0 <reference php> <php>..." >&2
	exit 2
fi
here=$(cd "$(dirname "$0")" && pwd)
out=$(mktemp)
trap 'rm -f "$out"' EXIT
ref=$1
shift
status=0
for script in difftest-chars.php difftest-random.php; do
	args=()
	[[ $script == difftest-random.php ]] && args=(50000 1)
	if ! "$ref" -n "$here/$script" ${args[@]+"${args[@]}"} > "$out" 2>&1; then
		echo "$script: the reference $ref exits with an error:" >&2
		tail -5 "$out" >&2
		exit 2
	fi
	want=$(md5sum < "$out" | cut -c1-32)
	echo "$script $want $(wc -l < "$out") reference $ref"
	for php in "$@"; do
		code=0
		"$php" -n "$here/$script" ${args[@]+"${args[@]}"} > "$out" 2>&1 || code=$?
		sum=$(md5sum < "$out" | cut -c1-32)
		mark=same
		if [[ $sum != "$want" ]]; then mark=DIFFERENT; status=1; fi
		if (( code != 0 )); then mark="FAILED (exit $code)"; status=1; fi
		echo "$script $sum $(wc -l < "$out") $mark $php"
	done
done
echo "exit $status"
exit $status
