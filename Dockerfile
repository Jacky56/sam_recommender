FROM python:3.9-buster

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py commons.py ./
COPY dataset/curated.csv ./dataset/

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app:app