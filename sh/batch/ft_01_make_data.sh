#!/bin/bash

##########
# 引数パターン sh ft_01_make_data.sh 2022-10-26
# date : 使用するデータセットの作成日
# GCSからデータセットの取得し学習用のデータセット作成
##########
CONTAINER_NAME=ft_app
FILE_NAME=ft_batch.py
DATE=$1

docker exec $CONTAINER_NAME python $FILE_NAME make_data -d $DATE &
