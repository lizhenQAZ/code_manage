import bisect


# 已有值的查找和插入易产生问题
# 二分查找
l = [11, 13, 15, 22]
print(bisect.bisect(l, 13))
print(bisect.bisect_left(l, 13))
print(bisect.bisect_right(l, 13))

l.reverse()
print(bisect.bisect(l, 13))
print(bisect.bisect_left(l, 13))  # [22 15 13 11]
print(bisect.bisect_right(l, 13))

# 二分插入排序
l = [11, 13, 15, 22]
bisect.insort(l, 13)
print(l)
l = [11, 13, 15, 22]
bisect.insort_left(l, 13)
print(l)
l = [11, 13, 15, 22]
bisect.insort_right(l, 13)
print(l)


l = [11, 13, 15, 22]
l.reverse()
bisect.insort(l, 13)
print(l)
l = [11, 13, 15, 22]
l.reverse()
bisect.insort_left(l, 13)
print(l)
l = [11, 13, 15, 22]
l.reverse()
bisect.insort_right(l, 13)
print(l)
