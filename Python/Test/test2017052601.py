#!usr/bin/python
# -*/- coding:utf-8 -*-

#test1 compare variables type
a="long"
A=type(a)
print A
B=isinstance(a,A)
print B

#test2 is and == difference
a=[1,2,3]
b=a
print (b is a),(b==a)
b=a[:]
print (b is a),(b==a)

#test3 search even amd odd numbers
list=[11,23,5,4,9,47]
even=[]
odd=[]
while len(list)>0:
    number=list.pop()
    if (number%2==0):
        even.append(number)
    else:
        odd.append(number)
print even,odd

#test4 search string and list
for letter in 'lizhen':
    print "current character is ",letter

fruits=['apple','orange','banana']
for fruit in fruits:
    print "current fruit is ",fruit

#test5 search element through index
fruits=['apple','orange','banana']
for index in range (len(fruits)):
    print index,"-current fruit is ",fruits[index]

#test6 cycle calculation througgh built-in enumerate function
sequense=[11,15,22,62,33,55]
for i,j in enumerate(sequense):
    print i,'-',j

#test7 pass clause usage
for letter in 'lizhen':
    if (letter == 'h'):
        pass
        print "this is pass clause group!"
    else:
        print "current character is ",letter
print "GOOD BYE!"

#test8 range function usage
for i in range(10):
    print i

#test9 search list value
info=['fruits','10000','36.8']
print info[0]
print info[1:2]

#test10 update list value
list=['lizhen',1992,26,'man']
print 'this year is ',list[2]
list[2]=27
print 'next year is ',list[2]

#test11 delete list value
list=['lizhen',1992,26,'man']
print list
del list[3]
print list