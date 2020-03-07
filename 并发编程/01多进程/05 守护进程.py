#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/6 18:04

from multiprocessing import Process
import time


def task(name):
    print('%s is running' % name)
    time.sleep(1)
    p = Process(target=task, args=(3,))
    # 守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
    p.start()


if __name__ == '__main__':
    p = Process(target=task, args=('子进程1',))
    p.daemon = True
    p.start()

    p.join()
    print('主')  # 守护进程会在主进程代码执行结束后就终止


# 练习题
from multiprocessing import Process
import time


def foo():
    print(123)
    time.sleep(1)
    print("end123")


def bar():
    print(456)
    time.sleep(3)
    print("end456")


if __name__ == '__main__':
    p1 = Process(target=foo)
    p2 = Process(target=bar)

    p1.daemon = True  # 守护进程
    p1.start()
    p2.start()
    print("main-------")

# main-------  主进程死掉，123不会再执行
# 456
# end456


# 强调：主进程kill,守护进程kill
