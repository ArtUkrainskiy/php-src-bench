#!/usr/bin/env python3
"""Check that functional validation rejects four meaningful matching errors."""
from pathlib import Path
import argparse
import json
import subprocess
import tempfile

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--cc', default='cc')
a = p.parse_args()
root = Path(__file__).resolve().parent
source = (root / 'standalone.c').read_text()
driver = (root / 'validate.c').read_text()
start = source.index('static zend_never_inline const char* ZEND_FASTCALL zend_memnstr_sunday_short(')
end = source.index('/* }}} */', start)
mutations = {
    'short-skipped-shift': ('(unsigned char)(needle_len + 1), sizeof(td)', '(unsigned char)(needle_len + 2), sizeof(td)'),
    'short-missing-last-byte': ('if (needle[i] != p[i])', 'if (i + 1 < needle_len && needle[i] != p[i])'),
    'wrong-twoway-shift': ('pos += i - cut + 1;', 'pos += i - cut + 2;'),
    'missing-full-verification': ('if (!memcmp(haystack + candidate, needle, needle_len)) {', 'if (1) {'),
}
results = []
with tempfile.TemporaryDirectory(prefix='substring-mutations-') as temporary:
    work = Path(temporary)
    for name, (before, after) in mutations.items():
        if name.startswith('short-'):
            part = source[start:end]
            assert before in part
            mutant = source[:start] + part.replace(before, after, 1) + source[end:]
        else:
            assert before in source
            mutant = source.replace(before, after, 1)
        (work / 'standalone.c').write_text(mutant)
        (work / 'validate.c').write_text(driver)
        subprocess.run([a.cc, '-O2', str(work / 'validate.c'), '-o', str(work / 'check')], check=True)
        result = subprocess.run([str(work / 'check'), '20000'], capture_output=True, text=True, timeout=30)
        assert result.returncode == 3, (name, result.returncode, result.stderr)
        results.append({'mutation': name, 'exit_code': result.returncode, 'message': result.stderr.strip()})
        print(name, 'rejected', flush=True)
(root / 'mutations.json').write_text(json.dumps(results, indent=2) + '\n')
