import re


s = 'That and this!'
m1 = re.findall('(th\w+) and (th\w+)', s, re.I)
print('1-', m1)
m2 = [g.groups() for g in re.finditer('(th\w+) and (th\w+)', s, re.I)]
print('2-', m2)
m3 = re.findall('(th\w+)', s, re.I)
print('3-', m3)
m4 = [g.group(1) for g in re.finditer('(th\w+)', s, re.I)]
print('4-', m4)