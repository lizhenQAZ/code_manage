import os
import paramiko


def send_cmd(child, cmd, prompt):
    child.sendline(cmd)
    child.expect(prompt)
    print(child.before)


def sshclient_execmd(hostname, port, username, password, adsl_user, adsl_pwd):
    paramiko.util.log_to_file("E5_Test.log")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password)
    # stdin, stdout, stderr = s.exec_command("adsl-start")
    stdin, stdout, stderr = s.exec_command("curl ifconfig.me")
    print(stdout.read())
    print(stderr.read())
    print()
    stdin.write('ping -c 3 www.baidu.com\n')
    print(stdout.read())
    print()
    s.close()


def main():
    addr = os.environ['ADSL_INFO'].split(";")[0]
    hostname, port, username, password, adsl_user, adsl_pwd = *addr.split("@")[1].split(":"), addr.split("@")[0], *os.environ['ADSL_INFO'].split(";")[1:-1]
    print(hostname, port, username, password, adsl_user, adsl_pwd)
    sshclient_execmd(hostname, port, username, password, adsl_user, adsl_pwd)


if __name__ == "__main__":
    main()
