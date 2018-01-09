# coding: utf-8
import subprocess
import time
# 3s重播一次脚本
ADSL_BASH = "adsl-stop; adsl-start"
while True:
    (status, output) = subprocess.getstatusoutput(ADSL_BASH)
    print(status)
    print(output)
    time.sleep(3)
