#!/usr/bin/env bash
# tests.sh <build dir>... — runs the php-src tests of ext/date in each full build (not --slim) and prints the
# summary and the failed tests. Writes tests.log into each build directory. A directory whose name contains
# "asan" is taken as an ASan build and runs with USE_ZEND_ALLOC=0. The new test of the change,
# ext/date/tests/date_format_escaped_timezone_chars.phpt, is in the change's tree only; copy it into a master
# build to run it there. Exits 0; read the counts.
set -u
for dir in "$@"; do
	(
		cd "$dir" || exit 1
		[[ $dir == *asan* ]] && export USE_ZEND_ALLOC=0
		TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php -n run-tests.php -q -n --no-color -j"$(nproc)" ext/date/tests > tests.log 2>&1
		echo "== $(basename "$dir")"
		grep -E '^Tests (passed|failed|skipped)' tests.log
		sed -n '/^FAILED TEST SUMMARY/,/^=====/p' tests.log | grep '\[ext/' || true
	)
done
exit 0
