#-*- encoding:UTF-8 -*-

import string
s = raw_input("please input a string:\n")
letters=0
spaces=0
digits=0
others=0
for c in s:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        spaces+=1
    elif c.isdigit():
        digits+=1
    else:
        others+=1
print "字母个数为： ",letters
print "空格个数为： ",spaces
print "数字个数为： ",digits
print "其他字符为： ",others