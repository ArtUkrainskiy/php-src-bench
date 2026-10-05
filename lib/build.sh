#!/usr/bin/env bash
# bench build <name> [<git-ref>|.]
#
# Builds a release php CLI of a php-src commit in its own git worktree, $BENCH_BUILDS/<name>.
# The php-src working tree is never modified: "." builds a snapshot of it (tracked and untracked
# files) through a temporary index. A build of an existing name is incremental; configure runs
# again only when the options, the compiler or the build system files changed.
set -euo pipefail
: "${BENCH_ROOT:?run this through ./bench}" "${PHP_SRC:?}" "${BENCH_BUILDS:?}"

name="${1:-}"
ref="${2:-HEAD}"
if [[ -z "$name" || "$name" == -* ]]; then
	echo "usage: bench build <name> [<git-ref>|.]" >&2
	exit 2
fi
if [[ ! "$name" =~ ^[A-Za-z0-9._-]+$ ]]; then
	echo "bench build: name must match [A-Za-z0-9._-]+" >&2
	exit 2
fi

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

if ! git -C "$PHP_SRC" rev-parse --git-dir >/dev/null 2>&1; then
	echo "bench build: php-src not found at $PHP_SRC (set PHP_SRC)" >&2
	exit 1
fi

configure_args=(--disable-all --disable-cgi --disable-phpdbg --enable-cli)
if [[ -n "${BENCH_CONFIGURE_EXTRA:-}" ]]; then
	read -r -a extra <<<"$BENCH_CONFIGURE_EXTRA"
	configure_args+=("${extra[@]}")
fi
# Fixed function/loop alignment keeps code placement shifts in unrelated code from showing up
# as 3-15% wall-time differences in untouched functions (see docs/methodology.md).
cflags="${BENCH_CFLAGS:--O2 -g -falign-functions=64 -falign-loops=32}"

src() { git -C "$PHP_SRC" "$@"; }

# Resolve the commit to build. '.' turns the working tree (tracked and untracked, non-ignored
# files) into a commit object through a temporary index; no branch, index or file is touched.
snapshot=false
if [[ "$ref" == "." ]]; then
	idx="$(mktemp)"
	trap 'rm -f "$idx"' EXIT
	cp "$(src rev-parse --absolute-git-dir)/index" "$idx"
	GIT_INDEX_FILE="$idx" src add -A
	tree="$(GIT_INDEX_FILE="$idx" src write-tree)"
	commit="$(src rev-parse HEAD)"
	base_commit="$commit"
	if [[ "$tree" != "$(src rev-parse 'HEAD^{tree}')" ]]; then
		snapshot=true
		commit="$(GIT_AUTHOR_NAME=php-src-bench GIT_AUTHOR_EMAIL=php-src-bench@localhost \
			GIT_COMMITTER_NAME=php-src-bench GIT_COMMITTER_EMAIL=php-src-bench@localhost \
			src commit-tree "$tree" -p "$commit" -m "php-src-bench snapshot of the working tree")"
	fi
else
	commit="$(src rev-parse --verify --quiet "$ref^{commit}")" || {
		echo "bench build: not a commit in $PHP_SRC: $ref" >&2
		exit 1
	}
	base_commit="$commit"
fi

dir="$BENCH_BUILDS/$name"
mkdir -p "$BENCH_BUILDS"
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

cc_version="$("$cc" --version | head -1)"
config_key="$(printf '%s\n' "${configure_args[@]}" "CFLAGS=$cflags" "CC=$cc" "$cc_version" | sha1sum | cut -d' ' -f1)"
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
	step "configure ${configure_args[*]} CFLAGS='$cflags'" env CC="$cc" CFLAGS="$cflags" ./configure "${configure_args[@]}"
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
BM_CC="$cc_version" \
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
		"cc" => getenv("BM_CC"),
		"version" => PHP_VERSION,
		"debug" => (bool) PHP_DEBUG,
	], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES), "\n";
' >"$dir/.bench-build.json"

echo "ok: $php ($("$php" -n -r 'echo PHP_VERSION;'))" >&2
