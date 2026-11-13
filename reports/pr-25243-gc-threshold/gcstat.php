<?php
// auto_prepend_file: prints wall time, GC stats and peak memory of the process to stderr at shutdown.
$GLOBALS['__gcstat_t0'] = hrtime(true);
register_shutdown_function(static function (): void {
    $s = gc_status();
    fprintf(STDERR, "GCSTAT pid %d wall %.3f gc %.3f runs %d collected %d threshold %d buffer %d peak %.1f\n",
        getmypid(), (hrtime(true) - $GLOBALS['__gcstat_t0']) / 1e9, $s['collector_time'], $s['runs'],
        $s['collected'], $s['threshold'], $s['buffer_size'], memory_get_peak_usage(true) / 2 ** 20);
});
