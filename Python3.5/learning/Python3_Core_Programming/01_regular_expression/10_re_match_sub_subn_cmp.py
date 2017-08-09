import re


m1 = re.sub('x', 'lizhen', 'x hello x')
print('1-', m1)

m2 = re.subn('x', 'lizhen', 'x hello x')
print('2-', m2)