#!/bin/bash

##########
# 引数パターン sh ft_00_evaluate_model.sh 2022-10-26
# date : 使用するデータセットの作成日
# GCSからデータセットの取得、モデル作成と評価まで
# ここではモデルの保存は行わない
##########
CONTAINER_NAME=ft_app
FILE_NAME=ft_batch.py
DATE=$1

docker exec $CONTAINER_NAME python $FILE_NAME evaluate_model -d $DATE &