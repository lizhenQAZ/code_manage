#!usr/bin/python
# -*- coding:utf-8 -*-
import re

# re.match
mess = "I am not a clever boy,but I is well diligent!"
match_mess = re.match(r"(\w+)\s", mess)
print '*'*100
if match_mess:
    print match_mess.group(0), match_mess.group(1)
    print match_mess.string
    print match_mess.groups()
    print match_mess.pos
    print match_mess.endpos
    print match_mess.start(0)
    print match_mess.end(0)
    print match_mess.span(0)
    print match_mess.expand(r"\1 \1")
else:
    print "no match!"

# re.search
search_mess = re.search(r"(\w+)\s", mess)
print '*'*100
search_result = search_mess.group(0) + search_mess.group(1) if search_mess else "no search!"
print search_result

# re.sub
sub_mess = re.sub(r"\s+", "-", mess)
print '*'*100
print sub_mess

# re.split
print '*'*100
print re.split(r"\s+", mess)

# re.findall
print '*'*100
print re.findall(r"\w+\s", mess)

# re.compile
pattern = re.compile(r"\w+\s")
print '*'*100
print pattern.findall(mess)

# re.finditer
print '*'*100
for i in re.finditer(r"\w+\s", mess):
    print i.group()

# re.subn
print '*'*100
print pattern.subn("hi-", mess)
