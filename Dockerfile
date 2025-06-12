FROM n8nio/n8n:latest-debian

USER root

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt .

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --prefer-binary -r requirements.txt

RUN playwright install --with-deps

COPY . .
