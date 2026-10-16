#!/usr/bin/env bash
# bench pr <N> [--base REF] [--remote NAME] [--no-merge] [build options...]
#
# Builds a php-src pull request for review: fetches its head and master from the remote that
# points at php/php-src, merges the head onto master the way GitHub would (without touching the
# working tree or any branch), and builds both sides with `bench build`:
#   pr<N>-base  master (or --base)
#   pr<N>-head  the PR merged onto it (with --no-merge: the PR head as it is)
# Build options (--cc, --profile, --slim, --no-werror) go to `bench build`; with --cc the names
# get a compiler suffix as usual. The fetched commits are kept under refs/bench/pr/<N>/.
set -euo pipefail
: "${BENCH_ROOT:?run this through ./bench}" "${PHP_SRC:?}" "${BENCH_BUILDS:?}"

usage="usage: bench pr <N> [--base REF] [--remote NAME] [--no-merge] [--cc LIST] [--profile P] [--slim] [--no-werror]"
number="${1:-}"
[[ "$number" =~ ^[0-9]+$ ]] || { echo "$usage" >&2; exit 2; }
shift
base_ref=""
remote=""
merge=1
build_opts=()
while (($#)); do
	case "$1" in
		--base) base_ref="${2:?$usage}"; shift 2 ;;
		--remote) remote="${2:?$usage}"; shift 2 ;;
		--no-merge) merge=0; shift ;;
		--cc|--profile) build_opts+=("$1" "${2:?$usage}"); shift 2 ;;
		--slim|--no-werror) build_opts+=("$1"); shift ;;
		*) echo "bench pr: unknown option $1" >&2; echo "$usage" >&2; exit 2 ;;
	esac
done

src() { git -C "$PHP_SRC" "$@"; }
src rev-parse --git-dir >/dev/null 2>&1 || { echo "bench pr: php-src not found at $PHP_SRC (set PHP_SRC)" >&2; exit 1; }

# The remote of php/php-src, whatever it is called here.
if [[ -z "$remote" ]]; then
	remote="$(src remote -v | awk '$2 ~ /github\.com[:\/]php\/php-src(\.git)?$/ && $3 == "(fetch)" {print $1; exit}')"
	[[ -n "$remote" ]] || { echo "bench pr: no remote of $PHP_SRC points at github.com/php/php-src; add one or pass --remote" >&2; exit 1; }
fi

refs="refs/bench/pr/$number"
echo "fetching PR $number and master from $remote" >&2
src fetch -q --no-tags "$remote" "+refs/pull/$number/head:$refs/head" "+refs/heads/master:$refs/master"
head="$(src rev-parse "$refs/head")"
if [[ -n "$base_ref" ]]; then
	base="$(src rev-parse --verify "$base_ref^{commit}")"
else
	base="$(src rev-parse "$refs/master")"
fi
echo "PR $number head ${head:0:11} ($(src log -1 --format=%s "$head")), base ${base:0:11}" >&2

target="$head"
if ((merge)); then
	# A merge commit with the date of the head: the same PR on the same base is the same commit,
	# so an existing build of it is recognised as up to date.
	if ! tree="$(src merge-tree --write-tree "$base" "$head" 2>/dev/null)"; then
		echo "bench pr: PR $number does not merge cleanly onto ${base:0:11}; rebase it, pass another --base, or build the head as it is with --no-merge" >&2
		exit 1
	fi
	tree="$(head -1 <<<"$tree")"
	date="$(src log -1 --format=%cI "$head")"
	target="$(GIT_AUTHOR_NAME=php-src-bench GIT_AUTHOR_EMAIL=php-src-bench@localhost GIT_AUTHOR_DATE="$date" \
		GIT_COMMITTER_NAME=php-src-bench GIT_COMMITTER_EMAIL=php-src-bench@localhost GIT_COMMITTER_DATE="$date" \
		src commit-tree "$tree" -p "$base" -p "$head" -m "php-src-bench: PR $number (${head:0:11}) merged onto ${base:0:11}")"
	src update-ref "$refs/merge" "$target"
	echo "merged: ${target:0:11}" >&2
fi

"$BENCH_ROOT/bench" build "${build_opts[@]}" "pr$number-base" "$base"
"$BENCH_ROOT/bench" build "${build_opts[@]}" "pr$number-head" "$target"

cat >&2 <<EOF

Built pr$number-base and pr$number-head$( [[ " ${build_opts[*]} " == *" --cc "* ]] && echo " (one per compiler: bench builds)" ).
Next:
  ./bench difftest code pr$number-base pr$number-head --code '<the function the PR changes>(\$s)' --count 20000
  ./bench compare <suite> <group>=pr$number-base<-compiler>:pr$number-head<-compiler> ...
EOF
