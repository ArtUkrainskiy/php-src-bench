#define main manifest_main
#include "standalone.c"
#undef main
#include <sys/mman.h>
#include <unistd.h>

static uint64_t rng_state = 20261030;
static unsigned next_random(void) {
    rng_state ^= rng_state << 13;
    rng_state ^= rng_state >> 7;
    rng_state ^= rng_state << 17;
    return (unsigned)rng_state;
}

static void check(const unsigned char *h, size_t hl, const unsigned char *n, size_t nl) {
    const unsigned char *want = memmem(h, hl, n, nl);
    finder funcs[] = {zend_candidate_find, base_find};
    for (size_t i = 0; i < sizeof funcs / sizeof funcs[0]; i++) {
        const unsigned char *got = funcs[i](h, hl, n, nl);
        if (got != want) {
            fprintf(stderr, "mismatch impl=%zu hl=%zu nl=%zu got=%td want=%td\n",
                    i, hl, nl, got ? got - h : -1, want ? want - h : -1);
            exit(3);
        }
    }
}

int main(int argc, char **argv) {
    unsigned char default_h[1086], default_n[31];
    memset(default_h, 'z', sizeof default_h); memset(default_n, 'a', sizeof default_n);
    memcpy(default_h + 1055, default_n, sizeof default_n);
    check(default_h, sizeof default_h, default_n, sizeof default_n);
    size_t count = argc > 1 ? strtoul(argv[1], NULL, 10) : 20000;
    unsigned char *h = malloc(65536), *n = malloc(4096);
    for (size_t t = 0; t < count; t++) {
        size_t hl = next_random() % (t % 4 ? 1024 : 65536);
        size_t nl = next_random() % (t % 4 ? 128 : 4096);
        if (t % 5 == 0) {
            hl = 1024 + next_random() % 15361;
            nl = 9 + next_random() % 23;
        }
        unsigned sigma = 1 + next_random() % 256;
        unsigned base = next_random() % 256;
        for (size_t i = 0; i < hl; i++) h[i] = base + next_random() % sigma;
        for (size_t i = 0; i < nl; i++) n[i] = base + next_random() % sigma;
        if (nl && nl <= hl && (next_random() & 1)) {
            size_t at = next_random() % (hl - nl + 1);
            memcpy(n, h + at, nl);
            if (next_random() & 1) n[next_random() % nl] ^= 1;
        }
        check(h, hl, n, nl);
    }
    free(h); free(n);

    // Place the logical ends directly against inaccessible pages. Test both
    // aligned and unaligned starts, and verify needle reads as well as haystack reads.
    size_t page = (size_t)sysconf(_SC_PAGESIZE);
    unsigned char *hm = mmap(NULL, 6 * page, PROT_READ | PROT_WRITE,
            MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    unsigned char *nm = mmap(NULL, 6 * page, PROT_READ | PROT_WRITE,
            MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (hm == MAP_FAILED || nm == MAP_FAILED) return 2;
    if (mprotect(hm, page, PROT_NONE) || mprotect(hm + 5 * page, page, PROT_NONE)
            || mprotect(nm, page, PROT_NONE) || mprotect(nm + 5 * page, page, PROT_NONE)) return 2;
    size_t guarded = 0;
    for (size_t length_index = 1; length_index <= 521; length_index++) {
        static const size_t boundaries[] = {1023, 1024, 1025, 4095, 4096, 4097, 8191, 8192, 8193};
        size_t hl = length_index <= 512 ? length_index : boundaries[length_index - 513];
        for (size_t nl = 1; nl <= 260; nl++) {
            h = hm + 5 * page - hl;
            n = nm + 5 * page - nl;
            memset(h, 'a', hl); memset(n, 'a', nl);
            check(h, hl, n, nl);
            n[nl - 1] = 'z';
            check(h, hl, n, nl);
            if (nl <= hl) { memcpy(h + hl - nl, n, nl); check(h, hl, n, nl); }
            guarded++;
        }
    }
    munmap(hm, 6 * page); munmap(nm, 6 * page);
    printf("random=%zu guarded=%zu: candidate/base/libc checks passed\n", count, guarded);
    return 0;
}
