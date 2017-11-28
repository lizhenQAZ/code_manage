# coding: utf-8


class A(object):
    def __init__(self):
        pass

    def execute(self):
        self.run()

    def run(self):
        print("A的方法")


class B(A):
    def __init__(self):
        pass

    def exe(self):
        super(B, self).execute()

    def run(self):
        print("B的方法")


if __name__ == '__main__':
    b = B()
    b.exe()
