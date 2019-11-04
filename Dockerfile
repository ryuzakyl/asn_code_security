FROM python:3.6-alpine
LABEL authors="Victor M. Mendiola Lau <ryuzakyl@gmail.com>, Madelin Díaz Ramos <madelinkind@gmail.com>"

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

RUN python manage.py migrate
