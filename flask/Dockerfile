# Debian based Python image
FROM python:3.8.6-buster

RUN apt-get update
RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

ARG STAGE
ENV STAGE=$STAGE
ENV PYTHONPATH ./:./src:$PYTHONPATH

RUN pytest ./test

CMD ["gunicorn", "-w", "3", "-b", ":5000", "-t", "360", "--reload", "wsgi:app"]