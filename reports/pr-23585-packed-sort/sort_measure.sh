#!/bin/bash
# Instruction-count matrix for PR #23585 sort optimization.
# sort cost = instructions(sort mode) - instructions(nop mode); change head vs base.
# Run from the report dir (where sort_bench.php lives). Build dirs:
#   $BUILDS/pr23585-{base,head}-$CC   (BUILDS defaults to ~/php-builds)
# $CC is the build-dir suffix, i.e. the compiler version bench stored
#   (gcc13, gcc14, clang18, clang20), not the --cc token.
# CORES_INS: CPU list for taskset (default 12-19); any isolated core(s) work.
# Needs perf with kernel.perf_event_paranoid <= 1.
set -u
set -o pipefail
cd "$(dirname "$0")"
CC=${1:-gcc13}
CORES_INS=${CORES_INS:-12-19}
B=${BUILDS:-$HOME/php-builds}/pr23585-base-$CC/sapi/cli/php
H=${BUILDS:-$HOME/php-builds}/pr23585-head-$CC/sapi/cli/php

ins(){ # bin type size batch op mode -> instruction count (handles hybrid cpu_atom/cpu_core)
  local out v
  out=$(taskset -c "$CORES_INS" perf stat -e instructions:u "$1" -n sort_bench.php "$2" "$3" "$4" "$5" "$6" 2>&1)
  # The run must finish: sort mode prints "done", nop mode prints a count. A crash
  # (OOM, segfault) leaves no marker, yet perf still reports instructions.
  if ! printf '%s\n' "$out" | grep -qxE 'done|[0-9]+'; then
    echo "run did not complete for $1 $2 $3 $5 $6:" >&2; printf '%s\n' "$out" | tail -3 >&2; exit 1
  fi
  v=$(printf '%s\n' "$out" | grep -E 'instructions' | grep -vE '<not' | head -1 | sed 's/,//g' | awk '{print $1}')
  case "$v" in ''|*[!0-9]*) echo "perf parse failed for $1 $2 $3 $5 $6" >&2; exit 1;; esac
  echo "$v"
}

declare -A BATCH=( [10]=60000 [64]=20000 [65535]=60 )

echo "== $CC =="
printf "%-7s %-8s %-6s %10s %10s %9s\n" op type size base head "head/base"
for op in sort rsort usort; do
 for t in ints floats strings; do
  for sz in 10 64 65535; do
    bn=${BATCH[$sz]}
    bnop=$(ins "$B" "$t" "$sz" "$bn" "$op" nop);  bsort=$(ins "$B" "$t" "$sz" "$bn" "$op" sort)
    hnop=$(ins "$H" "$t" "$sz" "$bn" "$op" nop);  hsort=$(ins "$H" "$t" "$sz" "$bn" "$op" sort)
    awk -v bs="$bsort" -v bn="$bnop" -v hs="$hsort" -v hn="$hnop" \
        -v op="$op" -v t="$t" -v sz="$sz" -v b="$bn" 'BEGIN{
      bd=bs-bn; hd=hs-hn;
      if(bd<=0){printf "%-7s %-8s %-6s  (bad: base sort cost <= 0, unexpected)\n",op,t,sz}
      else {printf "%-7s %-8s %-6s %10d %10d %+8.1f%%\n", op,t,sz, bd/b, hd/b, (hd-bd)/bd*100}
    }'
  done
 done
done
