<?php
// grapheme_strlen(), grapheme_substr(), grapheme_strpos() and grapheme_extract() on the inputs that
// decide the result of grapheme_ascii_check(): ASCII of several lengths (one byte per grapheme, the
// fast path), ASCII with CR LF or lone CR, ASCII with one non-ASCII character at the start or end,
// and text in several languages (non-ASCII within the first few bytes: the ICU path).

$fit = static function (string $text, int $bytes): string {
    $s = str_repeat($text, intdiv($bytes, strlen($text)) + 1);
    $s = substr($s, 0, $bytes);
    while (!preg_match('//u', $s)) {
        $s = substr($s, 0, -1);
    }
    return $s;
};
$en = 'The quick brown fox jumps over the lazy dog while the cat sleeps on a warm mat. ';

$inputs = [
    'ASCII 5 B' => 'Hello',
    'ASCII 10 B' => 'Hello you!',
    'ASCII 80 B' => $fit($en, 80),
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

$all = array_keys($inputs);
return [
    'inputs' => $inputs,
    'cases' => [
        'grapheme_strlen($s)' => ['code' => 'grapheme_strlen($s)', 'inputs' => $all],
        'grapheme_substr($s, 0, 8)' => ['code' => 'grapheme_substr($s, 0, 8)', 'inputs' => $all],
        "grapheme_strpos(\$s, 'zz')" => ['code' => "grapheme_strpos(\$s, 'zz')", 'inputs' => $all],
        'grapheme_extract($s, 8)' => ['code' => 'grapheme_extract($s, 8)', 'inputs' => $all],
    ],
];
