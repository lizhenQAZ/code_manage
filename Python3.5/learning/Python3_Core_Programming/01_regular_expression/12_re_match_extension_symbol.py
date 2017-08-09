import re


# 忽略大小写
m1 = re.findall(r'(?i)yes', 'yes? Yes. YES!!')
print('1-', m1)

# 忽略换行符
m2 = re.findall(r'(?s)th.+', '''
    The first line,
    the second line,
    the third line
''')
print('2-', m2)