#!/usr/bin/env bash
# tests.sh <build dir>... — runs the php-src tests of ext/intl in each full build (not --slim) and prints the
# summary and the failed tests. Writes tests.log into each build directory. A directory whose name contains
# "asan" is taken as an ASan build and runs with USE_ZEND_ALLOC=0. The new test of the change,
# ext/intl/tests/grapheme_ascii_check_positions.phpt, is in the change's tree only. Exits 0; read the counts.
set -u
for dir in "$@"; do
	(
		cd "$dir" || exit 1
		[[ $dir == *asan* ]] && export USE_ZEND_ALLOC=0
		TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php -n run-tests.php -q -n --no-color -j"$(nproc)" ext/intl/tests > tests.log 2>&1
		echo "== $(basename "$dir")"
		grep -E '^Tests (passed|failed|skipped)' tests.log || echo "no summary, see $dir/tests.log"
		sed -n '/^FAILED TEST SUMMARY/,/^=====/p' tests.log | grep '\[ext/' || true
	)
done
exit 0
