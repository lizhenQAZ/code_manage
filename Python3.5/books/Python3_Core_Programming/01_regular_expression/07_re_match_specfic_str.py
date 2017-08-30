import re


patt = '(\w{3})-(\d{3})'
m1 = re.match(patt, 'abc-123')
m2 = re.match(patt, 'abc-xyz')

print('1-%s', m1.groups())
try:
    print('2-%s', m2.groups())
except Exception as e:
    print('%s' % e)