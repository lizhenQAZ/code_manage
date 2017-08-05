#!ust/bin/python
# -*- coding:utf-8 -*-
import time
from math import sqrt

'''practice8~14~'''
#test1 display 9*9 multiplication formula
for i in range(1,10):
    for j in range(1,i+1):
        print "%s*%s=%s"%(i,j,i*j),
    print "\n"

#test2 output by delaying 1 second
dicts={1:'a',2:'b',}
for key , value in dict.items(dicts):
    print key , value
    time.sleep(1)#delay 1 second

#test3 formatting current time by delaying 1 second
print time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))
time.sleep(1)
print time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))

#test4 calcalate rabbits'sum

#test5 ouput leap number in 101~200 and total sum
leap=1
sum=0
for m in range(101,201):
    k=int(sqrt(m))
    for i in range(2,k+1):
        if m%i==0:
            leap=0
    if leap==1:
        print "%5d"%m
        sum+=1
    leap=1
print "%5d"%sum

#test6 get daffodils'number
for num in range(100,1000):
    k=int(num/100)
    j=int(num/10%10)
    i=int(num%10)
    if i**3+j**3+k**3==num:
        print num

#test7 factorization

