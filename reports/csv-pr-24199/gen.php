<?php
// Generates CSV test data: N rows x 10 fields; "plain" has no quoting, "quoted" has ~30% fields
// needing enclosure (commas, quotes, newlines), "wide" has 50 short fields.
mt_srand(42);
function field(bool $quoted): string {
    $w = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta'][mt_rand(0, 7)] . mt_rand(0, 99999);
    if (!$quoted) return $w;
    return match (mt_rand(0, 9)) { 0 => "$w, with comma", 1 => "$w \"quoted\" word", 2 => "$w\nline two", default => $w };
}
$dir = $argv[1];
foreach (['plain' => [10, false], 'quoted' => [10, true], 'wide' => [50, false]] as $name => [$nf, $q]) {
    $rows = [];
    for ($i = 0; $i < 20000; $i++) { $r = []; for ($j = 0; $j < $nf; $j++) $r[] = field($q); $rows[] = $r; }
    $fp = fopen("$dir/$name.csv", 'w');
    foreach ($rows as $r) fputcsv($fp, $r, ',', '"', '', "\r\n");
    fclose($fp);
    file_put_contents("$dir/$name.json", json_encode($rows));
    printf("%-7s %6d rows %8d bytes\n", $name, count($rows), filesize("$dir/$name.csv"));
}
