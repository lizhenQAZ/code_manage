import re


str = input('please enter 163 e-mail: ')
exp = '[a-zA-Z0-9_]{8,12}@163\.com'  # 文件结束标志   '.'转义
exp = '[a-zA-Z0-9_]{8,12}@163\.com$'
flag = re.match(exp, str)
if flag:
    print(True)
else:
    print(False)