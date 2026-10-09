<?php
// RFC 4180 conformance matrix: built-ins (escape "") vs ext/csv, same inputs.
$enc = function ($v) { return json_encode($v, JSON_INVALID_UTF8_SUBSTITUTE | JSON_UNESCAPED_SLASHES); };
$legacy = function ($s) use ($enc) {
    $rows = [];
    $h = fopen('php://memory', 'w+'); fwrite($h, $s); rewind($h);
    while (($r = fgetcsv($h, null, ',', '"', '')) !== false) $rows[] = $r;
    return $enc($rows);
};
$csv = function ($s) use ($enc) {
    if (!function_exists('Csv\buffer_to_collection')) return '-';
    try { return $enc(Csv\buffer_to_collection($s)); } catch (Throwable $t) { return get_class($t) . ': ' . $t->getMessage(); }
};
$cases = [
    'R1 CRLF records'            => "a,b\r\nc,d\r\n",
    'R2 no trailing CRLF'        => "a,b\r\nc,d",
    'LF only (common, not RFC)'  => "a,b\nc,d\n",
    'R4 spaces are data'         => "a , b\r\n",
    'R4 trailing comma = empty'  => "a,b,\r\n",
    'R5 quoted field'            => "\"a\",b\r\n",
    'R5 DQUOTE in unquoted'      => "a\"b,c\r\n",
    'R6 CRLF inside quotes'      => "\"a\r\nb\",c\r\n",
    'R6 comma inside quotes'     => "\"a,b\",c\r\n",
    'R7 doubled quote'           => "\"a\"\"b\",c\r\n",
    'junk after closing quote'   => "\"a\"b,c\r\n",
    'space before opening quote' => " \"a\",b\r\n",
    'space after closing quote'  => "\"a\" ,b\r\n",
    'unterminated quote'         => "\"a,b\r\nc,d\r\n",
    'empty line between'         => "a,b\r\n\r\nc,d\r\n",
    'empty field quoted'         => "\"\",b\r\n",
    'non-ASCII (not TEXTDATA)'   => "é,ü\r\n",
    'backslash (no escape)'      => "a\\\"b,c\r\n",
    'BOM then quote'             => "\xEF\xBB\xBF\"a\",b\r\n",
];
printf("%-28s | %-40s | %s\n", 'case', 'fgetcsv escape=""', 'ext/csv');
foreach ($cases as $n => $s) printf("%-28s | %-40s | %s\n", $n, $legacy($s), $csv($s));

echo "\n-- writer --\n";
$w = function ($f) use ($enc) { $h = fopen('php://memory', 'w+'); fputcsv($h, $f, ',', '"', ''); rewind($h); return $enc(stream_get_contents($h)); };
$wc = function ($f) use ($enc) { return function_exists('Csv\array_to_row') ? $enc(Csv\array_to_row($f)) : '-'; };
foreach ([['a','b'], ['a b','c'], ['a,b','c'], ['a"b','c'], ["a\nb",'c'], ['', 'c'], [' a ', 'c']] as $f)
    printf("%-28s | %-40s | %s\n", $enc($f), $w($f), $wc($f));
