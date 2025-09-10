
FROM python:3.11-slim

WORKDIR /app

COPY getting_first_data/requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY data/ ./data/

COPY utils/ ./utils/

COPY getting_first_data/ ./
CMD ["python", "gmain.py"]