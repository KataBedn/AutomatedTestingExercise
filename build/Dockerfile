FROM python:3.6

LABEL description="Install testing environment for python testing framework."

RUN apt-get update
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get install -y build-essential
WORKDIR /var/www/
