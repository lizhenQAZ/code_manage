#!/bin/bash


a=1
while [ "${a}" -lt 10 ]
do
  echo "a的值为 ${a}"
  a=$((a+1))
done

