# shellcheck shell=bash
# CPU lists of the containers, read by setup.sh, drupal-run.sh and record.py. The defaults are those of the runs:
# AMD Ryzen 9 5950X, where CPU n and n+16 are the two threads of one core; each group is whole cores.
# On another machine, set them in the environment or change them here before setup.sh (PostgreSQL's list is
# fixed when setup.sh creates its container).
export CPUS_STACK=${CPUS_STACK:-8-11,24-27}  # nginx, PHP-FPM, PgBouncer: 4 cores
export CPUS_PG=${CPUS_PG:-12-15,28-31}       # PostgreSQL: 4 cores
export CPUS_JMETER=${CPUS_JMETER:-6-7,22-23} # JMeter: 2 cores
