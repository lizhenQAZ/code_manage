# coding: utf-8
needles = [1, 3, 5]
haystack = [1, 2, 3, 5]
print(len(set(needles) & set(haystack)))
print(len(set(needles).intersection(haystack)))

