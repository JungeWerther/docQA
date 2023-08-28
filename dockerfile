FROM python:3.10.9

WORKDIR /app

RUN apt-get update && apt-get install -y tesseract-ocr poppler-utils

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

CMD ["python", "main.py"]