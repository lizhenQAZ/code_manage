def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)

    # 控制遍历的次数
    for i in range(n-1):  # 排列n-1次
        # 一般情况下稳定
        # O(n^2)
        flag = False
        # 控制角标移动  # 一次循环最大比较n-1次，最高角标递减
        for j in range(n-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                flag = True
        # 如果已经有序，直接退出循环
        if not flag:
            break

if __name__ == '__main__':
    li = [11, 22, 3, 77, 66, 88]
    bubble_sort(li)
    print(li)
