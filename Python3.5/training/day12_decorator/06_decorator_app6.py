class subject(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return self.func()


@subject
def foo3():
    return '---foo3---'


ret = foo3()
print(ret)
