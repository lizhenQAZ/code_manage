# 字符串长度排序
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
# print(sorted(fruits, key=len))

# 字符串逆序
# python3.5不支持
# print(sorted(fruits, key=reverse))
fruits.reverse()
print(fruits)

# reduce
from functools import reduce
from operator import add
print(reduce(add, range(101)))
print(sum(range(101)))

# lambda
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda item : item[::-1]))

# 判断可调用类型
print(callable(13))


# 函数注解
def clip(content: str, max_len: 'int >0' = 80) -> str:
    return "haha"
print(clip.__annotations__)

# reduce
from functools import reduce
from operator import mul
def fact(n):
    return reduce(mul, range(1, n+1))
print(fact(6))

# partial
from functools import partial
# 固定第一个参数为5
five = partial(mul, 5)
print(five(6))

