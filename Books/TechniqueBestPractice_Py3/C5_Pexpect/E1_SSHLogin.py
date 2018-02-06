import pexpect


# 启动ssh程序
child = pexpect.spawn('ssh python@ubuntu16_lz')
fout = open('mylog.txt', 'w')
print(child)
child.logfile = fout
# 等待产生输出
child.expect('password:')
# 匹配成功,发送字符串回应
child.sendline(input('输入密码:'))
child.expect('$')
child.sendline('ls /home')
child.expect('$')
