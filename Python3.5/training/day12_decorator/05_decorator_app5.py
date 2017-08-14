def set_h1(func):
    def call_func(*args, **kwargs):
        return '<h1>' + func(*args, **kwargs) + '</h1>'
    return call_func


def set_level(level):
    def set_title(func):
        def call_func(*args, **kwargs):
            print('当前的日志级别为%s-----' % level)
            return '<title>' + func(*args, **kwargs) + '</title>'
        return call_func
    return set_title


@set_level('1')
@set_h1
def foo3():
    return '---foo3---'


ret = foo3()
print(ret)
