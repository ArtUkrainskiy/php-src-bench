#!/bin/bash
# The full series on two cores of different CCDs, run from the report directory:
#   bash tools/full-run.sh <out dir> <php built with GCC> <php built with Clang>
# CPU 15 (sibling 31): random-key grid, edge cases, scenarios and the 1.5–3 KiB random-key cells. CPU 7 (sibling
# 23): a cross-core check of four random-key inputs, then the PHP-name grid, languages and the 1.5–3 KiB PHP-name
# cells. Other cores: CPU_A=15 SIB_A=31 CPU_B=7 SIB_B=23 in the environment. Paths must not contain spaces.
# The series run detached; each writes <out dir>/<name>.log and <out dir>/<name>/done.json at the end.
set -eu
cd "$(dirname "$0")/.."
out=$1; gcc=$2; clang=$3
a=${CPU_A:-15} sa=${SIB_A:-31} b=${CPU_B:-7} sb=${SIB_B:-23}
for c in "$a" "$sa" "$b" "$sb"; do
  [ -d "/sys/devices/system/cpu/cpu$c" ] || { echo "no CPU $c" >&2; exit 1; }
done
mkdir -p "$out"
PHP="--php gcc15=$gcc --php clang21=$clang"
CHECK="cells/controlled/any.n128.b4096.absent.json cells/controlled/unique.n8.b65536.one.json
       cells/controlled/replace.n1024.b16384.spread16.json cells/controlled/count.n32.b128.one.json"
setsid bash -c "python3 tools/run.py --out '$out/cpu15' --cpu $a --sibling $sa $PHP cells/controlled/*.json cells/counterexamples/*.json cells/scenarios/*.json cells/crossover/*.n[0-9]*.json \
  > '$out/cpu15.log' 2>&1" < /dev/null &
setsid bash -c "python3 tools/run.py --out '$out/corecheck' --cpu $b --sibling $sb $PHP $CHECK > '$out/cpu7.log' 2>&1 \
  && python3 tools/run.py --out '$out/cpu7' --cpu $b --sibling $sb $PHP cells/natural/*.json cells/languages/*.json cells/crossover/*.names*.json \
  >> '$out/cpu7.log' 2>&1" < /dev/null &
echo "started; done when $out/cpu15/done.json and $out/cpu7/done.json exist"
