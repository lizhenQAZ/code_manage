# coding: utf-8
import random


def print_string(strs):
    total_len = len(strs)
    max_len = 0
    max_strs = []
    for i in range(total_len):
        start = i
        for j in range(start+1, total_len):
            if strs[j] in strs[start:j]:
                temp_str = strs[start:j]
                if len(temp_str) == max_len:
                    max_strs.append({start: temp_str, j-1: max_len})
                elif len(temp_str) > max_len:
                    max_len = len(temp_str)
                    max_strs = []
                    max_strs.append({start: temp_str, j-1: max_len})
                start = j
                print(i, temp_str)
            # else:
            #     start = j + 1
    print(max_strs)

if __name__ == '__main__':
    base_str = 'ABCDEFGHIJKLMN1234567890'
    random_str = ''
    for i in range(50):
        random_str += random.choice(base_str)
    print(random_str)
    print_string(random_str)
