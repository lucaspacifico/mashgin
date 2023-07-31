FROM python:3.11-buster

RUN mkdir app
WORKDIR /app

COPY . .

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry lock \
    && poetry install 

