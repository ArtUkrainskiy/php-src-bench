#!/usr/bin/env bash
# modes.sh <php> <file.php> <mode> [args...]: runs a file in one of the modes the change has to agree in.
#   plain    no opcache
#   opt      opcache, optimization_level=-1, no JIT
#   tracing  opcache + tracing JIT, hot thresholds 1 (every loop and call is traced at once)
#   tracing-default  opcache + tracing JIT with the default thresholds (for timings)
#   function opcache + function JIT
# Files, not -r: opcache does not optimize -r code; file_update_protection=0 so new files are cached.
php="$1"; file="$2"; mode="$3"; shift 3
common=(-n -d display_errors=1 -d error_reporting=-1)
opc=(-d opcache.enable=1 -d opcache.enable_cli=1 -d opcache.optimization_level=-1 -d opcache.file_update_protection=0 -d opcache.jit_buffer_size=64M)
case "$mode" in
	plain) exec "$php" "${common[@]}" "$file" "$@" ;;
	opt) exec "$php" "${common[@]}" "${opc[@]}" -d opcache.jit=disable "$file" "$@" ;;
	tracing) exec "$php" "${common[@]}" "${opc[@]}" -d opcache.jit=tracing -d opcache.jit_hot_loop=1 -d opcache.jit_hot_func=1 -d opcache.jit_hot_return=1 -d opcache.jit_hot_side_exit=1 "$file" "$@" ;;
	tracing-default) exec "$php" "${common[@]}" "${opc[@]}" -d opcache.jit=tracing "$file" "$@" ;;
	function) exec "$php" "${common[@]}" "${opc[@]}" -d opcache.jit=function "$file" "$@" ;;
	*) echo "modes.sh: unknown mode $mode" >&2; exit 2 ;;
esac
