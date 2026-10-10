<?php
// Differential fuzz for ext/csv: random rows -> array_to_row/collection_to_buffer -> parse back
// with buffer_to_collection, createFromBuffer, createFromFile (file), row_to_array; prints one
// line per case so two builds can be diffed. Also checks round-trip equality.
$n = (int)($argv[1] ?? 3000); $seed = (int)($argv[2] ?? 7); mt_srand($seed);
$file = sys_get_temp_dir() . "/csvfuzz_$seed.csv";
$dialects = [[',', '"', "\r\n"], [';', "'", "\n"], ['|', '"', "\r\n"], ['--', 'aa', "\r\n"], ['xy', 'xyx', "\n"], [',', '""', "\r\n"], ["\t", '"', "\r\n"]];
$alpha = ['a', 'b', ' ', ',', ';', '|', '"', "'", "\n", "\r", "\r\n", 'x', 'y', 'aa', '--', 'é', "\xC3", "\x00", "\t", '1', '-'];
$gen = function () use ($alpha) { $s = ''; $l = mt_rand(0, 8); for ($i = 0; $i < $l; $i++) $s .= $alpha[mt_rand(0, count($alpha) - 1)]; return $s; };
$h = fn($v) => bin2hex(json_encode($v, JSON_INVALID_UTF8_SUBSTITUTE | JSON_PARTIAL_OUTPUT_ON_ERROR));
$fail = 0;
for ($i = 0; $i < $n; $i++) {
    [$d, $e, $eol] = $dialects[mt_rand(0, count($dialects) - 1)];
    $nf = mt_rand(1, 4); $nr = mt_rand(1, 4);
    $rows = []; for ($r = 0; $r < $nr; $r++) { $row = []; for ($f = 0; $f < $nf; $f++) $row[] = $gen(); $rows[] = $row; }
    $out = [];
    try {
        $buf = Csv\collection_to_buffer($rows, $d, $e, $eol);
        $out[] = 'buf=' . bin2hex($buf);
        $back = Csv\buffer_to_collection($buf, $d, $e, $eol);
        $out[] = 'rt=' . ($back === $rows ? 'ok' : 'MISMATCH ' . $h($back));
        $lazy = []; foreach (Csv\LazyLaxCollection::createFromBuffer($buf, $d, $e, $eol) as $row) $lazy[] = $row;
        $out[] = 'lazy=' . ($lazy === $rows ? 'ok' : 'MISMATCH ' . $h($lazy));
        file_put_contents($file, $buf);
        $ff = []; foreach (Csv\LazyLaxCollection::createFromFile($file, $d, $e, $eol) as $row) $ff[] = $row;
        $out[] = 'file=' . ($ff === $rows ? 'ok' : 'MISMATCH ' . $h($ff));
        $line = Csv\array_to_row($rows[0], $d, $e, $eol);
        $one = Csv\row_to_array($line, $d, $e, $eol);
        $out[] = 'row=' . ($one === $rows[0] ? 'ok' : 'MISMATCH ' . $h($one));
    } catch (Throwable $t) { $out[] = get_class($t) . ':' . $t->getMessage(); }
    $line = implode(' ', $out);
    if (str_contains($line, 'MISMATCH')) $fail++;
    echo $i, ' ', bin2hex($d), '/', bin2hex($e), ' ', $line, "\n";
}
fwrite(STDERR, "mismatches: $fail\n");
