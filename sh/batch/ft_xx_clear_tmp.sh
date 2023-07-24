#!/bin/bash

##########
# 引数パターン sh ft_xx_clear_temp.sh {dirName}
# dirname = data, model, log
# /tmp/{dirName} 配下を削除する
# data,log配下は目的が終われば基本消していい
# model配下はweeklyの推論で用いるため残す
# GCSに新しいモデルが更新された場合はdownload_modelを実行してローカルモデルも更新する
##########
CONTAINER_NAME=ft_app
DIRNAME=$1
TARGET_TMP_DIR=/tmp/${DIRNAME}

docker exec $CONTAINER_NAME /bin/bash -c "rm -rf  $TARGET_TMP_DIR/*" &
