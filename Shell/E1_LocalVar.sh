#!/bin/bash

:<<!
　1.命令变量
!
tmp1=`pwd`
echo $tmp1
tmp2=$(pwd)
echo $tmp2

:<<!
  2.普通变量
!
a=aaa
echo $a
b='bbb${a}bbb'
echo $b
c="ccc${a}ccc"
echo $c
