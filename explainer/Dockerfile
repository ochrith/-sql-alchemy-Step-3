FROM python:3.12-slim

WORKDIR /app

COPY explainer/requirements.txt ./explainer/requirements.txt

RUN pip install --no-cache-dir -r ./explainer/requirements.txt

COPY explainer/ ./explainer/
COPY database/ ./database/

CMD ["python", "-m", "explainer.main"]