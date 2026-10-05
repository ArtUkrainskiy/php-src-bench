<?php

/** A corpus file is not there: generated ones come from corpus/generate.py, real ones from corpus/real/fetch.sh. */
final class MissingCorpus extends RuntimeException
{
}

/** Test inputs for suites, built from corpus/<name>.txt (one short sentence per line). */
final class Corpus
{
    /** Entity pools for Corpus::entities(); "mixed" draws 70% named, 20% numeric, 10% invalid. */
    public const ENTITY_POOLS = [
        'basic' => ['&amp;', '&lt;', '&gt;', '&quot;', '&#039;'],
        'named' => ['&amp;', '&lt;', '&gt;', '&quot;', '&nbsp;', '&copy;', '&hellip;', '&mdash;', '&euro;', '&laquo;', '&raquo;', '&eacute;'],
        'html5' => ['&NotNestedGreaterGreater;', '&CounterClockwiseContourIntegral;', '&nGt;', '&apos;', '&Tab;', '&bigtriangleup;', '&frac12;', '&rarr;'],
        'numeric' => ['&#8212;', '&#x41;', '&#39;', '&#x1F600;', '&#160;', '&#x3C;'],
        'invalid' => ['&unknown;', '&#xZZ;', '&foo', '&;', '& ', '&#;', '&amp', '&notanentity;'],
    ];

    /** @var array<string, list<string>> */
    private static array $lines = [];

    /** @var list<string>|null English words for entities() */
    private static ?array $words = null;

    /**
     * English words from corpus/en.txt interleaved with entities so that about $share of the
     * bytes belong to entities (0.0: plain text, 1.0: entities only). At least $bytes long.
     * Uses its own LCG, so the output is identical on every PHP version.
     */
    public static function entities(float $share, int $bytes, string $pool = 'mixed', int $seed = 1): string
    {
        $words = self::$words ??= array_values(array_filter(explode(' ', implode(' ', self::lines('en')))));
        // One LCG step per piece of output. Its low bits repeat quickly, so every decision takes
        // its own range of higher bits (>> 4, >> 8, >> 16 below).
        $state = $seed;
        $out = '';
        $entityBytes = 0;
        while (strlen($out) < $bytes) {
            $state = ($state * 1103515245 + 12345) & 0x7fffffff;
            if ($share > 0 && $entityBytes <= $share * strlen($out)) {
                $entity = self::pickEntity($pool, $state);
                $out .= $entity;
                $entityBytes += strlen($entity);
            } else {
                $out .= $words[($state >> 8) % count($words)] . ' ';
            }
        }
        return $out;
    }

    private static function pickEntity(string $pool, int $state): string
    {
        if ($pool === 'mixed') {
            $roll = ($state >> 16) % 10;
            $pool = $roll < 7 ? 'named' : ($roll < 9 ? 'numeric' : 'invalid');
        }
        $entities = self::ENTITY_POOLS[$pool] ?? throw new InvalidArgumentException("unknown entity pool: $pool");
        return $entities[($state >> 4) % count($entities)];
    }

    /**
     * Whole lines of corpus/<name>.txt, repeated until the result has at least $bytes bytes.
     * Lines are never split, so multibyte sequences stay valid in any encoding.
     */
    public static function text(string $name, int $bytes): string
    {
        $lines = self::lines($name);
        $out = '';
        for ($i = 0; strlen($out) < $bytes; $i++) {
            $out .= $lines[$i % count($lines)] . "\n";
        }
        return $out;
    }

    /**
     * Exactly $bytes bytes of corpus/<name>.txt, the file repeated if it is shorter.
     * For files without useful line structure (minified code); may cut a multibyte
     * sequence or an entity at the end.
     */
    public static function slice(string $name, int $bytes): string
    {
        $data = implode("\n", self::lines($name)) . "\n";
        return substr(str_repeat($data, intdiv($bytes, strlen($data)) + 1), 0, $bytes);
    }

    /** @return list<string> lines of corpus/<name>.txt, read once */
    private static function lines(string $name): array
    {
        return self::$lines[$name] ??= self::load($name);
    }

    /** @return list<string> */
    private static function load(string $name): array
    {
        $file = dirname(__DIR__) . "/corpus/$name.txt";
        if (!is_file($file)) {
            $how = str_starts_with($name, 'real/') ? 'corpus/real/fetch.sh' : 'corpus/generate.py';
            throw new MissingCorpus("corpus file not found: $file (run $how)");
        }
        $data = (string) file_get_contents($file);
        return explode("\n", rtrim($data, "\n"));
    }
}
