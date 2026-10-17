Mutations of pr24188-head-gcc13 (mutations.php)

| mutation | difftest | tests |
|---|---|---|
| round starts from a fresh state instead of the copy | caught (1000 of 1000 inputs differ) | caught (2 failed) |
| inner state absorbs the opad block | caught (1000 of 1000 inputs differ) | caught (2 failed) |
| outer state absorbs no key block | caught (1000 of 1000 inputs differ) | caught (2 failed) |
| first block: inner round with the outer state | caught (1000 of 1000 inputs differ) | caught (2 failed) |
| iterations: inner round with the outer state | caught (1000 of 1000 inputs differ) | caught (1 failed) |
| iterations: outer round left out | caught (1000 of 1000 inputs differ) | caught (1 failed) |

Caught by at least one check: 6 of 6 mutations that build.
