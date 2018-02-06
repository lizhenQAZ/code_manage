# coding: utf-8


# ---1.有序列表排序
# list1 = [10, 20, 30, 40, 50]
# num = int(input('插入的数字: '))
# list1.append(num)
# cnt = len(list1)
# print(cnt)
# for i in range(cnt):
#     # 找到插入的位置
#     if num < list1[i]:
#         for j in range(cnt, i, -1):
#             list1[j-1] = list1[j-2]
#         list1[i] = num
#         break
# print(list1)


# ---2.桶排序
# def bucket_order(nums):
#     # 设置桶大小
#     max_num = max(nums)
#     # 设置桶的序列
#     bucket_nums = [0] * (max_num + 1)
#     # 统计每个数字出现的次数
#     for num in nums:
#         bucket_nums[num] += 1
#     bucket_len = len(bucket_nums)
#     # 设置排序后的序列
#     sorted_nums = []
#     # 排序，找出非0的位置，将当前值插入序列
#     for bucket_num in range(bucket_len):
#         if bucket_nums[bucket_num] != 0:
#             bucket_sub_len = bucket_nums[bucket_num]
#             for index in range(bucket_sub_len):
#                 sorted_nums.append(bucket_num)
#     return sorted_nums
# list2 = [10, 20, 15, 13, 30, 40, 50]
# print(bucket_order(list2))


# ---3.斐波那契数列, 非递归
# def fabo(num):
#     nums = [0, 1]
#     # num >= 2时，对数组进行操作
#     for i in range(num-2):
#         nums.append(nums[i] + nums[i+1])
#     return nums[num-1]
# print(fabo(10))


# ---4.冒泡排序
# def bubble_order(nums):
#     # 设置排序次数
#     order_time = len(nums)-1
#     flag = 1
#     for index in range(order_time, 0, -1):
#         if flag:
#             flag = 0
#             # 设置每次排序的比较次数
#             for j in range(index):
#                 if nums[j] > nums[j+1]:
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
#                     flag = 1
#         else:
#             # 数列已经有序
#             break
#     return nums
# l = [10, 30, 20, 40, 25]
# print(bubble_order(l))


# ---5.快速排序, 分成两个部分，小数在左边，大数在右边
# def quick_order(alist, first, last):
#     if first < last:
#         # 找到每次排序结束的节点位置
#         split_pos = find_pos(alist, first, last)
#         # 节点左边有序排列
#         quick_order(alist, first, split_pos-1)
#         # 节点右边有序排列
#         quick_order(alist, split_pos+1, last)
#
#
# def find_pos(lists, low, high):
#     key = lists[low]
#     while low < high:
#         while low < high and lists[high] >= key:
#             high -= 1
#         lists[low] = lists[high]
#         while low < high and lists[low] <= key:
#             low += 1
#         lists[high] = lists[low]
#     lists[low] = key
#     return low
# lists = [11, 15, 20, 4, 2, 50, 66, 1]
# quick_order(lists, 0, len(lists)-1)
# print(lists)
