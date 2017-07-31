#!usr/bin/python
# -*- coding:utf-8 -*-
import copy

'''practice1~7'''
#test1 get three different digits in 1~5
for i in range(1,6):
    for j in range (1,6):
        for k in range(1,6):
            if (i!=k) and (i!=j) and (j!=k):
                print i*100+j*10 +k

#test2 profit sharing <10w:10%;10~20w:10%;20~40w:7.5%;40~60w:5%;60~100w:3%;>100w:1%
i=int(raw_input("please enter sales:"))
if i<100000:
    print "bonus:",i*0.1
elif 100000<=i<200000:
    print "bonus:",100000*0.1+(i-100000)*0.1
elif 200000<=i<400000:
    print "bonus:",100000*0.1+(200000-100000)*0.1+(i-200000)*0.075
elif 400000<=i<600000:
    print "bonus:",100000*0.1+(200000-100000)*0.1+(400000-200000)*0.075+(i-400000)*0.05
elif 600000<=i<1000000:
    print "bonus:",100000*0.1+(200000-100000)*0.1+(400000-200000)*0.075+(600000-400000)*0.05+(i-600000)*0.03
else:
    print "bonus:",100000*0.1+(200000-100000)*0.1+(400000-200000)*0.075+(600000-400000)*0.05+(1000000-600000)*0.03+(i-1000000)*0.01

#test3 x+100=m^2,x+100+168=n^2

#test4 get today is the day of year

#test5 arrange 3 numbers in incressing order
list=[]
for i in range(0,3):
    x=int(raw_input("please enter number:"))
    list.append(x)
print "original list:",list
for i in range(0,len(list)):
    for j in range(i,len(list)):
        min = list[i]
        if list[j]<min:
            min = list[j]
            index = j
    if list[i]>min:
        temp=list[i]
        list[i]=min
        list[index]=temp
print "sorted list:",list

#test6 fabonacci sequence
def fabonacci(serial_num):
    if serial_num==0:
        return 0
    elif serial_num==1:
        return 1
    else:
        return fabonacci(serial_num-1)+fabonacci(serial_num-2)

serial_num=int(raw_input("plsase enter serial_num:"))
print "sequence is:",fabonacci(serial_num)

#test7 copy data to list
list=[25,38,13]
new_list=[0,]
for i in list:
    new_list.append(i)
print "final list is:",new_list

list=[25,38,13]
new_list=copy.copy(list)
print "final list:",new_list