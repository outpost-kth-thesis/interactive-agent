FROM python:latest AS base

WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install -r requirements.txt


COPY src ./src
