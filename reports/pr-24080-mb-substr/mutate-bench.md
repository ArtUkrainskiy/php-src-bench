Mutations of mut-fix-gcc13 (mutations.php)

| mutation | difftest | tests |
|---|---|---|
| mobile variants take the fast path | caught (88 of 2000 inputs differ) | missed |
| invalid strings take the fast path | caught (222 of 2000 inputs differ) | caught (2 failed) |
| chunk loop runs down to offset 0 | caught (1257 of 2000 inputs differ) | missed |
| chunk step one byte short | caught (794 of 2000 inputs differ) | missed |
| only ASCII bytes counted as characters | caught (1775 of 2000 inputs differ) | caught (5 failed) |
| offset past the end returns the end | caught (951 of 2000 inputs differ) | caught (1 failed) |
| strpos uses the fast path for unchecked strings | missed | missed |
| result length one character short | caught (1756 of 2000 inputs differ) | caught (5 failed) |

Caught by at least one check: 7 of 8 mutations that build.
