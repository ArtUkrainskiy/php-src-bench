# Callers of the forward substring search

Scope: bundled sources on the
[candidate branch](https://github.com/ArtUkrainskiy/php-src/tree/strpos-compact-sunday-pr).
`php_memnstr` aliases `zend_memnstr`. Eligibility requires a 9–31-byte needle
and at least 1024 remaining bytes at the helper call. For converted strings,
these are the lengths after conversion, not the original character counts.
Source eligibility is not a measured speedup or an instrumented branch trace.

## Functions with application fixtures

| Function | Affected operation | Suite |
|---|---|---|
| `strpos` | Forward search from the requested offset | `search`, `search-long` |
| `str_contains` | Forward existence check | `search`, `moderation-*` |
| `strstr` | Forward search before returning a substring | `search` |
| `strchr` | Alias of `strstr`; same PHP handler | `search`, correctness only |
| `substr_count` | Repeated non-overlapping forward searches | `substr-count` |
| `str_replace` | Multi-byte literal searches in count/replacement passes | `replace` |
| `str_ireplace` | Literal searches after ASCII lowercasing | `replace` |
| `strtr` | Array form with exactly one multi-byte key | `replace` |
| `explode` | Repeated delimiter searches | `explode` |
| `stream_get_line` | Delimiter search in the stream's buffered data | `stream-get-line` |

The first nine rows enter through `ext/standard/string.c`.
The `documents-*` suites supplement these API-specific fixtures with complete
HTML templates, MIME messages, JSON logs and independent posts. `controls-*`
contain routing and repeated-prefix diagnostics, including needles outside the
application range; they are excluded from application benefit tables.
`stream_get_line()` enters through `ext/standard/streamsfuncs.c`, then
`php_stream_get_record()` / `_php_stream_search_delim()` in `main/streams/streams.c`.
Its fixture prepares the stream before timing; each operation includes rewind
and one read. The stream buffer's available length determines the search path.
The fixtures read a memory stream, not a file or a network connection.

`strtr()` with multiple array keys and its three-argument character-translation
form use different code. Repeated searches can leave the compact path on a short
remaining suffix. These fixtures measure the whole PHP operation.

## Optional extension suites

| Function | Eligible path | Fixture status |
|---|---|---|
| `mb_strpos` | Forward search after conversion to UTF-8 | Measured and runtime validated |
| `mb_stripos` | Forward search after Unicode case folding and UTF-8 conversion | Measured and runtime validated |
| `mb_strstr` | Forward search before producing the result | Measured and runtime validated |
| `mb_stristr` | Uses the forward case-insensitive search | Measured and runtime validated |
| `mb_substr_count` | Repeated UTF-8 searches | Measured and runtime validated |
| `grapheme_strpos` | ASCII fast path with a nonnegative offset | Measured and runtime validated |
| `grapheme_stripos` | ASCII fast path after lowercasing | Measured and runtime validated |
| `grapheme_strstr` | Case-sensitive ASCII fast path | Measured and runtime validated |

Sources: `ext/mbstring/mbstring.c` and `ext/intl/grapheme/grapheme_string.cpp`.
The mbstring suite uses EN/RU/ZH, with absent and middle matches.
Case-insensitive fixtures use ASCII placeholders; they do not test Unicode
case-folding performance. mbstring offsets are codepoints; JSON match positions
remain UTF-8 bytes. The intl suite uses ASCII only. Non-ASCII grapheme searches
use ICU, and `grapheme_stristr()` does not use this forward ASCII fast path.

Run optional families explicitly with extension-enabled release binaries:

```sh
"$PHP_CANDIDATE" -n reports/compact-sunday/tools/validate.php \
  reports/compact-sunday/corpus mbstring
"$PHP_CANDIDATE" -n reports/compact-sunday/tools/validate.php \
  reports/compact-sunday/corpus intl
```

Repeat validation on master. If extensions are shared, pass the required
`-d extension=...` options. Missing functions fail validation and suite loading;
they are not silently skipped.

## Other conditional mechanisms without fixtures

| Mechanism | Where the helper participates | Coverage limit |
|---|---|---|
| `get_browser()` | Literal “contains” portions of browscap patterns; `ext/standard/browscap.c` | Depends on pattern and user-agent lengths; no configured browscap benchmark |
| Fileinfo: `finfo_buffer`, `finfo_file`, `finfo::buffer`, `finfo::file`, `mime_content_type` | Literal `FILE_SEARCH` magic rules in `ext/fileinfo/libmagic/softmagic.c` when the `HAVE_MEMMEM` branch is built and string flags are zero | Depends on the magic rule and build; no fixture or performance claim |
| Session URL rewriting | `php_session_reset_id()` can call `php_url_scanner_reset_session_var()` when trans_sid applies | Searches URL/form rewrite buffers; no fixture or performance claim |
| Extension C APIs | `zend_memnstr`, `php_str_to_str`, stream record helpers | Third-party extension callers are outside this inventory |

Session URL rewriting is separate from the session payload format. Its call
chain is in `ext/session/session.c` and `ext/standard/url_scanner_ex.re`.
The needle and buffer lengths decide whether the compact path is reached.

## Serialization, short literals and separate algorithms

`serialize()` and `unserialize()` do not use this helper to encode or parse
their payloads. Built-in session serializers delegate to those payload routines.
This change does not optimize session serialization or deserialization.
User callbacks may invoke string APIs independently.

Some internal callers use fixed literals too short for the compact path:

| Caller | Literal searched |
|---|---|
| `define()`, optimizer handling of `define()`, reflection method/property name parsing | `::` — 2 bytes |
| `file_get_contents()` URL check | `://` — 3 bytes |
| Modern DOM CDATA / processing instruction validation | `]]>` / `?>` — 3 / 2 bytes |
| `mb_decode_mimeheader()` | `?=` — 2 bytes |
| `IntlNumberFormatter::createFromSkeleton()` | `scale/` — 6 bytes |
| `var_export()` through `php_str_to_str()` | NUL — 1 byte |
| Windows mail escaping through `php_str_to_str()` | newline followed by dot — 2 bytes |

`explode('::', ...)` and `explode('||', ...)` also stay on the existing short
needle path. They do not belong in the compact-table benefit table.
`stripos()` and `stristr()` use `zend_memnistr`, which is unchanged.
Reverse searches, prefix/suffix checks and PCRE searches use separate algorithms.
