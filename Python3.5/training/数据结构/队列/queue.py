# Queue() 创建一个空的队列
# enqueue(item) 往队列中添加一个item元素
# dequeue() 从队列头部删除一个元素
# is_empty() 判断一个队列是否为空
# size() 返回队列的大小


class Queue(object):
    """队列"""
    def __init__(self):
        self.__items = []

    def is_empty(self):
        """队列判空"""
        return self.__items == []

    def size(self):
        """返回队列的大小"""
        return len(self.__items)

    def enqueue(self, item):
        """往队列里添加元素"""
        self.__items.insert(0, item)

    def dequeue(self):
        """从队列里删除元素"""
        return self.__items.pop()

if __name__ == '__main__':
    q = Queue()
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    print(q.size())  # 3
    print(q.dequeue())  # 1
    print(q.dequeue())  # 2
    print(q.dequeue())  # 3
