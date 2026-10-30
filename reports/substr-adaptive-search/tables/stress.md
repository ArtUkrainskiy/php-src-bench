# Repeated-prefix stress cases

Supplementary guards, not a frequency distribution of everyday requests. These compare the same final candidate and base. Every original pass, A/A control and warning remains visible.

## amd-adversarial

<!-- bench-table ../data/stress/amd-adversarial.json --header --full -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-38-generic.
Group gcc15: A = base-gcc15 (ef99f4248f1 GCC 15.2, profile docker), B = product-guard-gcc15 (ca89fb5fb96 GCC 15.2, profile docker).
Group clang21: A = base-clang21 (ef99f4248f1 clang 21.1, profile docker), B = product-guard-clang21 (ca89fb5fb96 clang 21.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 | instructions |
|---|--:|--:|--:|--:|
| first dense_anchor dense n3 #318 @ case-318 | 5,266,282 | 0% (0 … 0) ~ | 0% (0 … 0) | 0% |
| first allcommon_long allcommon_long n201 #320 @ case-320 | 34,771,274 | −100% (−100 … −100) | −100% (−100 … −100) | −100% |
| first periodic periodic n9 #323 @ case-323 | 1,172,645 | −8% (−8 … −8) layout? | +7% (+7 … +8) layout? | 0% |
| late dense pair @ pair-killer | 14,137,246 | −99% (−99 … −99) | −99% (−100 … −99) | −99% |
| late dense pair @ changing-density | 14,249,506 | −99% (−99 … −99) | −99% (−99 … −99) | −99% |
| late dense pair @ changing-density-match | 14,578,288 | −99% (−99 … −99) | −99% (−99 … −99) | −99% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| first dense_anchor dense n3 #318 @ case-318 | 5,269,102 | 0% (0 … 0) | 0% (0 … 0) |
| first allcommon_long allcommon_long n201 #320 @ case-320 | 34,760,084 | 0% (0 … 0) | 0% (−3 … 0) |
| first periodic periodic n9 #323 @ case-323 | 1,171,066 | 0% (−1 … +2) | 0% (0 … +1) |
| late dense pair @ pair-killer | 14,208,536 | −1% (−2 … +2) | 0% (−1 … +1) |
| late dense pair @ changing-density | 14,782,377 | 0% (−5 … +4) | +1% (0 … +4) |
| late dense pair @ changing-density-match | 14,837,029 | −3% (−6 … +8) | +5% (−2 … +11) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->

## amd-long-prefix

<!-- bench-table ../data/stress/amd-long-prefix.json --header --full -->
Machine: AMD Ryzen 9 5950X 16-Core Processor, CPU 15, kernel 7.0.0-38-generic.
Group gcc15: A = base-gcc15 (ef99f4248f1 GCC 15.2, profile docker), B = product-guard-gcc15 (ca89fb5fb96 GCC 15.2, profile docker).
Group clang21: A = base-clang21 (ef99f4248f1 clang 21.1, profile docker), B = product-guard-clang21 (ca89fb5fb96 clang 21.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 | instructions |
|---|--:|--:|--:|--:|
| first allcommon_long allcommon_long n201 #320 @ case-320 | 34,433,783 | −100% (−100 … −100) | −100% (−100 … −100) | −100% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| first allcommon_long allcommon_long n201 #320 @ case-320 | 34,395,839 | 0% (0 … 0) | 0% (0 … 0) |
<!-- /bench-table -->

## intel-adversarial

<!-- bench-table ../data/stress/intel-adversarial.json --header --full -->
Machine: 13th Gen Intel(R) Core(TM) i7-13700H, CPU 10, kernel 7.0.0-38-generic.
Group gcc13: A = base-gcc13 (ef99f4248f1 GCC 13.3, profile docker), B = product-guard-gcc13 (ca89fb5fb96 GCC 13.3, profile docker).
Group gcc14: A = base-gcc14 (ef99f4248f1 GCC 14.2, profile docker), B = product-guard-gcc14 (ca89fb5fb96 GCC 14.2, profile docker).
Group clang18: A = base-clang18 (ef99f4248f1 clang 18.1, profile docker), B = product-guard-clang18 (ca89fb5fb96 clang 18.1, profile docker).
Group clang20: A = base-clang20 (ef99f4248f1 clang 20.1, profile docker), B = product-guard-clang20 (ca89fb5fb96 clang 20.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: CPU governor is 'powersave': frequency scaling adds noise (sudo ./bench tune on).
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
Machine: load average is 5.6: other programs are competing for the CPU.
Machine: CPU 10 is 17% busy with other processes: timings will be noisy (wait for it to finish).
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| first dense_anchor dense n3 #318 @ case-318 | 5,642,203 | +1% (0 … +1) | 0% (−1 … 0) ~ | 0% (−1 … 0) ~ | 0% (−1 … +1) ~ | 0% |
| first allcommon_long allcommon_long n201 #320 @ case-320 | 35,223,264 | −100% (−100 … −100) | −100% (−100 … −100) | −100% (−100 … −100) | −100% (−100 … −100) | −100% |
| first periodic periodic n9 #323 @ case-323 | 1,276,643 | +1% (0 … +1) | 0% (0 … +1) ~ | 0% (−1 … +1) | +1% (0 … +1) | −5% … 0% |
| late dense pair @ pair-killer | 14,459,568 | −99% (−99 … −99) | −99% (−100 … −99) | −99% (−99 … −99) | −99% (−99 … −99) | −99% |
| late dense pair @ changing-density | 14,419,906 | −99% (−99 … −99) | −99% (−99 … −99) | −99% (−99 … −99) | −99% (−99 … −99) | −99% |
| late dense pair @ changing-density-match | 14,451,483 | −99% (−99 … −99) | −99% (−99 … −99) | −99% (−100 … −99) | −99% (−99 … −99) | −99% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| first dense_anchor dense n3 #318 @ case-318 | 5,676,148 | 0% (0 … +1) | 0% (−1 … 0) |
| first allcommon_long allcommon_long n201 #320 @ case-320 | 35,712,287 | 0% (0 … +1) | 0% (0 … +3) |
| first periodic periodic n9 #323 @ case-323 | 1,275,031 | 0% (0 … +1) | 0% (0 … 0) |
| late dense pair @ pair-killer | 14,437,064 | 0% (−1 … +1) | 0% (0 … 0) |
| late dense pair @ changing-density | 14,420,279 | 0% (0 … 0) | 0% (0 … 0) |
| late dense pair @ changing-density-match | 14,439,849 | 0% (0 … 0) | 0% (0 … 0) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->

## intel-long-prefix

<!-- bench-table ../data/stress/intel-long-prefix.json --header --full -->
Machine: 13th Gen Intel(R) Core(TM) i7-13700H, CPU 10, kernel 7.0.0-38-generic.
Group gcc13: A = base-gcc13 (ef99f4248f1 GCC 13.3, profile docker), B = product-guard-gcc13 (ca89fb5fb96 GCC 13.3, profile docker).
Group gcc14: A = base-gcc14 (ef99f4248f1 GCC 14.2, profile docker), B = product-guard-gcc14 (ca89fb5fb96 GCC 14.2, profile docker).
Group clang18: A = base-clang18 (ef99f4248f1 clang 18.1, profile docker), B = product-guard-clang18 (ca89fb5fb96 clang 18.1, profile docker).
Group clang20: A = base-clang20 (ef99f4248f1 clang 20.1, profile docker), B = product-guard-clang20 (ca89fb5fb96 clang 20.1, profile docker).
5 alternating passes per case, user-space cycles per call (perf stat, minus the empty loop), A against A at the start and the end.
Machine: CPU governor is 'powersave': frequency scaling adds noise (sudo ./bench tune on).
Machine: turbo boost is on: thermal and frequency drift between rounds (sudo ./bench tune on).
Machine: load average is 3.6: other programs are competing for the CPU.
Machine: CPU 10 is 27% busy with other processes: timings will be noisy (wait for it to finish).
negative = fewer cycles (faster)

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| first allcommon_long allcommon_long n201 #320 @ case-320 | 35,138,328 | −100% (−100 … −100) | −100% (−100 … −100) | −100% (−100 … −100) | −100% (−100 … −100) | −100% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 13.3) | A/A start | A/A end |
|---|--:|--:|--:|
| first allcommon_long allcommon_long n201 #320 @ case-320 | 35,223,481 | 0% (0 … 0) | 0% (0 … 0) |
<!-- /bench-table -->
