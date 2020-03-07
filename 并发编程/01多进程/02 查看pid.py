#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/5 19:59

from multiprocessing import Process
import time, os


def task():
    print('子进程：%s is running,parent id is <%s>' % (os.getpid(), os.getppid()))
    time.sleep(1)
    print('子进程：%s is done,parent id is <%s>' % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    p = Process(target=task)  # target表示调用对象，即子进程要执行的任务
    p.start()

    print('主进程：', os.getpid(), os.getppid())

# 当前进程---> os.getpid()
# 当前进程的父进程---> os.getppid()
