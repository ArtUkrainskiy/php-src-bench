#!/usr/bin/env python3
# Mutation check of difftest.php: apply one mutation to the PR's var.c in the vx-mut build
# (a `bench build` of master + PR), rebuild (re2c regenerates the scanner), compare difftest with master's output.
import os, subprocess

B = os.path.join(os.environ["BENCH_BUILDS"], "vx-mut")
HERE = os.path.dirname(os.path.abspath(__file__))
REF = open(os.path.join(HERE, "difftest-master.txt")).read()
F = "ext/standard/var.c"
MUT = [
    ("NUL counted as 10 extra bytes", "escaped_len += 11;", "escaped_len += 10;"),
    ("NUL in array keys not escaped", "php_var_export_append_escaped(buf, ZSTR_VAL(key), ZSTR_LEN(key), /* escape_nul */ true);", "php_var_export_append_escaped(buf, ZSTR_VAL(key), ZSTR_LEN(key), /* escape_nul */ false);"),
    ("quote not escaped when written", "\t\t\tif (c == '\\'' || c == '\\\\') {\n\t\t\t\t*target++ = '\\\\';", "\t\t\tif (c == '\\\\') {\n\t\t\t\t*target++ = '\\\\';"),
    ("length not counted (always bulk copy)", "if (escaped_len == len) {", "if (1) {"),
    ("one space less", "char *target = smart_str_extend(buf, (size_t) num_spaces);\n\tmemset(target, ' ', num_spaces);", "char *target = smart_str_extend(buf, (size_t) num_spaces - 1);\n\tmemset(target, ' ', num_spaces - 1);"),
    ("NUL escaped in property names", "php_var_export_append_escaped(buf, prop_name, prop_name_len, /* escape_nul */ false);", "php_var_export_append_escaped(buf, prop_name, prop_name_len, /* escape_nul */ true);"),
]

def run():
    r = subprocess.run([f"{B}/sapi/cli/php", "-n", os.path.join(HERE, "difftest.php"), "200000", "7"], capture_output=True, text=True, timeout=1200)
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
        diff = [l.split("  ")[0].strip() for l, r in zip(out.splitlines(), REF.splitlines()) if l != r]
        print(f"{name:32} {'CAUGHT: ' + ', '.join(diff) if diff else 'missed'}", flush=True)
    finally:
        open(path, "w").write(orig)
subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
print("unmutated:", "same as master" if run() == REF else "DIFFERENT")
