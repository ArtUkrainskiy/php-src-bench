<?php
// difftest.php — prints the results of every grapheme_* function that calls grapheme_ascii_check(), and of
// grapheme_stristr(), on inputs that hit both sides of the check, as one md5 per function plus the input count.
// Run on master and on the change: the output must be identical.
//   1. every string of length 0..6 over the alphabet a, CR, LF, "é" (2 bytes), "\xff" (invalid);
//   2. ASCII of length 0..40 with CR, LF, CR LF, "é", "\xff", "\x80", "\x7f" or NUL inserted at every position
//      (covers both 8-byte loop and tail positions);
//   3. texts in several languages and with CR LF line endings.
// grapheme_extract() runs on every 7th input and on every input longer than 6 bytes (to bound the run time),
// for every size 0..len+1, the three extract types and every start offset (strings longer than
// 12 bytes: offsets 0..9 and the last three):
// it checks size + 1 bytes from the start offset, so a CR at the last checked byte is followed by real data.

ini_set('memory_limit', '1G');
$alphabet = ['a', "\r", "\n", "\xc3\xa9", "\xff"];
$inputs = [''];
$level = [''];
for ($n = 1; $n <= 6; $n++) {
    $next = [];
    foreach ($level as $s) {
        foreach ($alphabet as $c) {
            $next[] = $s . $c;
        }
    }
    array_push($inputs, ...$next);
    $level = $next;
}
$base = str_repeat('abcdefghij', 4);
for ($len = 0; $len <= 40; $len++) {
    $a = substr($base, 0, $len);
    $inputs[] = $a;
    for ($pos = 0; $pos <= $len; $pos++) {
        foreach (["\r", "\n", "\r\n", "\xc3\xa9", "\xff", "\x80", "\x7f", "\0"] as $ins) {
            $inputs[] = substr($a, 0, $pos) . $ins . substr($a, $pos);
        }
    }
}
foreach (['The quick brown fox', 'El pingüino Wenceslao', 'Съешь же ещё этих булок', '我能吞下玻璃而不伤身体',
          'いろはにほへと ちりぬるを', '다람쥐 헌 쳇바퀴에 타고파', "Hello 👋 world 🌍 👨‍👩‍👧",
          "line1\r\nline2\r\n", "a\rb\rc\r", str_repeat("word ", 50) . "\r\n"] as $t) {
    $inputs[] = $t;
}

// One result as text; an exception thrown by the call is part of the result.
function t(callable $f): string
{
    try {
        return var_export($f(), true);
    } catch (Throwable $e) {
        return $e::class . ': ' . $e->getMessage();
    }
}

$out = [];
foreach ($inputs as $i => $s) {
    $out['strlen'][] = t(fn() => grapheme_strlen($s));
    $out['substr'][] = t(fn() => grapheme_substr($s, 1, 3)) . t(fn() => grapheme_substr($s, -2))
        . t(fn() => grapheme_substr($s, 0));
    $out['strpos'][] = t(fn() => grapheme_strpos($s . 'zz', 'zz')) . t(fn() => grapheme_strpos($s, "\r\n"))
        . t(fn() => grapheme_strpos($s, 'a', 1)) . t(fn() => grapheme_strpos("x\r\nab" . $s, $s === '' ? 'a' : $s));
    $out['stripos'][] = t(fn() => grapheme_stripos($s . 'ZZ', 'zz')) . t(fn() => grapheme_stripos($s, 'A'));
    $out['strrpos'][] = t(fn() => grapheme_strrpos($s . 'a', 'a')) . t(fn() => grapheme_strrpos($s, "\n"));
    $out['strripos'][] = t(fn() => grapheme_strripos($s . 'a', 'A')) . t(fn() => grapheme_strripos($s, "\r"));
    $out['strstr'][] = t(fn() => grapheme_strstr($s . 'xy', 'x')) . t(fn() => grapheme_stristr($s . 'XY', 'x', true));
    if ($i % 7 === 0 || strlen($s) > 6) {
        $e = '';
        $len = strlen($s);
        $starts = $len <= 12 ? range(0, max($len - 1, 0)) : array_merge(range(0, 9), range($len - 3, $len - 1));
        foreach ($starts as $start) {
            for ($size = 0; $size <= $len + 1; $size++) {
                foreach ([GRAPHEME_EXTR_COUNT, GRAPHEME_EXTR_MAXBYTES, GRAPHEME_EXTR_MAXCHARS] as $type) {
                    $next = null;
                    $e .= t(function () use ($s, $size, $type, $start, &$next) {
                        return grapheme_extract($s, $size, $type, $start, $next);
                    }) . var_export($next, true) . ';';
                }
            }
        }
        $out['extract'][] = $e;
    }
}
foreach ($out as $fn => $vals) {
    printf("%s %d %s\n", $fn, count($vals), md5(implode("\0", $vals)));
}
echo 'inputs ', count($inputs), "\n";
echo "done\n";
