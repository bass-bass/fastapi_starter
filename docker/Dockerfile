FROM python:3.9.6

RUN mkdir -p app \
    tmp/data \
    tmp/model
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

WORKDIR /app
