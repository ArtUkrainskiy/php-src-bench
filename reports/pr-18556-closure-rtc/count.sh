#!/bin/bash
# count.sh <php-cgi> <docroot> <uri> <out prefix> [extra php-cgi args...]
# callgrind over cgi.sh with 2 warm-up requests and then 2 or 12 measured ones; per-request numbers are
# (12 - 2) / 10, printed by cgcalls.py / cgcallees.py:
#   closures created, fresh run-time caches (_emalloc called from zend_create_closure_ex),
#   observer initializations (observer_fcall_init of the OpenTelemetry extension, when loaded).
# Takes a few minutes per call (valgrind).
set -eu
C=$1 D=$2 U=$3 O=$(realpath -m "$4"); shift 4
HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$(dirname "$O")"
for n in 2 12; do
  valgrind --tool=callgrind --trace-children=yes --callgrind-out-file="$O-$n.%p.cg" \
    "$HERE/cgi.sh" "$C" "$D" "$U" 2 $n "$@" > /dev/null 2> "$O-$n.log"
done
a=$(ls -S "$O"-2.*.cg | head -1); b=$(ls -S "$O"-12.*.cg | head -1)
python3 "$HERE/cgcalls.py" "$a" "$b" 10 'zend_create_closure_ex$|observer_fcall_init$|find_withspan_attribute$'
python3 "$HERE/cgcallees.py" "$a" "$b" 10 zend_create_closure_ex | grep -E 'self|_emalloc'
