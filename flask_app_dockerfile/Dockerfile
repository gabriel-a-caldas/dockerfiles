FROM python:3.12.8-slim-bullseye

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app

EXPOSE 5000

CMD ["python3", "-u", "app.py"]