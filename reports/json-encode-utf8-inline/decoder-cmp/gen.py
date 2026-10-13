#!/usr/bin/env python3
# Builds cmp.c: the UTF-8 case of get_next_char() from html.c as the reference, and
# php_next_utf8_char_inline() from html.h with its fallback pointed at that reference.
#   gen.py <php-src dir> > cmp.c
import re
import sys

src = sys.argv[1]
html_c = open(f'{src}/ext/standard/html.c').read().split('\n')
html_h = open(f'{src}/ext/standard/html.h').read()

start = next(i for i, l in enumerate(html_c) if l.startswith('static inline unsigned int get_next_char('))
case = next(i for i in range(start, len(html_c)) if html_c[i].strip() == 'case cs_utf_8:')
end = next(i for i in range(case, len(html_c)) if html_c[i].strip() == 'case cs_big5:')
body = '\n'.join(html_c[case + 1:end])

m = re.search(r'static zend_always_inline unsigned int php_next_utf8_char_inline\(.*?\n}\n', html_h, re.S)
inline = m.group(0).replace('static zend_always_inline', 'static inline')

print(r'''#include <assert.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef enum { SUCCESS = 0, FAILURE = -1 } zend_result;
#define EXPECTED(x) __builtin_expect(!!(x), 1)
#define UNEXPECTED(x) __builtin_expect(!!(x), 0)
#define ZEND_ASSERT(x) assert(x)
#define MB_FAILURE(pos, advance) do { *cursor = pos + (advance); *status = FAILURE; return 0; } while (0)
#define CHECK_LEN(pos, chars_need) ((str_len - (pos)) >= (chars_need))
#define utf8_lead(c)  ((c) < 0x80 || ((c) >= 0xC2 && (c) <= 0xF4))
#define utf8_trail(c) ((c) >= 0x80 && (c) <= 0xBF)

static unsigned int php_next_utf8_char(const unsigned char *str, size_t str_len, size_t *cursor, zend_result *status)
{
	size_t pos = *cursor;
	unsigned int this_char = 0;

	*status = SUCCESS;
	assert(pos <= str_len);

	if (!CHECK_LEN(pos, 1))
		MB_FAILURE(pos, 1);

	switch (0) {
	case 0:''')
print(body)
print(r'''	}

	*cursor = pos;
	return this_char;
}
''')
print(inline)
print(r'''
static unsigned long long calls, diffs;

static void check(const unsigned char *s, size_t len, size_t start)
{
	size_t c1 = start, c2 = start;
	zend_result s1 = SUCCESS, s2 = SUCCESS;
	unsigned int v1 = php_next_utf8_char(s, len, &c1, &s1);
	unsigned int v2 = php_next_utf8_char_inline(s, len, &c2, &s2);
	calls++;
	if (v1 != v2 || c1 != c2 || s1 != s2) {
		if (diffs++ < 10) {
			printf("diff len=%zu start=%zu bytes=", len, start);
			for (size_t i = 0; i < len; i++) printf("%02x", s[i]);
			printf(" ref=%u/%zu/%d inline=%u/%zu/%d\n", v1, c1, s1, v2, c2, s2);
		}
	}
}

int main(void)
{
	unsigned char buf[6];

	/* every sequence of up to four bytes with a lead byte 80..FF, every prefix length,
	 * at cursor 0 and after one ASCII byte */
	for (unsigned a = 0x80; a <= 0xff; a++) {
		for (unsigned b = 0; b < 256; b++) {
			for (unsigned c = 0; c < 256; c++) {
				for (unsigned d = 0; d < 256; d++) {
					buf[0] = 'x'; buf[1] = a; buf[2] = b; buf[3] = c; buf[4] = d; buf[5] = 'y';
					check(buf + 1, 4, 0);
					check(buf, 6, 1);
				}
				buf[1] = a; buf[2] = b; buf[3] = c;
				check(buf + 1, 3, 0);
			}
			buf[1] = a; buf[2] = b;
			check(buf + 1, 2, 0);
		}
		buf[1] = a;
		check(buf + 1, 1, 0);
	}
	for (unsigned a = 0; a < 0x80; a++) {
		buf[0] = a;
		check(buf, 1, 0);
	}
	buf[0] = 'x';
	check(buf, 1, 1);
	printf("calls %llu diffs %llu\n", calls, diffs);
	return diffs != 0;
}
''')
