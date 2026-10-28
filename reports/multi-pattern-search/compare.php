<?php
/* Compare every available multi-pattern approach, search and replace, in one harness.
 * Construct the structure once, then run K ops; measure at K and K=0 (build only),
 * subtract, divide by K. Mode `check` runs all once and asserts the equivalences.
 *
 * Usage: php -dextension=strmatch.so compare.php <mode> <N> <S> <K> [seed]
 *   search:  strpos | preg | phpac | ext_matches | ext_count | ext_getkw | ext_matchall
 *   replace: str_replace | strtr | preg_replace | phpac_replace | ext_replace
 *   build:   build_preg | build_phpac | build_phpac_r | build_ext_m | build_ext_r
 *   check:   run all, assert equivalences, print
 */

require __DIR__ . '/vendor/aho-corasick/src/MultiStringMatcher.php';
require __DIR__ . '/vendor/aho-corasick/src/MultiStringReplacer.php';
use AhoCorasick\MultiStringMatcher;
use AhoCorasick\MultiStringReplacer;

function gen_dict(int $n, int $seed): array {
    mt_srand($seed); $w=[]; $seen=[];
    while (count($w) < $n) { $l=mt_rand(4,12); $s=''; for($i=0;$i<$l;$i++)$s.=chr(mt_rand(97,122)); if(isset($seen[$s]))continue; $seen[$s]=1; $w[]=$s; }
    return $w;
}
function gen_text(int $bytes, array $d, int $seed): string {
    mt_srand($seed ^ 0x5a5a); $n=count($d); $o='';
    while (strlen($o) < $bytes) { if(mt_rand(0,99)<8){$o.=$d[mt_rand(0,$n-1)].' ';} else {$l=mt_rand(2,10);for($i=0;$i<$l;$i++)$o.=chr(mt_rand(97,122));$o.=' ';} }
    return substr($o,0,$bytes);
}

/* presence set (sorted) via the strpos oracle */
function presence_strpos(string $t, array $dict): array { $r=[]; foreach($dict as $w) if(str_contains($t,$w))$r[]=$w; sort($r); return $r; }

/* alternation sorted longest-first so PCRE picks the longest match */
function build_preg_pat(array $keys): string {
    usort($keys, fn($a,$b)=>strlen($b)<=>strlen($a));
    return '/'.implode('|', array_map('preg_quote', $keys)).'/';
}

$mode=$argv[1]??'check'; $N=(int)($argv[2]??500); $S=(int)($argv[3]??16384);
$K=(int)($argv[4]??0); $seed=(int)($argv[5]??1);

$dict=gen_dict($N,$seed);
$map=[]; foreach($dict as $i=>$w) $map[$w]='<'.($i%7).'>';
$text=gen_text($S,$dict,$seed);

if ($mode==='check') {
    $fail = 0; // non-zero exit on any UNEXPECTED mismatch
    // mark a hard-required equality; a real DIFF fails the run
    $req = function(string $label, bool $ok) use (&$fail) { printf("  %-24s %s\n", $label, $ok?'OK':'DIFF'); if(!$ok)$fail++; };

    // search presence: strpos oracle vs preg vs phpac vs ext getMatchedKeywords
    $oracle=presence_strpos($text,$dict);
    $pat=build_preg_pat($dict);
    $preg_raw = @preg_match_all($pat,$text,$mm); // false if the pattern is too large
    printf("search presence (N=%d S=%d present=%d):\n", $N,$S,count($oracle));
    if ($preg_raw === false) {
        printf("  %-24s %s\n", 'preg  == strpos', 'UNSUPPORTED (pattern did not compile)');
    } else {
        $preg=array_values(array_unique($mm[0])); sort($preg);
        $req('preg  == strpos', $preg===$oracle);
    }
    $ac=new MultiStringMatcher($dict); $acp=array_keys(array_flip(array_column($ac->searchIn($text),1))); sort($acp);
    $ext=(new Str\Matcher($dict))->getMatchedKeywords($text); sort($ext);
    $req('phpac == strpos', $acp===$oracle);
    $req('ext   == strpos', $ext===$oracle);

    // replace: strtr is the leftmost-longest oracle; ext and phpac must match it
    $o_strtr=strtr($text,$map);
    $ext_r=(new Str\Replacer($map))->replace($text);
    $ac_r=(new MultiStringReplacer($map))->searchAndReplace($text);
    $keys=$dict; usort($keys, fn($a,$b)=>strlen($b)<=>strlen($a)); $vals=array_map(fn($k)=>$map[$k], $keys);
    $o_strrep=str_replace($keys,$vals,$text);
    printf("replace (leftmost-longest oracle = strtr):\n");
    $req('ext_replace   == strtr', $ext_r===$o_strtr);
    $req('phpac_replace == strtr', $ac_r===$o_strtr);
    if ($preg_raw === false) {
        printf("  %-24s %s\n", 'preg_replace  == strtr', 'UNSUPPORTED (pattern did not compile)');
    } else {
        $o_preg=preg_replace_callback($pat, fn($m)=>$map[$m[0]], $text);
        $req('preg_replace  == strtr', $o_preg===$o_strtr);
    }
    // str_replace has cascading semantics: a difference is allowed, reported not failed
    printf("  %-24s %s\n", 'str_replace   == strtr', $o_strrep===$o_strtr?'OK':'differs (cascading semantics, expected)');
    exit($fail ? 1 : 0);
}

$sink=0;
switch ($mode) {
    /* ---- search, construct once + K ops ---- */
    case 'strpos':      for($i=0;$i<$K;$i++){$c=0;foreach($dict as $w)if(str_contains($text,$w))$c++;$sink+=$c;} break;
    case 'preg':        $p=build_preg_pat($dict); for($i=0;$i<$K;$i++){$sink+=preg_match_all($p,$text,$m)?count($m[0]):0;} break;
    case 'phpac':       $o=new MultiStringMatcher($dict); for($i=0;$i<$K;$i++)$sink+=count($o->searchIn($text)); break;
    case 'ext_matches': $o=new Str\Matcher($dict); for($i=0;$i<$K;$i++)$sink+=$o->matches($text)?1:0; break;
    case 'ext_count':   $o=new Str\Matcher($dict); for($i=0;$i<$K;$i++)$sink+=$o->countMatches($text); break;
    case 'ext_getkw':   $o=new Str\Matcher($dict); for($i=0;$i<$K;$i++)$sink+=count($o->getMatchedKeywords($text)); break;
    case 'ext_matchall':$o=new Str\Matcher($dict); for($i=0;$i<$K;$i++)$sink+=count($o->matchAll($text)); break;
    /* ---- replace, construct once + K ops ---- */
    case 'str_replace': $keys=$dict; usort($keys,fn($a,$b)=>strlen($b)<=>strlen($a)); $vals=array_map(fn($k)=>$map[$k],$keys);
                        for($i=0;$i<$K;$i++)$sink+=strlen(str_replace($keys,$vals,$text)); break;
    case 'strtr':       for($i=0;$i<$K;$i++)$sink+=strlen(strtr($text,$map)); break;
    case 'preg_replace':$p=build_preg_pat($dict); for($i=0;$i<$K;$i++)$sink+=strlen(preg_replace_callback($p,fn($m)=>$map[$m[0]],$text)); break;
    case 'phpac_replace':$o=new MultiStringReplacer($map); for($i=0;$i<$K;$i++)$sink+=strlen($o->searchAndReplace($text)); break;
    case 'ext_replace': $o=new Str\Replacer($map); for($i=0;$i<$K;$i++)$sink+=strlen($o->replace($text)); break;
    /* ---- build only, K times ---- */
    case 'build_preg':    for($i=0;$i<$K;$i++)$sink+=strlen(build_preg_pat($dict)); break;
    case 'build_phpac':   for($i=0;$i<$K;$i++)$sink+=count((new MultiStringMatcher($dict))->getKeywords()); break;
    case 'build_phpac_r': for($i=0;$i<$K;$i++){$o=new MultiStringReplacer($map);$sink++;} break;
    case 'build_ext_m':   for($i=0;$i<$K;$i++)$sink+=count((new Str\Matcher($dict))->getKeywords()); break;
    case 'build_ext_r':   for($i=0;$i<$K;$i++){$o=new Str\Replacer($map);$sink++;} break;
    default: fwrite(STDERR,"unknown mode $mode\n"); exit(2);
}
echo $sink,"\n";
