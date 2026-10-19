/* C++ side of the C/C++ test (xlang-c.c): reports the layout seen by C++ and updates the counters with
 * MYSQLND_STATS_UPDATE_VALUE() from several threads. */
extern "C" {
#include "php.h"
#include "ext/mysqlnd/mysqlnd.h"
#include "ext/mysqlnd/mysqlnd_statistics.h"
}
#include <cstddef>
#include <thread>
#include <vector>

extern "C" void cxx_layout(size_t out[4])
{
	out[0] = sizeof(MYSQLND_STATS);
	out[1] = offsetof(MYSQLND_STATS, values);
	out[2] = sizeof(((MYSQLND_STATS *) 0)->values[0]);
	out[3] = alignof(atomic_uint_least64_t);
}

extern "C" void cxx_bump(MYSQLND_STATS *s, unsigned threads, unsigned iterations)
{
	std::vector<std::thread> t;
	for (unsigned n = 0; n < threads; n++) {
		t.emplace_back([=] {
			for (unsigned i = 0; i < iterations; i++) {
				MYSQLND_STATS_UPDATE_VALUE(s, STAT_BYTES_SENT, 1);
				MYSQLND_STATS_UPDATE_VALUE(s, STAT_LAST - 1, 3);
			}
		});
	}
	for (auto &x : t) {
		x.join();
	}
}
