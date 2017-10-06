# 解码和编码方式必须一致
# encode
str = 'haha'
enc_str = str.encode('utf-8')
print(enc_str)
# decode
dec_str = enc_str.decode('utf-8')
print(dec_str)
# 获取文件编码
# fp = open("dummy.txt")
# print(fp.encoding)
# fp.close()


# bytes
# 获取字节对象
cafe = bytes('cafe', encoding='utf-8')
print(cafe)
# 获取字节元素
print(cafe[0])
# 获取字节切片对象
print(cafe[:1])

# bytearray
# 获取字节数组对象
cafe_arr = bytearray(cafe)
print(cafe_arr)

# 获取字节数组切片对象
print(cafe_arr[-1:])

# 编码出错处理
# 忽略
city = 'Beijing'
print(city.encode('utf-8', errors='ignore'))
# 替换成?
print(city.encode('utf-8', errors='replace'))
# 替换成xml实体
print(city.encode('utf-8', errors='xmlcharrefreplace'))

# 字节序
# 小字节序
city = "Haerbing"
print(list(city.encode('utf_16le')))
# 大字节序
print(list(city.encode('utf_16be')))

