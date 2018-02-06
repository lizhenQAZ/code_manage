def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    # 控制遍历的次数
    for i in range(1, len(alist)):  # 从第二个位置开始插入,
        # 控制角标移动
        # 最大角标递增,交换元素位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]


if __name__ == '__main__':
    li = [11, 22, 3, 77, 66, 88]
    insert_sort(li)
    print(li)
