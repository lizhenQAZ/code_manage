# 列表切片
l = [10, 20, 30, 40, 50, 60]
print(l[:3])
print(l[3:])

# 对象切片
s = 'bicycle'
print(s[::3])
print(s[::-1])

# 指定字符串切割
s = 'bicycle'
serial = slice(3, 6)
s_li = s.split("\n")
for item in s_li:
    print(item[serial])

# 切片赋值
l = list(range(10))
print(l)  # [0,1,2,3,4,5,6,7,8,9]
l[2:5] = [20, 30]
print(l)  # [0,1,20,30,5,6,7,8,9]
del l[5:7]
print(l)  # [0,1,20,30,5,8,9]
l[2::1] = [11, 12]
print(l)  # [0,1,11,12]
