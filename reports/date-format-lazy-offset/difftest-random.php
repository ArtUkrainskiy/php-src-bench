<?php
// difftest-random.php [count] [seed] — DateTimeImmutable::format(), date() and gmdate() on fixed edge formats and on
// random formats over every zone kind; one line per format and date (date() and gmdate() share a line). Compare between builds.
$count = (int) ($argv[1] ?? 20000);
$seed = (int) ($argv[2] ?? 1);

$utc = new DateTimeZone('UTC');
$dates = [
    'id-utc' => new DateTimeImmutable('2026-03-29 01:30:00.5', $utc),
    'id-madrid-dst' => new DateTimeImmutable('2026-07-01 12:00:00', new DateTimeZone('Europe/Madrid')),
    'id-madrid' => new DateTimeImmutable('2026-01-01 00:00:00', new DateTimeZone('Europe/Madrid')),
    'id-kolkata' => new DateTimeImmutable('2026-11-18 23:59:59.999999', new DateTimeZone('Asia/Kolkata')),
    'id-lord-howe' => new DateTimeImmutable('2026-01-15 08:00:00', new DateTimeZone('Australia/Lord_Howe')),
    'id-monrovia-1971' => new DateTimeImmutable('1971-06-01 00:00:00', new DateTimeZone('Africa/Monrovia')),
    'offset' => new DateTimeImmutable('2026-11-18T12:34:56-09:30'),
    'offset-min' => (new DateTimeImmutable('2026-11-18 12:00:00'))->setTimezone(new DateTimeZone('+05:45')),
    'offset-sec' => (new DateTimeImmutable('2026-11-18 12:00:00'))->setTimezone(new DateTimeZone('+05:45:30')),
    'abbr' => new DateTimeImmutable('2026-11-18 12:34:56 EST'),
    'abbr-dst' => new DateTimeImmutable('2026-07-18 12:34:56 PDT'),
    'zulu' => new DateTimeImmutable('2026-11-18T12:34:56Z'),
    'ts' => new DateTimeImmutable('@1763469296'),
    'ts-neg' => new DateTimeImmutable('@-1234567890'),
    'year-neg' => (new DateTimeImmutable('2026-01-01 00:00:00.000001', $utc))->setDate(-50, 2, 3),
    'year-neg5' => (new DateTimeImmutable('2026-01-01 00:00:00', $utc))->setDate(-5, 1, 9),
    'year-zero' => (new DateTimeImmutable('2026-01-01 23:59:59.000010', new DateTimeZone('America/St_Johns')))->setDate(0, 12, 31),
    'year-7' => (new DateTimeImmutable('2026-01-01 00:00:00', $utc))->setDate(7, 1, 9),
    'year-9999' => (new DateTimeImmutable('2026-12-31 23:59:59', $utc))->setDate(9999, 12, 31),
    'year-10000' => (new DateTimeImmutable('2026-01-01 00:00:00', $utc))->setDate(10000, 1, 1),
    'year-big' => (new DateTimeImmutable('2026-01-01 05:06:07.123', new DateTimeZone('Pacific/Chatham')))->setDate(12345, 6, 7),
    'year-max' => (new DateTimeImmutable('2026-01-01 00:00:00', $utc))->setDate(PHP_INT_MAX, 1, 1),
    'year-min' => (new DateTimeImmutable('2026-01-01 00:00:00', $utc))->setDate(PHP_INT_MIN, 1, 1),
    'year-min1' => (new DateTimeImmutable('2026-01-01 00:00:00', $utc))->setDate(PHP_INT_MIN + 1, 1, 1),
];

$fixed = [
    '\\T', '\\\\T', '\\e\\I\\O\\P\\p\\T\\Z\\c\\r', 'Y\\', '\\', '\\\\', 'Y-m-d\\TH:i:s', 'Y-m-d\\TH:i:sP',
    'D, d M Y H:i:s O', 'x', 'X', 'y', 'Y', 'o', 'B', 'u', 'v', 'U', 'L', 'W', 'z', 't', "\0Y", 'Y\\Y',
];
$chars = str_split('dDjlNSwzWFmMntLoXxYyaABgGhHisuveIOPpTZcrU\\-: /.,T0');

foreach ($dates as $name => $d) {
    foreach ($fixed as $f) {
        echo $name, ' ', bin2hex($f), ' ', $d->format($f), "\n";
    }
}

mt_srand($seed);
$names = array_keys($dates);
for ($n = 0; $n < $count; $n++) {
    $f = '';
    for ($k = mt_rand(1, 12); $k > 0; $k--) {
        $f .= $chars[mt_rand(0, count($chars) - 1)];
    }
    $name = $names[mt_rand(0, count($names) - 1)];
    echo $name, ' ', bin2hex($f), ' ', $dates[$name]->format($f), "\n";
}

foreach (['UTC', 'America/New_York', 'Asia/Kathmandu'] as $tz) {
    date_default_timezone_set($tz);
    foreach (array_merge($fixed, $chars) as $f) {
        foreach ([1763469296, -1234567890, 0] as $ts) {
            echo $tz, ' ', bin2hex($f), ' ', $ts, ' ', date($f, $ts), ' | ', gmdate($f, $ts), "\n";
        }
    }
}
