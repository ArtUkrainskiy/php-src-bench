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
