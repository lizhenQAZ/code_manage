import re


anyend = '.end'
m1 = re.match(anyend, 'bend')
print('1-%s' % m1)

m2 = re.match(anyend, '\nend')
print('2-%s' % m2)

m3 = re.match('3.14', '3.14')
print('3-%s' % m3)

m4 = re.match('3.14', '3414')
print('4-%s' % m4)

m5 = re.match('3\.14', '3.14')
print('5-%s' % m5)