# coding: utf-8
# 累乘
from functools import reduce
from operator import mul


def fact(n):
    return reduce(mul, range(1, n+1))
if __name__ == '__main__':
    print(fact(5))
