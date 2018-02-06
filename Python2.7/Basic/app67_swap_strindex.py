#-*- encoding=utf-8 -*-


def swap_max_and_min_value():
    global string
    head_str = string[0]
    tail_str = string[len(string)-1]
    max_val = string[0]
    min_val = string[0]
    for i in string:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i


    for i, element in enumerate(string):
        print i, element
        if element == max_val:
            string = element + string[1:i] + head_str + string[i+1:]
        elif element == min_val:
            string = string[0:i] + tail_str + string[i+1:len(string)-1] + element


def swap(x, y):
    temp = x
    x = y
    y = temp
    return y, x


string = '516843'
print(string)
swap_max_and_min_value()
print(string)