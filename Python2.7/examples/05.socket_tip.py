#!usr/bin/python
# -*- coding:utf-8 -*-
import socket

# socket.gethostname()
host_name = socket.gethostname()
print('*'*100)
print 'gethostname结果: ', host_name

# # socket.gethostbyname()
# host_ip = socket.gethostbyname(host_name)
# print('*'*100)
# print 'gethostbyname结果: ', host_ip
# print 'http://www.baidu.com - gethostbyname结果: ', socket.gethostbyname('http://www.baidu.com')

# socket.gethostbyname_ex()
# print('*'*100)
# print 'gethostbyname_ex结果: ', socket.gethostbyname_ex('www.jb51.com')

# socket.gethostbyaddr()
print('*'*100)
print 'gethostbyaddr结果: ', socket.gethostbyaddr('192.168.0.1')

# socket.getservbyname()
print('*'*100)
print 'http - getservbyname结果: ', socket.getservbyname('http', 'tcp')
print 'telnet - getservbyname结果: ', socket.getservbyname('telnet', 'tcp')

# socket.inet_aton()
hostname=socket.inet_aton('192.168.0.1')
print('*'*100)
print 'inet_aton结果: ', hostname
print 'inet_ntoa结果: ', socket.inet_ntoa(hostname)
