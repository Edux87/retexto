FROM python:3-alpine
ENV TERM xterm
MAINTAINER edanie15@gmail.com

RUN apk add --update bash ca-certificates && \
  python -m ensurepip && \
  pip install --upgrade pip setuptools && \
  rm -r /root/.cache

ADD dev-requirements.txt /
RUN pip install -r dev-requirements.txt

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD .pypirc /root

RUN mkdir /retexto
WORKDIR retexto
