FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt . 
RUN pip install -r requirements.txt
RUN python -m pip install chrome_extension_python
RUN playwright install --with-deps
RUN apt install -y openvpn dialog python3-pip python3-setuptools
RUN pip3 install protonvpn-cli
# Install system dependencies
RUN apt-get update && apt-get install -y \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libatspi2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
COPY . .

RUN chmod +x run.sh
CMD ["./run.sh"]
