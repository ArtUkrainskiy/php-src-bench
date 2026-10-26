#!/bin/bash
# Cycles on one P-core for a headline case, base vs head, paired passes.
# sort cost in cycles = cycles(sort) - cycles(nop), per sort. head/base% per pass.
# The nop baseline is measured once (generation cycles are stable); the sort
# passes are paired base/head. Take the median of the head/base% column.
# Run from the report dir. Build dirs: $BUILDS/pr23585-{base,head}-$CC.
# CORE_CYC: a single quiet CPU for taskset (default 2).
# Needs perf with kernel.perf_event_paranoid <= 1.
set -u
set -o pipefail
cd "$(dirname "$0")"
CC=${1:-gcc13}
SIZE=${2:-65535}
BATCH=${3:-60}
TYPE=${4:-ints}
OP=${5:-sort}
CORE_CYC=${CORE_CYC:-2}
B=${BUILDS:-$HOME/php-builds}/pr23585-base-$CC/sapi/cli/php
H=${BUILDS:-$HOME/php-builds}/pr23585-head-$CC/sapi/cli/php

cyc(){ # bin mode -> cycle count (handles hybrid cpu_atom/cpu_core)
  local out v
  out=$(taskset -c "$CORE_CYC" perf stat -e cycles:u "$1" -n sort_bench.php "$TYPE" "$SIZE" "$BATCH" "$OP" "$2" 2>&1)
  if ! printf '%s\n' "$out" | grep -qxE 'done|[0-9]+'; then
    echo "run did not complete for $1 $2:" >&2; printf '%s\n' "$out" | tail -3 >&2; exit 1
  fi
  v=$(printf '%s\n' "$out" | grep -E 'cycles' | grep -vE '<not' | head -1 | sed 's/,//g' | awk '{print $1}')
  case "$v" in ''|*[!0-9]*) echo "perf parse failed for $1 $2" >&2; exit 1;; esac
  echo "$v"
}

echo "== $CC $OP $TYPE size=$SIZE batch=$BATCH (core $CORE_CYC) =="
bnop=$(cyc "$B" nop); hnop=$(cyc "$H" nop)
printf "pass %6s %12s %12s %9s\n" "" base head "head/base"
for p in 1 2 3 4 5; do
  bs=$(cyc "$B" sort); hs=$(cyc "$H" sort)   # base then head one pass
  awk -v bs="$bs" -v bn="$bnop" -v hs="$hs" -v hn="$hnop" -v b="$BATCH" -v p="$p" 'BEGIN{
    bd=(bs-bn)/b; hd=(hs-hn)/b;
    printf "p%-2d %12d %12d %+8.1f%%\n", p, bd, hd, (hd-bd)/bd*100
  }'
done
