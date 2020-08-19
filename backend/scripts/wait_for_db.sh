#!/usr/bin/env bash

set -e

cmd="$@"

until mysql mysql -u ${DB_USER} -p${DB_PASS} -P ${DB_PORT} -h ${DB_HOST}; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"
exec $cmd
