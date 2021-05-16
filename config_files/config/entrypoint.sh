#!/usr/bin/env bash
postgres_ready() {
python << END
import psycopg2
import os
import sys
from urllib.parse import urlparse

result = urlparse(os.environ["DB_URL"])
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port
try:
    connection = psycopg2.connect(
        database=database,
        user=username,
        password=password,
        host=hostname,
        port=port
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}
cd app/api
until postgres_ready; do
  >&2 echo 'Database is unavailable... Waiting'
  sleep 1
done
>&2 echo 'Database is available'

uvicorn app:APP  --reload --host 0.0.0.0 --port 8080
