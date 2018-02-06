# coding=utf-8
import os
import sqlite3
import json
import pandas as pd
from pandas import DataFrame
import numpy as np
import MySQLdb


# Read Data
# Reading data locally
df = pd.read_csv('E1.csv')
print(df)

# Reading data from web
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(data_url)
print(df)

# Reading data from mysql
data_mysql = MySQLdb.connect(host='localhost', port=3306, user='guest', passwd='guest', db='001')
df = pd.read_sql('select * from authors;', con=data_mysql)
print(df)
data_mysql.close()

# Reading data from excel
df = pd.read_excel("E1.xlsx")
print(df)

# Writing data to csv
df.to_csv('E1_ExcelToCsv.csv', encoding='utf-8', index=False)

# Reading&Writing data to sqlite3
con = sqlite3.connect('001.db')
c = con.cursor()
c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
con.commit()
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
con.commit()
sql = "SELECT * FROM COMPANY"
df = pd.read_sql(sql, con)
con.close()
print(df)


# Data Transfer
# Head of the data
print(df.head())

# Tail of the data
print(df.tail())

# Extract dimension of data
print(df.shape)

# Extract row names or the index
print(df.index)

# Extract column names
print(df.columns)

# Extract row2~8&column1~2 data
print(df.ix[2:8, 1:3])

# Extract row1、3、5&column2、4 data
print(df.iloc[[1, 3, 5], [2, 4]])

# Extract row3 data
print(df.iloc[3])

# Extrat row2~3 data
print(df.iloc[2:4])

# Extract row3&column2 data
print(df.iloc[3, 2])
print(df.iat[3, 2])

# Drop column3 data
print(df.drop(df.columns[3:4], axis=1))

# Select column tip>8 data
print(df[df.tip > 8])

# Selelct column tip>8 & column total_bill>50 data
print(df[(df.tip > 8) & (df.total_bill > 50)])

# Selelct column tip>8 | column total_bill>50 data
print(df[(df.tip > 8) | (df.total_bill > 50)])

# Select column day、time & (column tip>7 | column total_bill>50) data
print(df[['day', 'time']][(df.tip > 7) | (df.total_bill > 50)])


# Statistic Describe
print(df.describe())


# Handle Data
# Transpose data
print(df.T)

# Sort data
print(df.sort_values(by='tip'))

# Group data
group = df.groupby('day')
print(group.first())
print(group.last())

# Change data
series = pd.Series([0, 1, 2, 3, 4, 5])
print(series)
print(series.replace(0, 1000))
print(series.replace([1, 2, 3], [10, 55, 999]))

# Handle missing data
# 1.Fill miising data
path = 'E1_usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)
print(frame['tz'])
# Replace missing data with number
print(frame['tz'].fillna(11111111))
# Replace missing data with string
print(frame['tz'].fillna('xxxx11111111'))
# Replace missing data with previous data
print(frame['tz'].fillna(method='pad'))
# Replace missing data with the latter data
print(frame['tz'].fillna(method='bfill'))
# 2.Delete missing data
# Delete missing row
print(frame['tz'].dropna(axis=0))
# 3.Fill missing data in interpolation method
czf_data = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
print(czf_data)
# Set column2 data nan
czf_data.ix[2, :] = np.nan
print(czf_data)
# Fill nan in interpolation method
print(czf_data.interpolate())
