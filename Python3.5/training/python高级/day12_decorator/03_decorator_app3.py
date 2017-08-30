def set_func(func):
    def call_func(*args, **kwargs):
        return func(*args, **kwargs)
    return call_func


@set_func
def foo1(num):
    return '---foo1---%d' % num


@set_func
def foo2(num1, num2):
    return '---foo2---%d---%d' % (num1, num2)


ret = foo1(10)
print(ret)

ret = foo2(20, 25)
print(ret)
