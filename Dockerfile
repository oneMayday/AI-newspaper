FROM python:3.10.11-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app/newspaper

EXPOSE 8000
EXPOSE 465