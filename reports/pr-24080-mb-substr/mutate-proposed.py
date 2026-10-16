#!/usr/bin/env python3
# Runs the proposed mb_substr_valid_utf8.phpt against the mutants that ext/mbstring/tests miss.
#   BENCH_BUILDS=<dir with the builds> mutate-proposed.py
import subprocess, pathlib
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / 'mutate.py').read_text().split('\norig = SRC.read_text()')[0]
m = {'__file__': str(HERE / 'mutate.py')}
exec(src, m)
BUILD, SRC, MUTANTS = m['BUILD'], m['SRC'], m['MUTANTS']
test = BUILD / 'ext/mbstring/tests/zz_proposed_mb_substr_valid_utf8.phpt'
test.write_text((HERE / 'mb_substr_valid_utf8.phpt').read_text())
orig = SRC.read_text()
def run():
	r = subprocess.run(f'cd {BUILD} && TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php -n run-tests.php -q --no-color {test}', shell=True, capture_output=True, text=True)
	return 'CAUGHT' if 'Tests failed    :     1' in r.stdout else ('missed' if 'Tests passed    :     1' in r.stdout else 'ERROR\n' + r.stdout[-500:])
try:
	print(f'{"unmutated":50} {run()}', flush=True)
	for i in (0, 2, 3, 5):
		name, old, new = MUTANTS[i]
		SRC.write_text(orig.replace(old, new))
		subprocess.run(f'cd {BUILD} && make -j8 > /dev/null 2>&1', shell=True)
		print(f'{name:50} {run()}', flush=True)
finally:
	SRC.write_text(orig)
	test.unlink()
	subprocess.run(f'cd {BUILD} && make -j8 > /dev/null 2>&1', shell=True)
