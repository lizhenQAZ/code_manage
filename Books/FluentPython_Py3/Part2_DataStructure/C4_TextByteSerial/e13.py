# coding: utf-8
# 规范化文本匹配
from unicodedata import normalize


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())
if __name__ == '__main__':
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1 == s2)
    print(nfc_equal(s1, s2))
    print(nfc_equal('A', 'a'))
    print()
    s3 = 'Straße'
    s4 = 'strasse'
    print(s3 == s4)
    print(nfc_equal(s3, s4))
    print(fold_equal(s3, s4))
    print(fold_equal(s1, s2))
    print(fold_equal('A', 'a'))
