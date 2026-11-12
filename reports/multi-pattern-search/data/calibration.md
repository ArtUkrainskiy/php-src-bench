# Calibration: how long to time each method

Before the run we looked for the cheapest timing setup whose result doesn't move between processes.

- **One process** is reproducible to about ±2%: the 90th percentile of the spread stays at 3–4.5% for every pass length. A longer timer doesn't remove this noise, it comes with the process.
- **The median of three processes** with 20 ms passes is reproducible to about ±0.7%: its spread is 1.0–1.4% at the 90th percentile. 40 ms passes don't do better.
- **A/A** stays within 1.3% from 20 ms passes.
- **The run** uses 5 passes and the median of 3 processes.

In calibration each method had its own number of calls to fill a pass. In the run every method makes the same number of calls, so the fastest method's pass is often shorter than 20 ms (see [METHOD.md](../METHOD.md)).

## Setup

Four inputs (`matches()` and `countMatches()` on 4 KiB, `replace()` on 64 KiB, `getMatchedKeywords()` on 128 B), both modes and both compilers, each timed in 5 fresh processes for every setup.
The calibration used an earlier version of the harness and extra PCRE variants. It measures noise, not the comparison.

- **Ratio spread**: how far the ratio of native to reference time moves between results built from different processes, in percent of the ratio.
- **Processes**: with 1, a result is one process. With 3, it is their median, taken over every choice of 3 of the 5 processes, so those results share processes.
- **Passes**: fewer passes are the first passes of the same 11-pass processes.

| Pass, ms | Passes | Processes | Time per method, ms | Ratio spread, median % | p90 % | max % | Max |A/A|, % | Native spread p90, % |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 1 | 6 | 2.00 | 3.48 | 3.64 | 4.20 | 2.21 |
| 2 | 3 | 3 | 18 | 0.66 | 2.17 | 2.58 | 4.20 | 1.55 |
| 2 | 5 | 1 | 10 | 1.43 | 3.48 | 3.68 | 3.70 | 2.22 |
| 2 | 5 | 3 | 30 | 0.61 | 1.67 | 2.29 | 3.70 | 1.32 |
| 2 | 7 | 1 | 14 | 1.34 | 3.48 | 3.68 | 3.31 | 2.21 |
| 2 | 7 | 3 | 42 | 0.65 | 1.67 | 2.29 | 3.31 | 1.32 |
| 2 | 11 | 1 | 22 | 1.66 | 3.48 | 3.68 | 3.23 | 2.57 |
| 2 | 11 | 3 | 66 | 0.60 | 1.63 | 2.41 | 3.23 | 1.70 |
| 5 | 3 | 1 | 15 | 2.02 | 3.33 | 3.34 | 2.17 | 1.71 |
| 5 | 3 | 3 | 45 | 0.55 | 1.93 | 2.68 | 2.17 | 1.07 |
| 5 | 5 | 1 | 25 | 1.85 | 4.41 | 5.36 | 1.87 | 1.43 |
| 5 | 5 | 3 | 75 | 0.78 | 1.86 | 2.12 | 1.87 | 1.19 |
| 5 | 7 | 1 | 35 | 1.76 | 4.53 | 4.53 | 1.86 | 1.90 |
| 5 | 7 | 3 | 105 | 0.79 | 1.86 | 2.24 | 1.86 | 1.03 |
| 5 | 11 | 1 | 55 | 1.77 | 4.17 | 4.83 | 1.86 | 1.75 |
| 5 | 11 | 3 | 165 | 0.73 | 2.07 | 2.70 | 1.86 | 0.65 |
| 10 | 3 | 1 | 30 | 1.52 | 3.49 | 3.81 | 1.96 | 2.34 |
| 10 | 3 | 3 | 90 | 0.62 | 2.27 | 2.62 | 1.96 | 0.88 |
| 10 | 5 | 1 | 50 | 1.48 | 3.81 | 4.09 | 1.96 | 2.50 |
| 10 | 5 | 3 | 150 | 0.79 | 2.16 | 2.62 | 1.96 | 0.84 |
| 10 | 7 | 1 | 70 | 1.16 | 3.74 | 3.81 | 1.57 | 2.43 |
| 10 | 7 | 3 | 210 | 0.71 | 1.95 | 2.75 | 1.57 | 0.77 |
| 10 | 11 | 1 | 110 | 1.20 | 3.23 | 3.81 | 1.34 | 2.32 |
| 10 | 11 | 3 | 330 | 0.59 | 1.67 | 2.75 | 1.34 | 0.77 |
| 20 | 3 | 1 | 60 | 1.63 | 3.30 | 3.78 | 1.30 | 1.20 |
| 20 | 3 | 3 | 180 | 0.57 | 1.38 | 1.60 | 1.30 | 1.02 |
| 20 | 5 | 1 | 100 | 1.65 | 3.39 | 3.62 | 1.02 | 1.30 |
| 20 | 5 | 3 | 300 | 0.43 | 1.33 | 1.46 | 1.02 | 0.97 |
| 20 | 7 | 1 | 140 | 1.65 | 2.96 | 3.56 | 0.89 | 1.36 |
| 20 | 7 | 3 | 420 | 0.39 | 1.40 | 1.53 | 0.89 | 0.99 |
| 20 | 11 | 1 | 220 | 1.54 | 3.26 | 3.30 | 0.84 | 1.16 |
| 20 | 11 | 3 | 660 | 0.45 | 0.99 | 1.40 | 0.84 | 0.84 |
| 40 | 3 | 1 | 120 | 1.23 | 3.44 | 3.68 | 0.78 | 1.59 |
| 40 | 3 | 3 | 360 | 0.36 | 2.29 | 3.11 | 0.78 | 0.85 |
| 40 | 5 | 1 | 200 | 1.32 | 3.48 | 3.68 | 0.78 | 1.58 |
| 40 | 5 | 3 | 600 | 0.33 | 2.35 | 3.11 | 0.78 | 0.66 |
| 40 | 7 | 1 | 280 | 1.25 | 3.34 | 3.64 | 0.73 | 2.06 |
| 40 | 7 | 3 | 840 | 0.40 | 2.64 | 3.02 | 0.73 | 0.73 |
| 40 | 11 | 1 | 440 | 1.51 | 3.32 | 3.54 | 0.67 | 2.13 |
| 40 | 11 | 3 | 1320 | 0.47 | 2.72 | 2.76 | 0.67 | 0.78 |

Raw data: [probe/calibration.jsonl](probe/calibration.jsonl), summary [probe/calibration-summary.txt](probe/calibration-summary.txt).
