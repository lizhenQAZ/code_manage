import dns.resolver

# baidu.com
print(">"*20, " 域名解析 ", "<"*20)
print("="*20, " A记录 ", "="*20)
domain = input("Please input a domian: ")
a = dns.resolver.query(domain, 'A')
for i in a.response.answer:
    for j in i:
        print("A记录：", j)


print("="*20, " MX记录 ", "="*20)
mx = dns.resolver.query(domain, 'MX')
for i in mx:
    print("MX记录： 属性=", i.preference, " 邮箱=", i.exchange)


print("="*20, " NS记录 ", "="*20)
ns = dns.resolver.query(domain, 'NS')
for i in ns.response.answer:
    for j in i:
        print("NS记录：", j.to_text())


# print("="*20, " CNAME记录 ", "="*20)
# cname = dns.resolver.query(domain, 'CNAME')
# for i in cname.response.answer:
#     for j in i:
#         print("CNAME记录：", j.to_text())


print("="*20, " 域名轮询 ", "="*20)
import http.client as httplib


ip_list = list()
appdomain = "www.baidu.com"


def get_iplist(domain=""):
    try:
        a = dns.resolver.query(domain, "A")
        print(domain)
    except Exception as e:
        print("域名解析失败:", str(e))
        return
    for i in a.response.answer:
        for j in i:
            ip_list.append(j)
    return True


def checkip(ip):
    ip = str(ip)
    checkurl = ip + ":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)
    try:
        conn.request("GET", "/", headers={"Host": appdomain})
        r = conn.getresponse()
        getcontent = r.read(15).decode('utf-8')
        print(getcontent)
    finally:
        if getcontent == '<!DOCTYPE html>':
            print(ip + "[OK]")
        else:
            print(ip + "[Error]")

if __name__ == "__main__":
    if get_iplist(appdomain) and len(ip_list) > 0:
        for ip in ip_list:
            checkip(ip)
    else:
        print("域名解析错误")
