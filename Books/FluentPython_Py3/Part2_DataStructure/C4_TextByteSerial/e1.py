# coding: utf-8
# 编码和解码
s = 'café'
print(len(s))
print()
b = s.encode('utf8')
print(b)
print(len(b))
print(b.decode('utf8'))
