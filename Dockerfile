
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY monitor.py .
COPY report.py .
COPY dashboard.py .

EXPOSE 5000
EXPOSE 8501

CMD ["python", "app.py"]
