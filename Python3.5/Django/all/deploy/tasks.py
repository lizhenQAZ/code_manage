#-*-coding:utf-8-*-
import time
from celery import task


@task
def sayhello():
    print("任务开始执行")
    time.sleep(10)
    print("任务执行结束")
