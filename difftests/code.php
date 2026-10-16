<?php
/*
 * Differential test for any expressions on $s, without writing a generator:
 *
 *   bench difftest code base dev --code 'mb_substr($s, 3, 10)' --code 'mb_strpos($s, "a")' \
 *       --setup 'mb_check_encoding($s, "UTF-8")' --seed 1 --count 20000
 *
 * Inputs (--input): utf8 (default) is 1- to 4-byte characters and combining sequences, 10% of
 * the strings with invalid sequences; ascii is printable ASCII; bytes is any byte. Lengths go up
 * to --max N characters (default 1100), half of them on or next to 16, 32, 64, 256, 512 or 1024.
 * Every expression runs on a fresh copy of the input; with --setup it runs a second time on a
 * copy that went through the setup first. A warning or an exception is part of the output.
 */
require dirname(__DIR__) . '/lib/difftest.php';

$codes = [];
$setup = null;
$kind = 'utf8';
$max = 1100;
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
    } else {
        $rest[] = $arg;
        continue;
    }
    $i++;
}
if (!$codes) {
    fwrite(STDERR, "usage: bench difftest code <A> <B> --code EXPR [--code EXPR...] [--setup CODE] [--input utf8|ascii|bytes] [--max N] [--seed N] [--count N]\n");
    exit(2);
}

function ctype_digit_ascii(string $s): bool
{
    return $s !== '' && strspn($s, '0123456789') === strlen($s);
}

$compile = static fn (string $code): Closure => eval('return static function ($s) { return ' . rtrim($code, "; \n") . '; };');
$functions = array_combine($codes, array_map($compile, $codes));
$prepare = $setup === null ? null : eval('return static function (&$s): void { ' . rtrim($setup, "; \n") . '; };');

$generate = static function (DifftestRng $rng) use ($kind, $max): string {
    $chars = $rng->length($max);
    if ($kind === 'utf8') {
        return $rng->utf8($chars, ['1', '1', '2', '3', '4', 'combining'], 10);
    }
    $out = '';
    for ($i = 0; $i < $chars; $i++) {
        $out .= $kind === 'ascii' ? chr(32 + $rng->next(95)) : chr($rng->next(256));
    }
    return $out;
};

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
