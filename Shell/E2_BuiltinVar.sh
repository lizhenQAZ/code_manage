#!/bin/bash

:<<!
　内置变量
!
# 获取指定参数
echo "脚本名为: $0"
# 获取参数个数
echo "获取到参数个数为: $#"
# 获取上一次执行结果
pwd
echo $?
# 获取随机字符串
echo $RANDOM | md5sum | awk '{print $1}'
# 截取字符串
str='hello world'
echo ${str:4:8}
echo ${str: -8}
