# coding: utf-8
# UnicodeEncodeError处理
city = 'São Paulo'
print(city.encode('utf_8'))
print(city.encode('utf_16'))
print(city.encode('iso8859_1'))
try:
    print(city.encode('cp437'))
except Exception as e:
    print(e)
print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))
