class Node(object):
    def __init__(self, item):
        # 存放数据元素
        self.item = item
        # 指定下一个结点
        self.next = None
        # 指定前一个结点
        self.pre = None


class DoubleLinkList(object):
    """双向链表"""
    def __init__(self):
        """头元素为空"""
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        # if self.__head is None:
        #     return True
        # else:
        #     return False
        return self.__head is None

    def length(self):
        """计算链表的长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def search(self, item):
        """查找指定结点"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def travel(self):
        """打印所有结点"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next

    def add(self, item):
        """向链表头部增加元素"""
        node = Node(item)
        if not self.is_empty():
            node.next = self.__head
            self.__head.pre = node
        self.__head = node

    def append(self, item):
        """向列表尾部增加元素"""
        if self.is_empty():
            self.add(item)
            return
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        node = Node(item)
        node.pre = cur
        cur.next = node

    def insert(self, pos, item):
        """向列表指定位置插入元素"""
        if self.is_empty():
            self.add(item)
            return
        if pos < 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            index = 0
            cur = self.__head
            while index < pos - 1:
                index += 1
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            node.pre = cur
            cur.next.pre = node
            cur.next = node

    def remove(self, item):
        # 参考源码
        # cur = self.__head
        # while cur is not None:
        #     if cur.item == item:
        #         # 如果是结点是中间结点
        #         if cur.next is not None:
        #             cur.pre.next = cur.next
        #             cur.next.pre = cur.pre
        #             return
        #         # 如果结点是头结点
        #         elif cur == self.__head:
        #             # 如果只有一个结点
        #             if self.length() == 1:
        #                 self.__head = None
        #                 return
        #             else:
        #                 self.__head.next = cur.next
        #                 cur.next.pre = self.__head
        #                 return
        #         # 如果结点是尾结点
        #         else:
        #             cur.pre.next = None
        #             cur.pre = None
        #             return
        #     cur = cur.next

        cur = self.__head
        while cur is not None:
            if cur.item == item:
                # 有后续节点，判断当前节点是否是头结点
                if cur.next is not None:
                    # 是头节点，将当前节点的后一个节点指向头结点的
                    if cur == self.__head:
                        self.__head = cur.next
                    # 不是头节点，将当前节点的后一个节点指向头结点的
                    else:
                        cur.next.pre = cur.pre
                        cur.pre.next = cur.next
                    return
                # 没有后续节点，判断是否只有一个节点
                # 只有一个节点，当前节点置为空
                if self.length() == 1:
                    self.__head = None
                # 不是一个节点，当前节点前一个节点指向为空
                else:
                    cur.pre.next = None
                return
            cur = cur.next


if __name__ == "__main__":
    single = DoubleLinkList()
    print(single.is_empty())  # 无元素时，True

    single.add(1)
    single.travel()  # 链表内容，1
    print(' ')
    single.add(2)
    print(single.is_empty())  # 增加两个元素，False
    print(single.length())  # 链表长度，2
    single.travel()  # 链表内容，2 1
    print(' ')

    print(single.search(2))  # 链表搜索元素，true
    print(single.search(3))  # false

    single.add(5)  # 链表头部增加元素
    single.travel()  # 5 2 1
    print(' ')

    single.append(3)  # 链表尾部增加元素
    single.travel()  # 链表内容，5 2 1 3
    print(' ')

    single.insert(1, 4)  # 链表指定位置增加元素
    single.travel()  # 5 4 2 1 3
    print(' ')

    single.remove(1)  # 链表删除指定元素
    single.travel()  # 5 4 2 3
    print(' ')
