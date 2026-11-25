#!/usr/bin/env bash
# mutants.sh <change build dir> <reference php> — do the checks catch a wrong change? Puts one mistake at a time
# into ext/date/php_date.c of a full build of the change, rebuilds it with make, and runs two checks:
# - difftest.sh against the reference php: "caught" when it exits 1, that is when the output, stderr included
#   (a crash or a sanitizer report), differs from the reference;
# - the new test date_format_escaped_timezone_chars.phpt: "fails" unless run-tests reports 1 passed test.
# Restores the file and rebuilds at the end. Prints a Markdown table and exits 0 whatever it finds.
# Run it once on a release build and once on an ASan build (with USE_ZEND_ALLOC=0): a mistake that only leaks
# memory shows on ASan only.
set -u
if (( $# != 2 )); then
	echo "usage: $0 <change build dir> <reference php>" >&2
	exit 2
fi
here=$(cd "$(dirname "$0")" && pwd)
build=$1
ref=$2
file=$build/ext/date/php_date.c
cp "$file" "$file.orig"
trap 'cp "$file.orig" "$file"; rm -f "$file.orig"; make -C "$build" -s -j"$(nproc)" > /dev/null 2>&1' EXIT

mutate() {
	local name=$1 from=$2 to=$3 diff phpt
	cp "$file.orig" "$file"
	if ! FROM=$from TO=$to python3 -c '
import os, sys
path = sys.argv[1]
text = open(path).read()
if text.count(os.environ["FROM"]) != 1:
    sys.exit(1)
open(path, "w").write(text.replace(os.environ["FROM"], os.environ["TO"]))' "$file"; then
		echo "| $name | not applied: the code to change is not found exactly once | |"
		return
	fi
	if ! make -C "$build" -s -j"$(nproc)" > /dev/null 2>&1; then
		echo "| $name | does not build | |"
		return
	fi
	"$here/difftest.sh" "$ref" "$build/sapi/cli/php" > /dev/null 2>&1 && diff=missed || diff=caught
	if (cd "$build" && TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php -n run-tests.php -q -n --no-color \
		ext/date/tests/date_format_escaped_timezone_chars.phpt 2>&1 | grep -qE '^Tests passed +: +1 '); then
		phpt=passes
	else
		phpt=fails
	fi
	echo "| $name | $diff | $phpt |"
}

echo "| mutation | difftest.sh | new test |"
echo "|---|---|---|"
mutate "'T' does not build the offset" \
	$'case \'T\':\n\t\t\t\tdate_format_need_offset(&offset, t, localtime);' $'case \'T\':'
mutate "'e' on an abbreviation does not build the offset" \
	$'case TIMELIB_ZONETYPE_ABBR:\n\t\t\t\t\t\t\t\t  date_format_need_offset(&offset, t, localtime);' $'case TIMELIB_ZONETYPE_ABBR:'
mutate "the offset is freed when it was not built" \
	$'if (offset) {\n\t\ttimelib_time_offset_dtor(offset);' $'if (localtime) {\n\t\ttimelib_time_offset_dtor(offset);'
mutate "the offset is built again at every time zone character" \
	"if (localtime && !*offset) {" "if (localtime) {"
exit 0
