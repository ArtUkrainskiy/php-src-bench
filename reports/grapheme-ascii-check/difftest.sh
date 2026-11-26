#!/usr/bin/env bash
# difftest.sh <reference php> <php>... — runs difftest.php on the reference and on every other binary and
# prints the MD5 and the line count of each output. The reference is also listed as its own first line.
# stderr goes into the output, so a crash, a warning or a sanitizer report also counts as a difference,
# and so does a non-zero exit code. Exits 2 on a usage error or when the reference itself fails, 1 when an
# output differs or a binary fails, else 0. For an ASan build, export USE_ZEND_ALLOC=0 first.
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
if ! "$ref" -n "$here/difftest.php" > "$out" 2>&1; then
	echo "the reference $ref exits with an error:" >&2
	tail -5 "$out" >&2
	exit 2
fi
want=$(md5sum < "$out" | cut -c1-32)
echo "difftest.php $want $(wc -l < "$out") reference $ref"
status=0
for php in "$@"; do
	code=0
	"$php" -n "$here/difftest.php" > "$out" 2>&1 || code=$?
	got=$(md5sum < "$out" | cut -c1-32)
	if (( code != 0 )); then
		echo "difftest.php $got $(wc -l < "$out") EXIT $code $php"
		status=1
	elif [[ $got == "$want" ]]; then
		echo "difftest.php $got $(wc -l < "$out") same $php"
	else
		echo "difftest.php $got $(wc -l < "$out") DIFFERS $php"
		status=1
	fi
done
echo "exit $status"
exit $status
