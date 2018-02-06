#!/bin/bash
lines=`awk '{print $2}' E13_File.txt`
tmp=0
for line in ${lines}
do
    echo 每次的输出结果: ${line}
    tmp=$((tmp+${line}))
done
echo 输出的总和: ${tmp}
