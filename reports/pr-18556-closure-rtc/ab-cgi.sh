#!/bin/bash
# ab-cgi.sh <out> <passes> <warmup> <n> <docroot> <uri> <cgiA> <cgiB>
# Alternating A/B of php-cgi -T (cgi.sh) on CPU ${CPU:-9}: cycles and instructions of the whole process
# (user + kernel: startup, the warm-up requests and n measured requests) divided by n; the overhead is the same on both sides.
# Extra php-cgi arguments for both sides: $AB_EXTRA. Raw lines: <pass> <A|B> <cycles> <instructions>.
# Prints per pass: cycles per request of A and B and the B/A ratios of cycles and instructions.
set -eu
OUT=$1 P=$2 W=$3 N=$4 D=$5 U=$6 A=$7 B=$8
HERE=$(cd "$(dirname "$0")" && pwd)
[ -e "$OUT" ] && { echo "$OUT exists" >&2; exit 1; }
: > "$OUT"
for p in $(seq 1 "$P"); do
  if [ $((p % 2)) -eq 1 ]; then order="A B"; else order="B A"; fi
  for s in $order; do
    if [ "$s" = A ]; then C=$A; else C=$B; fi
    perf stat -x, -o "$OUT.perf" -e cycles,instructions taskset -c "${CPU:-9}" \
      "$HERE/cgi.sh" "$C" "$D" "$U" "$W" "$N" ${AB_EXTRA:-} > /dev/null 2>&1
    r=$(awk -F, '/cycles|instructions/{printf "%s ", $1}' "$OUT.perf")
    [ -n "$r" ] || { echo "perf counted nothing" >&2; exit 1; }
    echo "$p $s $r" >> "$OUT"
  done
done
rm -f "$OUT.perf"
awk -v n="$N" '{c[$1,$2]=$3; i[$1,$2]=$4; if($1>m)m=$1}
  END{for(p=1;p<=m;p++) printf "pass %d  A %.0f  B %.0f cyc/req  B/A cycles %.4f  instr %.4f\n", p, c[p,"A"]/n, c[p,"B"]/n, c[p,"B"]/c[p,"A"], i[p,"B"]/i[p,"A"]}' "$OUT"
