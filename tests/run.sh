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

# The CPU the measuring checks pin to: BENCH_TEST_CPU, or the one `bench run` would pick.
cpu="${BENCH_TEST_CPU:-$("$php" -n -r 'require "lib/environment.php"; echo default_cpu();')}"
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

# 0. bench build: options are checked before anything is built
expect_output "unknown profile 'foo'" ./bench build --profile foo x
expect_output "unknown option --bogus" ./bench build --bogus x
expect_output "usage: bench build" ./bench build
expect_output "no such compiler: no-such-cc" ./bench build --cc no-such-cc x
group "bench build options"

# 1. Syntax
for file in bench lib/*.sh corpus/real/fetch.sh tests/run.sh; do
	bash -n "$file" || fail "bash syntax: $file"
done
for file in lib/*.php suites/*.php difftests/*.php tests/*.php; do
	"$php" -n -l "$file" >/dev/null || fail "php syntax: $file"
done
# The tool runs on builds made with --disable-all: no mbstring, ctype, iconv or posix in lib/
if grep -nE '\b(mb_[a-z_]+|ctype_[a-z]+|iconv[a-z_]*|posix_[a-z_]+)\(' lib/*.php difftests/code.php | grep -v '^\S*:[0-9]*:\s*[/*]' | grep -v 'function ' | grep -v "'mb_\|\"mb_"; then
	fail "lib/ calls a function of an extension that --disable-all builds lack (see above)"
fi
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
for variant in "" --full; do
	expected="tests/expected/table${variant:+-full}.md"
	actual="$(./bench table tests/fixtures/series/compare.json --labels tests/fixtures/series/compare-labels.txt $variant 2>&1)"
	if $update; then
		printf '%s\n' "$actual" >"$expected"
	elif [[ "$actual" != "$(cat "$expected")" ]]; then
		fail "bench table $variant (see: diff <(./bench table tests/fixtures/series/compare.json --labels tests/fixtures/series/compare-labels.txt $variant) $expected)"
	fi
done
expect_output "not a series from \`bench compare\`" ./bench table tests/fixtures/single.json
group "render: $(ls tests/fixtures/*.json | wc -l) fixtures, bench table"

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

# 6. Input patterns, setup and --code
cat >"$tmp/patterns.php" <<'SUITE'
<?php
return ['inputs' => ['a-1' => 'x', 'a-2' => 'yy', 'b-1' => 'zzz'], 'cases' => [
    'c' => ['code' => 'strlen($s)', 'inputs' => ['a-*']],
    'setup' => ['code' => 'strlen($s)', 'inputs' => ['b-1'], 'setup' => '$s .= "!!"'],
]];
SUITE
cat >"$tmp/nope.php" <<'SUITE'
<?php
return ['inputs' => ['a-1' => 'x'], 'cases' => ['nope' => ['code' => 'strlen($s)', 'inputs' => ['nope-*']]]];
SUITE
out="$(./bench run "$tmp/patterns.php" --a "$php" --filter '^(c|setup) ' --quick --no-save --cpu "$cpu" 2>&1)"
grep -q 'c @ a-1' <<<"$out" && grep -q 'c @ a-2' <<<"$out" && ! grep -q 'c @ b-1' <<<"$out" || fail "input patterns: $out"
grep -qE 'setup @ b-1 +5 ' <<<"$out" || fail "setup runs before measuring (5 bytes expected): $out"
inline_before="$(ls results/inline-*.php 2>/dev/null || true)"
out="$(./bench run --code 'strpos($s, "?>")' --inputs lang:title,en:1k --a "$php" --quick --no-save --cpu "$cpu" 2>&1)"
grep -qF 'strpos($s, "?>") @ emoji-title' <<<"$out" && grep -qF 'strpos($s, "?>") @ en-1k' <<<"$out" || fail "--code: $out"
expect_output "'en-1k' comes twice" ./bench run --code 'strlen($s)' --inputs lang:1k,en:1k --a "$php"
# only the suite this test wrote: the others belong to saved results
for f in $(ls results/inline-*.php 2>/dev/null); do grep -qxF "$f" <<<"$inline_before" || rm -f "$f"; done
group "input patterns, setup, --code"

# 6b. bench report: a new report, its checks, update of its tables
rep="$tmp/report"
./bench report new "$rep" --series tests/fixtures/series/compare.json --labels tests/fixtures/series/compare-labels.txt --title 'A report' >/dev/null 2>&1 \
	|| fail "bench report new"
grep -q '^<!-- bench-table compare.json --labels compare-labels.txt --full -->' "$rep/README.md" || fail "bench report new: table block"
grep -q 'mb_substr' "$rep/README.md" || fail "bench report new: the table is filled in"
expect_output "TODO left" ./bench report check "$rep"
sed -i '/TODO/d' "$rep/README.md"
expect_output "no problems found" ./bench report check "$rep"
sed -i '0,/| −35% |/s//| −99% |/' "$rep/README.md"
grep -q -- '−99%' "$rep/README.md" || fail "test setup: no cell to change"
expect_output "differs from its series" ./bench report check "$rep"
expect_output "updated" ./bench report update "$rep"
expect_output "no problems found" ./bench report check "$rep"
printf 'See [the data](missing.json) and [this](#no-such-heading).\nПривет\n' >>"$rep/README.md"
printf 'B=/home/someone/builds\n' >"$rep/run.sh"
out="$(./bench report check "$rep" 2>&1)"
for text in "broken link (missing.json)" "no heading for the anchor" "Cyrillic text" "a path of this machine: /home/someone/"; do
	grep -qF "$text" <<<"$out" || fail "bench report check does not report: $text"
done
group "bench report new, check, update"

# 6c. bench mutate and bench why: argument errors (a real run needs a full php-src build)
mkdir -p "$tmp/notabuild"
expect_output "is not a full build" ./bench mutate "$tmp/notabuild" "$tmp/patterns.php"
expect_output "Usage: bench mutate" ./bench mutate
expect_output "Usage: bench why" ./bench why html
group "bench mutate, bench why: arguments"

# 7. Suites the harness must refuse, with a message that names the case
cat >"$tmp/bad.php" <<'SUITE'
<?php
return ['inputs' => ['list' => [3, 1, 2], 'text' => 'abc'], 'cases' => [
    'sorts its input' => ['code' => 'sort($s)', 'inputs' => ['list']],
    'raises a warning' => ['code' => 'substr_count($s, "")', 'inputs' => ['text']],
    'prints' => ['code' => 'print($s)', 'inputs' => ['text']],
]];
SUITE
expect_output "case 'sorts its input @ list': the expression modifies its input" ./bench run "$tmp/bad.php" --a "$php" --filter sorts --quick --no-save --cpu "$cpu"
expect_output "case 'raises a warning @ text'" ./bench run "$tmp/bad.php" --a "$php" --filter warning --quick --no-save --cpu "$cpu"
expect_output "does a case of the suite print something" ./bench run "$tmp/bad.php" --a "$php" --filter prints --quick --no-save --cpu "$cpu"
expect_output "--rounds and --samples must be at least 1" ./bench run html --a "$php" --rounds 0 --cpu "$cpu"
expect_output "suite not found" ./bench run no-such-suite --a "$php"
expect_output "case 'nope' uses unknown input 'nope-*'" ./bench run "$tmp/nope.php" --a "$php" --quick --no-save --cpu "$cpu"
expect_output "is not <corpus>:<size>" ./bench run --code 'strlen($s)' --inputs 'lang' --a "$php"
expect_output "a group is <name>=<A>:<B>" ./bench compare html "$php"
expect_output "reserved or used twice" ./bench compare html aa="$php":"$php"
# A second process on a locked core is refused
core="$("$php" -n -r 'require "lib/environment.php"; echo min(cpu_siblings((int) $argv[1]));' "$cpu")"
exec {lockfd}>"/tmp/php-src-bench-core$core.lock"
flock -n "$lockfd" && expect_output "CPU $cpu (or its SMT sibling) is in use by another bench process" ./bench run html --a "$php" --quick --no-save --cpu "$cpu"
exec {lockfd}>&-
group "bad suites and options are refused"

# 8. A real, tiny run; what it saves renders again; the read-only commands work
out="$(./bench run html --a "$php" --b "$php" --filter 'htmlspecialchars @ (empty|word-8)$' --quick --cpu "$cpu" 2>&1)"
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

# 9. Differential test: identical output, a mismatch and a crash, with wrappers around one php
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
out="$(./bench difftest code "$php" "$tmp/php-a" "$php" --code 'strrev($s)' --code 'substr_count($s, "a")' --setup '$s .= ""' --count 50 2>&1)"
[[ "$(grep -c 'OK: 50 inputs' <<<"$out")" == 2 ]] || fail "bench difftest code with three builds: $out"
group "bench difftest: identical, mismatch, crash, three builds, --code"

if ((failed)); then
	echo "$failed failed"
	exit 1
fi
echo "all passed"
