from collections import Iterable
from collections import Iterator


class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator


class MyIterator(object):
    def __init__(self, mylist):
        self.mylist = mylist
        self.curpos = 0

    def __next__(self):
        if self.curpos < len(self.mylist.container):
            container = self.mylist.container[self.curpos]
            self.curpos += 1
            return container

        else:
            raise StopIteration

    def __iter__(self):
        return self


my_list = MyList()
my_list.add('nihao')
my_list.add('hha')
my_list.add('python')
for var in my_list:
    print(var)