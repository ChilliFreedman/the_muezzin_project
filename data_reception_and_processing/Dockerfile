FROM python:3.11-slim

WORKDIR /app

COPY data_reception_and_processing/requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY utils/ ./utils/

COPY data_reception_and_processing/ ./

CMD ["python", "main.py"]