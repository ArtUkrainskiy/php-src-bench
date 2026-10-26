<?php
// Realistic backend JSON, not synthetic single strings: a product catalogue and a
// multilingual comment feed. Keys and structural/id fields are ASCII (as in real APIs);
// localized fields (name, description, category, comment text) pull short snippets from
// the corpus, with the language rotating across records so no single script dominates.
// Cases cover json_encode (default escaping and UNESCAPED_UNICODE) and json_decode of
// both the escaped and the raw document.

mt_srand(1);
$LANGS = ['en', 'es', 'ru', 'ar', 'hi', 'zh', 'ja', 'ko'];

// Truncate valid UTF-8 to $n characters without mbstring (slim builds disable it).
$utf8cut = static function (string $s, int $n): string {
    $len = strlen($s);
    $i = 0;
    $c = 0;
    while ($i < $len && $c < $n) {
        $b = ord($s[$i]);
        $i += $b < 0x80 ? 1 : ($b < 0xe0 ? 2 : ($b < 0xf0 ? 3 : 4));
        $c++;
    }
    return substr($s, 0, $i);
};

$snippet = static function (string $lang, int $chars) use (&$linectr, $utf8cut): string {
    $line = trim(Corpus::line($lang, $linectr[$lang] = ($linectr[$lang] ?? 7) + 13));
    $line = rtrim($utf8cut($line, $chars));
    return $line === '' ? 'n/a' : $line;
};

$catalogue = static function () use ($LANGS, $snippet): array {
    mt_srand(1);
    $linectr = [];
    $items = [];
    for ($i = 0; $i < 300; $i++) {
        $lang = $LANGS[$i % count($LANGS)];
        $items[] = [
            'sku'         => sprintf('SKU-%06d', $i),
            'name'        => $snippet($lang, 24),
            'brand'       => sprintf('Brand%02d', $i % 40),
            'price'       => round(mt_rand(199, 499900) / 100, 2),
            'currency'    => 'USD',
            'rating'      => round(mt_rand(10, 50) / 10, 1),
            'reviews'     => mt_rand(0, 5000),
            'in_stock'    => (bool) (mt_rand(0, 1)),
            'category'    => $snippet($lang, 14),
            'description' => $snippet($lang, 110),
            'tags'        => ['new', 'sale', sprintf('cat%02d', $i % 20)],
        ];
    }
    return ['page' => 1, 'per_page' => 300, 'total' => 12000, 'items' => $items];
};

$comments = static function () use ($LANGS, $snippet): array {
    mt_srand(2);
    $linectr = [];
    $feed = [];
    for ($i = 0; $i < 400; $i++) {
        $lang = $LANGS[($i + 3) % count($LANGS)];
        $feed[] = [
            'id'         => 100000 + $i,
            'user'       => sprintf('user_%05d', mt_rand(0, 99999)),
            'lang'       => $lang,
            'created_at' => sprintf('2026-%02d-%02dT%02d:%02d:%02dZ', 1 + $i % 12, 1 + $i % 28, $i % 24, $i % 60, $i % 60),
            'likes'      => mt_rand(0, 2000),
            'text'       => $snippet($lang, 140),
        ];
    }
    return ['article_id' => 24666, 'count' => 400, 'comments' => $feed];
};

$encDefault = static fn (Closure $v): Closure => static fn (): string => json_encode($v(), JSON_THROW_ON_ERROR);
$encUU       = static fn (Closure $v): Closure => static fn (): string => json_encode($v(), JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);

return [
    'inputs' => [
        'catalogue-value'  => $catalogue,
        'catalogue-esc'    => $encDefault($catalogue),
        'catalogue-raw'    => $encUU($catalogue),
        'comments-value'   => $comments,
        'comments-esc'     => $encDefault($comments),
        'comments-raw'     => $encUU($comments),
    ],
    'cases' => [
        'json_encode'                    => ['code' => 'json_encode($s)',                          'inputs' => ['catalogue-value', 'comments-value']],
        'json_encode UNESCAPED_UNICODE'  => ['code' => 'json_encode($s, JSON_UNESCAPED_UNICODE)',  'inputs' => ['catalogue-value', 'comments-value']],
        'json_decode escaped'            => ['code' => 'json_decode($s, true)',                    'inputs' => ['catalogue-esc', 'comments-esc']],
        'json_decode raw'                => ['code' => 'json_decode($s, true)',                    'inputs' => ['catalogue-raw', 'comments-raw']],
    ],
];
