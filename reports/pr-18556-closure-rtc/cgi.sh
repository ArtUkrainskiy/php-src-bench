#!/bin/bash
# cgi.sh <php-cgi> <docroot> <uri> <warmup> <repeat> [extra php-cgi args...]
# One php-cgi -T process serving <uri> through <docroot>/index.php: full request startup and shutdown per
# iteration, opcache on (no timestamp checks), JIT off. The body goes to stdout.
C=$(cd "$(dirname "$1")" && pwd)/$(basename "$1") D=$2 U=$3 W=$4 N=$5; shift 5
cd "$D" || exit 1
exec env -i PATH=/usr/bin:/bin HOME="$HOME" REDIRECT_STATUS=200 REQUEST_METHOD=GET REQUEST_URI="$U" \
  SCRIPT_FILENAME="$D/index.php" SCRIPT_NAME=/index.php SERVER_NAME=localhost SERVER_PORT=80 HTTP_HOST=localhost \
  APP_ENV=prod APP_DEBUG=0 \
  "$C" -q -d cgi.force_redirect=0 -d max_execution_time=0 -d memory_limit=512M \
  -d opcache.enable=1 -d opcache.jit=disable -d opcache.validate_timestamps=0 -d opcache.file_update_protection=0 \
  -d opcache.memory_consumption=256 -d opcache.interned_strings_buffer=32 -d opcache.max_accelerated_files=50000 \
  "$@" -T "$W,$N" "$D/index.php"
