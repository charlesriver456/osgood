FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=-1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
COPY requirements-test.txt .

RUN python -m pip install -r requirements.txt
RUN python -m pip install -r requirements-test.txt

WORKDIR /app

COPY . .
