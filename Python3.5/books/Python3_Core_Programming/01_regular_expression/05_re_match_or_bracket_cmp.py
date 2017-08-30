import re


m1 = re.match('r2c2|o3d4', 'o3d4')
print('1-%s' % m1)

m2 = re.match('r2c2|o3d4', 'r2c2')
print('2-%s' % m2)

m3 = re.match('[ro][23][cd][24]', 'o3d4')
print('3-%s' % m3)

m4 = re.match('[ro][23][cd][24]', 'r2c2')
print('4-%s' % m4)