#-*- encoding:utf-8 -*-
l=[5,81,84,984,6262,74]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
for c in l:
    print c