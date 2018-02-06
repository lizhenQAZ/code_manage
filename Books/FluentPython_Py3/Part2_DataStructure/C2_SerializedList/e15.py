# coding: utf-8
t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except Exception as e:
    print(e)
finally:
    print(t)
    print()
