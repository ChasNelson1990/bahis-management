#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo "collecting static"
python /app/manage.py collectstatic --noinput > /app/collectstatic.log

echo "running gunicorn"
exec gunicorn config.asgi --bind 0.0.0.0:80 --chdir=/app -k uvicorn.workers.UvicornWorker
