def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n-1)

# 计算递归函数
print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

# 计算一组递归函数
print(map(factorial, range(11)))
print(list(map(factorial, range(11))))