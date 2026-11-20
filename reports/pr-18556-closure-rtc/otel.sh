#!/bin/bash
# Builds the OpenTelemetry extension against one build: ./otel.sh <build dir> [lazy]
# Result: <build dir>/opentelemetry.so (or opentelemetry-lazy.so with otel-lazy-withspan.diff applied).
# The extension is open-telemetry/opentelemetry-php-instrumentation at a fixed commit, built with the
# Docker-image flags against the headers of that build tree (no phpize: the builds are not installed).
set -eu
cd "$(dirname "$0")"
OTEL=816db17c8ac6e5ca11265930623e5965fe28e9ba
T=$(cd "$1" && pwd) lazy=${2:-}
[ -d otel-src ] || { git clone -q https://github.com/open-telemetry/opentelemetry-php-instrumentation.git otel-src; git -C otel-src checkout -q "$OTEL"; }
rm -rf otel-build && cp -a otel-src otel-build
[ -n "$lazy" ] && git -C otel-build apply ../otel-lazy-withspan.diff
cd otel-build/ext
${CC:-gcc} -shared -fPIC -fstack-protector-strong -O2 -g -DCOMPILE_DL_OPENTELEMETRY -I. -I"$T" -I"$T/main" \
	-I"$T/Zend" -I"$T/TSRM" -I"$T/ext" -I"$T/ext/date/lib" opentelemetry.c otel_observer.c \
	-o "$T/opentelemetry${lazy:+-lazy}.so"
cd ../.. && rm -rf otel-build
"$T/sapi/cli/php" -n -d extension="$T/opentelemetry${lazy:+-lazy}.so" -r 'echo phpversion("opentelemetry"), "\n";'
