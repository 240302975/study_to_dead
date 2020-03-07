#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/10 21:24

# 死锁
# from threading import Thread, Lock
# import time
#
# mutexA = Lock()
# mutexB = Lock()
#
#
# class MyThread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#
#     def f1(self):
#         mutexA.acquire()
#         print('%s 拿到A锁' % self.name)
#
#         mutexB.acquire()
#         print('%s 拿到B锁' % self.name)
#         mutexB.release()
#
#         mutexA.release()
#
#     def f2(self):
#         mutexB.acquire()
#         print('%s 拿到B锁' % self.name)
#         time.sleep(0.1)
#
#         mutexA.acquire()
#         print('%s 拿到A锁' % self.name)
#         mutexA.release()
#
#         mutexB.release()
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = MyThread()
#         t.start()

'''
Thread-1 拿到A锁
Thread-1 拿到B锁
Thread-1 拿到B锁
Thread-2 拿到A锁  # 出现死锁，整个程序阻塞住
'''

# 死锁： 是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象.
# 若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程.


# 互斥锁只能acquire一次
# from threading import Thread, Lock
# mutexA = Lock()
#
# mutexA.acquire()
# mutexA.release()


# 递归锁：可以连续acquire多次，每次acquire计数器+1，只有计数为0时，才能被其他线程抢到
from threading import Thread, RLock
import time

mutexA = mutexB = RLock()  # 一个线程拿到锁，counter加1,该线程内又碰到加锁的情况，则counter继续加1，这期间所有其他线程都只能等待，等待该线程释放所有锁，即counter递减到0为止


class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('\033[31m%s 拿到A锁\033[0m' % self.name)

        mutexB.acquire()
        print('\033[32m%s 拿到B锁\033[0m' % self.name)
        mutexB.release()

        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[33m%s 拿到B锁\033[0m' % self.name)
        time.sleep(0.1)

        mutexA.acquire()
        print('\033[34m%s 拿到A锁\033[0m' % self.name)
        mutexA.release()

        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()

'''
递归锁:在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。

这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，
从而使得资源可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获得资源。
'''
