Mutations of mut-fix-gcc13 (mutations.php)

| mutation | difftest | tests |
|---|---|---|
| mobile variants take the fast path | caught (100 of 2000 inputs differ) | missed |
| invalid strings take the fast path | caught (209 of 2000 inputs differ) | caught (2 failed) |
| chunk loop runs down to offset 0 | caught (1246 of 2000 inputs differ) | missed |
| chunk step one byte short | caught (1083 of 2000 inputs differ) | missed |
| only ASCII bytes counted as characters | caught (1791 of 2000 inputs differ) | caught (5 failed) |
| offset past the end returns the end | caught (653 of 2000 inputs differ) | caught (1 failed) |
| strpos uses the fast path for unchecked strings | missed | missed |
| result length one character short | caught (1789 of 2000 inputs differ) | caught (5 failed) |

Caught by at least one check: 7 of 8 mutations that build.
