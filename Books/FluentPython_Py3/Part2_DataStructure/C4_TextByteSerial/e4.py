# coding: utf-8
# 查看gif图像的首部
import struct
fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())
header = img[:10]
print(bytes(header))
print()
print(struct.unpack(fmt, header))
del header
del img
