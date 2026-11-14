#!/bin/bash
# Do the checks catch a wrong change? For each data/mutation-<N>.diff: apply it to a worktree of the
# change, build it (GCC, slim), run difftest.php against SQLite and the new php-src test, and compare
# with the output of the unchanged change. Prints one line per mutation.
# Usage: mutants.sh <php-src clone> <commit of the change> <reference difftest output (SQLite)>
# Run from the php-src-bench directory (it calls ./bench). Builds are named pdoobj-mut<N>.
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)
src=$(realpath "$1")
commit=$2
reference=$(realpath "$3")
test=ext/pdo_sqlite/tests/pdo_sqlite_fetch_obj_column_names.phpt
for diff in "$here"/data/mutation-[0-9].diff; do
    n=$(basename "$diff" .diff)
    n=${n#mutation-}
    tree=$(mktemp -d)/php-src
    git -C "$src" worktree add -q --detach "$tree" "$commit"
    git -C "$tree" apply "$diff"
    log=$(dirname "$tree")/build.log
    CC=gcc PHP_SRC=$tree BENCH_CONFIGURE_EXTRA="--enable-pdo --with-pdo-sqlite" ./bench build --slim pdoobj-mut"$n" . > "$log" 2>&1 \
        || { echo "mutation $n: the build failed, see $log" >&2; exit 1; }
    php=${BENCH_BUILDS:-$(dirname "$PWD")/php-builds}/pdoobj-mut$n/sapi/cli/php
    "$php" -n "$here/difftest.php" > "$tree/difftest-sqlite.txt" 2>&1 || true
    diff -a "$reference" "$tree/difftest-sqlite.txt" > "$here/data/mutation-$n-output.diff" || true
    lines=$(grep -c '^<' "$here/data/mutation-$n-output.diff" || true)
    # run-tests.php exits non-zero when the test fails, which is the expected result here
    result=$(cd "$tree" && { TEST_PHP_EXECUTABLE=$php "$php" run-tests.php -q -n "$test" 2>&1 || true; } \
        | grep -E '^Tests (passed|failed)' | tr -s ' ' | paste -sd' ' -)
    echo "mutation $n: difftest output lines that differ: $lines; new php-src test: $result"
    git -C "$src" worktree remove --force "$tree"
done
