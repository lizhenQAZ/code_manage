# coding: utf-8
# 处理UnicodeDecodeError
octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))
try:
    print(octets.decode('utf_8'))
except Exception as e:
    print(e)
print(octets.decode('utf_8', errors='replace'))
