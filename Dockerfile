FROM n8nio/n8n
USER root
RUN apk add --update python3
RUN pip install playwright
RUN playwright install --with-deps

COPY . .
