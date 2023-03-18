FROM python:3.9.16-alpine3.17

RUN pip install redis

WORKDIR /root
COPY ./src ./src

RUN touch /root/service.log
WORKDIR /root/src
CMD tail -f /root/service.log