import re

patt1 = '\w+@(\w*\.\w*\.[\w*\.]?)com'
patt2 = '\w+@(\w*\.[\w*\.]*)com'
str = 'www@xxx.yyy.com.ggg.hhh.com'

m1 = re.match(patt1, str)
m2 = re.match(patt2, str)
print('1-%s' % m1.group(1))
print('2-%s' % m2.group(1))