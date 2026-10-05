<?php
// html_entity_decode() with one entity every N bytes: cost as a function of the distance between entities.
//
// 4 KB inputs, "&amp; " after N - 6 letters; "adjacent" is entities back to back.
$period = static fn (int $bytes): string => str_repeat(str_repeat('a', $bytes - 6) . '&amp; ', intdiv(4096, $bytes));
return [
    'inputs' => [
        'period-80' => $period(80),
        'period-40' => $period(40),
        'period-24' => $period(24),
        'period-16' => $period(16),
        'period-12' => $period(12),
        'period-8' => $period(8),
        'adjacent' => str_repeat('&amp;', 800),
    ],
    'cases' => ['html_entity_decode' => 'html_entity_decode($s)'],
];
