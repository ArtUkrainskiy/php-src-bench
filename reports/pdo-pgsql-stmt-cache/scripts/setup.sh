#!/bin/bash
# Creates the benchmark site in this directory, once: Docker network drupal-bench, PostgreSQL 17.11 (container
# drupal-bench-pg on CPUS_PG of cpus.sh; it keeps running and every run uses it), Drupal 11.4 installed with drush
# in drupal-bench-web (used only to install, stopped at the end), generated content, 20 editors (bench1..bench20,
# password bench), caches cleared, automated_cron uninstalled.
# Then copies the site to ./app (served by drupal-run.sh), appends settings-bench.php to its settings.php,
# snapshots the database as drupal_tpl (every run starts from it) and writes nids.csv and site.txt.
# About 15 minutes; composer needs network access.
#   ./setup.sh
# To start again: docker rm -f drupal-bench-pg drupal-bench-web, and remove ./app, nids.csv and site.txt.
set -e
cd "$(dirname "$0")"
. ./cpus.sh
[ ! -e app ] || { echo "./app exists: remove it and the containers drupal-bench-pg, drupal-bench-web first" >&2; exit 1; }
DRUPAL_IMAGE=drupal@sha256:ae4852fac24f8b318c56b134086fb90ea143ddb8b5ded5475026851e497eac4b   # drupal:11-php8.4-apache
PG_IMAGE=postgres@sha256:2d2b8998d31037bf721cfdf764d76ba74171b4fab3431b7f72c27c56ddbdf9e3       # postgres:17.11
docker network inspect drupal-bench >/dev/null 2>&1 || docker network create drupal-bench >/dev/null
docker run -d --name drupal-bench-pg --network drupal-bench --cpuset-cpus "$CPUS_PG" \
	-e POSTGRES_USER=drupal -e POSTGRES_PASSWORD=drupal -e POSTGRES_DB=drupal "$PG_IMAGE" >/dev/null
docker run -d --name drupal-bench-web --network drupal-bench --cpuset-cpus "$CPUS_STACK" "$DRUPAL_IMAGE" >/dev/null
# over TCP: during its first start the image runs a temporary server on the Unix socket only
timeout 120 bash -c 'until docker exec drupal-bench-pg pg_isready -h 127.0.0.1 -U drupal -q; do sleep 1; done'
W="docker exec -w /opt/drupal drupal-bench-web"
D="$W vendor/bin/drush -y"
for i in $(seq 1 10); do   # packagist sometimes times out
	$W env COMPOSER_IPRESOLVE=4 composer require -q --no-interaction drush/drush:13.8.0 drupal/devel:5.5.0 && break
	[ "$i" = 10 ] && exit 1; sleep 60
done
$D site:install standard --db-url=pgsql://drupal:drupal@drupal-bench-pg:5432/drupal --account-pass=admin --site-name=bench
$W chown -R www-data:www-data web/sites/default/files
# Drupal 11.4: the standard profile left out the content types here; the core recipes add them, applied one by one
# (applying core/recipes/standard alone did not create them); node search is the search_node submodule.
for r in standard page_content_type tags_taxonomy article_tags comment_base article_comment content_search content_editor_role; do
	$D -q recipe "core/recipes/$r"
done
$D en devel_generate search search_node
$D pm:uninstall automated_cron
$D devel-generate:terms 200 --bundles=tags
$D devel-generate:users 100
$D devel-generate:content 3000 5 --bundles=article,page
for i in $(seq 1 20); do $D -q user:create "bench$i" --password=bench --mail="bench$i@example.invalid"; done
$D -q user:role:add content_editor "$(seq -f 'bench%g' -s, 1 20)"
$D -q role:perm:add content_editor "edit any article content,edit any page content,post comments,skip comment approval"
$D -q role:perm:add authenticated "access user profiles"
for i in $(seq 1 40); do $D -q cron; done   # index all nodes for search (100 per cron run)
$D -q cr
$W chmod -R u+w web/sites/default   # the installer makes it read-only; docker cp keeps the modes
docker cp drupal-bench-web:/opt/drupal ./app
cat settings-bench.php >> app/web/sites/default/settings.php
docker stop drupal-bench-web >/dev/null
P="docker exec drupal-bench-pg psql -U drupal -d postgres -tAq"
$P -c "CHECKPOINT" -c "CREATE DATABASE drupal_tpl TEMPLATE drupal"
Q="docker exec drupal-bench-pg psql -U drupal -d drupal_tpl -tAq"
{ echo nid; $Q -c "SELECT entity_id FROM node__comment WHERE comment_status = 2 ORDER BY entity_id"; } > nids.csv
{
	echo "drupal $(grep -o "VERSION = '[^']*'" app/web/core/lib/Drupal.php | cut -d"'" -f2)"
	python3 -c "import json; print(*(p['name'] + ' ' + p['version'] for p in json.load(open('app/composer.lock'))['packages'] if p['name'] in ('drush/drush', 'drupal/devel')), sep='\n')"
	$Q -c "SELECT 'nodes ' || count(*) FROM node_field_data" \
		-c "SELECT 'comments ' || count(*) FROM comment_field_data" \
		-c "SELECT 'terms ' || count(*) FROM taxonomy_term_field_data" \
		-c "SELECT 'users ' || count(*) || ', max uid ' || max(uid) FROM users_field_data WHERE uid > 0" \
		-c "SELECT 'articles with open comments ' || count(*) FROM node__comment WHERE comment_status = 2" \
		-c "SELECT 'search index items ' || count(DISTINCT sid) FROM search_dataset" \
		-c "SELECT 'watchdog rows ' || count(*) FROM watchdog"
} | tee site.txt
