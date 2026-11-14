#!/bin/bash
# php-src tests of ext/pdo_sqlite and ext/pdo_mysql, then the generic ext/pdo tests twice: against
# SQLite and against MySQL. Writes the counts and the names of failed tests to <output file>.
# Usage: tests.sh <php-src tree> <php binary> <output file> [--asan]
# The tree should be at the tested commit, so that its tests are the change's tests.
# MySQL: 127.0.0.1:53306, database bench, user root, password bench (README, Reproduce).
# JOBS sets the parallel test workers (default: nproc).
set -euo pipefail
src=$1
php=$(realpath "$2")
out=$(realpath "$3")
extra=${4:-}
cd "$src"
export TEST_PHP_EXECUTABLE=$php
export PDO_MYSQL_TEST_DSN='mysql:host=127.0.0.1;port=53306;dbname=bench'
export PDO_MYSQL_TEST_HOST=127.0.0.1 PDO_MYSQL_TEST_PORT=53306 PDO_MYSQL_TEST_DB=bench
export PDO_MYSQL_TEST_USER=root PDO_MYSQL_TEST_PASS=bench
run() {
    # run-tests.php exits non-zero when a test fails: the counts below are the result
    "$php" run-tests.php -q -j"${JOBS:-$(nproc)}" -n ${extra:+"$extra"} "$@" 2>&1 \
        | sed -n '/^Tests \(passed\|failed\|skipped\)/p; /^Expected fail/p; /^FAILED TEST SUMMARY/,/^=====/p' || true
}
{
    echo "== ext/pdo_sqlite ext/pdo_mysql"
    run ext/pdo_sqlite ext/pdo_mysql
    echo "== ext/pdo against SQLite"
    REDIR_TEST_DIR=$src/ext/pdo/tests/ PDOTEST_DSN=sqlite::memory: run ext/pdo
    echo "== ext/pdo against MySQL"
    REDIR_TEST_DIR=$src/ext/pdo/tests/ PDOTEST_DSN="$PDO_MYSQL_TEST_DSN" PDOTEST_USER=root PDOTEST_PASS=bench run ext/pdo
} > "$out"
cat "$out"
[ "$(grep -c '^Tests passed' "$out")" -eq 3 ] || { echo "tests.sh: a test run gave no result" >&2; exit 1; }
