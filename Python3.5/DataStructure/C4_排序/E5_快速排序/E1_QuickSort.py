def quick_sort(alist, start, end):
    """快速排序"""
    """排序终止条件"""
    if start >= end:
        return

    mid = alist[start]
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid
    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)

if __name__ == '__main__':
    li = [11, 22, 3, 77, 66, 88]
    quick_sort(li, 0, len(li) - 1)
    print(li)
