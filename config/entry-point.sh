#!/bin/bash

touch /app/logs/gunicorn.log
touch /app/logs/access.log
tail -n 0 -f /app/logs/*.log &

cd /app

exec gunicorn app:app \
    --name flaskapp \
    --bind 0.0.0.0:5000 \
    --worker-class gevent \
    --workers 5 \
    --timeout 90 \
    --log-level=info \
    --log-file=/app/logs/gunicorn.log \
    --access-logfile=/app/logs/access.log &

exec /usr/bin/supervisord
