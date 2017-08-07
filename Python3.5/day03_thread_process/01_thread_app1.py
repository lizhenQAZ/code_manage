from threading import Thread


def work1(nums):
    nums.append(44)
    print('---work1---%s' % nums)


def work2(nums):
    print('---work2---%s' % nums)


g_nums = [11, 25, 23]
t1 = Thread(target = work1, args = (g_nums,))
t1.start()
t2 = Thread(target = work2, args = (g_nums,))
t2.start()