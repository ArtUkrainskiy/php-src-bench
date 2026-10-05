#!/usr/bin/env bash
# bench tune on|off|status
#
# "on" switches every CPU to the performance governor and turns turbo boost off, which removes
# most frequency noise from wall-time measurements; "off" restores what was there before.
# The previous settings are kept in /run, so they survive until the next reboot at most.
set -euo pipefail
: "${BENCH_ROOT:?run this through ./bench}"

state=/run/php-src-bench-tune.state
cpu_sys=/sys/devices/system/cpu
no_turbo="$cpu_sys/intel_pstate/no_turbo"
boost="$cpu_sys/cpufreq/boost"

# How many CPUs have each value of a cpufreq setting, e.g. "8 performance 12 powersave";
# "n/a" where the machine has no frequency control (virtual machines).
summarize() {
	local files=("$cpu_sys"/cpu[0-9]*/cpufreq/"$1")
	if [[ ! -f "${files[0]}" ]]; then
		echo n/a
		return
	fi
	sort "${files[@]}" | uniq -c | xargs
}

status() {
	echo "governor (CPUs per value): $(summarize scaling_governor)"
	echo "energy_performance_preference (CPUs per value): $(summarize energy_performance_preference)"
	if [[ -f "$no_turbo" ]]; then
		echo "turbo: $([[ "$(cat "$no_turbo")" == 1 ]] && echo off || echo on)"
	elif [[ -f "$boost" ]]; then
		echo "boost: $([[ "$(cat "$boost")" == 1 ]] && echo on || echo off)"
	fi
	if [[ -f "$state" ]]; then
		echo "tuned by php-src-bench (previous settings saved in $state)"
	fi
}

require_root() {
	if [[ $EUID -ne 0 ]]; then
		echo "bench tune $1: needs root, run: sudo $BENCH_ROOT/bench tune $1" >&2
		exit 1
	fi
}

write() { echo "$2" >"$1" 2>/dev/null || echo "  warning: cannot write $2 to $1" >&2; }

case "${1:-status}" in
	status)
		status
		;;
	on)
		require_root on
		if [[ ! -f "$state" ]]; then
			for f in "$cpu_sys"/cpu[0-9]*/cpufreq/scaling_governor "$cpu_sys"/cpu[0-9]*/cpufreq/energy_performance_preference "$no_turbo" "$boost"; do
				[[ -f "$f" ]] && echo "$f $(cat "$f")"
			done >"$state"
		fi
		for f in "$cpu_sys"/cpu[0-9]*/cpufreq/scaling_governor; do write "$f" performance; done
		for f in "$cpu_sys"/cpu[0-9]*/cpufreq/energy_performance_preference; do
			# Not every driver has this setting, and intel_pstate forces it to "performance"
			# under the performance governor anyway: failing to write it is fine.
			echo performance >"$f" 2>/dev/null || true
		done
		[[ -f "$no_turbo" ]] && write "$no_turbo" 1
		[[ -f "$boost" ]] && write "$boost" 0
		status
		;;
	off)
		require_root off
		if [[ ! -f "$state" ]]; then
			echo "nothing to restore ($state not found)" >&2
			exit 1
		fi
		# The state file lists governors first, which is the order to restore in: the energy
		# preference cannot be changed while the performance governor is active.
		while read -r f v; do write "$f" "$v"; done <"$state"
		rm -f "$state"
		status
		;;
	*)
		echo "usage: bench tune on|off|status" >&2
		exit 2
		;;
esac
