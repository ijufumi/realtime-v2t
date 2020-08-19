#!/usr/bin/env bash

# Create DB
mysql -u ${DB_USER} -p${DB_PASS} -P ${DB_PORT} -h ${DB_HOST} -e "CREATE DATABASE IF NOT EXISTS v2t_db CHARACTER SET utf8mb4"

PYTHONPATH=. alembic upgrade head

# Run server
python main.py
