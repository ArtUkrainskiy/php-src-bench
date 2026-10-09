<?php
// Compares ext/csv (PR #24199) with fgetcsv/str_getcsv/fputcsv on the same data.
// Usage: php bench.php <datadir> <case> ; prints ns/row. Instructions via perf stat outside.
[$dir, $case] = [$argv[1], $argv[2]];
$name = explode(':', $case)[1] ?? 'plain';
$file = "$dir/$name.csv"; $buf = file_get_contents($file); $rows = json_decode(file_get_contents("$dir/$name.json"), true);
$n = count($rows); $reps = 5; $best = PHP_FLOAT_MAX; $out = null;
for ($r = 0; $r < $reps; $r++) {
    $t = hrtime(true);
    switch (explode(':', $case)[0]) {
        case 'read-file-fgetcsv':
            $fp = fopen($file, 'r'); $c = 0; while (($row = fgetcsv($fp, null, ',', '"', '')) !== false) { $c += count($row); } fclose($fp); $out = $c; break;
        case 'read-file-csv':
            $c = 0; foreach (Csv\LazyLaxCollection::createFromFile($file) as $row) { $c += count($row); } $out = $c; break;
        case 'read-buffer-str_getcsv':   // the usual way: split lines, parse each (breaks on embedded newlines, kept for the plain case)
            $c = 0; foreach (explode("\r\n", rtrim($buf, "\r\n")) as $line) { $c += count(str_getcsv($line, ',', '"', '')); } $out = $c; break;
        case 'read-buffer-csv':
            $out = count(Csv\buffer_to_collection($buf)); break;
        case 'read-buffer-csv-lax':
            $out = count(Csv\buffer_to_collection_lax($buf)); break;
        case 'read-buffer-csv-lazy':
            $c = 0; foreach (Csv\LazyLaxCollection::createFromBuffer($buf) as $row) { $c += count($row); } $out = $c; break;
        case 'write-file-fputcsv':
            $fp = fopen('php://memory', 'w+'); foreach ($rows as $row) fputcsv($fp, $row, ',', '"', '', "\r\n"); $out = ftell($fp); fclose($fp); break;
        case 'write-buffer-csv':
            $out = strlen(Csv\collection_to_buffer($rows)); break;
        case 'write-file-csv':
            $out = Csv\collection_to_file('php://memory', $rows); break;
        case 'row-str_getcsv':
            $c = 0; foreach (explode("\r\n", rtrim($buf, "\r\n")) as $line) { $c += count(str_getcsv($line, ',', '"', '')); } $out = $c; break;
        case 'row-csv':
            $c = 0; foreach (explode("\r\n", rtrim($buf, "\r\n")) as $line) { $c += count(Csv\row_to_array($line)); } $out = $c; break;
        case 'rowout-fputcsv':
            $fp = fopen('php://memory', 'w+'); foreach ($rows as $row) { fputcsv($fp, $row, ',', '"', '', "\r\n"); } $out = ftell($fp); fclose($fp); break;
        case 'rowout-csv':
            $c = 0; foreach ($rows as $row) { $c += strlen(Csv\array_to_row($row)); } $out = $c; break;
        default: fwrite(STDERR, "unknown case\n"); exit(1);
    }
    $best = min($best, (hrtime(true) - $t) / $n);
}
printf("%-28s %-7s %8.0f ns/row  (%s)\n", explode(':', $case)[0], $name, $best, var_export($out, true));
