#!/usr/bin/python
year = int(raw_input("year:\n"))
month = int(raw_input("month:\n"))
day = int(raw_input("day:\n"))
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334,)
leap = 0
sum = 0
if year % 400 == 0 or (year % 4 ==  0 and year % 100 != 0):
    leap = 1
sum = months[month - 1] + day
if leap == 1:
    sum += 1
print sum
