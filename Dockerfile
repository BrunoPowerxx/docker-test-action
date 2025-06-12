FROM n8nio/n8n
RUN apk add --update python3 py3-pip
RUN pip install playwright
RUN playwright install --with-deps

COPY . .
