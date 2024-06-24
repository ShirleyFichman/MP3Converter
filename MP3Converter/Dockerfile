FROM python:3.11-slim
LABEL authors="shirleyfichman"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .


RUN pip install

ENTRYPOINT ["python", "main.py"]