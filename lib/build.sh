#!/usr/bin/env bash
# bench build [--slim] [--profile P] [--cc LIST] [--no-werror] <name> [<git-ref>|.]
#
# Builds a release php CLI of a php-src commit in its own git worktree, $BENCH_BUILDS/<name>.
# The php-src working tree is never modified: "." builds a snapshot of it (tracked and untracked
# files) through a temporary index. A build of an existing name is incremental; configure runs
# again only when the options, the flags or the compiler changed, and a build that already has
# this commit and configuration is left as it is.
#
# Profiles (compiler flags and configure options):
#   docker  the flags of the official Docker image (docker-library/php) plus -g, --enable-werror;
#           the default, for numbers you publish
#   align   -O2 -g -falign-functions=64 -falign-loops=32: fixed code placement, for finding causes
#   plain   -O2 -g, what a plain ./configure uses
#   asan    a debug build with AddressSanitizer and UndefinedBehaviorSanitizer
# BENCH_CFLAGS and LDFLAGS override the profile's flags, BENCH_CONFIGURE_EXTRA adds options.
#
# --cc gcc,gcc-14,clang builds one build per compiler, named <name>-<tag>, where the tag comes from
# the compiler's version: gcc13, gcc14, clang18, ...
set -euo pipefail
: "${BENCH_ROOT:?run this through ./bench}" "${PHP_SRC:?}" "${BENCH_BUILDS:?}"

usage="usage: bench build [--slim] [--profile docker|align|plain|asan] [--cc LIST] [--no-werror] <name> [<git-ref>|.]"
slim="${BENCH_SLIM:-0}"
profile=docker
cc_list=""
werror=1
args=()
while (($#)); do
	case "$1" in
		--slim) slim=1; shift ;;
		--profile) profile="${2:-}"; shift 2 || { echo "$usage" >&2; exit 2; } ;;
		--profile=*) profile="${1#*=}"; shift ;;
		--cc) cc_list="${2:-}"; shift 2 || { echo "$usage" >&2; exit 2; } ;;
		--cc=*) cc_list="${1#*=}"; shift ;;
		--no-werror) werror=0; shift ;;
		-h|--help) echo "$usage"; exit 0 ;;
		-*) echo "bench build: unknown option $1" >&2; echo "$usage" >&2; exit 2 ;;
		*) args+=("$1"); shift ;;
	esac
done
name="${args[0]:-}"
ref="${args[1]:-HEAD}"
if [[ -z "$name" || ${#args[@]} -gt 2 ]]; then
	echo "$usage" >&2
	exit 2
fi
if [[ ! "$name" =~ ^[A-Za-z0-9._-]+$ ]]; then
	echo "bench build: name must match [A-Za-z0-9._-]+" >&2
	exit 2
fi

case "$profile" in
	docker|align|plain|asan) ;;
	*) echo "bench build: unknown profile '$profile' (docker, align, plain, asan)" >&2; exit 2 ;;
esac

IFS=, read -r -a compilers <<<"${cc_list// /}"
for c in "${compilers[@]}"; do
	command -v "$c" >/dev/null || { echo "bench build: no such compiler: $c" >&2; exit 1; }
done

# The tag of a compiler in build names: family and major version, e.g. gcc13, clang20.
cc_tag() {
	local v
	v="$("$1" --version 2>/dev/null | head -1)" || return 1
	if [[ "$v" == *clang* ]]; then
		[[ "$v" =~ version\ ([0-9]+) ]] && echo "clang${BASH_REMATCH[1]}"
	elif [[ "$v" =~ \)\ ([0-9]+)\.[0-9]+ || "$v" =~ ^gcc.*\ ([0-9]+)\.[0-9]+\.[0-9]+ ]]; then
		echo "gcc${BASH_REMATCH[1]}"
	fi
}

src() { git -C "$PHP_SRC" "$@"; }

if ! src rev-parse --git-dir >/dev/null 2>&1; then
	echo "bench build: php-src not found at $PHP_SRC (set PHP_SRC)" >&2
	exit 1
fi

# Resolve the commit to build into $commit, $base_commit and $snapshot. '.' turns the working tree
# (tracked and untracked, non-ignored files) into a commit object through a temporary index; no
# branch, index or file is touched. The snapshot gets HEAD's date, so the same tree on the same
# HEAD is the same commit, and an up-to-date build of it is recognised.
resolve_ref() {
	snapshot=false
	if [[ -n "${BENCH_SNAPSHOT_OF:-}" ]]; then
		# a child of --cc: the parent made the snapshot
		commit="$1"
		base_commit="$BENCH_SNAPSHOT_OF"
		snapshot=true
	elif [[ "$1" == "." ]]; then
		local idx tree date
		idx="$(mktemp)"
		cp "$(src rev-parse --absolute-git-dir)/index" "$idx"
		GIT_INDEX_FILE="$idx" src add -A
		tree="$(GIT_INDEX_FILE="$idx" src write-tree)"
		rm -f "$idx"
		commit="$(src rev-parse HEAD)"
		base_commit="$commit"
		if [[ "$tree" != "$(src rev-parse 'HEAD^{tree}')" ]]; then
			snapshot=true
			date="$(src log -1 --format=%cI HEAD)"
			commit="$(GIT_AUTHOR_NAME=php-src-bench GIT_AUTHOR_EMAIL=php-src-bench@localhost GIT_AUTHOR_DATE="$date" \
				GIT_COMMITTER_NAME=php-src-bench GIT_COMMITTER_EMAIL=php-src-bench@localhost GIT_COMMITTER_DATE="$date" \
				src commit-tree "$tree" -p "$commit" -m "php-src-bench snapshot of the working tree")"
		fi
	else
		commit="$(src rev-parse --verify --quiet "$1^{commit}")" || {
			echo "bench build: not a commit in $PHP_SRC: $1" >&2
			exit 1
		}
		base_commit="$commit"
	fi
}
resolve_ref "$ref"

# One build per compiler: run this script again for each, so that each build is checked,
# configured and recorded the same way as a single one. A snapshot of the working tree is made
# once here, so that every compiler builds the same sources.
if [[ -n "$cc_list" ]]; then
	opts=(--profile "$profile")
	[[ "$slim" == 1 ]] && opts+=(--slim)
	[[ "$werror" == 0 ]] && opts+=(--no-werror)
	failed=()
	for c in "${compilers[@]}"; do
		tag="$(cc_tag "$c")" || true
		[[ -n "$tag" ]] || { echo "bench build: cannot tell the version of $c" >&2; exit 1; }
		if $snapshot; then
			CC="$c" BENCH_SNAPSHOT_OF="$base_commit" "$0" "${opts[@]}" "$name-$tag" "$commit" || failed+=("$name-$tag")
		else
			CC="$c" "$0" "${opts[@]}" "$name-$tag" "$commit" || failed+=("$name-$tag")
		fi
	done
	if ((${#failed[@]})); then
		echo "bench build: failed: ${failed[*]}" >&2
		exit 1
	fi
	exit 0
fi

case "$profile" in
	docker)
		profile_cflags='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
		profile_ldflags='-Wl,-O1 -pie'
		profile_configure=()
		[[ "$werror" == 1 ]] && profile_configure+=(--enable-werror)
		;;
	align)
		profile_cflags='-O2 -g -falign-functions=64 -falign-loops=32'
		profile_ldflags=''
		profile_configure=()
		;;
	plain)
		profile_cflags='-O2 -g'
		profile_ldflags=''
		profile_configure=()
		;;
	asan)
		profile_cflags='-g -fno-omit-frame-pointer' # --enable-debug builds with -O0
		profile_ldflags=''
		profile_configure=(--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer)
		;;
	*) echo "bench build: unknown profile '$profile' (docker, align, plain, asan)" >&2; exit 2 ;;
esac

# ./configure uses $CC when it is set, so that is the compiler to check and to record.
cc="${CC:-cc}"
missing=()
for tool in autoconf bison re2c make "$cc" pkg-config; do
	command -v "$tool" >/dev/null || missing+=("$tool")
done
if ((${#missing[@]})); then
	echo "bench build: missing tools: ${missing[*]}" >&2
	echo "  Ubuntu/Debian: sudo apt install autoconf bison re2c build-essential pkg-config" >&2
	exit 1
fi

configure_args=(--disable-all --disable-cgi --disable-phpdbg --enable-cli "${profile_configure[@]}")
if [[ -n "${BENCH_CONFIGURE_EXTRA:-}" ]]; then
	read -r -a extra <<<"$BENCH_CONFIGURE_EXTRA"
	configure_args+=("${extra[@]}")
fi
cflags="${BENCH_CFLAGS:-$profile_cflags}"
ldflags="${BENCH_LDFLAGS-$profile_ldflags}"
# An LDFLAGS from the shell (dev shells, conda, nix) would silently replace the profile's flags.
if [[ -n "${LDFLAGS:-}" && "$LDFLAGS" != "$ldflags" ]]; then
	echo "bench build: ignoring LDFLAGS='$LDFLAGS' from the environment, using '$ldflags' (set BENCH_LDFLAGS to change it)" >&2
fi

cc_version="$("$cc" --version | head -1)"
# CPPFLAGS and LIBS from the environment reach configure too, so they are part of the key.
config_key="$(printf '%s\n' "${configure_args[@]}" "CFLAGS=$cflags" "LDFLAGS=$ldflags" "CPPFLAGS=${CPPFLAGS:-}" "LIBS=${LIBS:-}" "CC=$cc" "$cc_version" | sha1sum | cut -d' ' -f1)"

dir="$BENCH_BUILDS/$name"
# Nothing to do when the build already has this commit with this configuration (shared bases).
if [[ -f "$dir/.bench-build.json" ]] \
	&& grep -q "\"commit\": \"$commit\"" "$dir/.bench-build.json" \
	&& grep -q "\"config_key\": \"$config_key\"" "$dir/.bench-build.json"; then
	echo "up to date: $name ($(git -C "$PHP_SRC" log -1 --format='%h %s' "$commit"))" >&2
	exit 0
fi

# A full build takes about 400 MB, a failed one can leave a full disk behind.
min_free_gb="${BENCH_MIN_FREE_GB:-10}"
mkdir -p "$BENCH_BUILDS"
free_gb=$(( $(df -Pk "$BENCH_BUILDS" | awk 'NR == 2 {print $4}') / 1024 / 1024 ))
if (( free_gb < min_free_gb )); then
	echo "bench build: only ${free_gb} GB free in $BENCH_BUILDS (minimum ${min_free_gb} GB, BENCH_MIN_FREE_GB);" >&2
	echo "  see 'bench gc' for the builds that can go" >&2
	exit 1
fi

# A slim build keeps nothing to build on: replace it.
if [[ -f "$dir/.bench-build.json" && ! -e "$dir/.git" ]]; then
	rm -rf -- "$dir"
fi
prev_commit=""
if [[ -e "$dir/.git" ]]; then
	prev_commit="$(git -C "$dir" rev-parse HEAD)"
	if [[ -n "$(git -C "$dir" status --porcelain --untracked-files=no)" ]]; then
		echo "bench build: $dir has local modifications, refusing to check out" >&2
		exit 1
	fi
	git -C "$dir" checkout -q --detach "$commit"
else
	src worktree add -q --detach "$dir" "$commit"
fi

need_configure=false
need_clean=false
if [[ ! -f "$dir/Makefile" || "$config_key" != "$(cat "$dir/.bench-config-key" 2>/dev/null || true)" ]]; then
	need_configure=true
fi
if [[ -n "$prev_commit" && "$prev_commit" != "$commit" ]]; then
	changed="$(git -C "$dir" diff --name-only "$prev_commit" "$commit")"
	if grep -qE '(^|/)(configure\.ac|config\.m4|[^/]+\.m4|Makefile\.frag)$' <<<"$changed"; then
		need_configure=true
	fi
	# A changed header means a full rebuild: slower than trusting the dependency tracking of
	# the Makefiles, but there is then no way to end up with stale objects.
	if grep -qE '\.(h|def)$' <<<"$changed"; then
		need_clean=true
	fi
fi

log="$dir/.bench-build.log"
: >"$log"
step() {
	echo "  $1" >&2
	shift
	if ! (cd "$dir" && "$@") >>"$log" 2>&1; then
		tail -30 "$log" >&2
		echo "bench build: failed, full log: $log" >&2
		exit 1
	fi
}

echo "building '$name' at $(git -C "$dir" log -1 --format='%h %s')$($snapshot && echo ' (working tree snapshot)')" >&2
if $need_configure; then
	rm -f "$dir/.bench-config-key"
	step "buildconf" ./buildconf --force
	step "configure ${configure_args[*]} CFLAGS='$cflags' LDFLAGS='$ldflags'" env CC="$cc" CFLAGS="$cflags" LDFLAGS="$ldflags" ./configure "${configure_args[@]}"
	need_clean=true
fi
if $need_clean; then
	step "make clean" make clean
fi
step "make -j$(nproc)" make -j"$(nproc)"
echo "$config_key" >"$dir/.bench-config-key"

php="$dir/sapi/cli/php"
# "cflags" are the effective ones that configure put into the Makefile, "cflags_user" what was
# asked for; base_commit is the commit a working tree snapshot sits on.
BM_NAME="$name" BM_REF="$ref" BM_COMMIT="$commit" BM_SNAPSHOT="$snapshot" \
BM_SUBJECT="$(git -C "$dir" log -1 --format=%s)" \
BM_BASE_COMMIT="$base_commit" BM_BASE_SUBJECT="$(src log -1 --format=%s "$base_commit")" \
BM_CONFIGURE="${configure_args[*]}" \
BM_CFLAGS="$(sed -n 's/^CFLAGS_CLEAN = //p' "$dir/Makefile")" \
BM_CFLAGS_USER="$cflags" \
BM_LDFLAGS="$ldflags" \
BM_PROFILE="$profile$([[ "$cflags" != "$profile_cflags" || "$ldflags" != "$profile_ldflags" ]] && echo ' (flags overridden)')" \
BM_CONFIG_KEY="$config_key" \
BM_CC="$cc_version" \
BM_CC_COMMAND="$cc" \
BM_CONFIGURE_EXTRA="${BENCH_CONFIGURE_EXTRA:-}" \
BM_SLIM="$slim" \
"$php" -n -r '
	echo json_encode([
		"name" => getenv("BM_NAME"),
		"ref" => getenv("BM_REF"),
		"commit" => getenv("BM_COMMIT"),
		"subject" => getenv("BM_SUBJECT"),
		"snapshot" => getenv("BM_SNAPSHOT") === "true",
		"base_commit" => getenv("BM_BASE_COMMIT"),
		"base_subject" => getenv("BM_BASE_SUBJECT"),
		"built_at" => date("c"),
		"configure" => getenv("BM_CONFIGURE"),
		"cflags" => getenv("BM_CFLAGS"),
		"cflags_user" => getenv("BM_CFLAGS_USER"),
		"ldflags" => getenv("BM_LDFLAGS"),
		"profile" => getenv("BM_PROFILE"),
		"config_key" => getenv("BM_CONFIG_KEY"),
		"cc" => getenv("BM_CC"),
		"cc_command" => getenv("BM_CC_COMMAND"),
		"configure_extra" => getenv("BM_CONFIGURE_EXTRA"),
		"version" => PHP_VERSION,
		"debug" => (bool) PHP_DEBUG,
		"slim" => getenv("BM_SLIM") === "1",
	], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES), "\n";
' >"$dir/.bench-build.json"

# A snapshot commit is referenced by nothing else: keep it reachable while the build exists,
# so that `git gc` does not prune the sources of a slim build.
if $snapshot; then
	src update-ref "refs/bench/$name" "$commit"
else
	src update-ref -d "refs/bench/$name" 2>/dev/null || true
fi

# --slim keeps only the binary (with its debug info) and the metadata, about 55 MB instead of
# 400: the worktree, the sources and the objects go. Sources stay available from the commit.
if [[ "$slim" == 1 ]]; then
	tmp="$(mktemp -d "$BENCH_BUILDS/.slim-$name.XXXXXX")"
	chmod 755 "$tmp"
	mkdir -p "$tmp/sapi/cli"
	cp -p "$php" "$tmp/sapi/cli/php"
	cp -p "$dir/.bench-build.json" "$dir/.bench-build.log" "$tmp/"
	src worktree remove --force "$dir"
	mv "$tmp" "$dir"
fi

echo "ok: $php ($("$php" -n -r 'echo PHP_VERSION;'))$([[ "$slim" == 1 ]] && echo ', slim')" >&2
