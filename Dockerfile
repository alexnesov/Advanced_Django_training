FROM python:3.9-alpine3.13
LABEL maintainer="alex nesovic"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    /py/bin/pip install -r /tmp/requirements.txt 

ENV PATH="/py/bin:$PATH"

USER django-user
