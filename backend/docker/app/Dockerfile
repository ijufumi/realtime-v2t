FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python

WORKDIR /opt/backend
COPY . ${WORKDIR}

RUN poetry install
CMD python main.py
