FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "test_one.py"]
