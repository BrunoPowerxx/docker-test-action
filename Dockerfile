FROM python: 3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements

COPY . .

CMD ["pytest", "test_one.py"]