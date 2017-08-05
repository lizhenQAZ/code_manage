#-*- encodig:utf-8 -*-
list=[1,5,8,25,77,85]
length=len(list)
count=0
num=int(raw_input("please enter a number:"))
if list[0]>=list[1]:
    if num >= list[0]:
        pass
    else:
        for i in range(length):
            if num>=list[i]:
                count=i
                break
else:
    count=length
    if num <= list[0]:
        pass
    else:
        for i in range(length):
            if num <= list[i]:
                count = i
                print i
                break
list.insert(count,num)
print list