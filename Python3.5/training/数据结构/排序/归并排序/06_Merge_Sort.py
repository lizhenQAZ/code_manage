def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist

    m = n // 2
    # 二分
    llist = merge_sort(alist[:m])
    rlist = merge_sort(alist[m:])

    left = 0
    right = 0
    sorted_list = []
    l_len = len(llist)
    r_len = len(rlist)
    while left < l_len and right < r_len:
        if llist[left] <= rlist[right]:
            sorted_list.append(llist[left])
            left += 1
        else:
            sorted_list.append(rlist[right])
            right += 1
    sorted_list.extend(llist[left:])
    sorted_list.extend(rlist[right:])
    return sorted_list


if __name__ == '__main__':
    li = [11, 22, 3, 77, 66, 88]
    sorted_li = merge_sort(li)
    print(sorted_li)
