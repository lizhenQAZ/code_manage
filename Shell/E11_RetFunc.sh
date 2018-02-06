#!/bin/bash


:<<!
 返回值函数
!
func(){
    tmp=$(($1+$2))
    echo "${tmp}"
}
# 直接调用函数
func 11 12

res=$(func 22 23)
echo "res=${res}"


