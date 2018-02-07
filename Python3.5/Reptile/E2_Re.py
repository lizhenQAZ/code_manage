#coding:utf-8
import re

# 普通字符匹配自身
data= 'sh_python2'

# print (re.findall('py',data))

# .的用法
data2 = 'a\nb'
# dotall模式的两种形式
# print (re.findall('a.*b',data2,re.DOTALL))
# print (re.findall('a.*b',data2,re.S))

# 转义字符的用法
data3 = 'dsfa|bdsfdsf'
# print (re.findall('a\|b',data3))


# []
data4 = 'abc-adc'
# print (re.findall('a[bd]c',data4))
# print (re.findall('abc|adc',data4))

data5 = 'shdkfjh12435hfcjgkv'
# print (re.findall('\d+',data5))

data6 = "sjdhfksdh123"
# print (re.findall('\d{3}',data6))

# pattern = re.compile('.*',re.S)
# pattern

print (re.findall(r"a.*bc","a\nbc",re.DOTALL))
print (re.findall(r"a(.*b)c","a\nbc",re.DOTALL))
