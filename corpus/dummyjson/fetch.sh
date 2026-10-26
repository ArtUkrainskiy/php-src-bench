#!/bin/sh
# Real backend JSON samples from dummyjson.com, used by suites/jsondummy.php.
# Full collections (limit=0): products and users are field/nesting heavy, posts and
# comments and quotes and recipes carry free text. Re-run to refresh.
set -e
cd "$(dirname "$0")"
for ep in products comments posts users recipes carts quotes todos; do
	curl -fsS "https://dummyjson.com/$ep?limit=0" -o "$ep.json"
	echo "$ep.json: $(wc -c < "$ep.json") bytes"
done
