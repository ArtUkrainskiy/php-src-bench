#!/bin/bash
# count-worker.sh <php-cli> <out prefix> [extra php args...]
# callgrind over the worker loop (worker.php) with 30 and 60 requests; per worker request = (60 - 30) / 30.
# Prints closures created, fresh run-time caches (_emalloc under zend_create_closure_ex) and, with the
# OpenTelemetry extension loaded, observer initializations. Takes about 10 minutes per call (valgrind).
set -eu
PHP=$1 O=$2; shift 2
HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$(dirname "$O")"
for n in 30 60; do
  valgrind --tool=callgrind --callgrind-out-file="$O-$n.cg" "$PHP" -n -d opcache.enable_cli=1 -d opcache.jit=disable \
    -d opcache.file_update_protection=0 -d memory_limit=1G "$@" "$HERE/worker.php" "$HERE/apps/laravel" $n 100000 \
    > /dev/null 2> "$O-$n.log"
done
python3 "$HERE/cgcalls.py" "$O-30.cg" "$O-60.cg" 30 'zend_create_closure_ex$|observer_fcall_init$|find_withspan_attribute$'
python3 "$HERE/cgcallees.py" "$O-30.cg" "$O-60.cg" 30 zend_create_closure_ex | grep -E 'self|_emalloc'
