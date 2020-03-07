#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/13 0:10

# 协程：单线程下实现并发
# 基于yield并发执行
import time


def producer():
    g = consumer()
    next(g)
    for i in range(10000000):
        g.send(i)  # 实现单线程内程序之间的切换


def consumer():
    while True:
        res = yield  # yiled可以保存状态，yield的状态保存与操作系统的保存线程状态很像，但是yield是代码级别控制的，更轻量级


start_time = time.time()
producer()
stop_time = time.time()
print(stop_time - start_time)

# 如果多个任务都是纯计算的，这种切换反而会降低效率


# 串行执行
import time


def producer():
    res = []
    for i in range(10000000):
        res.append(i)
    return res


def consumer(res):
    pass


start_time = time.time()
res = producer()
consumer(res)
stop_time = time.time()
print(stop_time - start_time)

# yield并不能实现遇到io切换
import time


def consumer():
    """任务1:接收数据,处理数据"""
    while True:
        x = yield


def producer():
    """任务2:生产数据"""
    g = consumer()
    next(g)
    for i in range(10000000):
        g.send(i)
        time.sleep(2)


start = time.time()
producer()  # 并发执行,但是任务producer遇到io就会阻塞住,并不会切到该线程内的其他任务去执行

stop = time.time()
print(stop - start)

# 是单线程下的并发，又称微线程，纤程。协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的。

'''
总结协程特点：

必须在只有一个单线程里实现并发
修改共享数据不需加锁
用户程序里自己保存多个控制流的上下文栈
附加：一个协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（select机制））
'''