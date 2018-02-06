# coding: utf-8
# bytes和bytearray对象
cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])
print()
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])
