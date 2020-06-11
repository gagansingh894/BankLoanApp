FROM python:3.7-slim
LABEL Gagandeep Singh

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN  apt-get update && apt-get install -y gnupg2
RUN  apt-get -y install curl
RUN  apt-get -qq -y install curl
RUN  apt-get install wget ca-certificates
RUN  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |  apt-key add -
# RUN  'echo "deb http://apt.postgresql.org/pub/repos/apt/lsb_release -cs-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN  apt-get update
RUN  apt-get install -y postgresql postgresql-contrib
RUN  pip install -r /requirements.txt
RUN  mkdir /app

WORKDIR /app
COPY ./app /app

RUN adduser user
USER user





