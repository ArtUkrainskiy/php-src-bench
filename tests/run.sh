#!/usr/bin/env bash
# Self-tests of the tool: syntax, unit checks, rendering of saved results, suite loading, error
# paths and a tiny real run. Needs only a PHP 8.0+ (BENCH_PHP, one of the builds, or php in PATH).
#
#   tests/run.sh            run everything
#   tests/run.sh --update   rewrite tests/expected/ from the current output
#
# No "set -e" here: a failed check is counted and the rest still runs.
set -uo pipefail
cd "$(dirname "$(readlink -f "$0")")/.."

update=false
[[ "${1:-}" == "--update" ]] && update=true
php="$(./bench php)" || exit 1
export BENCH_PHP="$php" NO_COLOR=1
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

failed=0
failed_before=0
fail() { echo "FAIL  $*"; failed=$((failed + 1)); }
# Prints "ok" for a group of checks unless one of them failed since the previous group.
group() {
	((failed == failed_before)) && echo "ok    $*"
	failed_before=$failed
}
# expect_output <text> <command...>: the command's output (stdout and stderr) must contain the text
expect_output() {
	local text="$1" out
	shift
	out="$("$@" 2>&1)"
	grep -qF -- "$text" <<<"$out" || { fail "expected \"$text\" from: $*"; echo "$out" | head -5; }
}

# 1. Syntax
for file in bench lib/*.sh corpus/real/fetch.sh tests/run.sh; do
	bash -n "$file" || fail "bash syntax: $file"
done
for file in lib/*.php suites/*.php difftests/*.php tests/*.php; do
	"$php" -n -l "$file" >/dev/null || fail "php syntax: $file"
done
group "syntax"

# 2. Unit checks
out="$("$php" -n tests/unit.php 2>&1)" || { echo "$out"; fail "unit checks"; }
group "unit: $out"

# 3. Rendering: every fixture as a terminal table and as Markdown, warnings included
for fixture in tests/fixtures/*.json; do
	name="$(basename "$fixture" .json)"
	for format in txt md; do
		args=(show "$fixture")
		[[ $format == md ]] && args+=(--md)
		actual="$(./bench "${args[@]}" 2>&1)"
		expected="tests/expected/$name.$format"
		if $update; then
			printf '%s\n' "$actual" >"$expected"
		elif [[ "$actual" != "$(cat "$expected" 2>/dev/null)" ]]; then
			fail "render $name.$format (see: diff <(./bench ${args[*]} 2>&1) $expected)"
		fi
	done
done
expect_output "is not a result saved by bench run" ./bench show README.md
group "render: $(ls tests/fixtures/*.json | wc -l) fixtures"

# 4. Every suite loads; inputs from corpus/real may be absent, a suite without any case is a bug
for suite in suites/*.php; do
	name="$(basename "$suite" .php)"
	if cases="$("$php" -n lib/harness.php "$suite" '{"mode":"list"}' | "$php" -n -r '
		$list = json_decode(stream_get_contents(STDIN), true);
		$skipped = count($list["skipped"]);
		echo count($list["cases"]), " cases", $skipped ? ", $skipped inputs skipped (run corpus/real/fetch.sh)" : "";
		exit($list["cases"] || $skipped ? 0 : 1);')"; then
		group "suite $name: $cases"
	else
		fail "suite $name"
	fi
done

# 5. The committed corpus is what the generator produces
if command -v python3 >/dev/null; then
	python3 corpus/generate.py "$tmp" || fail "corpus/generate.py"
	for file in "$tmp"/*.txt; do
		cmp -s "$file" "corpus/$(basename "$file")" || fail "corpus/$(basename "$file") differs from corpus/generate.py output"
	done
	group "corpus is reproducible"
else
	echo "skip  corpus check (no python3)"
fi

# 6. Suites the harness must refuse, with a message that names the case
cat >"$tmp/bad.php" <<'SUITE'
<?php
return ['inputs' => ['list' => [3, 1, 2], 'text' => 'abc'], 'cases' => [
    'sorts its input' => ['code' => 'sort($s)', 'inputs' => ['list']],
    'raises a warning' => ['code' => 'substr_count($s, "")', 'inputs' => ['text']],
    'prints' => ['code' => 'print($s)', 'inputs' => ['text']],
]];
SUITE
expect_output "case 'sorts its input @ list': the expression modifies its input" ./bench run "$tmp/bad.php" --a "$php" --filter sorts --quick --no-save
expect_output "case 'raises a warning @ text'" ./bench run "$tmp/bad.php" --a "$php" --filter warning --quick --no-save
expect_output "does a case of the suite print something" ./bench run "$tmp/bad.php" --a "$php" --filter prints --quick --no-save
expect_output "--rounds and --samples must be at least 1" ./bench run html --a "$php" --rounds 0
expect_output "suite not found" ./bench run no-such-suite --a "$php"
group "bad suites and options are refused"

# 7. A real, tiny run; what it saves renders again; the read-only commands work
out="$(./bench run html --a "$php" --b "$php" --filter 'htmlspecialchars @ (empty|word-8)$' --quick 2>&1)"
saved="$(sed -n 's/^saved //p' <<<"$out")"
if grep -q 'htmlspecialchars @ word-8' <<<"$out" && [[ -f "$saved" ]]; then
	expect_output 'htmlspecialchars @ word-8' ./bench show "$saved"
	rm -f "$saved"
else
	echo "$out"
	fail "bench run"
fi
expect_output "kernel" ./bench check
expect_output "governor" ./bench tune status
group "bench run, show, check, tune status"

# 8. Differential test: identical output, a mismatch and a crash, with wrappers around one php
printf '#!/bin/sh\nexec "%s" "$@"\n' "$php" >"$tmp/php-a"
printf '#!/bin/sh\nDIFFERENT=1 exec "%s" "$@"\n' "$php" >"$tmp/php-differs"
printf '#!/bin/sh\nCRASH=1 exec "%s" "$@"\n' "$php" >"$tmp/php-crashes"
chmod +x "$tmp"/php-*
cat >"$tmp/generator.php" <<'GENERATOR'
<?php
// Three inputs; the second one differs with DIFFERENT=1, the process dies after the first with CRASH=1.
if (in_array('--dump', $argv, true)) {
    echo "output ", getenv('DIFFERENT') ? 'B' : 'A', "\ninput (1 bytes): 61\n";
    exit;
}
echo "0\tsame\n";
if (getenv('CRASH')) {
    exit(139);
}
echo "1\t", getenv('DIFFERENT') ? 'changed' : 'same', "\n2\tsame\n";
GENERATOR
expect_output "OK: 20 inputs, identical output" ./bench difftest html-encode "$php" "$php" --count 20
expect_output "MISMATCH: 1 of 3 inputs differ; the first is input 1" ./bench difftest "$tmp/generator.php" "$tmp/php-a" "$tmp/php-differs"
expect_output "FAILED: generator exited with status 139 on B" ./bench difftest "$tmp/generator.php" "$tmp/php-a" "$tmp/php-crashes"
expect_output "FAILED: generator exited with status 139 on A" ./bench difftest "$tmp/generator.php" "$tmp/php-crashes" "$tmp/php-a"
expect_output "no such generator" ./bench difftest no-such-generator "$php" "$php"
group "bench difftest: identical, mismatch, crash"

if ((failed)); then
	echo "$failed failed"
	exit 1
fi
echo "all passed"
