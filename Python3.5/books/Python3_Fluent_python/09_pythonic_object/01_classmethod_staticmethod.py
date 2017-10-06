class Demo:
    @classmethod
    def klassmeth(*cls):
        return cls

    @staticmethod
    def statmeth(*args):
        return args
print(Demo.klassmeth())
print(Demo.klassmeth('spam'))
print(Demo.statmeth())
print(Demo.statmeth('spam'))
