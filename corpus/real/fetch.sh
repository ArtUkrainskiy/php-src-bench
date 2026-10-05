#!/usr/bin/env bash
# Download the real documents that suites/realdata.php and suites/htmlspecialchars.php use as
# inputs. They are not kept in this repository; see README.md next to this script.
#
#   corpus/real/fetch.sh           download what is missing
#   corpus/real/fetch.sh --force   download everything again
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"

php_src=https://raw.githubusercontent.com/php/php-src/100e8f353ea8ef841339ba4c74a0966a7eea5157
bootstrap=https://raw.githubusercontent.com/twbs/bootstrap/cc867751d7202aeb9f60d971dcc3ca104a872bab

# file, sha256 ("-" for live pages that change over time), URL
sources=(
	"js-confutils.txt       025b0a82a2fb3364b68329d64b9e0aac2117ea36891c7db2562a120e651355af $php_src/win32/build/confutils.js"
	"md-release-process.txt 8b4fd8bc0fdf49e1bc3132e22d8d886c33f5ed7754c56605fc67d1f4fb4d224a $php_src/docs/release-process.md"
	"md-bootstrap.txt       84082a379145e7ee3acfdc2e120479ce4aad1020472f1af8ad742344627c7cd1 $bootstrap/README.md"
	"js-jquery.txt          78a85aca2f0b110c29e0d2b137e09f0a1fb7a8e554b499f740d6744dc8962cfe https://code.jquery.com/jquery-3.7.1.js"
	"js-jquery.min.txt      fc9a93dd241f6b045cbff0481cf4e1901becd0e12fb45166a8f17f95823f0b1a https://code.jquery.com/jquery-3.7.1.min.js"
	"html-phpnet.txt        - https://www.php.net/manual/en/function.html-entity-decode.php"
	"html-wikipedia.txt     - https://en.wikipedia.org/wiki/HTML"
)

failed=0
for source in "${sources[@]}"; do
	read -r file sum url <<<"$source"
	if [[ -s "$file" && "${1:-}" != "--force" ]]; then
		echo "have    $file"
		continue
	fi
	if ! curl -fsSL --retry 2 -o "$file.part" "$url"; then
		echo "FAILED  $file  ($url)" >&2
		rm -f "$file.part"
		failed=1
		continue
	fi
	if [[ "$sum" != - && "$(sha256sum "$file.part" | cut -d' ' -f1)" != "$sum" ]]; then
		echo "FAILED  $file  (unexpected content from $url)" >&2
		rm -f "$file.part"
		failed=1
		continue
	fi
	mv "$file.part" "$file"
	if [[ "$sum" == - ]]; then
		echo "fetched $file  (live page: its content changes over time)"
	else
		echo "fetched $file"
	fi
done
exit "$failed"
