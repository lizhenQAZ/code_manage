#!/usr/bin/python
import math
list=[]
for i in range(101,201):
    flag=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            flag=1
            break
    if flag==0:
        list.append(i)
print list
print 'total num is:',len(list)
