#!/bin/bash


:<<!
 until语句
!
a=10
until [ "${a}" -lt 1 ]
do
    echo "a的值是 ${a}"
    let a=a-1
done

