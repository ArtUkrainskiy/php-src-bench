<?php
// The paths around the change: serialization of date objects (it formats each date with 'x-m-d H:i:s.u'),
// gmdate(), date() with a time zone identifier as the default zone, and formats that use the offset more than
// once or through 'p' and 'e'. The default zone of this suite is Europe/Madrid; gmdate() ignores it.

date_default_timezone_set('Europe/Madrid');

$at = static fn (string $time, ?string $zone = null): Closure =>
    static fn (): DateTimeImmutable => new DateTimeImmutable($time, $zone === null ? null : new DateTimeZone($zone));

// 100 dates one day apart, so that the dates cross a daylight saving time transition.
$hundred = static function (string $zone): Closure {
    return static function () use ($zone): array {
        $tz = new DateTimeZone($zone);
        $first = new DateTimeImmutable('2026-01-15 08:30:00.123456', $tz);
        $dates = [];
        for ($i = 0; $i < 100; $i++) {
            $dates[] = $first->modify("+$i day");
        }
        return $dates;
    };
};

$zones = [
    'UTC' => $at('2026-11-18 12:34:56.123456', 'UTC'),
    'Europe/Madrid' => $at('2026-07-01 12:34:56.123456', 'Europe/Madrid'),
    'offset +05:30' => $at('2026-11-18T12:34:56.123456+05:30'),
    'abbreviation EST' => $at('2026-11-18 12:34:56.123456 EST'),
];

$cases = [];
foreach (['json_encode', 'serialize'] as $fn) {
    $cases["$fn(100 dates)"] = ['code' => "$fn(\$s)", 'inputs' => ['100 dates UTC', '100 dates Europe/Madrid']];
}
foreach (['Y-m-d H:i:s', 'c', DATE_ATOM, 'D, d M Y H:i:s \G\M\T'] as $format) {
    $cases['gmdate(' . var_export($format, true) . ')'] = ['code' => 'gmdate(' . var_export($format, true) . ', $s)', 'inputs' => ['timestamp']];
}
foreach (['Y-m-d', 'Y-m-d H:i:s', DATE_ATOM] as $format) {
    $cases['date(' . var_export($format, true) . ')'] = ['code' => 'date(' . var_export($format, true) . ', $s)', 'inputs' => ['timestamp']];
}
foreach (['p', 'e', 'Y-m-d H:i:s T (P)', 'P T e I Z'] as $format) {
    $cases['format(' . var_export($format, true) . ')'] = ['code' => '$s->format(' . var_export($format, true) . ')', 'inputs' => array_keys($zones)];
}

return [
    'inputs' => $zones + [
        'timestamp' => 1763469296,
        '100 dates UTC' => $hundred('UTC'),
        '100 dates Europe/Madrid' => $hundred('Europe/Madrid'),
    ],
    'cases' => $cases,
];
