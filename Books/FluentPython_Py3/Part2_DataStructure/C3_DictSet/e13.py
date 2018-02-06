# coding: utf-8
# 查找集合中Unicode含有SIGN这个单词的集合
from unicodedata import name
print({name(chr(i), '') for i in range(32, 256) if 'SIGN' in name(chr(i), '')})
