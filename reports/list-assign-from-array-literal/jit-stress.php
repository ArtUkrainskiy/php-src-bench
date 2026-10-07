<?php
// Hot loops around destructuring from an array literal, for runs with the JIT:
// the results must be the same on every build, the times show the effect of the change.

function swap_ints(int $n): int
{
    $a = 1;
    $b = 2;
    for ($i = 0; $i < $n; $i++) {
        [$a, $b] = [$b, $a];
    }
    return $a * 10 + $b;
}

function fibonacci(int $n): int
{
    $a = 0;
    $b = 1;
    for ($i = 0; $i < $n; $i++) {
        [$a, $b] = [$b, ($a + $b) % 1000000007];
    }
    return $a;
}

function rotate_strings(int $n): string
{
    $a = 'alpha';
    $b = 'beta';
    $c = 'gamma';
    for ($i = 0; $i < $n; $i++) {
        [$a, $b, $c] = [$b, $c, $a . ''];
    }
    return "$a $b $c";
}

function swap_array_elements(int $n): int
{
    $data = range(0, 15);
    for ($i = 0; $i < $n; $i++) {
        $x = $i & 15;
        $y = ($i * 7 + 3) & 15;
        [$data[$x], $data[$y]] = [$data[$y], $data[$x]];
    }
    return crc32(implode(',', $data));
}

function swap_properties(int $n): string
{
    $o = new stdClass;
    $o->a = 'left';
    $o->b = ['right'];
    for ($i = 0; $i < $n; $i++) {
        [$o->a, $o->b] = [$o->b, $o->a];
    }
    return json_encode($o);
}

// The types change half-way: the tracing JIT has to leave its trace and compile another one.
function changing_types(int $n): string
{
    $a = 1;
    $b = 2.5;
    for ($i = 0; $i < $n; $i++) {
        if ($i === $n >> 1) {
            $a = 'text';
            $b = [1, 2];
        }
        [$a, $b] = [$b, $a];
    }
    return json_encode([$a, $b]);
}

function with_skipped_and_extra(int $n): int
{
    $sum = 0;
    for ($i = 0; $i < $n; $i++) {
        [, $b] = [$i, $i + 1, $i + 2];
        $sum += $b;
    }
    return $sum;
}

function nested(int $n): int
{
    $a = 1;
    $b = 2;
    $c = 3;
    for ($i = 0; $i < $n; $i++) {
        [[$a, $b], $c] = [[$b, $c], $a];
    }
    return $a * 100 + $b * 10 + $c;
}

$n = (int) ($argv[1] ?? 200000);
$total = 0.0;
foreach (['swap_ints', 'fibonacci', 'rotate_strings', 'swap_array_elements', 'swap_properties', 'changing_types', 'with_skipped_and_extra', 'nested'] as $function) {
    $start = hrtime(true);
    $result = $function($n);
    $ms = (hrtime(true) - $start) / 1e6;
    $total += $ms;
    printf("%-24s %-42s", $function, is_string($result) ? $result : (string) $result);
    fprintf(STDERR, "%-24s %8.2f ms\n", $function, $ms);
    echo "\n";
}
fprintf(STDERR, "%-24s %8.2f ms\n", 'total', $total);
