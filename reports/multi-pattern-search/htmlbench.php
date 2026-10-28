<?php

use Str\Replacer;

/*
 * HTML named-entity decode: Str\Replacer vs the native html_entity_decode vs strtr.
 * The decode map (entity -> char) comes from PHP itself; the text uses only named
 * entities so all three agree. html_entity_decode carries a generated static table in
 * the binary; Str\Replacer builds its automaton at runtime (no binary bloat, pays a build).
 *
 * Usage: php -dextension=strmatch.so htmlbench.php <mode> <bytes> <rate%> <K> [seed]
 *   mode: check | native | strtr | ext | build_ext
 */

$mode = $argv[1] ?? 'ext';
$bytes = (int) ($argv[2] ?? 16384);
$rate = (int) ($argv[3] ?? 25);   // probability (%) that a generated token is an entity
$K = (int) ($argv[4] ?? 0);
$seed = (int) ($argv[5] ?? 5);

$table = get_html_translation_table(HTML_ENTITIES, ENT_QUOTES | ENT_HTML5, 'UTF-8');
$decode = array_flip($table);     // "&name;" => char
$ents = array_keys($decode);
$ne = count($ents);

mt_srand($seed);
$txt = '';
while (strlen($txt) < $bytes) {
    if (mt_rand(0, 99) < $rate) {
        $txt .= $ents[mt_rand(0, $ne - 1)];
    } else {
        $txt .= 'word'.mt_rand(0, 9).' ';
    }
}
$txt = substr($txt, 0, $bytes);

if ('check' === $mode) {
    $native = html_entity_decode($txt, ENT_QUOTES | ENT_HTML5, 'UTF-8');
    $str = strtr($txt, $decode);
    $ext = (new Replacer($decode))->replace($txt);
    $ok = ($native === $str) && ($native === $ext);

    // The rate above is a per-token probability, not the entity share of the bytes;
    // report the real byte share so the table labels are not mistaken for it.
    $ent_bytes = 0;
    foreach ($ents as $e) {
        $o = 0;
        while (($p = strpos($txt, $e, $o)) !== false) {
            $ent_bytes += strlen($e);
            $o = $p + strlen($e);
        }
    }
    $share = 100.0 * $ent_bytes / max(1, strlen($txt));
    printf(
        "entities=%d bytes=%d rate=%d%% entity-byte-share=%.1f%% : native==strtr==ext %s\n",
        $ne,
        strlen($txt),
        $rate,
        $share,
        $ok ? 'OK' : 'DIFF'
    );

    exit($ok ? 0 : 1);
}

$sink = 0;

switch ($mode) {
    case 'native':
        for ($i = 0; $i < $K; ++$i) {
            $sink += strlen(html_entity_decode($txt, ENT_QUOTES | ENT_HTML5, 'UTF-8'));
        }

        break;

    case 'strtr':
        for ($i = 0; $i < $K; ++$i) {
            $sink += strlen(strtr($txt, $decode));
        }

        break;

    case 'ext':
        $r = new Replacer($decode);
        for ($i = 0; $i < $K; ++$i) {
            $sink += strlen($r->replace($txt));
        }

        break;

    case 'build_ext':
        for ($i = 0; $i < $K; ++$i) {
            $r = new Replacer($decode);
            ++$sink;
        }

        break;

    default:
        fwrite(STDERR, "unknown mode\n");

        exit(2);
}

echo $sink, "\n";
