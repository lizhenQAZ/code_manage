def select_sort(alist):
    """选择排序"""
    n = len(alist)

    # 控制遍历的次数
    for i in range(n-1):  # 排列n-1次
        min_index = i
        # 控制角标移动  # 每次循环找到最小元素的位置，最小角标递增
        for j in range(i, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 交换元素位置
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]

if __name__ == '__main__':
    li = [11, 22, 3, 77, 66, 88]
    select_sort(li)
    print(li)
