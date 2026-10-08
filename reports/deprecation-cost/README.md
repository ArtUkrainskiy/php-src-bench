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

## The patch: build the suffix once

Branch `deprecated-suffix-cache`: the suffix a persistent `#[\Deprecated]` or `#[\NoDiscard]`
attribute produces (" since 8.5, as it has no effect since PHP 8.1") is built on the first use
and kept in the attribute, as an immutable persistent string; later calls take it from there
instead of constructing the attribute object again. A call to
`ReflectionProperty::setAccessible()` goes from 5,010 to 1,807 instructions, reported or
filtered alike; the message is byte for byte the same.

Why the cache lives in the attribute and not in the function: closures and reflection copy
`zend_internal_function` with `memcpy` and never free the copy, so a cache field there would
be filled in copies and leak. The attribute is one per declaration, shared by every copy of
the function and by every thread, and freed exactly once with the attribute.

What it does per environment:

- **php-fpm, php-cgi, CLI (NTS).** The function tables and their attributes are built in the
  master process; FPM workers inherit them copy-on-write. Each process fills the cache lazily
  on the first call of each deprecated function (one `malloc`'d string, the attribute's page
  copied on write) and frees it at shutdown. Nothing goes through shared memory and nothing
  needs to: at most 196 strings of a few dozen bytes per process.
- **ZTS (Apache worker/event with mod_php, FrankenPHP, parallel).** The attribute structs are
  shared by all threads. The first call in any thread builds the string and publishes it with
  a compare-and-swap; two threads racing both build it and the loser frees its copy. Readers do
  an acquire load of the pointer; the string is immutable (interned flag, so no refcount
  traffic; hash computed before publishing), so there is nothing to race on. Freed once at
  process shutdown.
- **opcache.** Not involved for internal functions, which are not in shared memory. Userland
  `#[\Deprecated]` and `#[\NoDiscard]` are not cached: their attribute structs live in
  opcache's shared memory, common to all workers, where a process-heap pointer cannot go, and
  their arguments may be constant expressions. Those calls keep the old path (~5,000); a cache
  for them needs a per-process table keyed by the attribute and is a separate change.
- **`dl()` in the CLI.** The extension's attributes are persistent too; same behaviour.

What does not depend on the environment: the saving applies regardless of `error_reporting`,
of an error handler and of logging, since all of it happened before any of those were
consulted. The one case that could behave differently doesn't: an extension registering a
`#[\Deprecated]` with invalid arguments made the constructor throw on every call before, and
still does, because a failed build is not cached.
