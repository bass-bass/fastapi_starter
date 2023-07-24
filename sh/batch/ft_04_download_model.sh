#!/bin/bash

##########
# 引数パターン sh ft_04_download_model.sh 2022-10-26
# date : 使用したいモデルの作成日付
# APIで使用するためにGCSからローカルへモデルのダウンロード
##########
CONTAINER_NAME=ft_app
FILE_NAME=ft_batch.py
DATE=$1

docker exec $CONTAINER_NAME python $FILE_NAME download_model -d $DATE &
