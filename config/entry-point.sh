#!/bin/bash

touch /app/logs/gunicorn.log
touch /app/logs/access.log
tail -n 0 -f /app/logs/*.log &

echo Starting nginx
# Start Gunicorn processes
echo Starting Gunicorn.

cd /app

exec gunicorn app:app \
    --name flaskapp \
    --bind unix:flaskapp.sock \
    --workers 3 \
    --log-level=info \
    --log-file=/app/logs/gunicorn.log \
    --access-logfile=/app/logs/access.log &

exec service nginx start
