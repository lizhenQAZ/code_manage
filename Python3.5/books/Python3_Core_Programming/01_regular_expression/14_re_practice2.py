import re


string = 'zhen li chen wu'
m = re.findall(r'([^ ]+)', string)
print(m)