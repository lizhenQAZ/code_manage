# coding: utf-8
# 初始化元组和数组
symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)
print()
import array
array.array('I', (ord(symbol) for symbol in symbols))
print()
