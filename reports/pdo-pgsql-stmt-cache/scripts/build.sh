#!/bin/bash
# Builds the two PHP-FPM variants of the Drupal series into ./build-base and ./build-v3:
# PHP 8.5.11 with the extension set and compiler flags of web-request-cost's harness/stack/build-php.sh
# (commit afd7ea6: the flags of the official php Docker image) plus ext/gd (Drupal needs an image toolkit),
# and the same with ../stmt-cache-8.5.11.patch.
# Also builds the runtime image drupal-runtime:<host's Ubuntu version>: web-request-cost's runtime image (the same
# Ubuntu release as the host, so that the host's builds run in it unchanged) plus the gd libraries.
# Paths may be relative to this directory.
#   WRC=<web-request-cost checkout at afd7ea6> PHP_TARBALL=<php-8.5.11.tar.xz from php.net> [PATCH=<stmt-cache-8.5.11.patch>] ./build.sh
# Host: Ubuntu (the runs: 26.04) with the build dependencies listed in the report's Reproduce section.
# Prints the sha256 prefix of each php-fpm and the defaults of the two new INI settings (false = not defined).
set -e
cd "$(dirname "$0")"
: "${WRC:?set WRC}" "${PHP_TARBALL:?set PHP_TARBALL}"
here=$PWD
patch=${PATCH:-$here/../stmt-cache-8.5.11.patch}
ubuntu=$(. /etc/os-release && echo "$VERSION_ID")
mkdir -p src
for v in base v3; do
	rm -rf "src/$v" && mkdir -p "src/$v"
	tar xf "$PHP_TARBALL" -C "src/$v" --strip-components=1
done
patch -d src/v3 -p1 < "$patch"
# build-php.sh with --enable-gd --with-freetype added to its extension list, building only the FPM/CLI variant
sed -e 's/--with-pdo-pgsql"/--with-pdo-pgsql --enable-gd --with-freetype"/' -e '/^build php85-zts/d' \
	"$WRC/harness/stack/build-php.sh" > build-php-gd.sh
grep -q 'enable-gd' build-php-gd.sh
for v in base v3; do
	PHP_SRC=$here/src/$v BUILD_DIR=$here/build-$v bash build-php-gd.sh
done
docker image inspect "blog-runtime:$ubuntu" >/dev/null 2>&1 ||
	docker build -t "blog-runtime:$ubuntu" --build-arg UBUNTU="$ubuntu" -f "$WRC/harness/stack/Dockerfile.runtime" "$WRC/harness/stack"
docker build -t "drupal-runtime:$ubuntu" --build-arg UBUNTU="$ubuntu" -f Dockerfile.runtime .
for v in base v3; do
	echo "build-$v: $(sha256sum "build-$v/php85-fpm/sapi/fpm/php-fpm" | cut -c1-16)," \
		"$("build-$v/php85-fpm/sapi/cli/php" -r 'echo "pdo_pgsql.prepare_threshold=", var_export(ini_get("pdo_pgsql.prepare_threshold"), true), " pdo_pgsql.statement_cache_size=", var_export(ini_get("pdo_pgsql.statement_cache_size"), true);')"
done
