# Reports

Results that are cited somewhere, usually in a php-src pull request, with everything needed to
check them: what was compared, the full tables, how the output was verified and the commands to
run it again.

| Report | php-src change |
|---|---|
| [htmlspecialchars-ascii-fast-path](htmlspecialchars-ascii-fast-path/) | ext/standard: Add a fast path for ASCII in htmlspecialchars() |

## Adding a report

One directory per change:

```sh
mkdir reports/<name>
./bench run <suite> --a base --b <build> --perf --wait-idle 600   # default rounds, quiet machine
sed "s|$(dirname "$PWD")/|../|g" results/<file>.json > reports/<name>/<suite>.json
./bench show reports/<name>/<suite>.json --md             # the table for README.md
```

The `sed` strips the absolute paths of your machine from the result. `README.md` of a report says:

- which two commits were compared, with links, and what the change is;
- the machine and its state during the run (governor, load, whether warnings were printed);
- a summary by kind of input, including what got slower or did not change;
- the full table of every suite that was run;
- how the output was verified (`bench difftest`, tests, sanitizers);
- the commands to reproduce it.

Build both sides from commits, not from a working tree snapshot, so that the report names
something others can check out. Numbers from other tools, such as php-src's
`benchmark/benchmark.php`, belong in the report too, with a sentence on how they were obtained.
