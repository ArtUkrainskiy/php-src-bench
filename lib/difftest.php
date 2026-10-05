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
}

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
