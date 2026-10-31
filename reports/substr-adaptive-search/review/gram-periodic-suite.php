<?php
// Additional attribution after the initial a^31b/ab pilot favoured no-gram4.
// Preserve that negative result; test periodic needles as a distinct workload.
$inputs = [
    'periodic-ascii' => substr(str_repeat('bb' . str_repeat('ab', 15), 3) . 'c' . str_repeat('abac', 16384), 0, 65536),
    'periodic-dna' => substr(str_repeat('TCGT' . str_repeat('ACGT', 7), 4) . 'x' . str_repeat('ACGA', 16384), 0, 65536),
];
return ['inputs' => $inputs, 'cases' => [
    'gram-periodic/ascii/absent' => ['code' => 'strpos($s, ' . var_export(str_repeat('ab', 16), true) . ')', 'inputs' => ['periodic-ascii']],
    'gram-periodic/dna/absent' => ['code' => 'strpos($s, ' . var_export(str_repeat('ACGT', 8), true) . ')', 'inputs' => ['periodic-dna']],
]];
