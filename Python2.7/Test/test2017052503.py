#!/usr/bin/python
# -*- coding:UTF-8 -*-
# filename:test2017052502.py

#test1 string processing
str="hello world!"
print str
print str[0]
print str[2:5]
print str[3:]
print str*3
print str+"the end!"

#test2 list processing
list=["1000","36.8","lizhen",]
tinylist=["lizhen",]
print list
print list[0]
print list[0:1]
print list[0:2]
print list[0:]
print list*3
print list+tinylist

#test3 tuple processing
tuple=("1000","36.8","lizhen",)
tinytuple=("lizhen",)
print tuple
print tuple[0]
print tuple[0:1]
print tuple[0:2]
print tuple[0:]
print tuple*3
print tuple+tinytuple

#test4 dictionary precessing
dict={}
dict['count']=1000
dict['temperature']=36.8
dict['name']="lizhen"
tinydict={'name':"lizhen",}
print dict
print dict['count']
print tinydict
print tinydict.keys()
print tinydict.values()
print dict,tinydict