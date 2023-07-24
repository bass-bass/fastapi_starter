#!/bin/bash
CONTAINER_NAME=ft_app
FILE_NAME=ft_api
APP_NAME=app
PORT=8887

#uvicornサーバーで起動
#docker exec $CONTAINER_NAME uvicorn $FILE_NAME:$APP_NAME --reload --host 0.0.0.0 --port $PORT &
#gunicornサーバーで起動
docker exec $CONTAINER_NAME gunicorn $FILE_NAME:$APP_NAME --workers 4 --reload --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker &
