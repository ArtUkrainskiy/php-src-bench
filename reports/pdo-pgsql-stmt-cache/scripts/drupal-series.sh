#!/bin/bash
# A series: every variant once per pass, PASSES passes, the variants in the listed order in odd passes and in
# reverse order in even passes; the same 2000 URLs (make-urls.py seed 42) in every run. A variant is build:mode;
# build "base2" is build-base again under another name, for an A/A control. BOUNCER=1 is passed to drupal-run.sh.
# Appends one JSON line per run to the output file and stops at the first run that fails.
#   [BOUNCER=1] VARIANTS="base:emulated base:emulated-persistent ..." PASSES=5 ./drupal-series.sh <out.jsonl>
set -eo pipefail
cd "$(dirname "$0")"
out=${1:?output file}
python3 make-urls.py 2000 42 > series-urls.csv
read -ra variants <<< "${VARIANTS:?set VARIANTS}"
for pass in $(seq 1 "${PASSES:-5}"); do
	order=("${variants[@]}")
	if [ $((pass % 2)) = 0 ]; then order=(); for ((i = ${#variants[@]} - 1; i >= 0; i--)); do order+=("${variants[i]}"); done; fi
	for v in "${order[@]}"; do
		bash drupal-run.sh "${v%%:*}" "${v#*:}" "p$pass-${v%%:*}-${v#*:}" series-urls.csv | tee -a "$out" | cut -c1-120
	done
done
echo "done $out"
