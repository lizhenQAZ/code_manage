#-*- encoding:utf-8 -*-
Tn=0
Sn=[]
sum=0
n=int(raw_input("个数为："))
a=int(raw_input("数字为："))
for count in range(n):
    Tn+=a
    a*=10
    Sn.append(Tn)
for element in Sn:
    sum+=element
print "sum is ",sum