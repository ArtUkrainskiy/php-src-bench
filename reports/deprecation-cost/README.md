# What a deprecated call costs

Background — how this came up, with the benchmark CI history that led to it:
[php-benchmark-history](../php-benchmark-history/).

php-src master `26e588f5637`, release build, `perf stat -e instructions:u` on a pinned P-core
(i7-13700H), 100,000 iterations; the figure is the cost above the same loop making a plain call
(`ReflectionProperty::getName()` or `strlen('')`). Callgrind on the same scripts gives the same
totals and the breakdown below.

| | `E_DEPRECATED` reported | filtered by `error_reporting` |
|---|---|---|
| deprecation declared with `#[\Deprecated]` (`ReflectionProperty::setAccessible()`) | 5,016 | 5,010 |
| classic deprecation (null passed to `strlen()`) | 2,152 | 2,146 |
| + a user error handler that returns false | +750 | +750 |
| + a framework-like handler (`sprintf` + store, checks `error_reporting()`) | +2,200 | +850 |
| + `log_errors=1`, `error_log=/dev/null` | +6,500 | — |

`error_reporting` without `E_DEPRECATED` saves nothing: the check is made in `php_error_cb()`,
after the message has been formatted, file and line looked up and `last_error` stored
(`error_get_last()` reports filtered errors too). A user error handler is called by its own mask,
regardless of `error_reporting`.

## Where the 5,000 go (callgrind, per call, difference to the baseline loop)

- ~2,860 — `get_deprecation_suffix_from_attribute()` in `Zend/zend_execute.c`: a `\Deprecated`
  object is constructed on every call — `zend_get_attribute_object()`,
  `object_init_with_constructor()`, `Deprecated::__construct` through `zend_call_function()` with
  named arguments (`zend_handle_named_arg`, `zend_parse_va_args`), two `zend_std_write_property`,
  two `zend_read_property_ex`, `zend_strpprintf()` for the suffix, `zend_objects_store_del()`.
  196 deprecations in 34 stubs on master are declared this way.
- ~1,200 — formatting the message (`xbuf_format_converter`, `zend_vstrpprintf`).
- ~600 — `php_error_cb()`, `get_filename_lineno()`, `clear_last_error()` and the `last_error` copy.
- the rest — `zend_error_zstr_at()`, allocations.

A classic deprecation has no first item, hence ~2,150.

## Reproduction

```
python3 measure.py /path/to/php
valgrind --tool=callgrind --callgrind-out-file=cg.out /path/to/php -n -d display_errors=0 \
  -d log_errors=0 -d html_errors=0 -d 'error_reporting=E_ALL&~E_DEPRECATED' \
  deprecation-cost.php none 20000
callgrind_annotate cg.out | head -60
```

`deprecation-cost.php MODE N`: `baseline` (plain call), `none` (deprecated call, no handler),
`noop` (handler returning false), `framework` (handler that formats and stores the message).
`null-deprecation.php MODE N`: the classic deprecation for comparison.

## The patch: read string arguments without constructing the attribute

php-src PR #24198: when the arguments of a `#[\Deprecated]` (`message`, `since`) or
`#[\NoDiscard]` (`message`) attribute are strings or null, positional or named, each bound
once, the suffix is built straight from them; anything else — a constant expression, another
type, a duplicate or unknown name — goes through the constructor as before and gets its errors
from it, and so does a call made while an exception is pending (opcache preloading relies on
the constructor not running there, so nothing is emitted). The message is byte for byte the
same.

| instructions per call | master | patched |
|---|---|---|
| `ReflectionProperty::setAccessible()` (`#[\Deprecated]`), `E_DEPRECATED` filtered | 5,010 | 2,772 |
| the same, reported | 5,016 | 2,778 |
| the same, logged to `error_log` | 11,467 | 9,231 |
| a deprecated user function, literal arguments | 4,641 | 2,516 |
| the same, a class constant folded at compile time | 4,590 | 2,501 |
| the same, a runtime constant (constructor path) | 4,831 | 4,976 |

The last row is the cost of trying the fast path and falling back: about 145 instructions.
What is left on the fast path is the deprecation machinery itself: formatting the message,
`php_error_cb()`, file and line, `last_error`.

This is the string bypass discussed in the review of the attribute's implementation
(php-src #11293): both authors wanted the object construction avoided for the plain-string
case, and the bypass announced there never reached the merge.

A first version cached the built suffix in the attribute instead (one atomic field in
`zend_attribute`, a persistent string published with a compare-and-swap, freed with the
attribute). It was ~950 instructions cheaper per internal call (1,807) but did not cover
user-code attributes, whose structs live in opcache shared memory, added 8 bytes to every
attribute and an atomic to a public header; the direct read is simpler and covers everything.

What changes for observers (`zend_execute_internal`): `Deprecated::__construct()` and
`NoDiscard::__construct()` are no longer called for literal arguments, so they are no longer
observed; two tests that recorded those frames were updated, and `nodiscard/007.phpt` now
shows both paths. Everything else — the deprecation path after the suffix, the constructor
path for non-literal arguments with its errors — is unchanged: 98 scripts covering every
argument form, declaration kind, context and error configuration give identical output on
master and the patch, with and without opcache and the JITs; the full test suite on a debug
ZTS build with 45 extensions passes.
