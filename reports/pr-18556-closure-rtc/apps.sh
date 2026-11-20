#!/bin/bash
# Sets up the two applications in apps/: ./apps.sh <php-cli> <composer.phar>
#   apps/laravel  Laravel 13 skeleton with the vendor tree of laravel-composer.lock (laravel/framework 13.43.0),
#                 SQLite with 200 users, routes "/" (the welcome Blade view) and "/users" (100 Eloquent models
#                 as JSON), production mode, config/route/view/event caches built.
#   apps/sfdemo   symfony/demo at a fixed commit, prod mode, SQLite database shipped with the demo.
# Uses the network (git, Composer). The php-cli should be one of the builds (any of them).
set -eu
PHP=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
COMPOSER=$(cd "$(dirname "$2")" && pwd)/$(basename "$2")
cd "$(dirname "$0")"
SFDEMO=f42980c690b4bf335fa41bbafdb075bb67b719c2
[ -e apps ] && { echo "apps exists" >&2; exit 1; }
mkdir apps

# Laravel
"$PHP" "$COMPOSER" create-project -q --no-interaction --prefer-dist --no-install --no-scripts laravel/laravel apps/laravel '^13'
cp laravel-composer.json apps/laravel/composer.json
cp laravel-composer.lock apps/laravel/composer.lock
cd apps/laravel
"$PHP" "$COMPOSER" install -q --no-interaction --prefer-dist --ignore-platform-req=php  # master is 8.7.0-dev
cp .env.example .env
sed -i 's/^APP_ENV=.*/APP_ENV=production/; s/^APP_DEBUG=.*/APP_DEBUG=false/; s/^SESSION_DRIVER=.*/SESSION_DRIVER=array/; s/^CACHE_STORE=.*/CACHE_STORE=file/' .env
"$PHP" artisan key:generate -q --force
cat > routes/web.php <<'EOF'
<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get("/users", function () {
    return \App\Models\User::query()->orderBy("id")->limit(100)->get();
});
EOF
cat > database/seeders/BenchSeeder.php <<'EOF'
<?php
namespace Database\Seeders;
use App\Models\User;
use Illuminate\Database\Seeder;
class BenchSeeder extends Seeder { public function run(): void { User::factory(200)->create(); } }
EOF
touch database/database.sqlite
"$PHP" artisan migrate -q --force
"$PHP" artisan db:seed -q --class=BenchSeeder --force
"$PHP" artisan optimize -q
cd ../..

# Symfony Demo
git clone -q https://github.com/symfony/demo.git apps/sfdemo
cd apps/sfdemo
git checkout -q "$SFDEMO"
printf 'APP_ENV=prod\nAPP_DEBUG=0\n' > .env.local
APP_ENV=prod "$PHP" "$COMPOSER" install -q --no-interaction --no-dev --optimize-autoloader --ignore-platform-req=php
APP_ENV=prod "$PHP" bin/console -q asset-map:compile
APP_ENV=prod "$PHP" bin/console -q cache:warmup
cd ../..
echo "apps ready"
