# Long-scan diagnostic profiles

Three passes on the English clean thread. The setup, lookup width, generated loop and code placement change together; these profiles do not isolate a unique cause.

## clang21

| event | A | B | B vs A |
|---|--:|--:|--:|
| cycles | 765,638 | 706,499 | −8% |
| instructions | 1,077,140 | 1,076,720 | 0% |
| branches | 308,476 | 308,496 | 0% |
| branch-misses | 2,207 | 2,223 | +1% |
| L1-icache-load-misses | 0.91 | 0.99 | +0.08 |
| iTLB-load-misses | 0.16 | 0.03 | -0.13 |

## gcc15

| event | A | B | B vs A |
|---|--:|--:|--:|
| cycles | 810,537 | 753,840 | −7% |
| instructions | 1,140,941 | 1,139,515 | 0% |
| branches | 308,988 | 308,688 | 0% |
| branch-misses | 2,267 | 2,271 | 0% |
| L1-icache-load-misses | 1.88 | 1.42 | -0.45 |
| iTLB-load-misses | 0.07 | 0.09 | +0.02 |

