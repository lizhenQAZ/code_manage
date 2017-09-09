# Deque() 创建一个空的双端队列
# add_front(item) 从队头加入一个item元素
# add_rear(item) 从队尾加入一个item元素
# remove_front() 从队头删除一个item元素
# remove_rear() 从队尾删除一个item元素
# is_empty() 判断双端队列是否为空
# size() 返回队列的大小


class Deque(object):
    """双端队列"""
    def __init__(self):
        self.__items = []

    def is_empty(self):
        """双端队列判空"""
        return self.__items == []

    def size(self):
        """返回双端队列的大小"""
        return len(self.__items)

    def add_front(self, item):
        """队头添加元素"""
        self.__items.insert(0, item)

    def add_rear(self, item):
        """队尾添加元素"""
        self.__items.append(item)

    def remove_front(self):
        """队头删除元素"""
        return self.__items.pop(0)

    def remove_rear(self):
        """队尾删除元素"""
        return self.__items.pop()

if __name__ == '__main__':
    q = Deque()
    q.add_front('1')
    q.add_front('2')
    q.add_front('3')
    q.add_rear('4')
    q.add_rear('5')
    q.add_rear('6')  # 3 2 1 4 5 6
    print(q.size())  # 3
    print(q.remove_front())  # 3
    print(q.remove_front())  # 2
    print(q.remove_front())  # 1
    print(q.remove_rear())  # 6
    print(q.remove_rear())  # 5
    print(q.remove_rear())  # 4
