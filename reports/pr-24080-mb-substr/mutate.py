#!/usr/bin/env python3
# Applies one mutation at a time to mb-g13-mut (a full build of the fix variant, GCC 13.3),
# rebuilds incrementally, runs difftest.php (seed 5, 2000 cases) against mb-g13-base and the
# ext/mbstring tests, and reports whether each catches it.
#   BENCH_BUILDS=<dir with the builds> mutate.py [mutation index ...]
import os, subprocess, sys, pathlib

BUILD = pathlib.Path(os.environ['BENCH_BUILDS']) / 'mb-g13-mut'
BASE = pathlib.Path(os.environ['BENCH_BUILDS']) / 'mb-g13-base'
HERE = pathlib.Path(__file__).resolve().parent
SRC = BUILD / 'ext/mbstring/mbstring.c'

MUTANTS = [
	('mobile variants take the fast path',
	 'if (enc == &mbfl_encoding_utf8 && ZSTR_IS_VALID_UTF8(input)) {',
	 'if (php_mb_is_no_encoding_utf8(enc->no_encoding) && ZSTR_IS_VALID_UTF8(input)) {'),
	('invalid strings take the fast path',
	 'if (enc == &mbfl_encoding_utf8 && ZSTR_IS_VALID_UTF8(input)) {',
	 'if (enc == &mbfl_encoding_utf8) {'),
	('chunk loop runs down to offset 0',
	 'while (offset > 256 && (size_t)(end - pos) >= 256) {',
	 'while (offset > 0 && (size_t)(end - pos) >= 256) {'),
	('chunk step one byte short',
	 'pos += 256;',
	 'pos += 255;'),
	('only ASCII bytes counted as characters',
	 'if (!IS_UTF8_CONTINUATION_BYTE(*pos)) {\n\t\t\t\t\tif (offset == 0) {',
	 'if (*pos < 0x80) {\n\t\t\t\t\tif (offset == 0) {'),
	('offset past the end returns the end',
	 'return offset == 0 ? end : NULL;',
	 'return end;'),
	('strpos uses the fast path for unchecked strings',
	 'needle_len, ZSTR_IS_VALID_UTF8(haystack_u8));',
	 'needle_len, true);'),
	('result length one character short',
	 'stop = offset_to_pointer_utf8(start, end, len, true);',
	 'stop = offset_to_pointer_utf8(start, end, len - 1, true);'),
]


def sh(cmd, **kw):
	return subprocess.run(cmd, shell=True, capture_output=True, text=True, **kw)


def difftest():
	out = {}
	for name, php in (('base', BASE), ('mut', BUILD)):
		r = sh(f'{php}/sapi/cli/php -n {HERE}/difftest.php 5 2000', timeout=600)
		out[name] = r.stdout
	if out['base'] == out['mut']:
		return 'missed'
	a, b = out['base'].splitlines(), out['mut'].splitlines()
	diff = sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))
	return f'CAUGHT ({diff} lines differ)'


def phpt():
	r = sh(f'cd {BUILD} && TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php -n run-tests.php -q -j8 --no-color ext/mbstring/tests', timeout=900)
	failed = [l.strip() for l in r.stdout.split('FAILED TEST SUMMARY')[-1].splitlines() if l.strip().endswith('.phpt]')] if 'FAILED TEST SUMMARY' in r.stdout else []
	return f'CAUGHT by {len(failed)}' if failed else 'missed'


orig = SRC.read_text()
try:
	only = sys.argv[1:]
	for i, (name, old, new) in enumerate(MUTANTS):
		if only and str(i) not in only:
			continue
		assert orig.count(old) == 1, name
		SRC.write_text(orig.replace(old, new))
		r = sh(f'cd {BUILD} && make -j8 > /dev/null 2>&1; echo $?')
		if r.stdout.strip() != '0':
			print(f'{name:50} BUILD FAILED', flush=True)
			continue
		print(f'{name:50} difftest: {difftest():28} phpt: {phpt()}', flush=True)
finally:
	SRC.write_text(orig)
	sh(f'cd {BUILD} && make -j8 > /dev/null 2>&1')
	print('unmutated difftest:', difftest(), flush=True)
