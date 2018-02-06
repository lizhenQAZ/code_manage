# coding: utf-8
# 累积
from functools import reduce


def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))
if __name__ == '__main__':
    print(fact(5))
