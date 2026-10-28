<?php
/* HTML named-entity decode: Str\Replacer vs the native html_entity_decode vs strtr.
 * The decode map (entity -> char) comes from PHP itself. Named-only text so all three
 * agree. html_entity_decode carries a generated static table in the binary; Str\Replacer
 * builds its automaton at runtime (no binary bloat, pays a build).
 * Usage: php -dextension=strmatch.so htmlbench.php <mode> <bytes> <density%> <K> [seed]
 *   mode: native | strtr | ext | build_ext */

$mode=$argv[1]??'ext'; $BYTES=(int)($argv[2]??16384); $DENS=(int)($argv[3]??25);
$K=(int)($argv[4]??0); $seed=(int)($argv[5]??5);

$t = get_html_translation_table(HTML_ENTITIES, ENT_QUOTES | ENT_HTML5, 'UTF-8');
$decode = array_flip($t);                 // "&name;" => char
$ents = array_keys($decode);
$ne = count($ents);

mt_srand($seed);
$txt = '';
while (strlen($txt) < $BYTES) {
    if (mt_rand(0, 99) < $DENS) $txt .= $ents[mt_rand(0, $ne - 1)];
    else $txt .= 'word' . mt_rand(0, 9) . ' ';
}
$txt = substr($txt, 0, $BYTES);

$sink = 0;
switch ($mode) {
    case 'native':    for ($i=0;$i<$K;$i++) $sink += strlen(html_entity_decode($txt, ENT_QUOTES | ENT_HTML5, 'UTF-8')); break;
    case 'strtr':     for ($i=0;$i<$K;$i++) $sink += strlen(strtr($txt, $decode)); break;
    case 'ext':       $r = new Str\Replacer($decode); for ($i=0;$i<$K;$i++) $sink += strlen($r->replace($txt)); break;
    case 'build_ext': for ($i=0;$i<$K;$i++) { $r = new Str\Replacer($decode); $sink++; } break;
    default: fwrite(STDERR, "unknown mode\n"); exit(2);
}
echo $sink, "\n";
