from collections import Iterable
from collections import Iterator


class Fibonacci(object):
    def __init__(self, num):
        self.num = num
        self.a = 0
        self.b = 1
        self.curpos = 0

    def __iter__(self):
        return Fibonacci()

    def __next__(self):
        if self.curpos <= self.num:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result

        else:
            raise StopIteration


my_array = Fibonacci(5)
for i in range(5):
    print(next(my_array))