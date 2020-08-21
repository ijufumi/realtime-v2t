FROM python:3.8-alpine

RUN apk update
RUN apk add bash
RUN apk add mysql-client
RUN apk add mariadb-dev
RUN apk add gcc
RUN apk add g++
RUN apk add musl-dev
RUN apk add libffi-dev
RUN apk add openssl-dev
RUN apk add ffmpeg

RUN pip install poetry

WORKDIR /opt/backend
COPY . ./

RUN poetry config virtualenvs.create false && poetry install
RUN chmod +x ./scripts/entrypoint.sh
RUN chmod +x ./scripts/wait_for_db.sh
ENTRYPOINT ./scripts/wait_for_db.sh ./scripts/entrypoint.sh
