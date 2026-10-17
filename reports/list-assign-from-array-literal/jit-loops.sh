#!/usr/bin/env bash
# jit-loops.sh <master php> <head php> <out.txt>: jit-stress.php with 300,000 iterations, opcache on,
# no JIT / tracing / function JIT, master and head alternating, 5 passes, pinned to CPU 2.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
m="$1"; h="$2"; out="$3"; : > "$out"
for pass in 1 2 3 4 5; do
	for mode in opt tracing-default function; do
		order="m h"; ((pass % 2)) || order="h m"
		for side in $order; do
			bin="$m"; [[ $side == h ]] && bin="$h"
			taskset -c 2 "$here/modes.sh" "$bin" "$here/jit-stress.php" "$mode" 300000 >"$out.$side.$mode.stdout" 2>"$out.err"
			sed "s/^/$pass $mode $side /" "$out.err" >> "$out"
		done
	done
done
for mode in opt tracing-default function; do cmp -s "$out.m.$mode.stdout" "$out.h.$mode.stdout" && echo "outputs equal: $mode" || echo "OUTPUTS DIFFER: $mode"; done
