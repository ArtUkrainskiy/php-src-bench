#!/usr/bin/env python3
# Mutation check of difftest.php: apply one mutation to PR #23961's html.c in the hcs-mut build
# (a `bench build` of master + #23961), rebuild, compare difftest with master's output.
import os, subprocess

B = os.path.join(os.environ.get("BENCH_BUILDS", os.path.expanduser("~/CLionProjects/php-builds")), "hcs-mut")
HERE = os.path.dirname(os.path.abspath(__file__))
REF = open(os.path.join(HERE, "difftest-master.txt")).read()
F = "ext/standard/html.c"
MUT = [
    ("accept \"utf-8\" + anything", "&& charset_hint[5] == '\\0';", ";"),
    ("accept \"utf_8\"", "charset_hint[3] == '-'", "(charset_hint[3] == '-' || charset_hint[3] == '_')"),
    ("first letter case-sensitive", "if (zend_tolower_ascii(codeset[0]) != first) {", "if ((unsigned char) codeset[0] != first) {"),
    ("second character not compared", "for (size_t j = 1; zend_tolower_ascii(charset_hint[j])", "for (size_t j = 2; zend_tolower_ascii(charset_hint[j])"),
    ("prefix of a codeset accepted", "if (codeset[j] == '\\0') {\n\t\t\t\treturn charset_map[i].charset;", "if (codeset[j] == '\\0' || charset_hint[j + 1] == '\\0') {\n\t\t\t\treturn charset_map[i].charset;"),
    ("no default: lookup of NULL", "\t\tif (!charset_hint) {\n\t\t\treturn cs_utf_8;\n\t\t}\n", "\t\tif (!charset_hint) {\n\t\t\tcharset_hint = \"\";\n\t\t}\n"),
]

def run():
    r = subprocess.run([f"{B}/sapi/cli/php", "-n", os.path.join(HERE, "difftest.php"), "10000", "7"], capture_output=True, text=True, timeout=1200)
    return r.stdout if r.returncode == 0 else f"exit {r.returncode}\n" + r.stdout

path = os.path.join(B, F)
orig = open(path).read()
for name, a, b in MUT:
    assert orig.count(a) == 1, name
    try:
        open(path, "w").write(orig.replace(a, b))
        subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
        out = run()
        if out.startswith("exit"):
            print(f"{name:32} CAUGHT: {out.splitlines()[0]}", flush=True)
            continue
        diff = [l.split()[0] + (" " + l.split()[1] if not l.split()[1].isdigit() else "") for l, r in zip(out.splitlines(), REF.splitlines()) if l != r]
        print(f"{name:32} {'CAUGHT: ' + ', '.join(diff) if diff else 'missed'}", flush=True)
    finally:
        open(path, "w").write(orig)
subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
print("unmutated:", "same as master" if run() == REF else "DIFFERENT")
