#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/13 15:15

from greenlet import greenlet
import time


def eat(name):
    print('%s eat 1' % name)
    # time.sleep(1)
    g2.switch('egon')
    print('%s eat 2' % name)
    g2.switch()


def play(name):
    print('%s play 1' % name)
    g1.switch()
    print('%s play 2' % name)


g1 = greenlet(eat)
g2 = greenlet(play)

g1.switch('egon')

# 使用greenlet模块可以非常简单地实现多个任务的切换

# 单纯的切换（在没有io的情况下或者没有重复开辟内存空间的操作），反而会降低程序的执行速度
# 顺序执行
import time


def f1():
    res = 1
    for i in range(100000000):
        res += i


def f2():
    res = 1
    for i in range(100000000):
        res *= i


start = time.time()
f1()
f2()
stop = time.time()
print('run time1 is %s' % (stop - start))  # 8.892194986343384

# 切换
from greenlet import greenlet
import time


def f1():
    res = 1
    for i in range(100000000):
        res += i
        g2.switch()


def f2():
    res = 1
    for i in range(100000000):
        res *= i
        g1.switch()


start = time.time()
g1 = greenlet(f1)
g2 = greenlet(f2)
g1.switch()
stop = time.time()
print('run time2 is %s' % (stop - start))  # 46.44094800949097
