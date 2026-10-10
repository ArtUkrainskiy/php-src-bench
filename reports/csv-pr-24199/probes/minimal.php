<?php
// Shortest failing round-trips per dialect, single row, fields from a tiny alphabet
$dialects = [['xy', 'xyx', "\n"], ['--', 'aa', "\r\n"], [',', '"', "\r\n"], ['ab', 'b', "\n"], [',', 'aa', "\n"]];
foreach ($dialects as [$d, $e, $eol]) {
    $alpha = array_values(array_unique(str_split($d . $e . 'z')));
    $found = [];
    for ($len = 1; $len <= 4 && count($found) < 3; $len++) {
        $total = count($alpha) ** $len;
        for ($k = 0; $k < $total && count($found) < 3; $k++) {
            $s = ''; $t = $k; for ($i = 0; $i < $len; $i++) { $s .= $alpha[$t % count($alpha)]; $t = intdiv($t, count($alpha)); }
            foreach ([[$s], [$s, 'z']] as $row) {
                try { $line = Csv\array_to_row($row, $d, $e, $eol); $back = Csv\row_to_array($line, $d, $e, $eol); $res = $back === $row ? null : 'parsed as ' . json_encode($back); }
                catch (Throwable $t2) { $res = get_class($t2) . ': ' . $t2->getMessage(); }
                if ($res !== null) { $found[] = sprintf("  %-14s -> %-22s %s", json_encode($row), json_encode($line), $res); break; }
            }
        }
    }
    printf("delimiter %s enclosure %s:\n%s\n", json_encode($d), json_encode($e), $found ? implode("\n", $found) : "  no failure up to 4 chars");
}
