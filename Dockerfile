FROM n8nio/n8n
USER root
RUN set -xe \
    && apt-get update \
    && apt-get install python-pip
RUN apk add --update python3
RUN pip install playwright
RUN playwright install --with-deps

COPY . .
