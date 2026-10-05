# Real documents

Inputs for `suites/realdata.php` and the `html-page`, `html-wiki`, `md` and `js` inputs of
`suites/htmlspecialchars.php`: text as it occurs in the wild, with the densities of `&`, `<` and
quotes that generated text does not have. The files are downloaded, not committed, because each
comes with its own license:

```sh
corpus/real/fetch.sh
```

| File | Source | Pinned |
|---|---|---|
| `js-confutils.txt` | php-src `win32/build/confutils.js` | commit `100e8f353ea` |
| `md-release-process.txt` | php-src `docs/release-process.md` | commit `100e8f353ea` |
| `md-bootstrap.txt` | Bootstrap `README.md` | commit `cc867751d72` |
| `js-jquery.txt`, `js-jquery.min.txt` | jQuery 3.7.1 from code.jquery.com | release |
| `html-phpnet.txt` | php.net manual page of `html_entity_decode()` | no, live page |
| `html-wikipedia.txt` | English Wikipedia article "HTML" | no, live page |

Pinned files are verified by checksum, so everybody measures the same bytes. The two HTML pages
change whenever their sites do. That does not matter for an A/B run, where both builds get the
same file, but numbers on these two inputs are not exactly comparable between machines or with
published reports.

A suite that needs a missing file skips those inputs and says so.
