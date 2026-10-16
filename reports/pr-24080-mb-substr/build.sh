#!/bin/bash
# build.sh <cc> <tag> <variant> <ref> [asan]: build mb-<tag>-<variant> with ./bench from the repository root.
#   PHP_SRC=<php-src checkout with the refs> ./build.sh gcc g13 base 1c9242e7fec
# Flags of the official Docker image, --enable-werror, mbstring without mbregex.
# base = master 1c9242e7fec, pr = master + #24080 (b218ba6b8d2) merged, fix = pr + fix.diff.
cd "$(dirname "$0")/../.."
F='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'; L='-Wl,-O1 -pie'; X='--enable-werror --enable-mbstring --disable-mbregex'
if [[ "$5" == asan ]]; then
	F='-O1 -g'; L=''; X='--enable-mbstring --disable-mbregex --enable-debug --enable-address-sanitizer --enable-undefined-sanitizer'
fi
CC=$1 BENCH_CFLAGS="$F" LDFLAGS="$L" BENCH_CONFIGURE_EXTRA="$X" ./bench build "mb-$2-$3" "$4"
