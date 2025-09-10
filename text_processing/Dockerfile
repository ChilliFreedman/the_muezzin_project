FROM python:3.11-slim

WORKDIR /app

COPY text_processing/requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY utils/ ./utils/

COPY text_processing/ ./

CMD ["python", "main.py"]