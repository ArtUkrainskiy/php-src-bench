#!/bin/bash
# Compares the machine code of every mysqlnd function in two NTS builds (master and the patch).
#   ./nts-objdump.sh <master php binary> <patched php binary>
# Functions: the text symbols whose debug line information points into ext/mysqlnd/ (nm -l; builds with -g). Addresses, jump targets
# and symbol offsets are normalized, so only instruction differences remain.
set -e
A=$1 B=$2
funcs=$(nm -l --defined-only "$A" | awk '$2 ~ /^[Tt]$/ && $4 ~ /\/ext\/mysqlnd\// {print $3}' | sort -u)
dis() {
	objdump -d --no-show-raw-insn "$1" | awk -v list="$funcs" '
		BEGIN { n = split(list, l, "\n"); for (i = 1; i <= n; i++) want[l[i]] = 1 }
		/^[0-9a-f]+ <[^>]+>:$/ { name = $2; gsub(/[<>:]/, "", name); on = (name in want); if (on) print "== " name; next }
		on && NF { sub(/^ *[0-9a-f]+:\t/, ""); gsub(/0x[0-9a-f]+/, "X"); gsub(/\<[0-9a-f]{4,}\>/, "X"); gsub(/<[^>]*>/, "<>"); print }'
}
t=$(mktemp -d)
dis "$A" > "$t/a"
dis "$B" > "$t/b"
echo "functions: $(command grep -c '^== ' "$t/a") / $(command grep -c '^== ' "$t/b"), differing lines: $(diff "$t/a" "$t/b" | command grep -c '^[<>]' || true)"
rm -r "$t"
