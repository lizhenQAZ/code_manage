def set_func(func):
    def call_func(*args, **kwargs):
        func(*args, **kwargs)
    return call_func


@set_func
def foo1(num):
    print('---foo1---%d' % num)


@set_func
def foo2(num1, num2):
    print('---foo2---%d---%d' % (num1, num2))


foo1(10)
foo2(20, 25)
