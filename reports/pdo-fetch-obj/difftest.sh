#!/bin/bash
# Runs difftest.php with each build, against SQLite and against MySQL, and prints the md5 of every
# output. Stops at the first run that fails. Outputs: <out dir>/<build>-sqlite.txt and -mysql.txt.
# Usage: difftest.sh <out dir> <php binary>...
# MySQL: the DSN in PDO_MYSQL_DSN, user root, password bench (README, Reproduce).
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)
: "${PDO_MYSQL_DSN:?set PDO_MYSQL_DSN, see README, Reproduce step 3}"
out=$1
shift
mkdir -p "$out"
for php in "$@"; do
    # <builds>/<name>/sapi/cli/php
    name=$(basename "$(dirname "$(dirname "$(dirname "$php")")")")
    # USE_ZEND_ALLOC=0 lets ASan see every allocation; release builds print the same with it.
    USE_ZEND_ALLOC=0 "$php" -n "$here/difftest.php" > "$out/$name-sqlite.txt"
    USE_ZEND_ALLOC=0 "$php" -n "$here/difftest.php" "$PDO_MYSQL_DSN" root bench > "$out/$name-mysql.txt"
done
cd "$out"
md5sum -- *-sqlite.txt *-mysql.txt
