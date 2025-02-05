FROM python:3.12.8-slim-bullseye

RUN mkdir -p /app

WORKDIR /app

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
