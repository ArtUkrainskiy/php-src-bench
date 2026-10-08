#!/usr/bin/env python3
import subprocess, sys, re
PHP = sys.argv[1] if len(sys.argv) > 1 else 'php'
N = 100000
def instr(mode, er, extra=()):
    cmd = ['taskset', '-c', '2', 'perf', 'stat', '-e', 'instructions:u', '-x,', PHP, '-n', '-d', 'display_errors=0', '-d', 'log_errors=0', '-d', 'html_errors=0', '-d', f'error_reporting={er}', *extra, 'deprecation-cost.php', mode, str(N)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    tot = 0
    for line in r.stderr.splitlines():
        f = line.split(',')
        if len(f) > 2 and 'instructions' in line and f[0].isdigit():
            tot += int(f[0])
    return tot
base = instr('baseline', 'E_ALL')
print(f'baseline (getName() in the loop): {base/N:.0f} instructions per iteration')
for mode, er, extra, label in [
    ('none', 'E_ALL', (), 'no handler, E_DEPRECATED reported (display/log off)'),
    ('none', 'E_ALL&~E_DEPRECATED', (), 'no handler, E_DEPRECATED filtered by error_reporting'),
    ('none', 'E_ALL', ('-d', 'log_errors=1', '-d', 'error_log=/dev/null'), 'no handler, logged to error_log'),
    ('noop', 'E_ALL', (), 'handler returning false, E_DEPRECATED reported'),
    ('noop', 'E_ALL&~E_DEPRECATED', (), 'handler returning false, E_DEPRECATED filtered'),
    ('framework', 'E_ALL', (), 'framework-like handler (sprintf + store), reported'),
    ('framework', 'E_ALL&~E_DEPRECATED', (), 'framework-like handler, filtered (handler checks error_reporting())'),
]:
    v = instr(mode, er, extra)
    print(f'{(v-base)/N:9.0f}  {label}')
