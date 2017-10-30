#-*- encoding:utf-8 -*-
if __name__ == '__main__':
    n = input('enter integer num: ')
    m = input('enter position integer num: ')
    number = []
    for i in range(n):
        number.append(input('please enter a num: '))
    print('原始列表： %s' % number)
    head_number = number[:n-m]
    print('头列表： %s' % head_number)
    tail_number = number[n-m:]
    print('尾列表： %s' % tail_number)
    dest_number = []
    dest_number.extend(tail_number)
    dest_number.extend(head_number)
    print('修改后的列表： %s' % dest_number)