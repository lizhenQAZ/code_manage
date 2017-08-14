def set_func(func):
    def call_func():
        func()
    return call_func

@set_func
def foo():
    print('---foo---')

foo()
