<?php
function compact_moderate(string $text, array $terms): int
{
    foreach ($terms as $index => $term) {
        if (str_contains($text, $term)) {
            return $index;
        }
    }
    return -1;
}

function compact_read_record($stream, int $length, string $delimiter)
{
    rewind($stream);
    return stream_get_line($stream, $length, $delimiter);
}
