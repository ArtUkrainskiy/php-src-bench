#!/bin/bash
# series.sh <out dir> [group...]: the A/B series of the report, one file pair per row (<name>.txt raw,
# <name>.sum per pass). About 35 minutes for all groups. Groups (default: all):
#   master    master -> pr: GCC, clang, GCC with OTel on three pages; worker loop: GCC, clang, GCC with OTel  (~11 min)
#   place     master -> placement and placement -> pr, GCC, three pages                             (~4 min)
#   cold      master -> cold (pr with the allocation in a cold function), GCC, three pages          (~2 min)
#   aa        master -> master, the same GCC build on both sides: the noise floor, three pages, worker (~5 min)
#   pr        placement -> pr, clang, three pages (GCC: in place)                                   (~2 min)
#   otel      with OpenTelemetry: placement -> pr; placement -> placement+OTel; OTel -> OTel lazy    (~7 min)
#   worker    Laravel worker loop: placement -> pr without OTel, with OTel, with OTel lazy          (~6 min)
# data/main is master, place, cold and aa; data/earlier is pr, otel and worker, plus gcc-master-pr-*,
# gcc-master-placement-sf-list and gcc-placement-pr-* from earlier runs of what are now the master and place groups.
# Needs: builds/{master,placement,pr,cold}-gcc15, builds/{master,placement,pr}-clang21 (build.sh), apps/ (apps.sh),
# opentelemetry.so and opentelemetry-lazy.so in builds/placement-gcc15 (otel.sh).
# CPU=<core> pins every measured process (default 9); keep the core and its SMT sibling idle.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
OUT=$1; shift
GROUPS_=${*:-master place cold aa pr otel worker}
[ -e "$OUT" ] && { echo "$OUT exists" >&2; exit 1; }
mkdir -p "$OUT"
perf stat -e cycles true > /dev/null 2>&1 || { echo "perf can't count cycles" >&2; exit 1; }
B=$HERE/builds L=$HERE/apps/laravel/public S=$HERE/apps/sfdemo/public
cgi() { echo "$B/$1/sapi/cgi/php-cgi"; }
cli() { echo "$B/$1/sapi/cli/php"; }
for b in master-gcc15 placement-gcc15 pr-gcc15 cold-gcc15 master-clang21 placement-clang21 pr-clang21; do
  [ -x "$(cgi $b)" ] || { echo "missing build $b" >&2; exit 1; }
done
pages() { # <name prefix> <A php-cgi> <B php-cgi>
  "$HERE/ab-cgi.sh" "$OUT/$1-lar-home.txt" 10 50 800 "$L" / "$2" "$3" > "$OUT/$1-lar-home.sum"
  "$HERE/ab-cgi.sh" "$OUT/$1-lar-users.txt" 10 10 120 "$L" /users "$2" "$3" > "$OUT/$1-lar-users.sum"
  "$HERE/ab-cgi.sh" "$OUT/$1-sf-list.txt" 10 20 400 "$S" /en/blog/ "$2" "$3" > "$OUT/$1-sf-list.sum"
}
OT="-d auto_prepend_file=$HERE/otel-hooks.php -d extension"
for g in $GROUPS_; do
  echo "group $g: $(date +%T)"
  case $g in
  pr)
    pages clang-placement-pr "$(cgi placement-clang21)" "$(cgi pr-clang21)" ;;
  master)
    so=$B/placement-gcc15/opentelemetry.so
    pages gcc-master-pr "$(cgi master-gcc15)" "$(cgi pr-gcc15)"
    pages clang-master-pr "$(cgi master-clang21)" "$(cgi pr-clang21)"
    AB_EXTRA="$OT=$so" pages otel-master-pr "$(cgi master-gcc15)" "$(cgi pr-gcc15)"
    "$HERE/ab-worker.sh" "$OUT/worker-master-pr.txt" 8 200 1000 "$(cli master-gcc15)" "$(cli pr-gcc15)" > "$OUT/worker-master-pr.sum"
    "$HERE/ab-worker.sh" "$OUT/worker-clang-master-pr.txt" 8 200 1000 "$(cli master-clang21)" "$(cli pr-clang21)" > "$OUT/worker-clang-master-pr.sum"
    "$HERE/ab-worker.sh" "$OUT/worker-otel-master-pr.txt" 8 200 1000 "$(cli master-gcc15)" "$(cli pr-gcc15)" \
      -d auto_prepend_file="$HERE/otel-hooks.php" -d extension="$so" > "$OUT/worker-otel-master-pr.sum" ;;
  place)
    pages gcc-master-placement "$(cgi master-gcc15)" "$(cgi placement-gcc15)"
    pages gcc-placement-pr "$(cgi placement-gcc15)" "$(cgi pr-gcc15)" ;;
  cold)
    pages gcc-master-cold "$(cgi master-gcc15)" "$(cgi cold-gcc15)" ;;
  aa)
    pages gcc-master-master "$(cgi master-gcc15)" "$(cgi master-gcc15)"
    "$HERE/ab-worker.sh" "$OUT/worker-master-master.txt" 8 200 1000 "$(cli master-gcc15)" "$(cli master-gcc15)" > "$OUT/worker-master-master.sum" ;;
  otel)
    # the same extension file for both sides: an .so built against placement-gcc15 loads into pr-gcc15 (same ABI)
    so=$B/placement-gcc15/opentelemetry.so lazy=$B/placement-gcc15/opentelemetry-lazy.so
    AB_EXTRA="$OT=$so" pages otel-placement-pr "$(cgi placement-gcc15)" "$(cgi pr-gcc15)"
    # OTel cost and the lazy WithSpan check: same php-cgi, the extension is added through wrappers
    mkdir -p "$OUT/wrap"
    printf '#!/bin/sh\nexec %s %s "$@"\n' "$(cgi placement-gcc15)" "$OT=$so" > "$OUT/wrap/otel"
    printf '#!/bin/sh\nexec %s %s "$@"\n' "$(cgi placement-gcc15)" "$OT=$lazy" > "$OUT/wrap/otel-lazy"
    chmod +x "$OUT/wrap/otel" "$OUT/wrap/otel-lazy"
    pages otel-cost "$(cgi placement-gcc15)" "$OUT/wrap/otel"
    pages otel-lazy "$OUT/wrap/otel" "$OUT/wrap/otel-lazy" ;;
  worker)
    so=$B/placement-gcc15/opentelemetry.so lazy=$B/placement-gcc15/opentelemetry-lazy.so
    "$HERE/ab-worker.sh" "$OUT/worker-placement-pr.txt" 8 200 1000 "$(cli placement-gcc15)" "$(cli pr-gcc15)" > "$OUT/worker-placement-pr.sum"
    "$HERE/ab-worker.sh" "$OUT/worker-otel-placement-pr.txt" 8 200 1000 "$(cli placement-gcc15)" "$(cli pr-gcc15)" \
      -d auto_prepend_file="$HERE/otel-hooks.php" -d extension="$so" > "$OUT/worker-otel-placement-pr.sum"
    "$HERE/ab-worker.sh" "$OUT/worker-otel-lazy-placement-pr.txt" 8 200 1000 "$(cli placement-gcc15)" "$(cli pr-gcc15)" \
      -d auto_prepend_file="$HERE/otel-hooks.php" -d extension="$lazy" > "$OUT/worker-otel-lazy-placement-pr.sum" ;;
  *) echo "unknown group $g" >&2; exit 1 ;;
  esac
done
python3 "$HERE/summary.py" "$OUT"
