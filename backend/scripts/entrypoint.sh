#!/usr/bin/env bash

# Create DB
mysql -u ${DB_USER} -p${DB_PASS} -P ${DB_PORT} -h ${DB_HOST} -e "create database v2t_db if not exist"

alembic upgrade head

# Run server
python main.py
