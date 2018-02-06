# coding: utf-8
# 将非字符串转化成字符串
import collections


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item
if __name__ == '__main__':
    d = StrKeyDict([('2', 'two'), ('4', 'four')])
    print(d['2'])
    print(d[4])
    try:
        print(d[1])
    except KeyError as e:
        print('KeyError')
    print()
    print(d.get('2'))
    print(d.get(4))
    print(d.get(1, 'N/A'))
    print()
    print(2 in d)
    print(1 in d)
