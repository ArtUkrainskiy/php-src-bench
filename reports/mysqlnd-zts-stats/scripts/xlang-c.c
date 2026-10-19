/* C side of the C/C++ test of struct st_mysqlnd_stats under ZTS: compares the layout seen by C and C++, allocates and
 * initializes the counters in C, lets xlang-cxx.cpp update them from 8 threads and reads them back in C.
 * Build: see the C++ item of README.md (Correctness). */
#include "php.h"
#include "ext/mysqlnd/mysqlnd.h"
#include "ext/mysqlnd/mysqlnd_statistics.h"
#include <stdio.h>
#include <stdlib.h>

void cxx_layout(size_t out[4]);
void cxx_bump(MYSQLND_STATS *s, unsigned threads, unsigned iterations);

int main(void)
{
	size_t cxx[4], c[4] = {sizeof(MYSQLND_STATS), offsetof(MYSQLND_STATS, values), sizeof(((MYSQLND_STATS *) 0)->values[0]), _Alignof(atomic_uint_least64_t)};
	cxx_layout(cxx);
	printf("C   sizeof(struct)=%zu offsetof(values)=%zu sizeof(elem)=%zu alignof(elem)=%zu lock_free=%d\n", c[0], c[1], c[2], c[3], (int) ATOMIC_LLONG_LOCK_FREE);
	printf("C++ sizeof(struct)=%zu offsetof(values)=%zu sizeof(elem)=%zu alignof(elem)=%zu\n", cxx[0], cxx[1], cxx[2], cxx[3]);
	/* the same allocation as mysqlnd_stats_init() */
	MYSQLND_STATS *s = calloc(1, sizeof(*s) + STAT_LAST * sizeof(s->values[0]));
	s->count = STAT_LAST;
	for (size_t i = 0; i < STAT_LAST; i++) {
		atomic_init(&s->values[i], 0);
	}
	cxx_bump(s, 8, 1000000);
	uint64_t a = atomic_load_explicit(&s->values[STAT_BYTES_SENT], memory_order_relaxed);
	uint64_t b = atomic_load_explicit(&s->values[STAT_LAST - 1], memory_order_relaxed);
	uint64_t z = atomic_load_explicit(&s->values[1], memory_order_relaxed);
	printf("read from C: values[STAT_BYTES_SENT]=%llu (expected 8000000), values[STAT_LAST-1]=%llu (expected 24000000), values[1]=%llu (expected 0)\n", (unsigned long long) a, (unsigned long long) b, (unsigned long long) z);
	int same = !memcmp(c, cxx, sizeof(c));
	puts(same && a == 8000000 && b == 24000000 && z == 0 ? "OK" : "FAIL");
	return !(same && a == 8000000 && b == 24000000 && z == 0);
}
