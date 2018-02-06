# coding: utf-8
from collections import OrderedDict


# 打印看不出效果
key_value = {'c': 10, 'a': 5, 'b': 7}
print(key_value)
sorted(key_value.items(), key=lambda x: x[1])
print(key_value)


ordered_dict = OrderedDict()
ordered_dict.clear()
ordered_dict['abc'] = 'abc'
print(ordered_dict)
ordered_dict['234'] = '234'
print(ordered_dict)
