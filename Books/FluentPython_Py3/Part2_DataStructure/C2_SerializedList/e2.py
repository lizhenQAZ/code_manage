# coding: utf-8
# 列表推导式(unicode码)
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)
print()
