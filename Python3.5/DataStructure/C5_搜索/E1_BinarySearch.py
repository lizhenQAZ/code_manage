def binary_search(alist, item):
    n = len(alist)
    if n == 0:
        return False
    else:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            return binary_search(alist[mid+1:], item)
        else:
            return binary_search(alist[:mid], item)


if __name__ == '__main__':
    li = [11, 22, 3, 77, 66, 88]
    print(binary_search(li, 77))
    print(binary_search(li, 55))
