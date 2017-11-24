def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    # 控制间隙
    gap = n // 2
    while gap > 0:
        # 控制排序次数
        for i in range(gap, n):
            j = i
            # 控制比较次数
            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]
                j -= gap
        # 每次间隙减半
        gap //= 2

if __name__ == '__main__':
    li = [11, 22, 3, 77, 66, 88]
    shell_sort(li)
    print(li)
    li = [2, 1, 3, 4]
    shell_sort(li)
    print(li)
