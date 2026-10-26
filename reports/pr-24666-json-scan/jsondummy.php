<?php
// Real backend JSON shapes from dummyjson.com (corpus/dummyjson/*.json), at several
// complexity levels, measured for json_encode/decode. Keys, ids, numbers and structure
// are kept exactly as the real API returns them. For the localized variants the free-text
// fields (title, body, description, quote, ...) are refilled from the corpus in a target
// language of similar length, so the structure is real but the text is non-ASCII — the
// "same API served in language X" case. English variants are left untouched.
//
// Complexity levels:
//   quotes   — flat, one short text field per record
//   posts    — text-heavy (title + body), shallow
//   comments — short text + a small nested user{}
//   products — many small fields, arrays (tags, reviews[]) and a nested dimensions{}/meta{}
//   users    — deep nesting (address{coordinates{}}, company{address{}}, bank{}, crypto{})

$DIR = dirname(__DIR__) . '/corpus/dummyjson';

$utf8cut = static function (string $s, int $n): string {
    $len = strlen($s); $i = 0; $c = 0;
    while ($i < $len && $c < $n) {
        $b = ord($s[$i]);
        $i += $b < 0x80 ? 1 : ($b < 0xe0 ? 2 : ($b < 0xf0 ? 3 : 4));
        $c++;
    }
    return substr($s, 0, $i);
};

// ~$chars characters of corpus text in $lang, concatenating lines. $cur is a per-language
// line cursor shared across all variants for the whole suite build (each input is built once),
// so the text is deterministic.
$cur = [];
$text = static function (string $lang, int $chars) use (&$cur, $utf8cut): string {
    $out = '';
    while (strlen($out) < $chars * 4) { // enough bytes even at 4 bytes/char
        $out .= Corpus::line($lang, $cur[$lang] = ($cur[$lang] ?? 0) + 7) . ' ';
    }
    return rtrim($utf8cut($out, $chars)) ?: 'n/a';
};

$TEXT_KEYS = ['title' => 1, 'body' => 1, 'description' => 1, 'quote' => 1, 'comment' => 1];

// Recursively refill free-text string fields with corpus text in $lang, keeping length ~equal.
$localize = static function ($node, string $lang) use (&$localize, $TEXT_KEYS, $text, $utf8cut) {
    if (!is_array($node)) return $node;
    $out = [];
    foreach ($node as $k => $v) {
        if (is_array($v)) {
            $out[$k] = $localize($v, $lang);
        } elseif (is_string($v) && isset($TEXT_KEYS[$k]) && $v !== '') {
            // count chars of original
            $len = strlen($v); $i = 0; $c = 0;
            while ($i < $len) { $b = ord($v[$i]); $i += $b < 0x80 ? 1 : ($b < 0xe0 ? 2 : ($b < 0xf0 ? 3 : 4)); $c++; }
            $out[$k] = $text($lang, max(3, $c));
        } else {
            $out[$k] = $v;
        }
    }
    return $out;
};

$load = static function (string $file) use ($DIR): array {
    return json_decode(file_get_contents("$DIR/$file"), true, 512, JSON_THROW_ON_ERROR);
};

// value builder: decoded file, optionally localized
$val = static function (string $file, ?string $lang = null) use ($load, $localize): Closure {
    return static function () use ($load, $localize, $file, $lang) {
        $data = $load($file);
        return $lang === null ? $data : $localize($data, $lang);
    };
};
$esc = static fn (Closure $v): Closure => static fn (): string => json_encode($v(), JSON_THROW_ON_ERROR);
$raw = static fn (Closure $v): Closure => static fn (): string => json_encode($v(), JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);

$inputs = [];
$enc = $encUU = $decEsc = $decRaw = [];
$variants = [
    'products-en'   => $val('products.json'),
    'users-en'      => $val('users.json'),
    'posts-en'      => $val('posts.json'),
    'posts-ru'      => $val('posts.json', 'ru'),
    'posts-zh'      => $val('posts.json', 'zh'),
    'posts-ja'      => $val('posts.json', 'ja'),
    'comments-ru'   => $val('comments.json', 'ru'),
    'quotes-ar'     => $val('quotes.json', 'ar'),
];
foreach ($variants as $name => $v) {
    $inputs["$name-v"]   = $v;
    $inputs["$name-esc"] = $esc($v);
    $inputs["$name-raw"] = $raw($v);
    $enc[]    = "$name-v";
    $encUU[]  = "$name-v";
    $decEsc[] = "$name-esc";
    $decRaw[] = "$name-raw";
}

return [
    'inputs' => $inputs,
    'cases' => [
        'json_encode'                   => ['code' => 'json_encode($s)',                         'inputs' => $enc],
        'json_encode UNESCAPED_UNICODE' => ['code' => 'json_encode($s, JSON_UNESCAPED_UNICODE)', 'inputs' => $encUU],
        'json_decode escaped'           => ['code' => 'json_decode($s, true)',                   'inputs' => $decEsc],
        'json_decode raw'               => ['code' => 'json_decode($s, true)',                   'inputs' => $decRaw],
    ],
];
