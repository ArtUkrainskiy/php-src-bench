<?php
// Owned fixtures matching the six recorded supplementary stress cases.
$needle = str_repeat('ab', 127) . 'bb';
$inputs = [
    'case-318' => str_repeat('z', 300000) . 'zqw' . str_repeat('a', 4000),
    'case-320' => str_repeat('a', 300000),
    'case-323' => str_repeat('abcabd', 50000),
    'pair-killer' => str_repeat('ab', 100000),
    'changing-density' => str_repeat('a' . str_repeat('x', 199), 70) . str_repeat('ab', 100000),
];
$inputs['changing-density-match'] = $inputs['changing-density'] . $needle;
return ['inputs' => $inputs, 'cases' => [
    'first dense_anchor dense n3 #318' => ['code' => 'strpos($s, \'zqw\')', 'inputs' => ['case-318']],
    'first allcommon_long allcommon_long n201 #320' => [
        'code' => 'strpos($s, ' . var_export(str_repeat('a', 200) . 'q', true) . ')', 'inputs' => ['case-320'],
    ],
    'first periodic periodic n9 #323' => ['code' => 'strpos($s, \'abcabcabd\')', 'inputs' => ['case-323']],
    'late dense pair' => [
        'code' => 'strpos($s, ' . var_export($needle, true) . ')',
        'inputs' => ['pair-killer', 'changing-density', 'changing-density-match'],
    ],
]];
