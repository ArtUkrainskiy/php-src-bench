#!/bin/bash
# ext/mysqlnd, ext/mysqli, ext/pdo_mysql tests of one build (a ZTS debug build configured with --with-openssl) against MySQL 8.4 on 127.0.0.1:53306, root/bench, database test.
#   ./run-tests.sh <php build directory> <output directory>
set -e
b=$(cd "$1" && pwd)
out=$(mkdir -p "$2" && cd "$2" && pwd)
mkdir -p "$out"
export MYSQL_TEST_HOST=127.0.0.1 MYSQL_TEST_PORT=53306 MYSQL_TEST_USER=root MYSQL_TEST_PASSWD=bench MYSQL_TEST_DB=test
export PDO_MYSQL_TEST_DSN='mysql:host=127.0.0.1;port=53306;dbname=test' PDO_MYSQL_TEST_USER=root PDO_MYSQL_TEST_PASS=bench
export TEST_PHP_EXECUTABLE=$b/sapi/cli/php NO_INTERACTION=1 REPORT_EXIT_STATUS=0
cd "$b"
"$b/sapi/cli/php" run-tests.php -q -j4 --show-diff -W "$out/summary.txt" \
	ext/mysqlnd ext/mysqli ext/pdo_mysql > "$out/output.txt" 2>&1 || true
command grep -E '^(FAIL|LEAK|BORK|SKIP)' "$out/output.txt" | sort > "$out/nonpass.txt" || true
command grep -E 'Tests (passed|failed|skipped)|Number of tests' "$out/output.txt" | head -8
