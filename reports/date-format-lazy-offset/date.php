<?php
// DateTimeImmutable::format() and date(): formats without time zone characters, with them, and escaped,
// on every kind of time zone (identifier, offset, abbreviation).

$at = static fn (string $time, ?string $zone = null): Closure =>
    static fn (): DateTimeImmutable => new DateTimeImmutable($time, $zone === null ? null : new DateTimeZone($zone));

$zones = [
    'UTC' => $at('2026-11-18 12:34:56.123456', 'UTC'),
    'Europe/Madrid' => $at('2026-07-01 12:34:56.123456', 'Europe/Madrid'),
    'America/New_York' => $at('2026-11-18 12:34:56.123456', 'America/New_York'),
    'offset +05:30' => $at('2026-11-18T12:34:56.123456+05:30'),
    'abbreviation EST' => $at('2026-11-18 12:34:56.123456 EST'),
];

$formats = [
    // formats without a time zone character
    'Y', 'Y-m-d', 'Y-m-d H:i:s', 'H:i', 'D, d M Y', 'Y-m-d\TH:i:s.u', 'U',
    // formats with a time zone character
    'c', 'Y-m-d\TH:i:sP', 'D, d M Y H:i:s O', 'T',
];

$cases = [];
foreach ($formats as $format) {
    $cases["format('$format')"] = [
        'code' => '$s->format(' . var_export($format, true) . ')',
        'inputs' => array_keys($zones),
    ];
}
$cases["date('Y-m-d')"] = ['code' => "date('Y-m-d', \$s)", 'inputs' => ['timestamp']];
$cases["date('Y-m-d H:i:s')"] = ['code' => "date('Y-m-d H:i:s', \$s)", 'inputs' => ['timestamp']];
$cases["date(DATE_ATOM)"] = ['code' => 'date(DATE_ATOM, $s)', 'inputs' => ['timestamp']];

return [
    'inputs' => $zones + ['timestamp' => 1763469296],
    'cases' => $cases,
];
