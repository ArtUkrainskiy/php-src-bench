<?php
// grapheme_strlen(), grapheme_substr(), grapheme_strpos() and grapheme_extract() on the inputs that
// decide the result of grapheme_ascii_check(): ASCII of 1 byte to 2 KB (one byte per grapheme, the
// fast path), ASCII with CR LF or lone CR, ASCII with one non-ASCII character at the start or end,
// and text in several languages (non-ASCII within the first few bytes: the ICU path).
// A second group of calls checks the needle too (grapheme_strstr(), grapheme_stripos(),
// grapheme_strrpos(), a one-byte needle) on short and long ASCII.
// "ASCII, mixed lengths" is 1024 ASCII strings of 1-24 bytes in a fixed random order (seed 1):
// each call takes the next one, so the loop exits of the check differ from call to call. These rows
// include the array lookup, the same on both sides.

$fit = static function (string $text, int $bytes): string {
    $s = str_repeat($text, intdiv($bytes, strlen($text)) + 1);
    $s = substr($s, 0, $bytes);
    while (!preg_match('//u', $s)) {
        $s = substr($s, 0, -1);
    }
    return $s;
};
$en = 'The quick brown fox jumps over the lazy dog while the cat sleeps on a warm mat. ';

$inputs = [];
foreach ([1, 2, 3, 4, 5, 8, 9, 10, 16, 80] as $n) {
    $inputs["ASCII $n B"] = $fit($en, $n);
}
$inputs += [
    'ASCII 2 KB' => $fit($en, 2048),
    'ASCII 2 KB, CR LF every 80 B' => $fit(substr($en, 0, 78) . "\r\n", 2048),
    'ASCII 2 KB, lone CR every 80 B' => $fit(substr($en, 0, 79) . "\r", 2048),
    'ASCII 2 KB, "é" first' => "\u{00E9}" . $fit($en, 2046),
    'ASCII 2 KB, "é" last' => $fit($en, 2046) . "\u{00E9}",
    'Spanish 80 B' => $fit('El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío. ', 80),
    'Russian 80 B' => $fit('Съешь же ещё этих мягких французских булок, да выпей чаю. ', 80),
    'Chinese 80 B' => $fit('我能吞下玻璃而不伤身体，天气很好，我们去公园散步吧。', 80),
    'Japanese 80 B' => $fit('いろはにほへと ちりぬるを わかよたれそ つねならむ ', 80),
    'Korean 80 B' => $fit('다람쥐 헌 쳇바퀴에 타고파, 오늘 날씨가 좋네요. ', 80),
    'emoji and text 80 B' => $fit('Hello 👋 world 🌍 family 👨‍👩‍👧 ok ', 80),
];
mt_srand(1);
$mixed = [];
for ($k = 0; $k < 1024; $k++) {
    $mixed[] = substr($en, mt_rand(0, 56), mt_rand(1, 24));
}
$inputs['ASCII, mixed lengths 1-24 B'] = $mixed;

$single = array_keys(array_filter($inputs, 'is_string'));
$needle = ['ASCII 1 B', 'ASCII 5 B', 'ASCII 9 B', 'ASCII 16 B', 'ASCII 80 B', 'ASCII 2 KB'];
$mix = ['ASCII, mixed lengths 1-24 B'];
$next = '$s[($__i ?? 0) & 1023]';
return [
    'inputs' => $inputs,
    'cases' => [
        'grapheme_strlen($s)' => ['code' => 'grapheme_strlen($s)', 'inputs' => $single],
        'grapheme_substr($s, 0, 8)' => ['code' => 'grapheme_substr($s, 0, 8)', 'inputs' => $single],
        "grapheme_strpos(\$s, 'zz')" => ['code' => "grapheme_strpos(\$s, 'zz')", 'inputs' => $single],
        'grapheme_extract($s, 8)' => ['code' => 'grapheme_extract($s, 8)', 'inputs' => $single],
        "grapheme_strpos(\$s, 'x')" => ['code' => "grapheme_strpos(\$s, 'x')", 'inputs' => $needle],
        "grapheme_strstr(\$s, 'o')" => ['code' => "grapheme_strstr(\$s, 'o')", 'inputs' => $needle],
        "grapheme_stripos(\$s, 'Z')" => ['code' => "grapheme_stripos(\$s, 'Z')", 'inputs' => $needle],
        "grapheme_strrpos(\$s, 'e')" => ['code' => "grapheme_strrpos(\$s, 'e')", 'inputs' => $needle],
        'grapheme_strlen(next string)' => ['code' => "grapheme_strlen($next)", 'inputs' => $mix],
        'grapheme_substr(next string, 0, 8)' => ['code' => "grapheme_substr($next, 0, 8)", 'inputs' => $mix],
        "grapheme_strpos(next string, 'zz')" => ['code' => "grapheme_strpos($next, 'zz')", 'inputs' => $mix],
    ],
];
