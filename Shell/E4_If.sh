#!/bin/bash


:<<!
 if语句
!
if [ "$1" = "start" ]
then
    echo "启动 $0 服务"
elif [ "$1" = "stop" ]
then
    echo "关闭 $0 服务"
elif [ "$1" = "restart" ]
then
    echo "重启 $0 服务"
else
    echo "参数错误, $0 脚本使用方式： $0 [ start | stop | restart ]"
fi

