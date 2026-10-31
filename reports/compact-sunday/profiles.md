# Long-scan diagnostic profiles

Median user-space counts per English moderation-thread operation over three passes.
Percentage changes are rounded to whole percent. Cache/TLB changes are absolute
events per operation, calculated before the displayed counts are rounded.
The setup, lookup width, generated loop and code placement change together; these profiles do not isolate a unique cause.

## Clang 21.1

| Event | master / op | compact / op | Δ vs master |
|---|--:|--:|--:|
| cycles | 765,638 | 706,499 | −8% |
| instructions | 1,077,140 | 1,076,720 | 0% |
| branches | 308,476 | 308,496 | 0% |
| branch-misses | 2,207 | 2,223 | +1% |
| L1-icache-load-misses | 0.91 | 0.99 | +0.08 events/op |
| iTLB-load-misses | 0.16 | 0.03 | -0.13 events/op |

## GCC 15.2

| Event | master / op | compact / op | Δ vs master |
|---|--:|--:|--:|
| cycles | 810,537 | 753,840 | −7% |
| instructions | 1,140,941 | 1,139,515 | 0% |
| branches | 308,988 | 308,688 | 0% |
| branch-misses | 2,267 | 2,271 | 0% |
| L1-icache-load-misses | 1.88 | 1.42 | -0.45 events/op |
| iTLB-load-misses | 0.07 | 0.09 | +0.02 events/op |

[Raw profile logs](data/profiles.tar.gz): A is master; B is compact.
