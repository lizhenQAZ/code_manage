# coding: utf-8
# 默认编码遇到的问题
print(open('cafe.txt', 'w', encoding='utf_8').write('café'))
print(open('cafe.txt').read())
