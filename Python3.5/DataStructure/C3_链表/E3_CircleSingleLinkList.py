class Node(object):
    def __init__(self, item):
        # 存放数据元素
        self.item = item
        # 指定下一个结点
        self.next = None


class CircleSingleLinkList(object):
    """单向循环链表"""
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
        if self.is_empty():
            return 0
        cur = self.__head
        count = 0
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count + 1

    def search(self, item):
        """查找指定结点"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            cur = cur.next
        # 判断尾结点
        if cur.item == item:
            return True
        else:
            return False

    def travel(self):
        """打印所有结点"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=' ')
            cur = cur.next
        # 打印尾结点
        print(cur.item)

    def add(self, item):
        """向链表头部增加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        cur = self.__head
        # 获取尾结点的位置
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """向列表尾部增加元素"""
        if self.is_empty():
            self.add(item)
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node = Node(item)
        cur.next = node
        node.next = self.__head

    def insert(self, pos, item):
        """向列表指定位置插入元素"""
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
            cur.next = node

    def remove(self, item):
        # 源码参考
        # if self.is_empty():
        #     return
        # cur = self.__head
        # # 记录前一个结点的位置
        # pre = None
        # while cur.next != self.__head:
        #     if cur.item == item:
        #         # 如果结点是头结点
        #         if cur == self.__head:
        #             while cur.next != self.__head:
        #                 cur = cur.next
        #             # 获取尾结点
        #             cur.next = self.__head.next
        #             self.__head = self.__head.next
        #             return
        #         # 如果结点是中间结点
        #         else:
        #             pre.next = cur.next
        #             return
        #     pre = cur
        #     cur = cur.next
        # # 获取尾结点
        # if cur.item == item:
        #     if self.length() == 1:
        #         self.__head = None
        #     else:
        #         pre.next = self.__head
        # return

        if self.is_empty():
            return
        cur = self.__head
        # 记录前一个结点的位置
        pre = None
        # 非尾节点
        while cur.next != self.__head:
            if cur.item == item:
                # 当前节点是头结点，将头结点指向当前节点的后一个节点
                if cur == self.__head:
                    self.__head = cur.next
                # 不是头结点，将当前节点的前一个节点指向后一个节点
                else:
                    pre.next = cur.next
                return
            pre = cur
            cur = cur.next
        # 尾节点
        # 能够找到，删除尾节点
        if cur.item == item:
            # 如果当前只有一个节点，将头结点置空
            if self.length() == 1:
                self.__head = None
            # 多个节点
            else:
                pre.next = self.__head
            return


if __name__ == "__main__":
    single = CircleSingleLinkList()
    print(single.is_empty())  # 无元素时，True

    single.add(1)
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
