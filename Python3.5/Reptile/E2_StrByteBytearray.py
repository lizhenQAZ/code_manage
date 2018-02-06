# str
str1 = '人生'
print('*'*30)
print('字符串的编码类型: ', type(str1.encode()))
print('字符串的编码值: ', str1.encode())
# bytes
byte1 = str1.encode()
print('*'*30)
print('字节类型的解码类型: ', type(byte1.decode()))
print('字节类型的解码值: ', byte1.decode())
# bytearray
bytearray1 = bytearray(str1.encode())
print('*'*30)
print('字节数组类型的解码类型: ', type(bytearray1))
print('字节数组类型的解码值: ', bytearray1)
bytearray1[:2] = bytearray('呵呵'.encode())
print('字节数组类型修改后的解码值: ', bytearray1)
