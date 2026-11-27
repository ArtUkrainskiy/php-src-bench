<?php
// grapheme_strlen(), grapheme_substr(), grapheme_strpos() and grapheme_extract() on the inputs that
// decide the result of grapheme_ascii_check(): ASCII of 1 byte to 4 KB (one byte per grapheme, the
// fast path), ASCII with CR LF or lone CR, ASCII with one non-ASCII character at the start or end,
// and text in several languages (non-ASCII within the first few bytes: the ICU path). ASCII, ASCII with
// "é" at the end and Chinese also come in 16 B to 4 KB, to show how the change depends on the length.
// "English, ’ every 170 B" is English text with a rare non-ASCII character: one ’ (3 bytes) per 170 B,
// the first at byte 121.
// A second group of calls checks the needle too (grapheme_strstr(), grapheme_stripos(),
// grapheme_strrpos(), a one-byte needle) on short and long ASCII.
// "ASCII, mixed lengths" is 1024 ASCII strings of 1-24 bytes in a fixed random order (seed 1):
// each call takes the next one, so the loop exits of the check differ from call to call. These rows
// include the array lookup, the same on both sides. "ASCII 1 KB, "é" at a random position" is 1024
// strings of 1 KB with one "é" inserted at a random byte (seed 2), taken the same way.

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
foreach ([1, 2, 3, 4, 5, 8, 9, 10, 16, 64, 256] as $n) {
    $inputs["ASCII $n B"] = $fit($en, $n);
}
$typo = $en . 'Nobody minded the noise, since the garden’s gate stayed open until the evening. And so a';
$zh = '我能吞下玻璃而不伤身体，天气很好，我们去公园散步吧。';
$inputs += [
    'ASCII 1 KB' => $fit($en, 1024),
    'ASCII 4 KB' => $fit($en, 4096),
    'ASCII 1 KB, CR LF every 80 B' => $fit(substr($en, 0, 78) . "\r\n", 1024),
    'ASCII 1 KB, lone CR every 80 B' => $fit(substr($en, 0, 79) . "\r", 1024),
    'ASCII 1 KB, "é" first' => "\u{00E9}" . $fit($en, 1022),
    'ASCII 16 B, "é" last' => $fit($en, 14) . "\u{00E9}",
    'ASCII 64 B, "é" last' => $fit($en, 62) . "\u{00E9}",
    'ASCII 256 B, "é" last' => $fit($en, 254) . "\u{00E9}",
    'ASCII 1 KB, "é" last' => $fit($en, 1022) . "\u{00E9}",
    'ASCII 4 KB, "é" last' => $fit($en, 4094) . "\u{00E9}",
    'Chinese 16 B' => $fit($zh, 16),
    'Chinese 64 B' => $fit($zh, 64),
    'Chinese 256 B' => $fit($zh, 256),
    'Chinese 1 KB' => $fit($zh, 1024),
    'Chinese 4 KB' => $fit($zh, 4096),
    'Spanish 256 B' => $fit('El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío. ', 256),
    'Russian 256 B' => $fit('Съешь же ещё этих мягких французских булок, да выпей чаю. ', 256),
    'Japanese 256 B' => $fit('いろはにほへと ちりぬるを わかよたれそ つねならむ ', 256),
    'Korean 256 B' => $fit('다람쥐 헌 쳇바퀴에 타고파, 오늘 날씨가 좋네요. ', 256),
    'English 256 B, ’ every 170 B' => $fit($typo, 256),
    'English 1 KB, ’ every 170 B' => $fit($typo, 1024),
    'English 4 KB, ’ every 170 B' => $fit($typo, 4096),
    'emoji and text 256 B' => $fit('Hello 👋 world 🌍 family 👨‍👩‍👧 ok ', 256),
];
mt_srand(1);
$mixed = [];
for ($k = 0; $k < 1024; $k++) {
    $mixed[] = substr($en, mt_rand(0, 56), mt_rand(1, 24));
}
$inputs['ASCII, mixed lengths 1-24 B'] = $mixed;
mt_srand(2);
$rare = [];
for ($k = 0; $k < 1024; $k++) {
    $rare[] = substr_replace($fit($en, 1022), "\u{00E9}", mt_rand(0, 1022), 0);
}
$inputs['ASCII 1 KB, "é" at a random position'] = $rare;

$single = array_keys(array_filter($inputs, 'is_string'));
$needle = ['ASCII 1 B', 'ASCII 5 B', 'ASCII 9 B', 'ASCII 16 B', 'ASCII 64 B', 'ASCII 256 B', 'ASCII 1 KB', 'ASCII 4 KB'];
$mix = ['ASCII, mixed lengths 1-24 B', 'ASCII 1 KB, "é" at a random position'];
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
