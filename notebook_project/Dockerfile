FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y netcat-openbsd

CMD sh -c "echo 'Ждём PostgreSQL...' && \
           while ! nc -z db 5432; do sleep 0.5; done && \
           echo 'База готова. Миграции...' && \
           python manage.py migrate && \
           python manage.py runserver 0.0.0.0:8000"
