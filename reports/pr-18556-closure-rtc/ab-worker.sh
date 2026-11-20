#!/bin/bash
# ab-worker.sh <out> <passes> <n_lo> <n_hi> <phpA> <phpB> [extra php args...]
# Alternating A/B of the Laravel worker loop (worker.php, CLI, opcache on, JIT off) on CPU ${CPU:-9}:
# cycles and instructions per worker request = (run with n_hi requests - run with n_lo requests) / (n_hi - n_lo),
# so the one-time boot is cancelled out.
set -eu
OUT=$1 P=$2 LO=$3 HI=$4 A=$5 B=$6; shift 6
[ -e "$OUT" ] && { echo "$OUT exists" >&2; exit 1; }
X=("$@")
L=$(cd "$(dirname "$0")" && pwd)/apps/laravel
W=$(cd "$(dirname "$0")" && pwd)/worker.php
run() { # php n [extra...]
  local php=$1 n=$2; shift 2
  perf stat -x, -o "$OUT.tmp" -e cycles,instructions taskset -c "${CPU:-9}" "$php" -n \
    -d opcache.enable_cli=1 -d opcache.jit=disable -d opcache.file_update_protection=0 -d opcache.validate_timestamps=0 \
    -d memory_limit=1G "$@" "$W" "$L" "$n" 100000000 > /dev/null 2>&1
  awk -F, '/cycles|instructions/{printf "%s ", $1}' "$OUT.tmp"
}
: > "$OUT"
for p in $(seq 1 "$P"); do
  if [ $((p % 2)) -eq 1 ]; then order="A B"; else order="B A"; fi
  for s in $order; do
    if [ "$s" = A ]; then C=$A; else C=$B; fi
    lo=$(run "$C" "$LO" "${X[@]}"); hi=$(run "$C" "$HI" "${X[@]}")
    echo "$p $s $lo $hi" >> "$OUT"
  done
done
rm -f "$OUT.tmp"
awk -v d=$((HI - LO)) '{c[$1,$2]=($5-$3)/d; i[$1,$2]=($6-$4)/d; if($1>m)m=$1}
  END{for(p=1;p<=m;p++) printf "pass %d  A %.0f  B %.0f cyc/req  B/A cycles %.4f  instr %.4f\n", p, c[p,"A"], c[p,"B"], c[p,"B"]/c[p,"A"], i[p,"B"]/i[p,"A"]}' "$OUT"
