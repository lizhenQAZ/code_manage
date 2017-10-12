import psutil
import datetime


print(">"*20, " 系统性能信息 ", "<"*20)
print("="*20, " cpu信息 ", "="*20)
print("user的cpu时间比:", psutil.cpu_times().user)
print("cpu的逻辑个数:", psutil.cpu_count())
print("cpu的物理个数:", psutil.cpu_count(logical=False))


print("="*20, " 内存信息 ", "="*20)
mem = psutil.virtual_memory()
print("全部内存信息:", mem)
print("内存总数:", mem.total)
print("空闲内存数:", mem.free)
print("全部交换内存信息:", psutil.swap_memory())


print("="*20, " 磁盘信息 ", "="*20)
print("磁盘完整信息:", psutil.disk_partitions())
print("磁盘分区的使用情况:", psutil.disk_usage('/'))
print("磁盘的总IO个数:", psutil.disk_io_counters())
print("磁盘的每个分区的IO个数:", psutil.disk_io_counters(perdisk=True))


print("="*20, " 网络信息 ", "="*20)
print("网络的总IO数", psutil.net_io_counters())
print("每个网络的IO数", psutil.net_io_counters(pernic=True))


print("="*20, "其他系统信息", "="*20)
print("系统用户信息:", psutil.users())
print("系统开机时间", psutil.boot_time())
print("系统开机时间格式转化", datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))


print(">"*20, " 系统进程管理 ", "<"*20)
print("="*20, " 进程信息 ", "="*20)
print("所有的进程PID:", psutil.pids())
p = psutil.Process(1283)
print("当前进程名:", p.name())
print("当前进程路径:", p.exe())
print("当前进程工作目录:", p.cwd())
print("当前进程状态:", p.status())
print("当前进程的创建时间:", p.create_time())
print("当前进程的uid信息:", p.uids())
print("当前进程的gid信息:", p.gids())
print("当前进程的cpu时间:", p.cpu_times())
print("当前进程的cpu亲和度:", p.cpu_affinity())
print("当前进程的内存利用率", p.memory_percent())
print("当前进程的内存rss、vms信息", p.memory_info())
print("当前进程的IO信息", p.io_counters())
print("当前进程的fs、family、laddr等信息", p.connections())
print("当前进程的线程数", p.num_threads())


print("="*20, " popen信息 ", "="*20)
from subprocess import PIPE
p = psutil.Popen(["/usr/bin/python3", "-c", "print('hello')"], stdout=PIPE)
print("当前命令:", p.name())
print("当前命令的用户:", p.username())
print("当前命令的结果:", p.communicate())
# print("当前命令的cpu时间:", p.cpu_times())
