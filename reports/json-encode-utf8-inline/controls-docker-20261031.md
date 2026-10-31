# Docker-profile A/A controls

Paired median changes and min–max ranges across passes.

## intel, before

| call | master, CPU cycles per call (aa-g13-before) | aa-g13-before | aa-c20-before |
|---|--:|--:|--:|
| ASCII, 4 KiB | 8,161 | 0% (−2 … +2) | +1% (−5 … +3) |
| Cyrillic, 4 KiB | 35,167 | −1% (−4 … +2) | 0% (−2 … +1) |
| Emoji, 4 KiB | 25,477 | 0% (−39 … +3) | −1% (−2 … +2) |
| 1,000 arrays of 10 fields | 888,103 | −1% (−5 … +4) | 0% (−2 … +7) |

## intel, after

| call | master, CPU cycles per call (aa-g13-after) | aa-g13-after | aa-c20-after |
|---|--:|--:|--:|
| ASCII, 4 KiB | 8,203 | −1% (−2 … +1) | 0% (−3 … +6) |
| Cyrillic, 4 KiB | 35,146 | −1% (−2 … +4) | 0% (−1 … +1) |
| Emoji, 4 KiB | 25,014 | +1% (0 … +3) | 0% (−1 … +2) |
| 1,000 arrays of 10 fields | 899,537 | 0% (−1 … +2) | +1% (0 … +4) |

## amd, before

| call | master, CPU cycles per call (aa-g15-before) | aa-g15-before | aa-c21-before |
|---|--:|--:|--:|
| ASCII, 4 KiB | 8,561 | 0% (−7 … +8) | 0% (−2 … +2) |
| Cyrillic, 4 KiB | 42,813 | 0% (−1 … +13) | 0% (−2 … +2) |
| Emoji, 4 KiB | 29,849 | 0% (−1 … +1) | 0% (−2 … +2) |
| 1,000 arrays of 10 fields | 1,083,561 | 0% (−2 … +2) | 0% (−8 … +1) |

## amd, after

| call | master, CPU cycles per call (aa-g15-after) | aa-g15-after | aa-c21-after |
|---|--:|--:|--:|
| ASCII, 4 KiB | 8,574 | 0% (−6 … +16) | 0% (−1 … +3) |
| Cyrillic, 4 KiB | 42,865 | 0% (−7 … +11) | 0% (−1 … +2) |
| Emoji, 4 KiB | 29,856 | 0% (−2 … +1) | 0% (−2 … +1) |
| 1,000 arrays of 10 fields | 1,085,195 | 0% (−3 … +3) | 0% (−1 … +2) |
