import multiprocessing


num = [11, 22]


def work1():
    for i in range(3):
        num.append(i)
        print('---work1---%s---' % num)


def work2():
    print('---work2---%s---' % num)


if __name__ == '__main__':
    num = [11, 22]
    p1 = multiprocessing.Process(target=work1)
    p2 = multiprocessing.Process(target=work2)
    p1.start()
    p1.join()
    p2.start()