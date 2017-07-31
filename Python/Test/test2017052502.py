#!/usr/bin/python
# -*- coding:UTF-8 -*-
# filename:test2017052502.py

#test1 if-elif-else condition code group
flag=1
if flag==0:
    print False
elif flag==1:
    print True
else:
    print "over 1"

#test2 variable assignment
counter=1000
temperature=36.8
name="lizhen"
print counter
print temperature
print name

#teat3 multivariable assignment
#same value
a1=b1=c1=1
print a1,b1,c1
#different values
a2,b2,c2=1000,36.8,"lzihen"
print a2,b2,c2

#test4 delete object reference
var_a,var_b=1000,36.8
print var_a,var_b
del var_a,var_b
print var_a,var_b