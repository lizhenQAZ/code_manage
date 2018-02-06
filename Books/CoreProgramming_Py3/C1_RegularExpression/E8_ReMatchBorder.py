import re


m1 = re.search('^The', 'The end.')
print('1-', m1.group())

m2 = re.search(r'\bthe', 'bite the dog!')
print('2-', m2.group())