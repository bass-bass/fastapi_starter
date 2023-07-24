#!/bin/bash

##########
# 引数パターン sh ft_02_make_model.sh
# date : ft_01で指定した日付
# 作成したデータセットでモデルの作成、ローカルに保存
##########
CONTAINER_NAME=ft_app
FILE_NAME=ft_batch.py
DATE=$1

docker exec $CONTAINER_NAME python $FILE_NAME make_model &