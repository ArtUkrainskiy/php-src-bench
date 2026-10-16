#!/usr/bin/env bash
# bench pr <N> [--base REF] [--remote NAME] [--no-merge] [build options...]
#
# Builds a php-src pull request for review: fetches its head and master from the remote that
# points at php/php-src, merges the head onto master the way GitHub would (without touching the
# working tree or any branch), and builds both sides with `bench build`:
#   pr<N>-base  master (or --base)
#   pr<N>-head  the PR merged onto it (with --no-merge: the PR head as it is)
# Build options (--cc, --profile, --slim, --no-werror) go to `bench build`; with --cc the names
# get a compiler suffix as usual. The fetched commits are kept under refs/bench/pr/<N>/; a later
# run uses the same master unless --update is given, so that builds made one compiler at a time
# share their base. Needs git 2.38 or newer (git merge-tree --write-tree).
set -euo pipefail
: "${BENCH_ROOT:?run this through ./bench}" "${PHP_SRC:?}" "${BENCH_BUILDS:?}"

usage="usage: bench pr <N> [--base REF] [--remote NAME] [--update] [--no-merge] [--cc LIST] [--profile P] [--slim] [--no-werror]"
number="${1:-}"
[[ "$number" =~ ^[0-9]+$ ]] || { echo "$usage" >&2; exit 2; }
shift
base_ref=""
remote=""
merge=1
update=0
build_opts=()
while (($#)); do
	case "$1" in
		--base) base_ref="${2:?$usage}"; shift 2 ;;
		--remote) remote="${2:?$usage}"; shift 2 ;;
		--no-merge) merge=0; shift ;;
		--update) update=1; shift ;;
		--cc|--profile) build_opts+=("$1" "${2:?$usage}"); shift 2 ;;
		--cc=*|--profile=*) build_opts+=("$1"); shift ;;
		-h|--help) sed -n '2,13p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
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
fetch=("+refs/pull/$number/head:$refs/head")
if ((update)) || ! src rev-parse -q --verify "$refs/master" >/dev/null; then
	fetch+=("+refs/heads/master:$refs/master")
else
	echo "using master ${refs}/master as fetched before ($(src rev-parse --short=11 "$refs/master")); --update fetches it again" >&2
fi
echo "fetching PR $number from $remote" >&2
if ! err="$(src fetch -q --no-tags "$remote" "${fetch[@]}" 2>&1)"; then
	if grep -q "couldn't find remote ref" <<<"$err"; then
		echo "bench pr: there is no PR $number on $remote" >&2
	else
		echo "bench pr: git fetch failed: $err" >&2
	fi
	exit 1
fi
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
	status=0
	tree="$(src merge-tree --write-tree --name-only "$base" "$head" 2>"${TMPDIR:-/tmp}/bench-pr-$$.err")" || status=$?
	err="$(cat "${TMPDIR:-/tmp}/bench-pr-$$.err")"
	rm -f "${TMPDIR:-/tmp}/bench-pr-$$.err"
	if ((status == 1)); then
		echo "bench pr: PR $number does not merge cleanly onto ${base:0:11}; conflicts in:" >&2
		sed -n '2,/^$/p' <<<"$tree" | sed 's/^/  /' >&2
		echo "rebase it, pass another --base, or build the head as it is with --no-merge" >&2
		exit 1
	elif ((status != 0)); then
		echo "bench pr: git merge-tree failed (git 2.38 or newer is needed, this is $(git --version | awk '{print $3}')): $err" >&2
		exit 1
	fi
	tree="$(head -1 <<<"$tree")"
	if [[ "$tree" == "$(src rev-parse "$base^{tree}")" ]]; then
		echo "bench pr: PR $number changes nothing on top of ${base:0:11} (merged already, or empty); both sides would be the same" >&2
		exit 1
	fi
	date="$(src log -1 --format=%cI "$head")"
	target="$(GIT_AUTHOR_NAME=php-src-bench GIT_AUTHOR_EMAIL=php-src-bench@localhost GIT_AUTHOR_DATE="$date" \
		GIT_COMMITTER_NAME=php-src-bench GIT_COMMITTER_EMAIL=php-src-bench@localhost GIT_COMMITTER_DATE="$date" \
		src -c commit.gpgSign=false commit-tree "$tree" -p "$base" -p "$head" -m "php-src-bench: PR $number (${head:0:11}) merged onto ${base:0:11}")"
	src update-ref "$refs/merge" "$target"
	echo "merged: ${target:0:11}" >&2
fi

# Recorded in the builds, so that a report can say `bench pr` instead of a local merge commit.
BENCH_PR="$number ${base:0:11} ${head:0:11} $merge" "$BENCH_ROOT/bench" build ${build_opts[@]+"${build_opts[@]}"} "pr$number-base" "$base"
BENCH_PR="$number ${base:0:11} ${head:0:11} $merge" "$BENCH_ROOT/bench" build ${build_opts[@]+"${build_opts[@]}"} "pr$number-head" "$target"

cat >&2 <<EOF

Built pr$number-base and pr$number-head$( [[ " ${build_opts[*]} " == *" --cc "* ]] && echo " (one per compiler: bench builds)" ).
Next:
  ./bench difftest code pr$number-base pr$number-head --code '<the function the PR changes>(\$s)' --count 20000
  ./bench compare <suite> <group>=pr$number-base<-compiler>:pr$number-head<-compiler> ...
EOF
