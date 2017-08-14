def set_h1(func):
    def call_func(*args, **kwargs):
        return '<h1>' + func(*args, **kwargs) + '</h1>'
    return call_func


def set_title(func):
    def call_func(*args, **kwargs):
        return '<title>' + func(*args, **kwargs) + '</title>'
    return call_func


@set_title
@set_h1
def foo3():
    return '---foo3---'


ret = foo3()
print(ret)
