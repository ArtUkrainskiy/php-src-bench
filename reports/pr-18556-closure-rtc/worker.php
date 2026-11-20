<?php
// worker.php <laravel root> <n> [every]: boots Laravel once and serves n requests in a loop
// (/, /users, /users?page=2 by turn) through the HTTP kernel, like a worker without Octane's state reset.
// Prints heap, real heap, peak, RSS and GC counters every [every] requests.
$root = $argv[1]; $n = (int) $argv[2]; $every = (int) ($argv[3] ?? 500);
require $root . '/vendor/autoload.php';
$app = require $root . '/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Http\Kernel::class);
$uris = ['/', '/users', '/users?page=2'];
$rss = static function (): int { preg_match('/VmRSS:\s+(\d+)/', file_get_contents('/proc/self/status'), $m); return (int) $m[1]; };
$t0 = hrtime(true); $len = 0;
for ($i = 1; $i <= $n; $i++) {
    $req = Illuminate\Http\Request::create($uris[$i % 3], 'GET');
    $resp = $kernel->handle($req);
    $len += strlen($resp->getContent());
    $kernel->terminate($req, $resp);
    unset($req, $resp);
    if ($i % $every === 0 || $i === 1) {
        $g = gc_status();
        printf("%5d heap %6.2f MB real %6.2f MB peak %6.2f MB rss %7d KB gc runs %4d collected %8d  %.2f ms/req\n",
            $i, memory_get_usage() / 1048576, memory_get_usage(true) / 1048576, memory_get_peak_usage() / 1048576,
            $rss(), $g['runs'], $g['collected'], (hrtime(true) - $t0) / 1e6 / $i);
    }
}
printf("bytes %d\n", $len);
