class Stack(object):
    """栈:通过列表或链表的实现"""
    def __init__(self):
        self.__items = []

    def spush(self, item):
        """添加元素到栈顶"""
        self.__items.append(item)

    def spop(self):
        """删除栈顶元素"""
        return self.__items.pop()

    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            return
        return self.__items[-1]

    def is_empty(self):
        """判断栈顶元素为空"""
        return self.__items == []

    def count(self):
        """判断栈中的元素"""
        return len(self.__items)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())  # True
    print(stack.count())  # 0
    stack.spush(1)
    stack.spush(2)
    print(stack.is_empty())  # False
    print(stack.count())  # 2
    print(stack.peek())  # 2
    print(stack.spop())  # 2
    print(stack.is_empty())  # False
    print(stack.count())  # 1
