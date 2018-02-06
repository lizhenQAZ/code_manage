# coding: utf-8
# immutable
a = 1


def fun(a):
    a = 2
fun(a)
print(a)  # 1

# mutable
b = []


def fun(b):
    b.append(1)
fun(b)
print(b)  # [1]
