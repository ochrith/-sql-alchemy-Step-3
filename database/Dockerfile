FROM python:3.12-slim

WORKDIR /app

COPY database/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY database/ ./database

CMD ["python", "-m","database.main.py"]