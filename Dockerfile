FROM python:3.7

LABEL version="0.1"

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD Pipfile /code/
ADD Pipfile.lock /code/

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /code/