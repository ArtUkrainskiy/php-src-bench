<?php
// Break-even sweep for PR #24666: per-call cost (cycles and instructions) vs share of non-ASCII characters.
// Each input is 20000 characters; a fraction of them are one non-ASCII char (2- or 3-byte),
// spread evenly, the rest 'a'. Encode inputs are the raw string; decode inputs are that string
// encoded with JSON_UNESCAPED_UNICODE (raw multibyte inside a JSON string).

$N = 20000;
$cyr = "\u{044f}";   // U+044F CYRILLIC SMALL LETTER YA, 2 bytes
$cjk = "\u{4e2d}";   // U+4E2D, 3 bytes
$pcts = [0, 2, 5, 10, 15, 20, 30, 50, 100];

$mkstr = static function (int $pct, string $ch) use ($N): Closure {
    return static function () use ($pct, $ch, $N): string {
        $s = '';
        $acc = 0;
        for ($i = 0; $i < $N; $i++) {
            $acc += $pct;
            if ($acc >= 100) { $s .= $ch; $acc -= 100; }   // Bresenham: exactly pct% of chars
            else { $s .= 'a'; }
        }
        return $s;
    };
};
$mkdoc = static function (int $pct, string $ch) use ($mkstr): Closure {
    return static function () use ($pct, $ch, $mkstr): string {
        return json_encode($mkstr($pct, $ch)(), JSON_UNESCAPED_UNICODE);
    };
};

$inputs = [];
$enc2 = $enc3 = $dec2 = $dec3 = [];
foreach ($pcts as $p) {
    $inputs["s2-$p"] = $mkstr($p, $cyr); $enc2[] = "s2-$p";
    $inputs["s3-$p"] = $mkstr($p, $cjk); $enc3[] = "s3-$p";
    $inputs["d2-$p"] = $mkdoc($p, $cyr); $dec2[] = "d2-$p";
    $inputs["d3-$p"] = $mkdoc($p, $cjk); $dec3[] = "d3-$p";
}

return [
    'inputs' => $inputs,
    'cases' => [
        'encode 2byte'  => ['code' => 'json_encode($s)', 'inputs' => $enc2],
        'encode 3byte'  => ['code' => 'json_encode($s)', 'inputs' => $enc3],
        'decode 2byte'  => ['code' => 'json_decode($s)', 'inputs' => $dec2],
        'decode 3byte'  => ['code' => 'json_decode($s)', 'inputs' => $dec3],
    ],
];
