<?php
$inputs = ['"a"b', '"a"b"', '"a" ,b', '"abc', '"', 'a,"', '""""', '""', 'a,b,', "a,b\r\n", "a,b\r\nc,d", '', "\r\n", "a\nb,c", "\xEF\xBB\xBF\"a\",b", "a\\\"b,c", 'a\\,b', " a ,b ", '"a",,"b"', "a,\"b\"\"c\",d", "a\r\nb", "\"a\"\"\"", "a,b\n", "a,b\r", "\"x\",\"y\"\r\n\"z\""];
foreach ($inputs as $in) {
    $legacy = str_getcsv($in, ',', '"', '');
    try { $new = Csv\row_to_array($in); } catch (Throwable $e) { $new = get_class($e) . ': ' . $e->getMessage(); }
    $same = $legacy === $new;
    echo ($same ? "same   " : "DIFF   "), json_encode($in), "\n";
    if (!$same) echo "        legacy=", json_encode($legacy), "\n        new=", json_encode($new), "\n";
}
echo "--- writer\n";
$rows = [['a', 'b'], ['a b', 'c'], ['a"b'], ['a,b'], ["a\nb"], ["a\rb"], [''], [' a '], ["a\tb"], ['"'], ['a\\b'], ['a\\"b'], [null, true, false, 1.5]];
foreach ($rows as $r) {
    $fh = fopen('php://memory', 'w+'); fputcsv($fh, $r, ',', '"', '', "\r\n"); rewind($fh); $legacy = stream_get_contents($fh);
    $new = Csv\array_to_row($r);
    echo ($legacy === $new ? "same   " : "DIFF   "), json_encode($r), ($legacy === $new ? "" : "\n        legacy=" . json_encode($legacy) . "\n        new=" . json_encode($new)), "\n";
}
echo "--- fgetcsv on blank line and file\n";
$fh = fopen('php://memory', 'w+'); fwrite($fh, "a,b\r\n\r\nc,d\r\n"); rewind($fh); $l = []; while (($x = fgetcsv($fh, null, ',', '"', '')) !== false) $l[] = $x;
echo "legacy=", json_encode($l), "\n";
echo "lax=", json_encode(Csv\buffer_to_collection_lax("a,b\r\n\r\nc,d\r\n")), "\n";
