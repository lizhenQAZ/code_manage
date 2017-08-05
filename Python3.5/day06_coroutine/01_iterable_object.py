from collections import Iterable
from collections import Iterator


class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        pass


my_list = MyList()
print(isinstance(my_list, Iterable))
print(isinstance(my_list, Iterator))