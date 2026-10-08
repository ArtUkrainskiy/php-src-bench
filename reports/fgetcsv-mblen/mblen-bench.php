<?php
// Per-call cost of the php_mblen() users: ns per row (CSV) or per call, best of N runs.
$dir = $argv[1] ?? __DIR__ . '/data';
$N = 5;
$best = function (callable $f, int $iters) use ($N) {
    $b = INF;
    for ($r = 0; $r < $N; $r++) { $t = hrtime(true); $f(); $t = hrtime(true) - $t; $b = min($b, $t / $iters); }
    return $b;
};
$rows = fn($file) => count(file($file));
foreach (['plain', 'quoted', 'wide'] as $k) {
    $file = "$dir/$k.csv"; $n = $rows($file);
    $t = $best(function () use ($file) { $fp = fopen($file, 'r'); while (fgetcsv($fp, null, ',', '"', '') !== false); fclose($fp); }, $n);
    printf("fgetcsv %-7s %6.0f ns/row\n", $k, $t);
    $lines = file($file, FILE_IGNORE_NEW_LINES);
    $t = $best(function () use ($lines) { foreach ($lines as $l) str_getcsv($l, ',', '"', ''); }, count($lines));
    printf("str_getcsv %-4s %6.0f ns/row\n", $k, $t);
}
$args = ['/usr/local/bin/some-tool', "it's a \"quoted\" arg with spaces", str_repeat('abcdefgh', 16), 'путь/к/файлу.txt'];
foreach ($args as $i => $a) {
    $t = $best(function () use ($a) { for ($i = 0; $i < 100000; $i++) escapeshellarg($a); }, 100000);
    printf("escapeshellarg #%d (%3d bytes) %6.0f ns\n", $i, strlen($a), $t);
}
$paths = ['/var/www/html/vendor/symfony/console/Command/Command.php', 'C:\\x\\y.txt', 'файл.txt'];
foreach ($paths as $i => $p) {
    $t = $best(function () use ($p) { for ($i = 0; $i < 100000; $i++) basename($p); }, 100000);
    printf("basename #%d (%3d bytes) %6.0f ns\n", $i, strlen($p), $t);
}
