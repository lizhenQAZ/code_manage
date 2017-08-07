import re


var = input('please enter a var name:')
# exp = '[A-Za-z_][\w_]*' # 中文可以匹配
exp = '[A-Za-z_][a-zA-Z0-9_]*'
if re.match(exp, var):
    print(True)
else:
    print(False)