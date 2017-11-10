#!/bin/bash


:<<!
 for循环打印
!
file = `ls ./`
for x in ${file}
do
 echo "ls -l后,发现一个文件${x}"
done

:<<!
 seq打印
!
num=$(seq 10)
for i in  ${num}
do
 echo "获取的数字 ${i}"
done

