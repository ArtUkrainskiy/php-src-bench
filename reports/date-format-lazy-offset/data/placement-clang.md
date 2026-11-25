# Code placement, clang 21.1: `format('c')` on a +05:30 offset

`bench why date <master clang build> <change clang build> --filter "format\(.c.\) @ offset" --functions date_format,ap_php_slprintf,ap_php_conv_10,php_conv_fp,_emalloc,timelib_time_offset_ctor --passes 7 --cpu 15`, A = master, B = the change.

| event | A | B | B vs A |
|---|--:|--:|--:|
| cycles | 865 | 974 | +13% |
| instructions | 3,554 | 3,566 | 0% |
| branches | 714 | 716 | 0% |
| branch-misses | 0.00 | 0.00 | +0.00 |
| L1-icache-load-misses | 0.00 | 0.00 | +0.00 |
| iTLB-load-misses | 0.00 | -0.00 | -0.00 |

| function | A address | A size | B address | B size | moved by | alignment A / B |
|---|--:|--:|--:|--:|--:|--:|
| date_format | 0x224a40 | 3090 | 0x224a40 | 2983 | +0 | 0 / 0 |
| ap_php_slprintf | 0x59a620 | 211 | 0x59a6d0 | 211 | +176 | 32 / 16 |
| ap_php_conv_10 | 0x599f60 | 99 | 0x59a010 | 99 | +176 | 32 / 16 |
| php_conv_fp | 0x599fd0 | 1509 | 0x59a080 | 1509 | +176 | 16 / 0 |
| _emalloc | 0x5f3e00 | 218 | 0x5f3eb0 | 218 | +176 | 0 / 48 |
| timelib_time_offset_ctor | 0x252a60 | 15 | 0x252b10 | 15 | +176 | 32 / 16 |

`perf record -e cycles:u`, 3,000,000 × `$d->format("c")` on 2026-11-18T12:34:56.123456+05:30, CPU 15, share of user-space cycles:

| symbol | master | change |
|---|--:|--:|
| strx_printv | 66.72% | 68.81% |
| date_format | 7.16% | 4.27% |
| _emalloc | 5.11% | 3.31% |
| _efree | 3.12% | < 3% |
