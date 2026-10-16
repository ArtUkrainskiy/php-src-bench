#!/usr/bin/env bash
# bench gc [--older-than DAYS] [--yes] [<pattern>...]
#
# Lists the builds with their size, age and kind (full worktree or slim). With patterns
# (shell globs on the build name) or --older-than it marks the matching builds; they are
# only removed with --yes. Free space is reported before and after.
set -euo pipefail
: "${BENCH_ROOT:?run this through ./bench}" "${PHP_SRC:?}" "${BENCH_BUILDS:?}"

older=""
yes=false
patterns=()
while (($#)); do
	case "$1" in
		--older-than) older="${2:?--older-than needs a number of days}"; shift 2 ;;
		--yes) yes=true; shift ;;
		-h|--help) sed -n '2,7p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
		-*) echo "bench gc: unknown option $1" >&2; exit 2 ;;
		*) patterns+=("$1"); shift ;;
	esac
done
select=false
[[ -n "$older" || ${#patterns[@]} -gt 0 ]] && select=true

free() { df -Ph "$BENCH_BUILDS" | awk 'NR == 2 {print $4 " free of " $2}'; }

now=$(date +%s)
marked=()
total=0
marked_total=0
printf '%-1s %-32s %8s %5s %-5s %s\n' '' build size days kind commit
shopt -s nullglob
for dir in "$BENCH_BUILDS"/*/; do
	dir="${dir%/}"
	name="${dir##*/}"
	[[ -f "$dir/.bench-build.json" || -e "$dir/.git" ]] || continue
	kind=full
	[[ -e "$dir/.git" ]] || kind=slim
	mb=$(du -sm "$dir" 2>/dev/null | cut -f1)
	built=$(stat -c %Y "$dir/sapi/cli/php" 2>/dev/null || stat -c %Y "$dir")
	days=$(( (now - built) / 86400 ))
	commit=$( { sed -n 's/.*"commit": "\([0-9a-f]\{11\}\).*/\1/p' "$dir/.bench-build.json" 2>/dev/null || git -C "$dir" rev-parse --short=11 HEAD 2>/dev/null || true; } | head -1)
	hit=false
	if $select; then
		hit=true
		if ((${#patterns[@]})); then
			hit=false
			for p in "${patterns[@]}"; do
				# shellcheck disable=SC2053
				[[ "$name" == $p ]] && hit=true
			done
		fi
		if [[ -n "$older" ]] && (( days < older )); then
			hit=false
		fi
	fi
	total=$((total + mb))
	mark=' '
	if $hit; then
		mark='x'
		marked+=("$name")
		marked_total=$((marked_total + mb))
	fi
	printf '%-1s %-32s %6s M %5s %-5s %s\n' "$mark" "$name" "$mb" "$days" "$kind" "${commit:--}"
done
echo "total $(awk -v m=$total 'BEGIN {printf "%.1f", m / 1024}') GB in ${BENCH_BUILDS}; $(free)"
$select || exit 0

if ((${#marked[@]} == 0)); then
	echo "nothing matches"
	exit 0
fi
echo "marked x: ${#marked[@]} builds, $(awk -v m=$marked_total 'BEGIN {printf "%.1f", m / 1024}') GB"
if ! $yes; then
	echo "run again with --yes to remove them"
	exit 0
fi
for name in "${marked[@]}"; do
	"$BENCH_ROOT/bench" rm "$name"
done
echo "now $(free)"
