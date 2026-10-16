#!/bin/bash
# The differential test matrix: dt-<build>-s<seed>.txt per build, stderr in dt-<build>-s<seed>.err.
# Compare each PR/fix build with the base build of the same compiler and seed; the ASan builds
# (seed 4) with g13-base (diff | awk '{print $3, $4}' | sort | uniq -c gives dt-summary.txt).
#   BENCH_BUILDS=<dir with the builds> ./difftest-run.sh
cd "$(dirname "$0")"
B=${BENCH_BUILDS:?set BENCH_BUILDS to the directory with the builds}
run() { env USE_ZEND_ALLOC=${3:-1} "$B/mb-$1/sapi/cli/php" -n difftest.php "$2" "${4:-20000}" > "dt-$1-s$2.txt" 2> "dt-$1-s$2.err"; }
run g13-base 1 & run g13-pr 1 & run g13-fix 1 & run g13-base 3 1 10000 &
run g13-base 2 & run g13-pr 2 & run g13-fix 2 &
wait
run g14-base 3 1 10000 & run g14-pr 3 1 10000 & run c18-base 3 1 10000 & run c18-pr 3 1 10000 &
run c20-base 3 1 10000 & run c20-pr 3 1 10000 &
wait
run g13-base 4 1 3000 & run c18-asan 4 0 3000 & run c18-fixasan 4 0 3000 &
wait
