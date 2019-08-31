# Pull base image
FROM python:3.7-alpine

RUN apk add --no-cache --update \
    build-base \
    postgresql-dev \
    bash \
    && rm -rf /var/cache/apk/*

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /eventbook
# Set work directory
WORKDIR /eventbook

ADD requirements.txt /eventbook/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

ADD . /eventbook/