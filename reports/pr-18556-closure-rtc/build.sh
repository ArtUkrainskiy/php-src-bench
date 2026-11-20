#!/bin/bash
# Builds one PHP for the series: ./build.sh <master|placement|pr|cold> <gcc15|clang21> [asan]
# Result: builds/<name>-<cc>[-asan]/ (an in-tree build of php-src: sapi/cgi/php-cgi, sapi/cli/php).
#   master     php-src master
#   placement  master + placement-<cc>.diff: dead code in Zend/zend_closures.c that moves all code after
#              zend_closures.o by the same number of bytes as the PR does (checked with nm, see README)
#   pr         master + pr18556.diff: php/php-src#18556 ported to this master (the PR branch no longer
#              merges: the signature of zend_create_closure_ex() changed since)
#   cold       pr + pr18556-cold.diff: the cache allocation moved into a ZEND_COLD function (same logic)
#   asan       --enable-debug with ASan/UBSan, for run-tests.php --asan
# Needs git, gcc 15 or clang 21, bison, re2c, autoconf, pkg-config and the -dev packages of libxml2, sqlite3,
# oniguruma, openssl, zlib, curl, libpq, icu, libzip, libgd, argon2, sodium, readline
# (Ubuntu: libxml2-dev libsqlite3-dev libonig-dev libssl-dev zlib1g-dev libcurl4-openssl-dev libpq-dev
# libicu-dev libzip-dev libgd-dev libargon2-dev libsodium-dev libreadline-dev).
set -eu
cd "$(dirname "$0")"
name=$1 cc=$2 asan=${3:-}
MASTER=0f55811bca0bdc31b80ce24c810ebc5bd9819929
case $cc in
	gcc15) CC=${GCC15:-gcc} CXX=${GXX15:-g++} ;;
	clang21) CC=${CLANG21:-clang} CXX=${CLANGXX21:-clang++} ;;
	*) echo "unknown compiler $cc" >&2; exit 1 ;;
esac
case $name in master|placement|pr|cold) ;; *) echo "unknown build $name" >&2; exit 1 ;; esac
dir=builds/$name-$cc${asan:+-asan}
[ -e "$dir" ] && { echo "$dir exists" >&2; exit 1; }
mkdir -p builds
git init -q "$dir"
cd "$dir"
git fetch -q --depth 1 https://github.com/php/php-src.git "$MASTER"
git checkout -q FETCH_HEAD
[ "$name" = placement ] && git apply "../../placement-$cc.diff"
[ "$name" = pr ] || [ "$name" = cold ] && git apply ../../pr18556.diff
[ "$name" = cold ] && git apply ../../pr18556-cold.diff
./buildconf --force > /dev/null
# Flags of the official Docker image (docker-library/php), plus -g. Extensions are static.
FLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
EXTRA=
[ -n "$asan" ] && EXTRA='--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer --disable-werror'
CC=$CC CXX=$CXX CFLAGS="$FLAGS" CXXFLAGS="$FLAGS" LDFLAGS='-Wl,-O1 -pie' ./configure -q --disable-all \
	--disable-phpdbg --enable-cli --enable-cgi --enable-ctype --enable-tokenizer --enable-filter \
	--enable-session --enable-posix --enable-fileinfo --enable-phar --with-libxml --enable-dom --enable-xml \
	--enable-simplexml --enable-xmlreader --enable-xmlwriter --enable-mbstring --enable-mysqlnd \
	--with-password-argon2 --with-sodium --with-curl --with-iconv --with-openssl --with-readline --with-zlib \
	--enable-sockets --enable-pcntl --enable-pdo --with-pdo-sqlite --with-sqlite3 --with-pdo-mysql \
	--with-pdo-pgsql --enable-bcmath --enable-calendar --enable-exif --enable-intl --enable-gd --with-jpeg \
	--with-webp --with-zip $EXTRA
make -j"$(nproc)" > /dev/null
# zend_test as a shared extension, for the observer tests (run-tests.php -d extension=...)
FLAGS_ZT='-O2 -g'
[ -n "$asan" ] && FLAGS_ZT='-O0 -g -fsanitize=address,undefined -fno-omit-frame-pointer'
(cd ext/zend_test && $CC -shared -fPIC $FLAGS_ZT -DCOMPILE_DL_ZEND_TEST -I. -I../.. -I../../main -I../../Zend \
	-I../../TSRM -I../../ext -I../../ext/date/lib $(pkg-config --cflags libxml-2.0) *.c -o ../../zend_test.so)
sapi/cli/php -n -v | head -1
nm sapi/cgi/php-cgi | grep -E ' T execute_ex$'
