#!/usr/bin/env python3
"""Prepare a private bench copy that loads shared modules without rebuilding measured CLIs."""
import argparse
import json
from pathlib import Path
import shutil

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--bench-root', type=Path, required=True)
p.add_argument('--out', type=Path, required=True)
p.add_argument('--map', type=Path, required=True, help='JSON: absolute PHP binary path -> absolute module directory')
a = p.parse_args()
a.out = a.out.resolve()
assert not a.out.exists(), 'Use a fresh private runner directory'
mapping = json.loads(a.map.read_text())
for binary, directory in mapping.items():
    assert Path(binary).is_file()
    assert all((Path(directory) / (name + '.so')).is_file() for name in ['mbstring', 'intl'])
a.out.mkdir(parents=True)
for name in ['lib', 'suites']:
    shutil.copytree(a.bench_root / name, a.out / name)
shutil.copy2(a.bench_root / 'bench', a.out / 'bench')
(a.out / 'corpus').mkdir()
(a.out / 'modules-map.json').write_text(json.dumps(mapping, indent=2) + '\n')
process = a.out / 'lib/process.php'
s = process.read_text()
old = "    return [$php, '-n', '-d', 'memory_limit=-1', HARNESS, $suite, json_encode($options)];"
assert s.count(old) == 1, 'Runner changed; review the startup adapter before using it'
new = """    $map = json_decode(file_get_contents(__DIR__ . '/../modules-map.json'), true, 512, JSON_THROW_ON_ERROR);
    $dir = $map[realpath($php)];
    return [$php, '-n', '-d', 'memory_limit=-1', '-d', 'extension_dir=' . $dir,
        '-d', 'extension=mbstring.so', '-d', 'extension=intl.so',
        HARNESS, $suite, json_encode($options)];"""
process.write_text(s.replace(old, new))
print(a.out / 'bench')
