#!/bin/sh
CURRENT_DIR=`pwd`
HOME_DIR=`dirname $CURRENT_DIR`
LOG_DIR=$HOME_DIR/log
STD_OUT_LOG=$LOG_DIR/boot.log
STD_ERR_LOG=$LOG_DIR/error.log

touch ${STD_OUT_LOG}
touch ${STD_ERR_LOG}