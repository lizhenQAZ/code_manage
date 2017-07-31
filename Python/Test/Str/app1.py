#-*- encoding:utf-8 -*-
str='hello world'
#find查询到指定字符的最小索引值
print str.find('e')
#rfind查询到指定字符的最大索引值
print str.rfind('o')
#count
print str.count('l')
#replace
print str.replace('r','R')
#split
print str.split(' ',0)
#capitalize
print str.capitalize()
#title
print str.title()
#startswith
print str.startswith('a')
#endswith
print str.endswith('o')
#lower
print str.lower()
#upper
print str.upper()
#ljust
print str.ljust(20)
#rjust
print str.rjust(20)
#center
print str.center(20)
#lstrip
print str.lstrip('l')
#rstrip
print str.rstrip('d')
#strip
print str.strip('h')
#rindex
print str.rindex('o')
#partition
print str.partition('w')
#rpartition
print str.rpartition('w')
#splitlines
print str.splitlines()
#isalpha
print str.isalpha()
#isdigit
print str.isdigit()
#isalnum
print str.isalnum()
#isspace
print str.isspace()
#join
print str.join(str.split('w'))