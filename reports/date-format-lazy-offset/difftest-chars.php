<?php
// difftest-chars.php — prints DateTimeImmutable::format(), date() and gmdate() for every format character on every kind of time zone; run it on two builds and compare the output.
$zones = [
    'id-utc' => new DateTimeImmutable('2026-03-29 01:30:00.5', new DateTimeZone('UTC')),
    'id-madrid-dst' => new DateTimeImmutable('2026-07-01 12:00:00', new DateTimeZone('Europe/Madrid')),
    'id-madrid' => new DateTimeImmutable('2026-01-01 00:00:00', new DateTimeZone('Europe/Madrid')),
    'id-kolkata' => new DateTimeImmutable('2026-11-18 23:59:59.999999', new DateTimeZone('Asia/Kolkata')),
    'offset' => new DateTimeImmutable('2026-11-18T12:34:56-09:30'),
    'abbr' => new DateTimeImmutable('2026-11-18 12:34:56 EST'),
    'abbr-dst' => new DateTimeImmutable('2026-07-18 12:34:56 PDT'),
    'zulu' => new DateTimeImmutable('2026-11-18T12:34:56Z'),
    'year-neg' => (new DateTimeImmutable('2026-01-01 00:00:00.000001', new DateTimeZone('UTC')))->setDate(-50, 2, 3),
    'year-zero' => (new DateTimeImmutable('2026-01-01 23:59:59.000010', new DateTimeZone('America/St_Johns')))->setDate(0, 12, 31),
    'year-big' => (new DateTimeImmutable('2026-01-01 05:06:07.123', new DateTimeZone('Pacific/Chatham')))->setDate(12345, 6, 7),
    'year-huge' => (new DateTimeImmutable('2026-01-01 01:02:03', new DateTimeZone('UTC')))->setDate(99999, 1, 1),
    'neg-offset-min' => new DateTimeImmutable('2026-11-18T00:00:05.000999-03:30'),
    'ts-neg' => new DateTimeImmutable('@-1234567890'),
    'year-7' => (new DateTimeImmutable('2026-01-01 00:00:00', new DateTimeZone('UTC')))->setDate(7, 1, 9),
    'year-neg5' => (new DateTimeImmutable('2026-01-01 00:00:00', new DateTimeZone('UTC')))->setDate(-5, 1, 9),
];
$chars = array_merge(range('a', 'z'), range('A', 'Z'), ['\\T', '\\\\T', 'Y-m-d\\TH:i:sP', 'D, d M Y H:i:s O', '\\e\\I']);
foreach ($zones as $zn => $d) {
    foreach ($chars as $c) {
        echo "$zn [$c] ", $d->format($c), "\n";
    }
}
date_default_timezone_set('America/New_York');
foreach ($chars as $c) {
    echo "date [$c] ", date($c, 1763469296), " | gmdate ", gmdate($c, 1763469296), "\n";
}
