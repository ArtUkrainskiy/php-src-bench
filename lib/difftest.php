<?php
/*
 * What every differential test generator in difftests/ needs: the command line, a random
 * number generator that gives the same sequence on every PHP version, and the loop that
 * prints one line per generated input. See docs/suites.md.
 */

/** A linear congruential generator: mt_rand() and random_int() may differ between PHP versions. */
final class DifftestRng
{
    private int $state;

    public function __construct(int $seed)
    {
        $this->state = ($seed * 2654435761 + 1) & 0x7fffffff;
    }

    /** An integer in [0, $bound). */
    public function next(int $bound): int
    {
        $this->state = ($this->state * 1103515245 + 12345) & 0x7fffffff;
        return ($this->state >> 8) % $bound; // the low bits of an LCG repeat quickly
    }

    public function chance(int $percent): bool
    {
        return $this->next(100) < $percent;
    }

    /** A random element of a list. */
    public function pick(array $from)
    {
        return $from[$this->next(count($from))];
    }

    /**
     * A length up to $max that lands on or next to a boundary in $boundaries half of the time
     * (255, 256, 257 for 256): where block loops and buffer growth change course.
     */
    public function length(int $max, array $boundaries = [16, 32, 64, 256, 512, 1024]): int
    {
        if ($this->chance(50)) {
            return max(0, min($max, $this->pick($boundaries) + $this->next(3) - 1));
        }
        return $this->next($max + 1);
    }

    /**
     * A string of $chars characters drawn from the UTF-8 classes in $classes (keys of
     * DIFFTEST_UTF8). With $invalidPercent chance, 1 to 3 of them are replaced with sequences
     * that are not UTF-8 (stray continuation bytes, truncated, overlong, surrogates, too large).
     */
    public function utf8(int $chars, array $classes = ['1', '2', '3', '4'], int $invalidPercent = 0): string
    {
        $parts = [];
        for ($i = 0; $i < $chars; $i++) {
            $parts[] = $this->pick(DIFFTEST_UTF8[$this->pick($classes)]);
        }
        if ($parts && $this->chance($invalidPercent)) {
            for ($k = 1 + $this->next(3); $k > 0; $k--) {
                $parts[$this->next(count($parts))] = $this->pick(DIFFTEST_UTF8['invalid']);
            }
        }
        return implode('', $parts);
    }
}

const DIFFTEST_UTF8 = [
    '1' => ['a', 'z', 'A', ' ', '0', '.', "\n", "\0", "\x7F", '&', '<', '"'],
    '2' => ["\u{80}", "\u{A9}", "\u{AE}", "\u{E9}", "\u{416}", "\u{5D0}", "\u{627}", "\u{7FF}"],
    '3' => ["\u{800}", "\u{20AC}", "\u{4E2D}", "\u{3042}", "\u{AC00}", "\u{915}", "\u{FEFF}", "\u{FFFD}", "\u{E000}", "\u{E63E}", "\u{FFFF}"],
    '4' => ["\u{10000}", "\u{1F600}", "\u{1F1FA}\u{1F1F8}", "\u{1F44D}\u{1F3FD}", "\u{20000}", "\u{10FFFF}"],
    // combining marks and joiners: one visible character, several code points
    'combining' => ["e\u{301}", "\u{915}\u{94D}\u{937}", "\u{1F468}\u{200D}\u{1F469}", "1\u{FE0F}\u{20E3}"],
    'invalid' => [
        "\x80", "\xBF", "\xC0\x80", "\xC1\xBF", "\xC2", "\xE0\x80\x80", "\xE2\x82", "\xED\xA0\x80", "\xED\xBF\xBF",
        "\xF0\x80\x80\x80", "\xF0\x9F\x98", "\xF4\x90\x80\x80", "\xF5\x80\x80\x80", "\xF8\x88\x80\x80\x80", "\xFE", "\xFF",
    ],
];

/**
 * Generates --count inputs with $generate(DifftestRng): string and prints for each of them
 * "<index>\t<md5 of all outputs>", where $outputs(string $input) yields label => output.
 * With --dump INDEX it prints that input and all of its outputs in hex instead.
 */
function difftest_run(array $argv, callable $generate, callable $outputs): void
{
    $opt = ['seed' => 1, 'count' => 20000, 'dump' => null];
    for ($i = 1; $i < count($argv); $i++) {
        if (preg_match('/^--(seed|count|dump)$/', $argv[$i], $m) && isset($argv[$i + 1]) && preg_match('/^\d+$/', $argv[$i + 1])) {
            $opt[$m[1]] = (int) $argv[++$i];
        } else {
            fwrite(STDERR, "usage: {$argv[0]} [--seed N] [--count N] [--dump INDEX]\n");
            exit(2);
        }
    }

    $rng = new DifftestRng($opt['seed']);
    for ($index = 0; $index < $opt['count']; $index++) {
        $input = $generate($rng);
        if ($opt['dump'] !== null && $index !== $opt['dump']) {
            continue;
        }
        $hash = hash_init('md5');
        foreach ($outputs($input) as $label => $output) {
            // the length goes in too, so that outputs cannot run into each other
            hash_update($hash, strlen($output) . ':' . $output);
            if ($opt['dump'] !== null) {
                printf("%-60s %s\n", $label, bin2hex($output));
            }
        }
        if ($opt['dump'] !== null) {
            printf("input (%d bytes): %s\n", strlen($input), bin2hex($input));
            return;
        }
        echo $index, "\t", hash_final($hash), "\n";
    }
}
