# coding: utf-8
# 逆序
def reverse(word):
    return word[::-1]
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(reverse('testing'))
print(sorted(fruits))
print(sorted(fruits, key=reverse))
