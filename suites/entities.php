<?php
// Entity decoding on text with a growing share of entities, from plain text to entities only.
//
// Cases: html_entity_decode(), htmlspecialchars_decode() and htmlspecialchars(double_encode: false).
// mixed-N%: about N% of the input bytes belong to entities (70% named, 20% numeric, 10% invalid).
// only-<pool>: entities from one pool only, see Corpus::ENTITY_POOLS.

$bytes = 4096;

$inputs = [];
foreach ([0, 1, 5, 10, 25, 50, 75, 100] as $pct) {
    $inputs["mixed-$pct%"] = static fn (): string => Corpus::entities($pct / 100, $bytes);
}
foreach (array_keys(Corpus::ENTITY_POOLS) as $pool) {
    $inputs["only-$pool"] = static fn (): string => Corpus::entities(1.0, $bytes, $pool);
}
$inputs['only-amp'] = str_repeat('&amp;', intdiv($bytes, 5));
$inputs['bare-amp'] = str_repeat('&', $bytes);

// Input size at a realistic density, and plain text with a single '&' at the very end.
foreach (['64' => 64, '256' => 256, '64k' => 65536] as $label => $size) {
    $inputs["mixed-5%/$label"] = static fn (): string => Corpus::entities(0.05, $size);
}
$inputs['tail-amp'] = static fn (): string => Corpus::text('en', $bytes) . '&';

$sweep = array_filter(array_keys($inputs), static fn (string $name): bool => (bool) preg_match('/^mixed-\d+%$/', $name));
$sizes = ['mixed-5%/64', 'mixed-5%/256', 'mixed-5%/64k', 'tail-amp']; // the 4 KB size is mixed-5% of the sweep

return [
    'inputs' => $inputs,
    'cases' => [
        'html_entity_decode' => [
            'code' => 'html_entity_decode($s)',
            'inputs' => [...$sweep, 'only-amp', 'only-basic', 'only-named', 'only-numeric', 'only-invalid', 'bare-amp', ...$sizes],
        ],
        'html_entity_decode ENT_HTML5' => [
            'code' => 'html_entity_decode($s, ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML5)',
            'inputs' => [...$sweep, 'only-html5'],
        ],
        'htmlspecialchars_decode' => [
            'code' => 'htmlspecialchars_decode($s)',
            'inputs' => [...$sweep, 'only-basic', ...$sizes],
        ],
        'htmlspecialchars !double_encode' => [
            'code' => 'htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, null, false)',
            'inputs' => [...$sweep, 'only-named', 'only-invalid'],
        ],
    ],
];
