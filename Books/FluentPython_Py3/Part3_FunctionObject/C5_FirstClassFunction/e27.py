# coding: utf-8
# unicode规范化函数
import unicodedata
import functools
nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))
