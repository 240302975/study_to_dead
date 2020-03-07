#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/10 22:39

# 信号量
from threading import Thread, Semaphore, currentThread
import time, random

sm = Semaphore(3)


def task():
    # sm.acquire()
    # print('%s in' % currentThread().getName())
    # sm.release()
    with sm:
        print('%s in' % currentThread().getName())
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task)
        t.start()

'''
Semaphore管理一个内置的计数器，
每当调用acquire()时内置计数器-1；
调用release() 时内置计数器+1；
计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。
'''

# 信号量也是一把锁，可以指定信号量为5，
# 对比互斥锁同一时间只能有一个任务抢到锁去执行，信号量同一时间可以有多个任务拿到锁去执行
