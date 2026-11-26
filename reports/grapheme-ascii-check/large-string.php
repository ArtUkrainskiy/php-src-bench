<?php
// large-string.php — every function that calls grapheme_ascii_check() on 2^31 + 8 bytes of ASCII, with
// offsets near the start and the end. Prints each result (a string as its length) and the last intl error:
// the ASCII paths don't reset it, so it can come from an earlier call. grapheme_strpos(), grapheme_stripos(),
// grapheme_strrpos(), grapheme_strripos() and grapheme_substr() use int32_t offsets on their ASCII path, so
// strings this long go to ICU, which can't take them: the result is false, NULL or an error, never a crash.
// grapheme_strlen(), grapheme_strstr() and grapheme_extract() have no such limit on their ASCII path.
// Needs about 9 GB of memory: run with -d memory_limit=-1.
$s = str_repeat('a', 2 ** 31 + 8);
$calls = [
    'grapheme_strlen($s)' => fn() => grapheme_strlen($s),
    "grapheme_strpos(\$s, 'b')" => fn() => grapheme_strpos($s, 'b'),
    "grapheme_stripos(\$s, 'b', -1)" => fn() => grapheme_stripos($s, 'b', -1),
    "grapheme_strrpos(\$s, 'a', -2)" => fn() => grapheme_strrpos($s, 'a', -2),
    "grapheme_strripos(\$s, 'A', 1)" => fn() => grapheme_strripos($s, 'A', 1),
    'grapheme_substr($s, 0, 8)' => fn() => grapheme_substr($s, 0, 8),
    "grapheme_strstr(\$s, 'b')" => fn() => grapheme_strstr($s, 'b'),
    "grapheme_strstr(\$s, 'a', true)" => fn() => grapheme_strstr($s, 'a', true),
    'grapheme_extract($s, 3, GRAPHEME_EXTR_COUNT, 2 ** 31)' => fn() => grapheme_extract($s, 3, GRAPHEME_EXTR_COUNT, 2 ** 31),
    'grapheme_extract($s, 2 ** 31 - 1)' => fn() => grapheme_extract($s, 2 ** 31 - 1),
];
foreach ($calls as $name => $call) {
    try {
        $r = $call();
        $result = (is_string($r) ? 'string of ' . strlen($r) . ' bytes' : var_export($r, true))
            . ' (' . intl_get_error_message() . ')';
    } catch (Throwable $e) {
        $result = $e::class . ': ' . $e->getMessage();
    }
    unset($r);
    echo $name, ' = ', $result, "\n";
}
echo "done\n";
