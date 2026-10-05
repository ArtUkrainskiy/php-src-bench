#!/usr/bin/env bash
# bench difftest <generator> <buildA|php> <buildB|php> [generator args...]
#
# Differential test: runs a generator script with two PHP binaries and compares what they print.
# A generator (difftests/<name>.php, or any path) prints one line per generated input,
# "<index>\t<hash of all outputs>". On a mismatch the first differing input is run again on both
# binaries with "--dump <index>", which makes the generator print the input and every output.
set -euo pipefail
: "${BENCH_ROOT:?run this through ./bench}" "${BENCH_BUILDS:?run this through ./bench}"

usage="usage: bench difftest <generator> <buildA|php> <buildB|php> [--seed N] [--count N]"
generators="$(cd "$BENCH_ROOT/difftests" && ls ./*.php | sed 's|^\./||; s|\.php$||' | xargs)"
if [[ $# -lt 3 || "$1" == -* ]]; then
	echo "$usage" >&2
	echo "generators: $generators" >&2
	exit 2
fi

generator="$1"
if [[ ! -f "$generator" ]]; then
	generator="$BENCH_ROOT/difftests/$1.php"
	[[ -f "$generator" ]] || { echo "bench difftest: no such generator: $1 (available: $generators)" >&2; exit 2; }
fi

# A build name or a path to a php binary -> absolute path of the binary
resolve() {
	if [[ -x "$1" && ! -d "$1" ]]; then
		readlink -f "$1"
	elif [[ -x "$BENCH_BUILDS/$1/sapi/cli/php" ]]; then
		readlink -f "$BENCH_BUILDS/$1/sapi/cli/php"
	else
		echo "bench difftest: no such build or binary: $1" >&2
		exit 2
	fi
}
a="$(resolve "$2")"
b="$(resolve "$3")"
shift 3

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# Both sides run at the same time. A crash or a sanitizer abort of either one is a finding.
"$a" -n "$generator" "$@" >"$tmp/a" &
pid_a=$!
status_b=0
"$b" -n "$generator" "$@" >"$tmp/b" || status_b=$?
status_a=0
wait "$pid_a" || status_a=$?
name="$(basename "$generator" .php)"
if ((status_a != 0)); then
	echo "FAILED: $name exited with status $status_a on A ($a) after $(wc -l <"$tmp/a") inputs" >&2
	exit 1
fi
if ((status_b != 0)); then
	echo "FAILED: $name exited with status $status_b on B ($b) after $(wc -l <"$tmp/b") inputs" >&2
	exit 1
fi
if [[ ! -s "$tmp/a" ]]; then
	echo "FAILED: $name generated no inputs" >&2
	exit 1
fi

if cmp -s "$tmp/a" "$tmp/b"; then
	echo "OK: $(wc -l <"$tmp/a") inputs, identical output ($name $*)"
	exit 0
fi

# diff exits with 1 when the files differ, which is the case here
diff "$tmp/a" "$tmp/b" >"$tmp/diff" || true
index="$(grep -m1 '^[<>]' "$tmp/diff" | cut -f1 | tr -d '<> ')"
echo "MISMATCH: $(grep -c '^<' "$tmp/diff" || true) of $(wc -l <"$tmp/a") inputs differ; the first is input $index" >&2
echo "--- A: $a" >&2
echo "+++ B: $b" >&2
"$a" -n "$generator" "$@" --dump "$index" >"$tmp/dump-a" || true
"$b" -n "$generator" "$@" --dump "$index" >"$tmp/dump-b" || true
grep '^input' "$tmp/dump-a" >&2 || true
diff "$tmp/dump-a" "$tmp/dump-b" | head -20 >&2 || true
exit 1
