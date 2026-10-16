<?php
// Mutations of the mb_substr() fast path (php-src PR 24080, the version with the UTF-8-only condition).
$calls = [
    'mb_substr($s, 0, 10)', 'mb_substr($s, 255)', 'mb_substr($s, 257, 300)', 'mb_substr($s, 600, 5)', 'mb_substr($s, -1)',
    'mb_substr($s, -300, 20)', 'mb_substr($s, 3, -2)', 'mb_strpos($s, "a", 300)', 'mb_strrpos($s, "a", -5)',
    'mb_substr($s, 1, 1, "UTF-8-Mobile#DOCOMO")', 'mb_strimwidth($s, 2, 30)',
];
$args = ['--setup', 'mb_check_encoding($s, "UTF-8")', '--seed', '5', '--count', '2000'];
foreach ($calls as $call) {
    array_push($args, '--code', $call);
}

return [
    'difftest' => ['generator' => 'code', 'against' => 'mut-base-gcc13', 'args' => $args],
    'tests' => ['ext/mbstring/tests'],
    'mutations' => [
        'mobile variants take the fast path' => ['file' => 'ext/mbstring/mbstring.c',
            'from' => 'if (enc == &mbfl_encoding_utf8 && ZSTR_IS_VALID_UTF8(input)) {',
            'to' => 'if (php_mb_is_no_encoding_utf8(enc->no_encoding) && ZSTR_IS_VALID_UTF8(input)) {'],
        'invalid strings take the fast path' => ['file' => 'ext/mbstring/mbstring.c',
            'from' => 'if (enc == &mbfl_encoding_utf8 && ZSTR_IS_VALID_UTF8(input)) {',
            'to' => 'if (enc == &mbfl_encoding_utf8) {'],
        'chunk loop runs down to offset 0' => ['file' => 'ext/mbstring/mbstring.c',
            'from' => 'while (offset > 256 && (size_t)(end - pos) >= 256) {',
            'to' => 'while (offset > 0 && (size_t)(end - pos) >= 256) {'],
        'chunk step one byte short' => ['file' => 'ext/mbstring/mbstring.c', 'from' => 'pos += 256;', 'to' => 'pos += 255;'],
        'only ASCII bytes counted as characters' => ['file' => 'ext/mbstring/mbstring.c',
            'from' => "if (!IS_UTF8_CONTINUATION_BYTE(*pos)) {\n\t\t\t\t\tif (offset == 0) {",
            'to' => "if (*pos < 0x80) {\n\t\t\t\t\tif (offset == 0) {"],
        'offset past the end returns the end' => ['file' => 'ext/mbstring/mbstring.c',
            'from' => 'return offset == 0 ? end : NULL;', 'to' => 'return end;'],
        'strpos uses the fast path for unchecked strings' => ['file' => 'ext/mbstring/mbstring.c',
            'from' => 'needle_len, ZSTR_IS_VALID_UTF8(haystack_u8));', 'to' => 'needle_len, true);'],
        'result length one character short' => ['file' => 'ext/mbstring/mbstring.c',
            'from' => 'stop = offset_to_pointer_utf8(start, end, len, true);',
            'to' => 'stop = offset_to_pointer_utf8(start, end, len - 1, true);'],
    ],
];
