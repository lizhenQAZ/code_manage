#coding:utf-8
import json

data = '{"class":"sh_python2"}'

dict_data=json.loads(data)
# print(type(dict_data))
#
# str_data = json.dumps(dict_data)
# print (type(str_data))

f = open('07_data.txt','w')
json.dump(dict_data,f)
f.close()

f = open('07_data.txt','r')
data = json.load(f)
print (data)
print (type(data))