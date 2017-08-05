#!usr/bin/python
# -*- coding:utf-8 -*-
import re

#test1 re.match
str="I am not a clever boy,but I is well diligent!"
match=re.match(r"(\w+)\s",str)
if match:
    print match.group(0),match.group(1)
    print match.string
    print match.groups()
    print match.pos
    print match.endpos
    print match.start(0)
    print match.end(0)
    print match.span(0)
    print match.expand(r"\1 \1")
else:
    print "no match!"

#test2 re.search
search=re.search(r"(\w+)\s",str)
if search:
    print search.group(0),search.group(1)
else:
    print "no search!"

#test3 re.sub
sub=re.sub(r"\s+","-",str)
print sub

#test4 re.split
print re.split(r"\s+",str)

#test5 re.findall
print re.findall(r"\w+\s",str)

#test6 re.compile
regex=re.compile(r"\w+\s")
print regex.findall(str)

#test7 re.finditer
for i in re.finditer(r"\w+\s",str):
    print i.group()

#test8 re.subn
print regex.subn("hi-",str)