from IPy import IP


print(">"*20, " IP处理 ", "<"*20)
print("="*20, " IP基本处理 ", "="*20)
print("IPv4类型:", IP("10.0.0.0/8").version())
print("IPv6类型:", IP("::1").version())
print("IP网段下的总个数:", IP("192.168.0.0/16").len())
print("IP网段下的所有IP:")
# for index, x in enumerate(IP("192.168.0.0/16")):
#     print("第", index, "个IP地址：", x)
print("地址反向解析:", IP("192.168.78.12").reverseNames())
print("私网ip类型:", IP("192.168.78.12").iptype())
print("公网ip类型:", IP("8.8.8.8").iptype())
print("ip转化成整形:", IP("8.8.8.8").int())
print("ip转化成十六进制:", IP("8.8.8.8").strHex())
print("十六进制转化成IP形式:", IP(0x8080808))
print("网络地址转换1:", IP("192.168.1.0").make_net("255.255.255.0"))
print("网络地址转换2:", IP("192.168.1.0/255.255.255.0", make_net=True))
print("网络地址转换3:", IP("192.168.1.0-192.168.1.255", make_net=True))
print("网段输出1", IP("192.168.1.0/24").strNormal(0))
print("网段输出2", IP("192.168.1.0/24").strNormal(1))
print("网段输出3", IP("192.168.1.0/24").strNormal(2))
print("网段输出4", IP("192.168.1.0/24").strNormal(3))


print("="*20, "多网络计算", "="*20)
print("判断ip地址是否在另一个网段", '192.168.1.100' in IP('192.168.1.0/24'))
print("判断网段是否在另一个网段", IP('192.168.1.0/24') in IP('192.168.0.0/16'))
print("判断网段是否重叠1", True if IP("192.168.0.0/23").overlaps("192.168.1.0/24") else False)
print("判断网段是否重叠2", True if IP("192.168.1.0/24").overlaps("192.168.2.0") else False)
print("判断IP和网段的信息:'")
ip_s = input("please input an IP or net-range: ")
ips = IP(ip_s)
if len(ips) > 1:
    print("IP网络地址:", ips.net())
    print("IP网络掩码地址:", ips.netmask())
    print("IP网络广播地址:", ips.broadcast())
    print("IP网络子网数:", len(ips))

print("IP反向解析:", ips.reverseNames()[0])
print("IP十六进制地址:", ips.strHex())
print("IP二进制地址:", ips.strBin())
print("IP地址类型:", ips.iptype())
