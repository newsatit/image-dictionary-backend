FROM python:3.7

LABEL version="0.1"

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

ADD Pipfile /usr/src/app/
ADD Pipfile.lock /usr/src/app/

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /usr/src/app/