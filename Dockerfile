FROM python:3.8
LABEL maintainer="alex nesov"

ENV PYTHONUNBUFFERED 1 
# we don't buffer the output it prints diert to the console

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \ 
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# not root user for securytiy reasons ("django-user")

# One entire run block to avoir creating an image layer at each single commmand that we run
# We want to keep our images as much as lightweight as possible


# rm -rf /tmp --> we remove this because we dont want to have extra independicies that we wont need in the future
# Objective is lightweight and speed during deployment 

ENV PATH="/py/bin:$PATH"

USER django-user