-- Tables of the php-src #24385 benchmark: schema pr24385, 7 tables of 10,000 rows.
--   psql -v ON_ERROR_STOP=1 -U postgres < pgsql.sql   (drops and recreates the schema)
-- The seeds make the data reproducible; the statements stay in the order of the runs, because the order changes the data.
-- 9.2e18 is just below 2^63 (about 9.22e18), the int8 limit.
DROP SCHEMA IF EXISTS pr24385 CASCADE;
CREATE SCHEMA pr24385;
SELECT setseed(0.24385);
CREATE TABLE pr24385.int2 AS SELECT (floor(random()*65536)-32768)::int2 a,(floor(random()*65536)-32768)::int2 b,(floor(random()*65536)-32768)::int2 c,(floor(random()*65536)-32768)::int2 d FROM generate_series(1,10000);
CREATE TABLE pr24385.int4_small AS SELECT (floor(random()*1000))::int4 a,(floor(random()*1000))::int4 b,(floor(random()*1000))::int4 c,(floor(random()*1000))::int4 d FROM generate_series(1,10000);
CREATE TABLE pr24385.int4 AS SELECT (floor(random()*4294967296)-2147483648)::int4 a,(floor(random()*4294967296)-2147483648)::int4 b,(floor(random()*4294967296)-2147483648)::int4 c,(floor(random()*4294967296)-2147483648)::int4 d FROM generate_series(1,10000);
CREATE TABLE pr24385.int8 AS SELECT ((random()*2-1)*9.2e18)::int8 a,((random()*2-1)*9.2e18)::int8 b,((random()*2-1)*9.2e18)::int8 c,((random()*2-1)*9.2e18)::int8 d FROM generate_series(1,10000);
CREATE TABLE pr24385.mixed AS SELECT g::int4 id,(floor(random()*100000))::int4 n, md5(g::text) t1, 'title '||g t2, 'user'||(g%97) t3, 'en' t4, 'published' t5, md5((g*7)::text) t6, 'x'||g t7, '2026-10-22' t8, 'note '||(g%13) t9 FROM generate_series(1,10000) g;
CREATE TABLE pr24385.text AS SELECT md5(g::text) a, 'title '||g b, 'user'||(g%97) c, 'note '||(g%13) d FROM generate_series(1,10000) g;
-- check: min and max of pr24385.int8.a
SELECT min(a), max(a), min(length(a::text)) FROM pr24385.int8;
-- int8_small was added after the first series, with its own seed
SELECT setseed(0.24386);
CREATE TABLE pr24385.int8_small AS SELECT g::int8 a, (floor(random()*1000000))::int8 b, (floor(random()*10000))::int8 c, (floor(random()*100))::int8 d FROM generate_series(1,10000) g;
