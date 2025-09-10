FROM python:3.11-slim

WORKDIR /app

COPY transcribing_and_updating/requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY utils/ ./utils/

COPY transcribing_and_updating/ ./



CMD ["python", "main.py"]