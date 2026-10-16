<?php
/*
 * Differential test for any expressions on $s, without writing a generator:
 *
 *   bench difftest code base dev --code 'mb_substr($s, 3, 10)' --code 'mb_strpos($s, "a")' \
 *       --setup 'mb_check_encoding($s, "UTF-8")' --seed 1 --count 20000
 *
 * Inputs (--input): utf8 (default) is 1- to 4-byte characters and combining sequences, about 10%
 * of the strings with invalid sequences, among them 3% with a truncated sequence at the very end;
 * ascii is printable ASCII; bytes is any byte. Lengths are in bytes, up to --max N (default 2100),
 * half of them on or next to a boundary: 16, 32, 64, 256, 512, 1024, 2048 (the sizes block loops
 * work in), or the list given with --boundaries, e.g. the block sizes of hash functions
 * (--boundaries 64,72,104,128,136,144). Boundaries above --max are left out.
 * Every expression runs on a fresh copy of the input; with --setup it runs a second time on a
 * copy that went through the setup first. A warning or an exception is part of the output.
 */
require dirname(__DIR__) . '/lib/difftest.php';

$codes = [];
$setup = null;
$kind = 'utf8';
$max = 2100;
$boundaries = [16, 32, 64, 256, 512, 1024, 2048];
$rest = [$argv[0]];
for ($i = 1; $i < count($argv); $i++) {
    $arg = $argv[$i];
    $value = $argv[$i + 1] ?? null;
    if ($arg === '--code' && $value !== null) {
        $codes[] = $value;
    } elseif ($arg === '--setup' && $value !== null) {
        $setup = $value;
    } elseif ($arg === '--input' && in_array($value, ['utf8', 'ascii', 'bytes'], true)) {
        $kind = $value;
    } elseif ($arg === '--max' && $value !== null && ctype_digit_ascii($value)) {
        $max = (int) $value;
    } elseif ($arg === '--boundaries' && $value !== null
        && array_filter(explode(',', $value), 'ctype_digit_ascii') === explode(',', $value)) {
        $boundaries = array_map('intval', explode(',', $value));
    } else {
        $rest[] = $arg;
        continue;
    }
    $i++;
}
if (!$codes) {
    fwrite(STDERR, "usage: bench difftest code <A> <B> --code EXPR [--code EXPR...] [--setup CODE] [--input utf8|ascii|bytes] [--max N] [--boundaries N,N,...] [--seed N] [--count N]\n");
    exit(2);
}

function ctype_digit_ascii(string $s): bool
{
    return $s !== '' && strspn($s, '0123456789') === strlen($s);
}

// The newline ends a trailing // comment before the closing brace.
// A boundary above the longest input would only make inputs of exactly --max bytes.
$boundaries = array_values(array_filter($boundaries, static fn (int $b): bool => $b <= $max));
if (!$boundaries) {
    fwrite(STDERR, "--boundaries: none of them is within --max $max\n");
    exit(2);
}

$compile = static fn (string $code): Closure => eval('return static function ($s) { return ' . rtrim($code, "; \n") . "\n;\n};");
$functions = array_combine($codes, array_map($compile, $codes));
$prepare = $setup === null ? null : eval('return static function (&$s): void { ' . rtrim($setup, "; \n") . "\n;\n};");

// A function this build does not have (an extension left out) would be the same exception on
// every build, and the test would pass without testing anything.
foreach ($functions + ($prepare ? ['setup' => $prepare] : []) as $code => $f) {
    try {
        $probe = 'abc';
        $f($probe);
    } catch (Error $e) {
        if (str_contains($e->getMessage(), 'undefined function') || str_contains($e->getMessage(), 'not found')) {
            fwrite(STDERR, "$code: " . $e->getMessage() . " (build PHP with the extension, BENCH_CONFIGURE_EXTRA)\n");
            exit(3);
        }
    }
}

$generate = static function (DifftestRng $rng) use ($kind, $max, $boundaries): string {
    $bytes = $rng->length($max, $boundaries);
    if ($kind !== 'utf8') {
        $out = '';
        for ($i = 0; $i < $bytes; $i++) {
            $out .= $kind === 'ascii' ? chr(32 + $rng->next(95)) : chr($rng->next(256));
        }
        return $out;
    }
    // Characters until the length is reached, then whole characters off and ASCII on, so that
    // the string is exactly $bytes long and still ends on a character boundary.
    $out = $rng->utf8(intdiv($bytes, 2) + 1, ['1', '1', '2', '3', '4', 'combining'], 10);
    while (strlen($out) < $bytes) {
        $out .= $rng->utf8(16, ['1', '1', '2', '3', '4', 'combining']);
    }
    $out = substr($out, 0, $bytes);
    $out = rtrim_partial_utf8($out);
    $out .= str_repeat('a', $bytes - strlen($out));
    if ($bytes > 0 && $rng->chance(3)) {
        $tail = $rng->pick(["\xC3", "\xE2\x82", "\xF0\x9F\x98", "\xED\xA0"]);
        $out = substr($out, 0, max(0, $bytes - strlen($tail))) . $tail;
    }
    return $out;
};

/** $s without a UTF-8 sequence cut off at its end (invalid sequences elsewhere stay). */
function rtrim_partial_utf8(string $s): string
{
    for ($back = 1; $back <= min(3, strlen($s)); $back++) {
        $byte = ord($s[strlen($s) - $back]);
        if ($byte < 0x80) {
            return $s;
        }
        if ($byte >= 0xC0) {
            $need = $byte >= 0xF0 ? 4 : ($byte >= 0xE0 ? 3 : 2);
            return $back < $need ? substr($s, 0, -$back) : $s;
        }
    }
    return $s;
}

/** What a call made of $s, as a string: its result, or the warning or exception it raised. */
$run = static function (Closure $f, string $s): string {
    $warning = '';
    set_error_handler(static function (int $no, string $msg) use (&$warning): bool {
        $warning .= "warning: $msg\n";
        return true;
    });
    try {
        $result = serialize($f($s));
    } catch (Throwable $e) {
        $result = 'exception: ' . get_class($e) . ': ' . $e->getMessage();
    } finally {
        restore_error_handler();
    }
    return $warning . $result;
};

$outputs = static function (string $input) use ($functions, $prepare, $run): Generator {
    foreach ($functions as $code => $f) {
        // strrev(strrev()) makes a new string: flags that PHP keeps on a string stay on the copy.
        yield $code => $run($f, strrev(strrev($input)));
        if ($prepare !== null) {
            $copy = strrev(strrev($input));
            $prepare($copy);
            yield "setup: $code" => $run($f, $copy);
        }
    }
};

difftest_run($rest, $generate, $outputs);
