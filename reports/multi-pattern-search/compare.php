<?php

/*
 * Compare every available multi-pattern approach, search and replace, in one harness.
 * Construct the structure once, then run K operations; measure at K and at K=0 (build
 * only), subtract, divide by K. Mode `check` runs each once and asserts the equivalences.
 *
 * Usage: php -dextension=strmatch.so compare.php <mode> <N> <S> <K> [seed]
 *   search:  strpos | preg | phpac | ext_matches | ext_count | ext_getkw | ext_matchall
 *   replace: str_replace | strtr | preg_replace | phpac_replace | ext_replace
 *   build:   build_preg | build_phpac | build_phpac_r | build_ext_m | build_ext_r
 *   check:   run all once, assert the equivalences, print
 */

require __DIR__.'/vendor/aho-corasick/src/MultiStringMatcher.php';

require __DIR__.'/vendor/aho-corasick/src/MultiStringReplacer.php';

use AhoCorasick\MultiStringMatcher;
use AhoCorasick\MultiStringReplacer;
use Str\Matcher;
use Str\Replacer;

function gen_dict(int $n, int $seed): array
{
    mt_srand($seed);
    $words = [];
    $seen = [];
    while (count($words) < $n) {
        $len = mt_rand(4, 12);
        $w = '';
        for ($i = 0; $i < $len; ++$i) {
            $w .= chr(mt_rand(97, 122));
        }
        if (isset($seen[$w])) {
            continue;
        }
        $seen[$w] = true;
        $words[] = $w;
    }

    return $words;
}

function gen_text(int $bytes, array $dict, int $seed): string
{
    mt_srand($seed ^ 0x5A5A);
    $n = count($dict);
    $out = '';
    while (strlen($out) < $bytes) {
        if (mt_rand(0, 99) < 8) {
            $out .= $dict[mt_rand(0, $n - 1)].' ';
        } else {
            $len = mt_rand(2, 10);
            for ($i = 0; $i < $len; ++$i) {
                $out .= chr(mt_rand(97, 122));
            }
            $out .= ' ';
        }
    }

    return substr($out, 0, $bytes);
}

// Presence set (sorted) via the str_contains oracle.
function presence_strpos(string $text, array $dict): array
{
    $r = [];
    foreach ($dict as $w) {
        if (str_contains($text, $w)) {
            $r[] = $w;
        }
    }
    sort($r);

    return $r;
}

// Alternation sorted longest-first so PCRE picks the longest match.
function build_preg_pat(array $keys): string
{
    usort($keys, fn ($a, $b) => strlen($b) <=> strlen($a));

    return '/'.implode('|', array_map('preg_quote', $keys)).'/';
}

$mode = $argv[1] ?? 'check';
$N = (int) ($argv[2] ?? 500);
$S = (int) ($argv[3] ?? 16384);
$K = (int) ($argv[4] ?? 0);
$seed = (int) ($argv[5] ?? 1);

$dict = gen_dict($N, $seed);
$map = [];
foreach ($dict as $i => $w) {
    $map[$w] = '<'.($i % 7).'>';
}
$text = gen_text($S, $dict, $seed);

if ('check' === $mode) {
    $fail = 0; // non-zero exit on any unexpected mismatch

    // A hard-required equality; a real DIFF fails the run.
    $req = function (string $label, bool $ok) use (&$fail): void {
        printf("  %-24s %s\n", $label, $ok ? 'OK' : 'DIFF');
        if (!$ok) {
            ++$fail;
        }
    };

    // Search presence: str_contains oracle vs preg vs pure-PHP AC vs ext.
    $oracle = presence_strpos($text, $dict);
    $pat = build_preg_pat($dict);
    $preg_raw = @preg_match_all($pat, $text, $mm); // false if the pattern is too large
    printf("search presence (N=%d S=%d present=%d):\n", $N, $S, count($oracle));

    if (false === $preg_raw) {
        printf("  %-24s %s\n", 'preg  == strpos', 'UNSUPPORTED (pattern did not compile)');
    } else {
        // preg_match_all is non-overlapping, so its presence set can legitimately
        // differ (e.g. ['abcd','bc'] on 'abcd' finds only 'abcd'); report, do not fail.
        $preg = array_values(array_unique($mm[0]));
        sort($preg);
        printf("  %-24s %s\n", 'preg  == strpos', $preg === $oracle ? 'OK' : 'differs (preg is non-overlapping)');
    }

    $ac = new MultiStringMatcher($dict);
    $acp = array_keys(array_flip(array_column($ac->searchIn($text), 1)));
    sort($acp);
    $ext = (new Matcher($dict))->getMatchedKeywords($text);
    sort($ext);
    $req('phpac == strpos', $acp === $oracle);
    $req('ext   == strpos', $ext === $oracle);

    // Replace: strtr is the leftmost-longest oracle; ext and the pure-PHP replacer must match.
    $o_strtr = strtr($text, $map);
    $ext_r = (new Replacer($map))->replace($text);
    $ac_r = (new MultiStringReplacer($map))->searchAndReplace($text);

    $keys = $dict;
    usort($keys, fn ($a, $b) => strlen($b) <=> strlen($a));
    $vals = array_map(fn ($k) => $map[$k], $keys);
    $o_strrep = str_replace($keys, $vals, $text);

    printf("replace (leftmost-longest oracle = strtr):\n");
    $req('ext_replace   == strtr', $ext_r === $o_strtr);
    $req('phpac_replace == strtr', $ac_r === $o_strtr);

    if (false === $preg_raw) {
        printf("  %-24s %s\n", 'preg_replace  == strtr', 'UNSUPPORTED (pattern did not compile)');
    } else {
        $o_preg = preg_replace_callback($pat, fn ($m) => $map[$m[0]], $text);
        $req('preg_replace  == strtr', $o_preg === $o_strtr);
    }

    // str_replace cascades, so a difference is allowed: reported, not failed.
    printf("  %-24s %s\n", 'str_replace   == strtr', $o_strrep === $o_strtr ? 'OK' : 'differs (cascading semantics, expected)');

    exit($fail ? 1 : 0);
}

// Measurement: construct the structure once, then run K operations; $sink prevents
// the loop body from being optimized away.
$sink = 0;

switch ($mode) {
    // ---- search ----
    case 'strpos':
        for ($i = 0; $i < $K; ++$i) {
            $c = 0;
            foreach ($dict as $w) {
                if (str_contains($text, $w)) {
                    ++$c;
                }
            }
            $sink += $c;
        }

        break;

    case 'preg':
        $pat = build_preg_pat($dict);
        for ($i = 0; $i < $K; ++$i) {
            $sink += preg_match_all($pat, $text, $m) ? count($m[0]) : 0;
        }

        break;

    case 'phpac':
        $o = new MultiStringMatcher($dict);
        for ($i = 0; $i < $K; ++$i) {
            $sink += count($o->searchIn($text));
        }

        break;

    case 'ext_matches':
        $o = new Matcher($dict);
        for ($i = 0; $i < $K; ++$i) {
            $sink += $o->matches($text) ? 1 : 0;
        }

        break;

    case 'ext_count':
        $o = new Matcher($dict);
        for ($i = 0; $i < $K; ++$i) {
            $sink += $o->countMatches($text);
        }

        break;

    case 'ext_getkw':
        $o = new Matcher($dict);
        for ($i = 0; $i < $K; ++$i) {
            $sink += count($o->getMatchedKeywords($text));
        }

        break;

    case 'ext_matchall':
        $o = new Matcher($dict);
        for ($i = 0; $i < $K; ++$i) {
            $sink += count($o->matchAll($text));
        }

        break;

        // ---- replace ----
    case 'str_replace':
        $keys = $dict;
        usort($keys, fn ($a, $b) => strlen($b) <=> strlen($a));
        $vals = array_map(fn ($k) => $map[$k], $keys);
        for ($i = 0; $i < $K; ++$i) {
            $sink += strlen(str_replace($keys, $vals, $text));
        }

        break;

    case 'strtr':
        for ($i = 0; $i < $K; ++$i) {
            $sink += strlen(strtr($text, $map));
        }

        break;

    case 'preg_replace':
        $pat = build_preg_pat($dict);
        for ($i = 0; $i < $K; ++$i) {
            $sink += strlen(preg_replace_callback($pat, fn ($m) => $map[$m[0]], $text));
        }

        break;

    case 'phpac_replace':
        $o = new MultiStringReplacer($map);
        for ($i = 0; $i < $K; ++$i) {
            $sink += strlen($o->searchAndReplace($text));
        }

        break;

    case 'ext_replace':
        $o = new Replacer($map);
        for ($i = 0; $i < $K; ++$i) {
            $sink += strlen($o->replace($text));
        }

        break;

        // ---- build only, K times ----
    case 'build_preg':
        for ($i = 0; $i < $K; ++$i) {
            $sink += strlen(build_preg_pat($dict));
        }

        break;

    case 'build_phpac':
        for ($i = 0; $i < $K; ++$i) {
            $sink += count((new MultiStringMatcher($dict))->getKeywords());
        }

        break;

    case 'build_phpac_r':
        for ($i = 0; $i < $K; ++$i) {
            $o = new MultiStringReplacer($map);
            ++$sink;
        }

        break;

    case 'build_ext_m':
        for ($i = 0; $i < $K; ++$i) {
            $sink += count((new Matcher($dict))->getKeywords());
        }

        break;

    case 'build_ext_r':
        for ($i = 0; $i < $K; ++$i) {
            $o = new Replacer($map);
            ++$sink;
        }

        break;

    default:
        fwrite(STDERR, "unknown mode {$mode}\n");

        exit(2);
}

echo $sink, "\n";
