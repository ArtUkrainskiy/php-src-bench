#!/usr/bin/env bash
# bench difftest <generator> <buildA|php> <buildB|php> [<buildC|php>...] [generator args...]
#
# Differential test: runs a generator script with PHP binaries and compares what they print; every
# binary after the first is compared with the first.
# A generator (difftests/<name>.php, or any path) prints one line per generated input,
# "<index>\t<hash of all outputs>". On a mismatch the first differing input is run again on both
# binaries with "--dump <index>", which makes the generator print the input and every output.
set -euo pipefail
: "${BENCH_ROOT:?run this through ./bench}" "${BENCH_BUILDS:?run this through ./bench}"

usage="usage: bench difftest <generator> <A> <B> [<C>...] [--seed N] [--count N] [generator options]"
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
generator_name="$1"
shift
binaries=()
while (($#)) && [[ "$1" != -* ]]; do
	binaries+=("$(resolve "$1")")
	shift
done
if ((${#binaries[@]} < 2)); then
	echo "$usage" >&2
	exit 2
fi
a="${binaries[0]}"

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# All binaries run at the same time. A crash or a sanitizer abort of any one is a finding.
pids=()
for i in "${!binaries[@]}"; do
	"${binaries[$i]}" -n "$generator" "$@" >"$tmp/$i" 2>"$tmp/$i.err" &
	pids+=($!)
done
name="$(basename "$generator" .php)"
failed=0
for i in "${!binaries[@]}"; do
	status=0
	wait "${pids[$i]}" || status=$?
	if ((status != 0)); then
		letter="$(printf "\\x$(printf %x $((65 + i)))")"
		echo "FAILED: $name exited with status $status on $letter (${binaries[$i]}) after $(wc -l <"$tmp/$i") inputs" >&2
		head -5 "$tmp/$i.err" >&2
		failed=1
	fi
done
((failed)) && exit 1
# A sanitizer that is set to recover reports on stderr and exits 0: show what was printed.
for i in "${!binaries[@]}"; do
	if [[ -s "$tmp/$i.err" ]]; then
		echo "stderr of ${binaries[$i]}:" >&2
		head -20 "$tmp/$i.err" >&2
	fi
done
if [[ ! -s "$tmp/0" ]]; then
	echo "FAILED: $name generated no inputs" >&2
	exit 1
fi

result=0
for ((i = 1; i < ${#binaries[@]}; i++)); do
	b="${binaries[$i]}"
	label="$( ((${#binaries[@]} > 2)) && echo "${binaries[$i]}: " || true)"
	if cmp -s "$tmp/0" "$tmp/$i"; then
		echo "${label}OK: $(wc -l <"$tmp/0") inputs, identical output ($name $*)"
		continue
	fi
	result=1
	# diff exits with 1 when the files differ, which is the case here
	diff "$tmp/0" "$tmp/$i" >"$tmp/diff" || true
	index="$(grep -m1 '^[<>]' "$tmp/diff" | cut -f1 | tr -d '<> ')"
	echo "${label}MISMATCH: $(grep -c '^<' "$tmp/diff" || true) of $(wc -l <"$tmp/0") inputs differ; the first is input $index" >&2
	echo "--- A: $a" >&2
	echo "+++ B: $b" >&2
	"$a" -n "$generator" "$@" --dump "$index" >"$tmp/dump-a" || true
	"$b" -n "$generator" "$@" --dump "$index" >"$tmp/dump-b" || true
	grep '^input' "$tmp/dump-a" >&2 || true
	diff "$tmp/dump-a" "$tmp/dump-b" | head -20 >&2 || true
done
exit "$result"
