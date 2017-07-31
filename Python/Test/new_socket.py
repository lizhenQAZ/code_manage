#!usr/bin/python
# -*- coding:utf-8 -*-

#socket.gethostname socket.gethostbyname socket.gethostbyname_ex socket.gethostbyaddr socket.getservbyname socket.inet_aton socket.inet_ntoa
import socket
hostname=socket.gethostname()
print hostname
hostip=socket.gethostbyname(hostname)
print hostip
print socket.gethostbyname('www.jb51.com')
print socket.gethostbyname_ex('www.jb51.com')
print socket.gethostbyaddr('192.168.0.1')
print socket.getservbyname('http','tcp')
print socket.getservbyname('telnet','tcp')
hostname=socket.inet_aton('192.168.0.1')
print socket.inet_aton('192.168.0.1')
print socket.inet_ntoa(hostname)

