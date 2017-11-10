#!/bin/bash


#脚本验证
case "$1" in
    "start")
        echo "启动 $0 服务"
    ;;
    "stop")
　　　　echo "关闭 $0 服务"
　　;;
    "restart")
	echo "重启 $0 服务"
    ;;
    *)
	echo "参数错误, $0 使用方式: $0 [ start | stop | restart ]"
    ;;
esac
  
