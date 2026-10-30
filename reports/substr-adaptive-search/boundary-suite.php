<?php
// Reproduce the owned 112-case routing grid without storing repeated input bytes.
$inputs = $cases = [];
$add = static function (string $name, string $hay, string $needle) use (&$inputs, &$cases): void {
    $inputs[$name] = $hay;
    $cases[$name] = ['code' => 'strpos($s, ' . var_export($needle, true) . ')', 'inputs' => [$name]];
};
$fill = static function (string $pattern, int $size): string {
    return substr(str_repeat($pattern, intdiv($size, strlen($pattern)) + 1), 0, $size);
};
foreach ([31, 32, 33, 64, 256] as $n) {
    foreach ([8191, 8192, 8193, 65536] as $h) {
        $add("dense-prefix/n$n/h$h", str_repeat('a', $h), str_repeat('a', $n - 1) . 'b');
        $add("periodic/n$n/h$h", $fill('ab', $h), substr(str_repeat('ab', intdiv($n - 1, 2)) . 'bb', 0, $n));
        $hay = $fill('product catalog search: order paid, parcel delivered, tracking updated. ', $h);
        $needle = $fill('checkout-complete/request-id=', $n);
        $add("ordinary-miss/n$n/h$h", $hay, $needle);
        $add("early-match/n$n/h$h", $needle . substr($hay, 0, $h - $n), $needle);
        $add("late-match/n$n/h$h", substr($hay, 0, $h - $n) . $needle, $needle);
    }
}
foreach ([32, 256] as $n) {
    foreach ([4095, 4096, 4097] as $remaining) {
        $hay = str_repeat('x', 8192) . str_repeat('a', $remaining + 16);
        $needle = str_repeat('a', $n - 1) . 'b';
        $add("late-density/n$n/remaining$remaining/absent", $hay, $needle);
        $add("late-density/n$n/remaining$remaining/match", substr($hay, 0, -1) . 'b', $needle);
    }
}
return ['inputs' => $inputs, 'cases' => $cases];
