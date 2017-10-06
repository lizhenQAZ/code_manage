suit_types = ['S', 'M', 'L']
suit_sizes = ['36', '38', '41']
# 方式一
suits = tuple(size_x for size_x in suit_sizes)
print(suits)
# 方式二
import array
array_suits = array.array('I', (int(size_x) for size_x in suit_sizes))
print(array_suits)
