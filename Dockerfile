FROM alpine:3.4
ENV TERM xterm
MAINTAINER edanie15@gmail.com

RUN apk add --no-cache python bash && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

ADD dev-requirements.txt /
RUN pip install -r dev-requirements.txt

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD .pypirc /root

RUN mkdir /retexto
WORKDIR retexto
