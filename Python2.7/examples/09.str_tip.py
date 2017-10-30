#-*- encoding:utf-8 -*-
str='hello world'
# str.find()查询到指定字符的最小索引值
print '*' * 100
print 'find结果: ', str.find('e')
# str.rfind()查询到指定字符的最大索引值
print '*' * 100
print 'rfind结果: ', str.rfind('o')
# str.count()
print '*' * 100
print 'count结果: ', str.count('l')
# str.replace()
print '*' * 100
print 'replace结果: ', str.replace('r','R')
# str.split()
print '*' * 100
print 'split结果:', str.split(' ',0)
# str.capitalize()
print '*' * 100
print 'capitalize结果: ', str.capitalize()
# str.title()
print '*' * 100
print 'title结果: ', str.title()
# str.startswith()
print '*' * 100
print 'startswith结果: ', str.startswith('a')
# str.endswith()
print '*' * 100
print 'endswith结果: ', str.endswith('o')
# str.lower()
print '*' * 100
print 'lower结果: ', str.lower()
# str.upper()
print '*' * 100
print 'upper结果: ', str.upper()
# str.ljust()
print '*' * 100
print 'ljust结果: ', str.ljust(20)
# str.rjust()
print '*' * 100
print 'rjust结果: ', str.rjust(20)
# str.center()
print '*' * 100
print 'center结果: ', str.center(20)
# str.lstrip()
print '*' * 100
print 'lstrip结果: ', str.lstrip('l')
# str.rstrip()
print '*' * 100
print 'rstrip结果: ', str.rstrip('d')
# str.strip()
print '*' * 100
print 'strip结果: ', str.strip('h')
# str.rindex()
print '*' * 100
print 'rindex结果: ', str.rindex('o')
# str.partition()
print '*' * 100
print 'partition结果: ', str.partition('w')
# str.rpartition()
print '*' * 100
print 'rpartition结果: ', str.rpartition('w')
# str.splitlines()
print '*' * 100
print 'splitlines结果: ', str.splitlines()
# str.isalpha()
print '*' * 100
print 'isalpha结果: ', str.isalpha()
# str.isdigit()
print '*' * 100
print 'isdigit结果: ', str.isdigit()
# str.isalnumz()
print '*' * 100
print 'isalnum结果: ', str.isalnum()
# str.isspace()
print '*' * 100
print 'isspace结果: ', str.isspace()
# str.join()
print '*' * 100
print 'join结果: ', str.join(str.split('w'))
