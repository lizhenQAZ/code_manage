# coding: utf-8
from math import sqrt
from array import array
from itertools import zip_longest


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __repr__(self):
        return 'Vector(%r, %r)' % tuple((x for x in self._components))

    def __abs__(self):
        return sqrt(sum(x * x for x in self._components))

    def __bool__(self):
        for x in self._components:
            if x == 0:
                return True
        return False

    def __add__(self, other):
        return Vector(x + y for x, y in zip_longest(self, other, fillvalue=0.0))

    def __mul__(self, scalar):
        return Vector(x * scalar for x in self._components)

    def __rmul__(self, scalar):
        return self * scalar

    def __getitem__(self, index):
        return self._components[index]


if __name__ == '__main__':
    # 向量结果
    print(Vector([2, 4]))
    # 向量相加
    print(Vector([2, 4]) + Vector([2, 1]))
    # 向量取模
    print(abs(Vector([3, 4])))
    # 向量点积
    print(Vector([3, 4]) * 3)
    # 向量叉积
    print(3 * Vector([3, 4]))
    # 统计字符串出现的次数
    print("afdadxsxsdasdgf".count('a'))
