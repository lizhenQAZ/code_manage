#coding:utf-8

# data = 'sh_python2'
data = '上海_python2'
print(type(data))
print(data)

print('*'*50)
b_data = data.encode()
print(type(b_data))
print(b_data)

s_data = b_data.decode('gbk')
print(type(s_data))
print(s_data)
