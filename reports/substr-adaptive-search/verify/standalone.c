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
#define ZEND_MEMNSTR_GRAM_SAMPLE_SIZE 256
#define ZEND_MEMNSTR_GRAM_MAX_SAMPLE_HITS 8
#define ZEND_MEMNSTR_GRAM_STEP 13
#define ZEND_MEMNSTR_SUNDAY_ACCOUNT_MIN 8
#define ZEND_MEMNSTR_SUNDAY_SAMPLE 16
#define ZEND_MEMNSTR_ADAPTIVE_MIN_NEEDLE 32
#define ZEND_MEMNSTR_ADAPTIVE_MIN_HAYSTACK 8192
#define ZEND_MEMNSTR_ADAPTIVE_MIN_REMAINING 4096

static_assert(ZEND_MEMNSTR_ADAPTIVE_MIN_NEEDLE <= UINT8_MAX,
	"Short Sunday shifts must fit in uint8_t");

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

static zend_never_inline const char* ZEND_FASTCALL zend_memnstr_sunday(const char *haystack, const char *needle, size_t needle_len, const char *end) /* {{{ */
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
/* }}} */

static zend_never_inline const char* ZEND_FASTCALL zend_memnstr_sunday_short(const char *haystack, const char *needle, size_t needle_len, const char *end) /* {{{ */
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
/* }}} */

#if defined(__SSE2__)
/* Byte commonness in typical text (higher = more common = a worse memchr anchor). */
static const unsigned char zend_byte_commonness[256] = {
	1, 1, 1, 1, 1, 1, 1, 1, 1, 40, 50, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	255, 30, 30, 1, 1, 1, 1, 30, 30, 30, 1, 1, 30, 30, 30, 30,
	70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 30, 30, 1, 1, 1, 30,
	1, 95, 40, 55, 60, 115, 45, 42, 75, 85, 10, 22, 65, 47, 82, 90,
	44, 9, 77, 80, 100, 50, 30, 41, 12, 41, 7, 30, 1, 30, 1, 30,
	1, 190, 80, 110, 120, 230, 90, 85, 150, 170, 20, 45, 130, 95, 165, 180,
	88, 18, 155, 160, 200, 100, 60, 83, 25, 82, 15, 30, 1, 30, 1, 1,
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
};

#endif

/* Critical factorization for the Crochemore-Perrin Two-Way search. The suffix
 * is represented by its start, avoiding a signed -1 index and narrowing size_t. */
static size_t zend_memnstr_max_suffix(const unsigned char *needle, size_t length,
		size_t *period, bool reverse)
{
	size_t left = 0, right = 1, offset = 0, p = 1;

	while (offset < length - right) {
		unsigned char a = needle[right + offset], b = needle[left + offset];
		if (reverse ? a > b : a < b) {
			right += offset + 1;
			offset = 0;
			p = right - left;
		} else if (a == b) {
			if (offset + 1 != p) {
				offset++;
			} else {
				right += p;
				offset = 0;
			}
		} else {
			left = right;
			right = left + 1;
			offset = 0;
			p = 1;
		}
	}
	*period = p;
	return left;
}

/* Linear-time fallback. Periodic needles remember the part already compared
 * before a period shift, so repeated prefixes cannot restart quadratic work. */
static const char *zend_memnstr_twoway(const char *haystack, const char *needle,
		size_t needle_len, const char *end)
{
	size_t length = (size_t)(end - haystack);
	if (needle_len > length) {
		return NULL;
	}
	const unsigned char *n = (const unsigned char *)needle;
	size_t p1, p2, cut, period, memory = 0, memory_after_shift;
	size_t c1 = zend_memnstr_max_suffix(n, needle_len, &p1, false);
	size_t c2 = zend_memnstr_max_suffix(n, needle_len, &p2, true);
	if (c1 >= c2) {
		cut = c1;
		period = p1;
	} else {
		cut = c2;
		period = p2;
	}
	if (period <= needle_len - cut && !memcmp(needle, needle + period, cut)) {
		memory_after_shift = needle_len - period;
	} else {
		period = MAX(cut, needle_len - cut) + 1;
		memory_after_shift = 0;
	}

	size_t pos = 0, last = length - needle_len;
	while (pos <= last) {
		size_t i = MAX(cut, memory);
		while (i < needle_len && needle[i] == haystack[pos + i]) {
			i++;
		}
		if (i < needle_len) {
			pos += i - cut + 1;
			memory = 0;
			continue;
		}
		i = cut;
		while (i > memory && needle[i - 1] == haystack[pos + i - 1]) {
			i--;
		}
		if (i <= memory) {
			return haystack + pos;
		}
		pos += period;
		memory = memory_after_shift;
	}
	return NULL;
}

#if defined(__SSE2__)
/* A four-byte anchor can still filter small alphabets after a pair stops
 * paying off. Probe its selectivity before taking this path, and retain the
 * same whole-scan verification budget as the pair. */
static const char *zend_memnstr_gram4(const char *haystack, const char *needle,
		size_t needle_len, const char *end)
{
	size_t length = (size_t)(end - haystack);
	if (needle_len > length) {
		return NULL;
	}
	if (needle_len < 4 || length - needle_len < ZEND_MEMNSTR_GRAM_SAMPLE_SIZE) {
		return zend_memnstr_twoway(haystack, needle, needle_len, end);
	}
	size_t anchor = 0;
	unsigned int best = UINT_MAX;
	for (size_t i = 0; i <= needle_len - 4; i++) {
		unsigned int rank = zend_byte_commonness[(unsigned char)needle[i]]
				+ zend_byte_commonness[(unsigned char)needle[i + 1]]
				+ zend_byte_commonness[(unsigned char)needle[i + 2]]
				+ zend_byte_commonness[(unsigned char)needle[i + 3]];
		if (rank < best) {
			best = rank;
			anchor = i;
		}
	}
	uint32_t gram;
	memcpy(&gram, needle + anchor, sizeof gram);
	size_t candidates = 0;
	for (size_t i = 0; i < ZEND_MEMNSTR_GRAM_SAMPLE_SIZE; i++) {
		uint32_t word;
		memcpy(&word, haystack + i + anchor, sizeof word);
		candidates += word == gram;
	}
	if (candidates > ZEND_MEMNSTR_GRAM_MAX_SAMPLE_HITS) {
		return zend_memnstr_twoway(haystack, needle, needle_len, end);
	}

	__m128i v0 = _mm_set1_epi8(needle[anchor]);
	__m128i v1 = _mm_set1_epi8(needle[anchor + 1]);
	__m128i v2 = _mm_set1_epi8(needle[anchor + 2]);
	__m128i v3 = _mm_set1_epi8(needle[anchor + 3]);
	size_t span = length - needle_len + 1, pos = 0;
	size_t checks_left = length / needle_len;
	/* Sixteen loaded bytes contain thirteen complete four-byte anchors.
	 * Advancing by thirteen covers the starts spanning the next block. */
	while (span - pos >= ZEND_MEMNSTR_GRAM_STEP) {
		__m128i chunk = _mm_loadu_si128((const __m128i *)(haystack + pos + anchor));
		unsigned int mask = (unsigned int)_mm_movemask_epi8(_mm_cmpeq_epi8(chunk, v0))
				& ((unsigned int)_mm_movemask_epi8(_mm_cmpeq_epi8(chunk, v1)) >> 1)
				& ((unsigned int)_mm_movemask_epi8(_mm_cmpeq_epi8(chunk, v2)) >> 2)
				& ((unsigned int)_mm_movemask_epi8(_mm_cmpeq_epi8(chunk, v3)) >> 3)
				& ((1U << ZEND_MEMNSTR_GRAM_STEP) - 1);
		while (mask) {
			size_t candidate = pos + zend_ulong_ntz(mask);
			if (!memcmp(haystack + candidate, needle, needle_len)) {
				return haystack + candidate;
			}
			if (--checks_left == 0) {
				return zend_memnstr_twoway(haystack + candidate + 1, needle, needle_len, end);
			}
			mask &= mask - 1;
		}
		pos += ZEND_MEMNSTR_GRAM_STEP;
	}
	for (; pos < span; pos++) {
		uint32_t word;
		memcpy(&word, haystack + pos + anchor, sizeof word);
		if (word == gram) {
			if (!memcmp(haystack + pos, needle, needle_len)) {
				return haystack + pos;
			}
			if (--checks_left == 0) {
				return zend_memnstr_twoway(haystack + pos + 1, needle, needle_len, end);
			}
		}
	}
	return NULL;
}
#endif

/* Called when Sunday comparisons stop paying for their progress. Limit
 * total candidate verification to O(haystack length), then hand the remaining
 * suffix to Two-Way. This budget covers the entire scan, including a change in
 * candidate density after an initially selective prefix. */
static const char *zend_memnstr_adaptive(const char *haystack,
		const char *needle, size_t needle_len, const char *end)
{
	size_t length = (size_t)(end - haystack);
	if (UNEXPECTED(needle_len == 0)) {
		return haystack;
	}
	if (UNEXPECTED(needle_len > length)) {
		return NULL;
	}
	if (UNEXPECTED(needle_len == 1)) {
		return (const char *)memchr(haystack, *needle, length);
	}

#if defined(__SSE2__)
	size_t a = 0, b;
	for (size_t i = 1; i < needle_len; i++) {
		if (zend_byte_commonness[(unsigned char)needle[i]]
				< zend_byte_commonness[(unsigned char)needle[a]]) {
			a = i;
		}
	}
	b = a == 0 ? 1 : 0;
	for (size_t i = 0; i < needle_len; i++) {
		if (i != a && ((needle[b] == needle[a] && needle[i] != needle[a])
				|| (needle[i] != needle[a]
					&& zend_byte_commonness[(unsigned char)needle[i]]
						< zend_byte_commonness[(unsigned char)needle[b]]))) {
			b = i;
		}
	}
	__m128i va = _mm_set1_epi8(needle[a]), vb = _mm_set1_epi8(needle[b]);
	size_t span = length - needle_len + 1, pos = 0;
	size_t checks_left = length / needle_len;

	/* A full block of candidate starts guarantees both loads stay in bounds,
	 * even when an anchor sits at the last byte of the needle. */
	while (span - pos >= 16) {
		__m128i ca = _mm_loadu_si128((const __m128i *)(haystack + pos + a));
		__m128i cb = _mm_loadu_si128((const __m128i *)(haystack + pos + b));
		unsigned int mask = (unsigned int)_mm_movemask_epi8(_mm_and_si128(
				_mm_cmpeq_epi8(ca, va), _mm_cmpeq_epi8(cb, vb)));
		while (mask) {
			size_t candidate = pos + zend_ulong_ntz(mask);
			if (!memcmp(haystack + candidate, needle, needle_len)) {
				return haystack + candidate;
			}
			if (--checks_left == 0) {
				return zend_memnstr_gram4(haystack + candidate + 1, needle, needle_len, end);
			}
			mask &= mask - 1;
		}
		pos += 16;
	}
	for (; pos < span; pos++) {
		if (haystack[pos + a] == needle[a] && haystack[pos + b] == needle[b]) {
			if (!memcmp(haystack + pos, needle, needle_len)) {
				return haystack + pos;
			}
			if (--checks_left == 0) {
				return zend_memnstr_gram4(haystack + pos + 1, needle, needle_len, end);
			}
		}
	}
	return NULL;
#else
	return zend_memnstr_twoway(haystack, needle, needle_len, end);
#endif
}

/* On long needles, switch from Sunday only when failed partial comparisons
 * cost more than the bytes advanced through the haystack. */
static zend_never_inline const char *zend_memnstr_sunday_adaptive(const char *haystack, const char *needle, size_t needle_len, const char *end) /* {{{ */
{
	unsigned int td[256];
	size_t i;
	const char *p, *search_end = end, *window = haystack;
	size_t length = (size_t)(end - haystack);
	size_t deep_checks = 0;
	uint64_t deep_work = 0;

	if (needle_len == 0 || length < needle_len) {
		return NULL;
	}

	/* The shift table stores unsigned int distances. Larger needles go straight
	 * to Two-Way, which uses size_t throughout its preprocessing and search. */
	if (UNEXPECTED(needle_len >= INT_MAX)) {
		return zend_memnstr_twoway(haystack, needle, needle_len, end);
	}
	zend_memnstr_ex_pre(td, needle, needle_len, 0);

	p = haystack;
	end -= needle_len;
	/* This function only receives needles of at least MIN_NEEDLE bytes.
	 * Keep the original scalar comparison loop. Account only for long failed
	 * prefixes, so ordinary mismatches do not pay for counters or memcmp. */
	while (p <= end) {
		for (i = 0; i < needle_len; i++) {
			if (needle[i] != p[i]) {
				break;
			}
		}
		if (UNEXPECTED(i >= ZEND_MEMNSTR_SUNDAY_ACCOUNT_MIN)) {
			if (i == needle_len) {
				return p;
			}
			/* At most SAMPLE * (INT_MAX - 1) bytes are counted, including on
			 * 32-bit targets. Use the actual failed-prefix work, not needle_len. */
			deep_work += i + 1;
			if (++deep_checks == ZEND_MEMNSTR_SUNDAY_SAMPLE) {
				if (deep_work > (size_t)(p - window)
						&& (size_t)(search_end - (p + 1)) >= ZEND_MEMNSTR_ADAPTIVE_MIN_REMAINING) {
					return zend_memnstr_adaptive(p + 1, needle, needle_len, search_end);
				}
				window = p + 1;
				deep_checks = 0;
				deep_work = 0;
			}
		}
		if (UNEXPECTED(p == end)) {
			return NULL;
		}
		p += td[(unsigned char)p[needle_len]];
	}
	return NULL;
}
/* }}} */

ZEND_API const char* ZEND_FASTCALL zend_memnstr_ex(const char *haystack, const char *needle, size_t needle_len, const char *end) /* {{{ */
{
	/* Keep routing outside the search loops. Short needles use byte-sized
	 * shifts; adaptive preprocessing is reserved for long scans. */
	if (EXPECTED(needle_len < ZEND_MEMNSTR_ADAPTIVE_MIN_NEEDLE)) {
		return zend_memnstr_sunday_short(haystack, needle, needle_len, end);
	}
	if (UNEXPECTED((size_t)(end - haystack) >= ZEND_MEMNSTR_ADAPTIVE_MIN_HAYSTACK)) {
		return zend_memnstr_sunday_adaptive(haystack, needle, needle_len, end);
	}
	return zend_memnstr_sunday(haystack, needle, needle_len, end);
}
/* }}} */

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
    if (nl == 0) return h;
    if (nl > hl) return NULL;
    return (const unsigned char *)zend_memnstr((const char *)h, (const char *)n, nl, (const char *)h + hl);
}
static const unsigned char *zend_pair_find(const unsigned char *h, size_t hl, const unsigned char *n, size_t nl) {
    if (nl == 0) return h;
    if (nl > hl) return NULL;
    return (const unsigned char *)zend_memnstr_adaptive((const char *)h, (const char *)n, nl, (const char *)h + hl);
}
static const unsigned char *zend_twoway_find(const unsigned char *h, size_t hl, const unsigned char *n, size_t nl) {
    if (nl == 0) return h;
    if (nl > hl) return NULL;
    return (const unsigned char *)zend_memnstr_twoway((const char *)h, (const char *)n, nl, (const char *)h + hl);
}
#if !defined(__SSE2__)
#define zend_memnstr_gram4 zend_memnstr_twoway
#endif
static const unsigned char *zend_gram_find(const unsigned char *h, size_t hl, const unsigned char *n, size_t nl) {
    if (nl == 0) return h;
    if (nl > hl) return NULL;
    return (const unsigned char *)zend_memnstr_gram4((const char *)h, (const char *)n, nl, (const char *)h + hl);
}
