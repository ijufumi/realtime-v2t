FROM python:3.8-alpine

RUN apk update
RUN apk add mysql-client
RUN apk add gcc
RUN apk add musl-dev
RUN apk add libffi-dev
RUN apk add openssl-dev

RUN pip install poetry

WORKDIR /opt/backend
COPY . ./
RUN ls

RUN poetry config virtualenvs.create false && poetry install
CMD chmod +x ./scripts/entrypoint.sh
CMD ./scripts/entrypoint.sh
