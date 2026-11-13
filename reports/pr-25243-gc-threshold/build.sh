#!/bin/bash
# Builds one PHP for the series: ./build.sh <master|25243|reset> <gcc15|clang21>
# Result: builds/gc-<name>-<cc>/sapi/cli/php (an in-tree build of php-src).
# Needs git, the compiler (gcc-15 or clang-21), bison, re2c, autoconf, pkg-config and the -dev packages
# of libxml2, sqlite3, oniguruma, openssl, zlib, curl, libpq (Ubuntu: libxml2-dev libsqlite3-dev
# libonig-dev libssl-dev zlib1g-dev libcurl4-openssl-dev libpq-dev).
set -eu
cd "$(dirname "$0")"
name=$1 cc=$2
MASTER=4f3d9508be9231940b946a618e8bda24fbbfbb1b
PR=af71b8e0f66fce3ed9b03da0143c67397c12b9d5
case $cc in
	gcc15) CC=gcc-15 ;;
	clang21) CC=clang-21 ;;
	*) echo "unknown compiler $cc" >&2; exit 1 ;;
esac
dir=builds/gc-$name-$cc
[ -e "$dir" ] && { echo "$dir exists" >&2; exit 1; }
mkdir -p builds
git clone -q https://github.com/php/php-src.git "$dir"
cd "$dir"
git checkout -q "$MASTER"
if [ "$name" != master ]; then
	git fetch -q origin pull/25243/head
	git -c user.name=build -c user.email=build@localhost merge -q --no-edit "$PR"
	# blob of Zend/zend_gc.c with the PR merged, as in reset.diff
	git rev-parse HEAD:Zend/zend_gc.c | grep -q '^bbbb77db3ec' || { echo "unexpected zend_gc.c" >&2; exit 1; }
fi
if [ "$name" = reset ]; then
	git apply ../../reset.diff
fi
./buildconf --force > /dev/null
# Flags of the official Docker image (docker-library/php), plus -g. Extensions are static: series.sh runs php -n.
CC=$CC CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64' \
	LDFLAGS='-Wl,-O1 -pie' ./configure -q --disable-all --disable-cgi --disable-phpdbg --enable-cli \
	--with-libxml --enable-phar --enable-tokenizer --enable-ctype --enable-mbstring --with-openssl --with-zlib \
	--enable-filter --enable-dom --enable-xml --enable-simplexml --enable-xmlwriter --enable-xmlreader \
	--enable-session --enable-fileinfo --enable-posix --enable-pcntl --with-iconv --with-curl --enable-pdo \
	--with-pdo-sqlite --with-sqlite3 --with-pdo-mysql --with-mysqli --with-pdo-pgsql --with-pgsql
make -j"$(nproc)" > /dev/null
sapi/cli/php -n -v | head -1
