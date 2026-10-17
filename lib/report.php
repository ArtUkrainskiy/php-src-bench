<?php
/*
 * `bench report new|update|check`: a report directory under reports/ that a pull request can
 * link to, made from a `bench compare` series, and the checks to run before committing it.
 *
 * Tables in a report's Markdown files are generated, never typed: a block
 *
 *   <!-- bench-table compare.json --labels labels.txt --full -->
 *   ...
 *   <!-- /bench-table -->
 *
 * holds the output of `bench table` with those arguments (paths relative to the Markdown file);
 * `update` rewrites the blocks, `check` fails when one differs from what the series gives.
 */
declare(strict_types=1);

const TABLE_BLOCK = '/^<!-- bench-table (.+?) -->\n(.*?)^<!-- \/bench-table -->$/ms';

function usage_report(): void
{
    echo <<<'USAGE'
    Usage: bench report new <dir> --series <series.json> [--labels FILE] [--title TEXT] [--force]
           bench report update <dir>
           bench report check <dir>

      new     a report directory: README.md with the sections a review needs, the tables of the
              series in generated blocks, a Reproduce section made from the series, and copies
              of the series, its suite and the labels without paths of this machine
      update  regenerate every bench-table block of the Markdown files in <dir>, and remove
              the paths of this machine from the JSON files (saved results and series)
      check   before committing: paths of this machine, Cyrillic in Markdown, broken relative
              links and anchors, tables that differ from their series, TODO left in the text,
              builds of working-tree snapshots that nobody else can check out

    USAGE;
}

function cmd_report(array $positional, array $options): int
{
    [$what, $dir] = [$positional[0] ?? '', $positional[1] ?? ''];
    if (isset($options['help']) || $dir === '' || !in_array($what, ['new', 'update', 'check'], true)) {
        usage_report();
        return isset($options['help']) ? 0 : 2;
    }
    $dir = rtrim($dir, '/');
    if ($what === 'new') {
        report_new($dir, $options);
        echo "wrote $dir/README.md: fill in the TODOs, then run `bench report check $dir`\n";
        return 0;
    }
    if (!is_dir($dir)) {
        throw new BenchError("no such directory: $dir");
    }
    if ($what === 'update') {
        // Saved results and series name the binaries and the suite by their paths on this machine.
        foreach (glob("$dir/*.json") ?: [] as $file) {
            $text = (string) file_get_contents($file);
            $new = report_sanitize($text);
            if ($new !== $text) {
                file_put_contents($file, $new);
                echo "removed paths of this machine from $file\n";
            }
        }
        foreach (glob("$dir/*.md") ?: [] as $file) {
            $text = (string) file_get_contents($file);
            $new = report_render_blocks($text, dirname($file));
            if ($new !== $text) {
                file_put_contents($file, $new);
                echo "updated $file\n";
            }
        }
        return 0;
    }
    [$errors, $warnings] = report_check($dir);
    foreach ($warnings as $w) {
        warn($w);
    }
    foreach ($errors as $e) {
        fwrite(STDERR, "error: $e\n");
    }
    echo $errors ? count($errors) . " problem(s) in $dir\n" : "$dir: no problems found\n";
    return $errors ? 1 : 0;
}

/* ---------------------------------------------------------------- new */

function report_new(string $dir, array $options): void
{
    $seriesFile = (string) ($options['series'] ?? throw new BenchError('bench report new needs --series <series.json>'));
    $series = json_decode((string) @file_get_contents($seriesFile), true);
    if (!is_array($series) || ($series['kind'] ?? '') !== 'compare') {
        throw new BenchError("not a series from `bench compare`: $seriesFile");
    }
    if (is_file("$dir/README.md") && !isset($options['force'])) {
        throw new BenchError("$dir/README.md exists; use `bench report update` for its tables, or --force to start over");
    }
    @mkdir($dir, 0777, true);

    // The suite goes next to the series, which then names it without a directory.
    $suite = (string) $series['suite'];
    $suiteName = basename($suite);
    if (is_file($suite)) {
        copy($suite, "$dir/$suiteName");
    } else {
        warn("the suite of the series is not at $suite any more: copy it into $dir by hand");
    }
    $series['suite'] = $suiteName;
    $seriesName = basename($seriesFile);
    file_put_contents("$dir/$seriesName", report_sanitize(json_encode($series, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR)) . "\n");
    $tableArgs = $seriesName;
    if (isset($options['labels'])) {
        $labels = basename((string) $options['labels']);
        copy((string) $options['labels'], "$dir/$labels");
        $tableArgs .= " --labels $labels";
    }

    $title = (string) ($options['title'] ?? 'TODO: what changes, e.g. "mb_substr() fast path (php-src PR NNNNN)"');
    $date = date('j F Y', strtotime((string) $series['date']) ?: time());
    $machine = $series['env']['cpu_model'] ?? 'an unknown CPU';
    $readme = <<<MD
    # $title

    TODO: one paragraph: which change, which commits (link them), what the report measures. Measured on $date on $machine.

    ## Summary

    - TODO: the result in one line per finding, with numbers: what got faster, what got slower, what was not checked.

    ## Results

    Change in CPU cycles per call relative to A (negative = fewer cycles, faster); median over the passes of B against A of the same pass.

    <!-- bench-table $tableArgs --header -->
    <!-- /bench-table -->

    Full table, with the range over the passes and the change in instructions:

    <!-- bench-table $tableArgs --full -->
    <!-- /bench-table -->

    ## Code

    TODO: what the change does, how it was read, what could be simpler or faster (with numbers or "not measured").

    ## Tests

    TODO: what was compared with master (`bench difftest`, sanitizers), which inputs, what the tests of the PR cover.

    ## Reproduce

    {REPRODUCE}

    MD;
    $readme = str_replace('{REPRODUCE}', report_reproduce($series, $dir, $seriesName, $tableArgs), $readme);
    file_put_contents("$dir/README.md", report_render_blocks($readme, $dir));
}

/** Text without the paths of this machine: builds, the tool's directory, the home directory. */
function report_sanitize(string $text): string
{
    $replace = [BENCH_BUILDS => '<builds>', BENCH_ROOT => '.'];
    if (($src = getenv('PHP_SRC')) !== false && $src !== '') {
        $replace[rtrim($src, '/')] = '<php-src>';
    }
    if (($home = getenv('HOME')) !== false && strlen($home) > 1) {
        $replace[rtrim($home, '/')] = '~';
    }
    // JSON escapes slashes only without JSON_UNESCAPED_SLASHES; cover both spellings.
    foreach ($replace as $from => $to) {
        $text = str_replace([$from, str_replace('/', '\/', $from)], $to, $text);
    }
    return $text;
}

/** The commands that make the series again, from what the series recorded about its builds. */
function report_reproduce(array $series, string $dir, string $seriesName, string $tableArgs): string
{
    $sets = [];
    $snapshots = [];
    foreach ($series['builds'] as $name => $b) {
        $build = $b['build'] ?? null;
        if ($build === null || !isset($build['commit'], $build['configure'])) {
            $sets["?$name"] = ['line' => "# $name: not made by `bench build`, build it the same way by hand"];
            continue;
        }
        // Built with --cc: <prefix>-gcc13 and so on; otherwise one build with CC=...
        $multi = (bool) preg_match('/^(.+)-(?:gcc|clang)\d+$/', $name, $m);
        $prefix = $multi ? $m[1] : $name;
        $key = $prefix . ' ' . $build['commit'];
        $sets[$key]['prefix'] = $prefix;
        $sets[$key]['commit'] = substr($build['commit'], 0, 11);
        // Builds made before the compiler command was recorded only know the version.
        $sets[$key]['cc'][] = $build['cc_command'] ?? 'TODO(' . (compiler_name($build) ?? $build['cc']) . ')';
        $profile = preg_replace('/ \(.*$/', '', $build['profile'] ?? report_profile_of((string) ($build['cflags_user'] ?? '')));
        $sets[$key]['profile'] = $profile;
        $sets[$key]['extra'] = $build['configure_extra'] ?? report_configure_extra((string) $build['configure'], $profile);
        $sets[$key]['slim'] = !empty($build['slim']);
        $sets[$key]['multi'] = $multi;
        $sets[$key]['pr'] = $build['pr'] ?? null;
        $sets[$key]['werror'] = str_contains((string) $build['configure'], '--enable-werror');
        // Flags given by hand instead of the profile's
        $sets[$key]['flags'] = str_contains((string) ($build['profile'] ?? ''), 'overridden')
            ? sprintf('BENCH_CFLAGS=%s BENCH_LDFLAGS=%s ', escapeshellarg((string) $build['cflags_user']), escapeshellarg((string) ($build['ldflags'] ?? '')))
            : '';
        if (!empty($build['snapshot'])) {
            $snapshots[] = substr($build['commit'], 0, 11);
        }
    }
    $lines = [];
    $prDone = [];
    foreach ($sets as $set) {
        if (isset($set['line'])) {
            $lines[] = $set['line'];
            continue;
        }
        // Builds made by bench pr: the merge commit exists only here, bench pr makes it again.
        if (!empty($set['pr'])) {
            $pr = $set['pr'];
            if (!isset($prDone[$pr['number']])) {
                $env = $set['extra'] ? 'BENCH_CONFIGURE_EXTRA=' . escapeshellarg($set['extra']) . ' ' : '';
                $noWerror = $set['profile'] === 'docker' && !$set['werror'] ? ' --no-werror' : '';
                $lines[] = sprintf('%s./bench pr %s --base %s%s%s --profile %s%s --cc %s   # head %s', $env, $pr['number'], $pr['base'],
                    $pr['merged'] === '1' ? '' : ' --no-merge', $set['slim'] ? ' --slim' : '', $set['profile'], $noWerror, implode(',', array_unique($set['cc'])), $pr['head']);
                $prDone[$pr['number']] = true;
            }
            continue;
        }
        $env = ($set['extra'] ? 'BENCH_CONFIGURE_EXTRA=' . escapeshellarg($set['extra']) . ' ' : '') . $set['flags'];
        $noWerror = $set['profile'] === 'docker' && !$set['werror'] ? ' --no-werror' : '';
        $compilers = implode(',', array_unique($set['cc']));
        $lines[] = $set['multi']
            ? sprintf('%s./bench build%s --profile %s%s --cc %s %s %s', $env, $set['slim'] ? ' --slim' : '', $set['profile'], $noWerror, $compilers, $set['prefix'], $set['commit'])
            : sprintf('%sCC=%s ./bench build%s --profile %s%s %s %s', $env, $compilers, $set['slim'] ? ' --slim' : '', $set['profile'], $noWerror, $set['prefix'], $set['commit']);
    }
    $groups = [];
    foreach ($series['groups'] as $g) {
        if (!in_array($g['name'], ['aa', 'aa2'], true)) {
            $groups[] = "{$g['name']}={$g['a']}:{$g['b']}";
        }
    }
    $c = $series['config'] ?? [];
    $opts = '';
    foreach (['passes' => 5, 'target_ms' => 50] as $k => $default) {
        if (isset($c[$k]) && $c[$k] != $default) {
            $opts .= ' --' . str_replace('_', '-', $k) . " {$c[$k]}";
        }
    }
    if (!empty($c['filter'])) {
        $opts .= ' --filter ' . escapeshellarg((string) $c['filter']);
    }
    if (isset($c['control']) && !$c['control']) {
        $opts .= ' --no-control';
    }
    $rel = report_repo_path($dir);
    $lines[] = "./bench compare $rel/{$series['suite']} " . implode(' ', $groups) . $opts;
    $lines[] = "./bench table results/<date>-compare-" . basename((string) $series['suite'], '.php') . '.json '
        . preg_replace('/(\S+\.txt)/', "$rel/\$1", str_replace($seriesName . ' ', '', $tableArgs . ' ')) . '--full';
    $text = "From the root of [php-src-bench](https://github.com/ArtUkrainskiy/php-src-bench), with php-src next to it:\n\n```\n"
        . implode("\n", $lines) . "\n```\n\nThe series in this report: [`$seriesName`]($seriesName); `bench table $seriesName` renders it.";
    if ($snapshots) {
        $text .= "\n\nTODO: " . implode(', ', array_unique($snapshots)) . ' is a snapshot of a working tree that only this machine has: push it as a branch and name the branch here.';
    }
    return $text;
}

/** The profile whose flags a build without a recorded profile used, or "align" (the old default). */
function report_profile_of(string $cflags): string
{
    if (str_contains($cflags, '-fstack-protector-strong')) {
        return 'docker';
    }
    if (str_contains($cflags, '-falign-functions')) {
        return 'align';
    }
    return $cflags === '-O2 -g' ? 'plain' : 'align';
}

/** The options BENCH_CONFIGURE_EXTRA added: the configure line without the fixed ones and the profile's. */
function report_configure_extra(string $configure, string $profile): string
{
    $fixed = ['--disable-all', '--disable-cgi', '--disable-phpdbg', '--enable-cli'];
    $fixed = array_merge($fixed, [
        'docker' => ['--enable-werror'],
        'asan' => ['--enable-debug', '--enable-address-sanitizer', '--enable-undefined-sanitizer'],
    ][$profile] ?? []);
    return implode(' ', array_diff(preg_split('/\s+/', trim($configure)) ?: [], $fixed));
}

/** The report directory relative to the repository root, or as given when it is elsewhere. */
function report_repo_path(string $dir): string
{
    $real = realpath($dir) ?: $dir;
    return str_starts_with($real, BENCH_ROOT . '/') ? substr($real, strlen(BENCH_ROOT) + 1) : $dir;
}

/* ---------------------------------------------------------------- tables */

/** $text with every bench-table block filled with what `bench table` prints for its arguments. */
function report_render_blocks(string $text, string $baseDir): string
{
    return (string) preg_replace_callback(TABLE_BLOCK, static function (array $m) use ($baseDir): string {
        return "<!-- bench-table {$m[1]} -->\n" . report_table($m[1], $baseDir) . "<!-- /bench-table -->";
    }, $text);
}

/** The output of `bench table <args>`, with paths in the arguments relative to $baseDir. */
function report_table(string $args, string $baseDir): string
{
    $words = preg_split('/\s+/', trim($args)) ?: [];
    $file = "$baseDir/" . array_shift($words);
    $series = json_decode((string) @file_get_contents($file), true);
    if (!is_array($series) || ($series['kind'] ?? '') !== 'compare') {
        throw new BenchError("bench-table block: not a series: $file");
    }
    if (array_key_exists('complete', $series) && !$series['complete']) {
        throw new BenchError("bench-table block: $file is incomplete (interrupted); finish it with bench compare --resume");
    }
    $labels = [];
    $flags = [];
    $baseName = 'master';
    for ($i = 0; $i < count($words); $i++) {
        $w = $words[$i];
        if ($w === '--labels') {
            $labelsFile = "$baseDir/" . ($words[++$i] ?? '');
            $lines = is_file($labelsFile) ? file($labelsFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) : false;
            if (!$lines) {
                throw new BenchError("bench-table block: cannot read the labels $labelsFile");
            }
            $labels = parse_labels($lines, array_keys($series['cases'] ?? []));
        } elseif ($w === '--base-name') {
            $baseName = $words[++$i] ?? 'master';
        } elseif (in_array($w, ['--full', '--bpc', '--header'], true)) {
            $flags[$w] = true;
        } else {
            throw new BenchError("bench-table block: unknown argument '$w'");
        }
    }
    foreach (array_keys($labels) as $id) {
        if (!isset($series['cases'][$id])) {
            throw new BenchError("bench-table block: the labels name '$id', which the series does not have");
        }
    }
    $out = isset($flags['--header']) ? series_header($series) . "\n" : '';
    $out .= series_table($series, $labels, isset($flags['--full']), $baseName, isset($flags['--bpc']));
    // What was wrong with the builds or results stays with the numbers.
    foreach ($series['warnings'] ?? [] as $warning) {
        $out .= "\nWarning: $warning\n";
    }
    return $out;
}

/* ---------------------------------------------------------------- check */

/** @return array{list<string>, list<string>} errors and warnings */
function report_check(string $dir): array
{
    $errors = [];
    $warnings = [];
    $files = [];
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir, FilesystemIterator::SKIP_DOTS));
    foreach ($iterator as $f) {
        if ($f->isFile() && $f->getSize() < 20_000_000) {
            $files[] = $f->getPathname();
        }
    }
    sort($files);
    $personal = report_personal_patterns();
    foreach ($files as $file) {
        $text = (string) file_get_contents($file);
        if (str_contains($text, "\0")) {
            continue; // binary
        }
        foreach ($personal as $pattern) {
            if (preg_match($pattern, $text, $m, PREG_OFFSET_CAPTURE)) {
                $line = substr_count($text, "\n", 0, $m[0][1]) + 1;
                $errors[] = "$file:$line: a path of this machine: {$m[0][0]}";
            }
        }
        if (str_ends_with($file, '.json')) {
            $series = json_decode($text, true);
            foreach ((is_array($series) ? $series['builds'] ?? [] : []) as $name => $b) {
                if (!empty($b['build']['snapshot'])) {
                    $warnings[] = "$file: build $name is a working-tree snapshot (" . substr($b['build']['commit'], 0, 11) . '): nobody else can check it out';
                }
            }
        }
        if (!str_ends_with($file, '.md')) {
            continue;
        }
        if (preg_match('/\p{Cyrillic}/u', $text, $m, PREG_OFFSET_CAPTURE)) {
            $errors[] = "$file:" . (substr_count($text, "\n", 0, $m[0][1]) + 1) . ': Cyrillic text in a public report';
        }
        if (preg_match_all('/\bTODO\b/', $text, $all, PREG_OFFSET_CAPTURE)) {
            $errors[] = "$file:" . (substr_count($text, "\n", 0, $all[0][0][1]) + 1) . ': ' . count($all[0]) . ' TODO left';
        }
        $errors = array_merge($errors, report_check_links($file, $text));
        // A marker spelled differently is not a block: the table in it would never be checked.
        $blocks = preg_match_all(TABLE_BLOCK, $text);
        if (substr_count($text, 'bench-table') !== 2 * $blocks) {
            $errors[] = "$file: a bench-table marker that is not a complete block (" . substr_count($text, 'bench-table') . " markers, $blocks blocks)";
        }
        try {
            if (report_render_blocks($text, dirname($file)) !== $text) {
                $errors[] = "$file: a bench-table block differs from its series (bench report update)";
            }
        } catch (BenchError $e) {
            $errors[] = "$file: " . $e->getMessage();
        }
    }
    return [$errors, $warnings];
}

/** Regular expressions for paths that only exist on this machine. */
function report_personal_patterns(): array
{
    $patterns = ['#/home/[a-z_][a-z0-9_.-]*/#', '#/Users/[A-Za-z0-9_.-]+/#', '#[A-Z]:\\\\Users\\\\#'];
    // The same directories spelled from the home directory: ~/projects/php-builds in a script.
    $home = getenv('HOME') ?: '';
    $parent = dirname(BENCH_ROOT);
    if (strlen($home) > 1 && str_starts_with($parent, rtrim($home, '/') . '/')) {
        $patterns[] = '#(~|\$HOME|\$\{HOME\})' . preg_quote(substr($parent, strlen(rtrim($home, '/'))), '#') . '\b#';
    }
    foreach ([BENCH_BUILDS, getenv('PHP_SRC') ?: null] as $path) {
        if ($path) {
            $patterns[] = '#' . preg_quote(rtrim($path, '/'), '#') . '#';
        }
    }
    return $patterns;
}

/** Relative links of a Markdown file whose target or anchor does not exist. */
function report_check_links(string $file, string $text): array
{
    $errors = [];
    $prose = (string) preg_replace('/^```.*?^```/ms', '', $text); // links in code blocks are not links
    $anchors = static function (string $md): array {
        $slugs = [];
        $md = (string) preg_replace('/^```.*?^```/ms', '', $md); // a "#" line in a code block is no heading
        $seen = [];
        foreach (preg_match_all('/^#{1,6} (.+)$/m', $md, $m) ? $m[1] : [] as $heading) {
            // GitHub: lower case, punctuation dropped, spaces to "-", "-1", "-2" for repeats
            $slug = str_replace(' ', '-', (string) preg_replace('/[^\p{L}\p{N} _-]/u', '', ascii_lower(trim($heading))));
            $slugs[] = isset($seen[$slug]) ? $slug . '-' . $seen[$slug] : $slug;
            $seen[$slug] = ($seen[$slug] ?? 0) + 1;
        }
        return $slugs;
    };
    preg_match_all('/\[[^\]]*\]\(([^)\s]+)\)/', $prose, $links);
    foreach (array_unique($links[1]) as $link) {
        if (preg_match('#^[a-z]+:#i', $link)) {
            continue; // https:, mailto:
        }
        [$path, $anchor] = array_pad(explode('#', $link, 2), 2, null);
        $target = $path === '' ? $file : dirname($file) . '/' . rawurldecode($path);
        if (!file_exists($target)) {
            $errors[] = "$file: broken link ($link)";
        } elseif ($anchor !== null && $anchor !== '' && str_ends_with($target, '.md')
            && !in_array($anchor, $anchors((string) file_get_contents($target)), true)) {
            $errors[] = "$file: no heading for the anchor in ($link)";
        }
    }
    return $errors;
}

/** Lowercase of ASCII letters only: the tool must run without mbstring. */
function ascii_lower(string $s): string
{
    return strtr($s, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz');
}
