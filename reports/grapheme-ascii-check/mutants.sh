#!/usr/bin/env bash
# mutants.sh <change build dir> <reference php> — do the checks catch a wrong change? Puts one mistake at a time
# into ext/intl/grapheme/grapheme_util.cpp of a full `bench build` of the change (a git worktree), rebuilds it
# with make, and runs two checks:
# - difftest.sh against the reference php: "caught" when it exits 1 (an output differs or the binary fails),
#   "same" when it exits 0, "error" otherwise (the reference itself failed);
# - the grapheme tests of ext/intl (ext/intl/tests/grapheme*.phpt): the number that fail.
# With WITHOUT_NEW_TEST=1 the new test grapheme_ascii_check_positions.phpt is left out of the second check.
# The last mutation reads one byte past the checked length, as master did: on the strings PHP passes it gives
# the same results, so both checks are expected to miss it.
# Starts from the committed source and restores it at the end with git checkout, then rebuilds. Removes the
# files run-tests leaves next to the grapheme tests (*.diff, *.out, *.exp, *.log, *.php, *.sh).
# Prints a Markdown table and exits 0 whatever it finds.
set -u
if (( $# != 2 )); then
	echo "usage: $0 <change build dir> <reference php>" >&2
	exit 2
fi
here=$(cd "$(dirname "$0")" && pwd)
build=$1
ref=$2
rel=ext/intl/grapheme/grapheme_util.cpp
file=$build/$rel
git -C "$build" checkout -q -- "$rel" || exit 2
cp "$file" "$file.orig"
# shellcheck disable=SC2329  # called by the EXIT trap
restore() {
	git -C "$build" checkout -q -- "$rel"
	rm -f "$file.orig"
	make -C "$build" -s -j"$(nproc)" > /dev/null 2>&1 || echo "mutants.sh: the rebuild after restoring $rel failed" >&2
}
trap restore EXIT

tests=()
for t in "$build"/ext/intl/tests/grapheme*.phpt; do
	[[ ${WITHOUT_NEW_TEST:-0} == 1 && $t == */grapheme_ascii_check_positions.phpt ]] && continue
	tests+=("${t#"$build"/}")
done

mutate() {
	local name=$1 from=$2 to=$3 diff failed code
	cp "$file.orig" "$file"
	if ! FROM=$from TO=$to python3 -c '
import os, sys
path = sys.argv[1]
text = open(path).read()
if os.environ["FROM"] and text.count(os.environ["FROM"]) != 1:
    sys.exit(1)
open(path, "w").write(text.replace(os.environ["FROM"], os.environ["TO"]) if os.environ["FROM"] else text)' "$file"; then
		echo "| $name | not applied: the code to change is not found exactly once | |"
		return
	fi
	if ! make -C "$build" -s -j"$(nproc)" > /dev/null 2>&1; then
		echo "| $name | does not build | |"
		return
	fi
	code=0
	"$here/difftest.sh" "$ref" "$build/sapi/cli/php" > /dev/null 2>&1 || code=$?
	case $code in
		0) diff=same ;;
		1) diff=caught ;;
		*) diff=error ;;
	esac
	failed=$(cd "$build" && TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php -n run-tests.php -q -n --no-color \
		"${tests[@]}" 2>&1 | grep -E '^Tests failed' | awk '{print $4}')
	(cd "$build/ext/intl/tests" && rm -f grapheme*.diff grapheme*.out grapheme*.exp grapheme*.log grapheme*.php grapheme*.sh)
	echo "| $name | $diff | ${failed:-?} |"
}

echo "| mutation | difftest.sh | grapheme tests failed (of ${#tests[@]}) |"
echo "|---|---|---|"
mutate "none (control)" "" ""
mutate "CR LF in 8-byte words not checked" \
	"if ((crlf - UINT64_C(0x0101010101010101)) & ~crlf & UINT64_C(0x8080808080808080)) {" "if (0) {"
mutate "second word read at p, not p + 1" \
	"memcpy(&next, p + 1, sizeof(next));" "memcpy(&next, p, sizeof(next));"
mutate "mask misses the top byte of a word" \
	"if (word & UINT64_C(0x8080808080808080)) {" "if (word & UINT64_C(0x0080808080808080)) {"
mutate "CR LF not checked in the tail" \
	"if (*p > 0x7f || (*p == '\r' && p[1] == '\n')) {" "if (*p > 0x7f) {"
mutate "0x80 passes as ASCII in the tail" \
	"if (*p > 0x7f || (*p == '\r' && p[1] == '\n')) {" "if (*p > 0x80 || (*p == '\r' && p[1] == '\n')) {"
mutate "last byte not checked" \
	"if (p < end && *p > 0x7f) {" "if (0) {"
mutate "word loop reads the byte after the length (as master did)" \
	"for (; end - p > 8; p += 8) {" "for (; end - p >= 8; p += 8) {"
exit 0
