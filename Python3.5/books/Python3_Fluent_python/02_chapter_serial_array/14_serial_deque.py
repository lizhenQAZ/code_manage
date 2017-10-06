from collections import deque
# 创建双向队列
dq = deque(range(10), maxlen=10)
print(dq)

# 队列的正向移动
dq.rotate(3)
print(dq)

# 队列的反向移动
dq.rotate(-3)
print(dq)

# 队列的左侧添加元素
dq.appendleft(20)
print(dq)

# 队列的左侧添加列表
dq.extendleft([30, 40, 50])
print(dq)