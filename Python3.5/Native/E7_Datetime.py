# coding: utf-8
import datetime


day_of_week = datetime.datetime.now().weekday() + 1
print(day_of_week)
cur_time = datetime.datetime.now().strftime('%Y-%m-%d').split('-')
day_of_month = cur_time[2]
# cur_time = datetime.datetime.now().strftime('%j')
print(day_of_month)
day_of_year = datetime.datetime(int(cur_time[0]), int(cur_time[1]), int(cur_time[2])).strftime('%j')
print(day_of_year)
