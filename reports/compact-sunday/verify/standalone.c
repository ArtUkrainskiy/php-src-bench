#define _GNU_SOURCE
#include <stdbool.h>
#include <assert.h>
#include <limits.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <immintrin.h>
#define zend_always_inline inline __attribute__((always_inline))
#define zend_never_inline __attribute__((noinline))
#define ZEND_API
#define ZEND_FASTCALL
#define EXPECTED(x) __builtin_expect(!!(x), 1)
#define UNEXPECTED(x) __builtin_expect(!!(x), 0)
#define ZEND_ASSERT(x) assert(x)
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
static inline unsigned int zend_ulong_ntz(unsigned long n) { return __builtin_ctzl(n); }
static zend_always_inline void base_pre(unsigned int td[], const char *needle, size_t needle_len, int reverse) /* {{{ */ {
	int i;

	for (i = 0; i < 256; i++) {
		td[i] = needle_len + 1;
	}

	if (reverse) {
		for (i = needle_len - 1; i >= 0; i--) {
			td[(unsigned char)needle[i]] = i + 1;
		}
	} else {
		size_t i;

		for (i = 0; i < needle_len; i++) {
			td[(unsigned char)needle[i]] = (int)needle_len - i;
		}
	}
}
/* }}} */

ZEND_API const char* ZEND_FASTCALL base_ex(const char *haystack, const char *needle, size_t needle_len, const char *end) /* {{{ */
{
	unsigned int td[256];
	size_t i;
	const char *p;

	if (needle_len == 0 || (end - haystack) < needle_len) {
		return NULL;
	}

	base_pre(td, needle, needle_len, 0);

	p = haystack;
	end -= needle_len;

	while (p <= end) {
		for (i = 0; i < needle_len; i++) {
			if (needle[i] != p[i]) {
				break;
			}
		}
		if (i == needle_len) {
			return p;
		}
		if (UNEXPECTED(p == end)) {
			return NULL;
		}
		p += td[(unsigned char)(p[needle_len])];
	}

	return NULL;
}
/* }}} */

static zend_always_inline const char *
base_memnstr(const char *haystack, const char *needle, size_t needle_len, const char *end)
{
	const char *p = haystack;
	size_t off_s;

	ZEND_ASSERT(end >= p);

	if (needle_len == 1) {
		return (const char *)memchr(p, *needle, (end-p));
	} else if (UNEXPECTED(needle_len == 0)) {
		return p;
	}

	off_s = (size_t)(end - p);

	if (needle_len > off_s) {
		return NULL;
	}

	if (EXPECTED(off_s < 1024 || needle_len < 9)) {	/* glibc memchr is faster when needle is too short */
		const char ne = needle[needle_len-1];
		end -= needle_len;

		while (p <= end) {
			if ((p = (const char *)memchr(p, *needle, (end-p+1)))) {
				if (ne == p[needle_len-1] && !memcmp(needle+1, p+1, needle_len-2)) {
					return p;
				}
			} else {
				return NULL;
			}
			p++;
		}

		return NULL;
	} else {
		return base_ex(haystack, needle, needle_len, end);
	}
}

static zend_always_inline void zend_memnstr_ex_pre(unsigned int td[], const char *needle, size_t needle_len, int reverse) /* {{{ */ {
	int i;

	for (i = 0; i < 256; i++) {
		td[i] = needle_len + 1;
	}

	if (reverse) {
		for (i = needle_len - 1; i >= 0; i--) {
			td[(unsigned char)needle[i]] = i + 1;
		}
	} else {
		size_t i;

		for (i = 0; i < needle_len; i++) {
			td[(unsigned char)needle[i]] = (int)needle_len - i;
		}
	}
}
/* }}} */

static zend_never_inline const char* ZEND_FASTCALL zend_memnstr_sunday(const char *haystack, const char *needle, size_t needle_len, const char *end)
{
	unsigned int td[256];
	size_t i;
	const char *p;

	if (needle_len == 0 || (end - haystack) < needle_len) {
		return NULL;
	}

	zend_memnstr_ex_pre(td, needle, needle_len, 0);

	p = haystack;
	end -= needle_len;

	while (p <= end) {
		for (i = 0; i < needle_len; i++) {
			if (needle[i] != p[i]) {
				break;
			}
		}
		if (i == needle_len) {
			return p;
		}
		if (UNEXPECTED(p == end)) {
			return NULL;
		}
		p += td[(unsigned char)(p[needle_len])];
	}

	return NULL;
}

static zend_never_inline const char* ZEND_FASTCALL zend_memnstr_sunday_short(const char *haystack, const char *needle, size_t needle_len, const char *end)
{
	uint8_t td[256];
	size_t i;
	const char *p;

	if (needle_len == 0 || (end - haystack) < needle_len) {
		return NULL;
	}

	/* The dispatcher only sends short needles here, so every
	 * Sunday shift fits in one byte. Avoid filling a 1 KiB table per word. */
	memset(td, (unsigned char)(needle_len + 1), sizeof(td));
	for (i = 0; i < needle_len; i++) {
		td[(unsigned char)needle[i]] = (unsigned char)(needle_len - i);
	}

	p = haystack;
	end -= needle_len;

	while (p <= end) {
		for (i = 0; i < needle_len; i++) {
			if (needle[i] != p[i]) {
				break;
			}
		}
		if (i == needle_len) {
			return p;
		}
		if (UNEXPECTED(p == end)) {
			return NULL;
		}
		p += td[(unsigned char)(p[needle_len])];
	}

	return NULL;
}

ZEND_API const char* ZEND_FASTCALL zend_memnstr_ex(const char *haystack, const char *needle, size_t needle_len, const char *end)
{
	if (EXPECTED(needle_len < 32)) {
		return zend_memnstr_sunday_short(haystack, needle, needle_len, end);
	}
	return zend_memnstr_sunday(haystack, needle, needle_len, end);
}

static zend_always_inline const char *
zend_memnstr(const char *haystack, const char *needle, size_t needle_len, const char *end)
{
	const char *p = haystack;
	size_t off_s;

	ZEND_ASSERT(end >= p);

	if (needle_len == 1) {
		return (const char *)memchr(p, *needle, (end-p));
	} else if (UNEXPECTED(needle_len == 0)) {
		return p;
	}

	off_s = (size_t)(end - p);

	if (needle_len > off_s) {
		return NULL;
	}

	if (EXPECTED(off_s < 1024 || needle_len < 9)) {	/* glibc memchr is faster when needle is too short */
		const char ne = needle[needle_len-1];
		end -= needle_len;

		while (p <= end) {
			if ((p = (const char *)memchr(p, *needle, (end-p+1)))) {
				if (ne == p[needle_len-1] && !memcmp(needle+1, p+1, needle_len-2)) {
					return p;
				}
			} else {
				return NULL;
			}
			p++;
		}

		return NULL;
	} else {
		return zend_memnstr_ex(haystack, needle, needle_len, end);
	}
}


typedef const unsigned char *(*finder)(const unsigned char *, size_t, const unsigned char *, size_t);
static const unsigned char *zend_candidate_find(const unsigned char *h, size_t hl, const unsigned char *n, size_t nl) {
    return (const unsigned char *)zend_memnstr((const char *)h, (const char *)n, nl, (const char *)h + hl);
}
static const unsigned char *base_find(const unsigned char *h, size_t hl, const unsigned char *n, size_t nl) {
    return (const unsigned char *)base_memnstr((const char *)h, (const char *)n, nl, (const char *)h + hl);
}
