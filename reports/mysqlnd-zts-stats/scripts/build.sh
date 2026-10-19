#!/bin/bash
# Builds PHP ZTS (embed) from a source archive and FrankenPHP 1.13.1 against it.
#   FRANKENPHP_SRC=<frankenphp-1.13.1 source> ./build.sh php-master-b7256ee [suffix]   (archive <name>.tar.gz in this directory)
#   EXTRA_CONFIGURE="--with-mysqli" ./build.sh php-master-b7256ee mysqli   -> php-master-b7256ee-mysqli/
# The archive: git archive --prefix=<name>/ <commit> | gzip > <name>.tar.gz (master b7256eee301, or it with ../mysqlnd-stats-atomic.patch applied)
# Result: <name>/  (PHP build, libs/libphp.so) and <name>/frankenphp
set -e
cd "$(dirname "$0")"
name=$1
D=$PWD/$name${2:+-$2}
GO=${GO:-$(dirname "$(command -v go)")}
FSRC=${FRANKENPHP_SRC:?}
test -d "$D" || { mkdir -p "$D.tmp" && tar xzf "$name.tar.gz" -C "$D.tmp" && mv "$D.tmp/$name" "$D" && rmdir "$D.tmp"; }
cd "$D"
test -x configure || ./buildconf --force > buildconf.log 2>&1
flags='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
if ! test -f Makefile; then
	CFLAGS="$flags" CPPFLAGS="$flags" LDFLAGS='-Wl,-O1 -pie' ./configure --disable-all --disable-cgi --disable-phpdbg --enable-cli \
		--enable-zts --enable-embed --disable-zend-signals --enable-zend-max-execution-timers \
		--with-openssl --enable-mysqlnd --enable-pdo --with-pdo-mysql $EXTRA_CONFIGURE > configure.log 2>&1
fi
taskset -c 16-31 make -j16 > make.log 2>&1
echo "php: $(sapi/cli/php -v | head -1)"
rm -rf "$D/frankenphp-src"
cp -a "$FSRC" "$D/frankenphp-src"
# master removed zend_atomic.h (php-src #23927): C11 atomics in place of zend_atomic_bool in FrankenPHP 1.13.1
sed -i 's/zend_atomic_bool_store(/atomic_store(/g; s/zend_atomic_bool_load(/atomic_load(/g; s/zend_atomic_bool/atomic_bool/g' \
	"$D/frankenphp-src/frankenphp.c" "$D/frankenphp-src/frankenphp.h"
# master removed sapi_module_struct.terminate_process (php-src #23524)
sed -i '/NULL, *\/\* Child terminate \*\//d' "$D/frankenphp-src/frankenphp.c"
B=$D
LIBS=$(sh "$B/scripts/php-config" --libs)
(cd "$D/frankenphp-src/caddy/frankenphp" && PATH=$GO:$PATH GOTOOLCHAIN=local CGO_ENABLED=1 \
	CGO_CFLAGS="-O2 -I$B -I$B/main -I$B/Zend -I$B/TSRM -I$B/ext -I$B/ext/date/lib" \
	CGO_LDFLAGS="-L$B/libs -lphp $LIBS -Wl,-rpath,$B/libs" \
	go build -tags=nobadger,nomysql,nopgx,nowatcher,nomercure,novulcain -o "$D/frankenphp" . > "$D/frankenphp-build.log" 2>&1) \
	|| { echo "frankenphp build failed, see $D/frankenphp-build.log"; tail -n 20 "$D/frankenphp-build.log"; exit 1; }
echo "frankenphp: $("$D/frankenphp" version | head -1)"
ldd "$D/frankenphp" | command grep libphp
