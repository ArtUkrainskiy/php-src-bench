<?php
// Differential run of every php_mblen() user over random byte strings in a given locale.
// Prints one line per case; diff the output between builds.
error_reporting(E_ALL & ~E_DEPRECATED);
$locale = $argv[1];
$n = (int)($argv[2] ?? 2000);
if (setlocale(LC_CTYPE, $locale) === false) { echo "no locale $locale\n"; exit(1); }
mt_srand(12345);
$lead = ['SJIS' => [0x81, 0x9F, 0xE0, 0xFC], 'GBK' => [0x81, 0xB0, 0xFE], 'EUC' => [0xA1, 0xB0, 0xFE, 0x8E], 'BIG5' => [0xA4, 0xC9, 0xF9], 'UTF' => [0xC3, 0xE3, 0xF0]];
$leads = $lead[str_contains($locale, 'SJIS') ? 'SJIS' : (str_contains($locale, 'GBK') ? 'GBK' : (str_contains($locale, 'EUC') ? 'EUC' : (str_contains($locale, 'BIG5') ? 'BIG5' : 'UTF')))];
$specials = [',', '"', '\\', '|', "'", ';', ' ', "\t", "\n", "\r", '/', '&', '`', '$', '~', '@', 'a', 'Z', '0', "\0"];
$gen = function () use ($leads, $specials) {
    $s = '';
    $len = mt_rand(0, 12);
    for ($i = 0; $i < $len; $i++) {
        switch (mt_rand(0, 5)) {
            case 0: case 1: $s .= $specials[mt_rand(0, count($specials) - 1)]; break;
            case 2: $s .= chr($leads[mt_rand(0, count($leads) - 1)]) . $specials[mt_rand(0, count($specials) - 1)]; break; // lead + ASCII trail
            case 3: $s .= chr($leads[mt_rand(0, count($leads) - 1)]) . chr(mt_rand(0x80, 0xFE)); break; // lead + high trail
            case 4: $s .= chr($leads[mt_rand(0, count($leads) - 1)]); break; // lone lead
            case 5: $s .= chr(mt_rand(0x80, 0xFF)); break; // random high byte
        }
    }
    return $s;
};
$h = fn($v) => is_array($v) ? json_encode(array_map(fn($x) => $x === null ? null : bin2hex($x), $v)) : (is_string($v) ? bin2hex($v) : var_export($v, true));
$prev = '';
for ($i = 0; $i < $n; $i++) {
    $s = $gen();
    $out = [];
    $out[] = $h(str_getcsv($s, ',', '"', '\\'));
    $out[] = $h(str_getcsv($s, '|', '"', ''));
    $out[] = $h(str_getcsv($s, ';', "'", ''));
    $f = fopen('php://memory', 'w+'); fwrite($f, $s . "\n" . $prev . "\n"); rewind($f);
    $rows = []; while (($r = fgetcsv($f, null, ',', '"', '\\')) !== false) $rows[] = $h($r); $out[] = implode('/', $rows);
    $sh = str_replace("\0", '', $s);
    $out[] = $h(escapeshellarg($sh));
    $out[] = $h(escapeshellcmd($sh));
    $out[] = $h(basename($sh));
    $out[] = $h(basename($sh, 'a'));
    $out[] = $h(pathinfo($sh, PATHINFO_FILENAME));
    echo bin2hex($s), ' ', implode(' ', $out), "\n";
    $prev = $s;
}
