# coding: utf-8


# __new__
class Singleton(object):
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    a = 1


# decorator
def Singleton2(cls, *args, **kwargs):
    instance = {}

    def getinstance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getinstance


@Singleton2
class MyClass2:
    a = 1
