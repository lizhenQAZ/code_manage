import re


bt = 'bat|blt|bit'
m1 = re.match(bt, 'bat')
m2 = re.match(bt, 'blt')
m3 = re.match(bt, 'bit')
print('m1 %s' % m1.group())
print('m2 %s' % m2.group())
print('m3 %s' % m3.group())