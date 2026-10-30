# Profiles supporting the final interpretation

Unchanged instruction counts do not remove an elapsed-time loss. The profiles below
compare the same stock and ca89 builds. Their counters are separate diagnostic
measurements and must not be combined with elapsed runs to derive exact IPC.

- GCC 15 HTTP headers with a large body: [five-pass native profile](../data/amd/final-confirmation/gcc15-case066-why.log).
- GCC 15 HTTP with a large cookie: [five-pass native profile](../data/amd/final-confirmation/gcc15-case185-why.log).
- Clang 21 long moderation and the instruction/time disagreement: [profile](../data/profiles/amd-why-clang21-ipc.txt).
- Long Intel scans: [Clang 20](../data/profiles/why-clang20-slower.txt), [Clang 18](../data/profiles/why-clang18-slower.txt), [GCC 13](../data/profiles/why-gcc13-slower.txt).
- Additional quiet Intel profiles: [GCC 13](../data/profiles/gcc13-why.log), [GCC 14](../data/profiles/gcc14-why.log), [Clang 18](../data/profiles/clang18-why.log).
- AMD disassembly: [stock](../data/profiles/asm-amd-base.txt), [short Sunday](../data/profiles/asm-amd-short.txt), [adaptive Sunday](../data/profiles/asm-amd-adaptive.txt).

The GCC HTTP profiles show additional instruction-cache misses with unchanged
instruction counts. The PHP entry-point addresses shown by those profiles are
unchanged; the helper layout differs. This is consistent with placement/cache
effects, but does not establish the unique cause of every measured difference.
All residual losses and unresolved rows remain in the elapsed tables.
