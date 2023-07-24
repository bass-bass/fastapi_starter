#!/bin/bash

##########
# 引数パターン sh ft_03_upload_model.sh 2022-10-26
# date : ft_03で指定した日付
# ローカルに保存したモデルをGCSへアップロード
##########
CONTAINER_NAME=ft_app
FILE_NAME=ft_batch.py
DATE=$1

docker exec $CONTAINER_NAME python $FILE_NAME upload_model -d $DATE &
