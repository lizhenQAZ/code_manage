fruits = ['grape', 'raspberry', 'apple', 'banana']
# 拷贝排序
print('----------sorted-----------')
print(sorted(fruits))
print(fruits)
print('----------sorted reverse-----------')
print(sorted(fruits, reverse=True))
print(fruits)
print('----------sorted key-----------')
print(sorted(fruits, key=len))
print(fruits)
print('----------sorted key reverse-----------')
print(sorted(fruits, key=len, reverse=True))
print(fruits)
print('----------sort-----------')

# 就地排序
print(fruits.sort())
print(fruits)
