#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 1:46

# 1、开进程的开销远大于开线程
import time
from threading import Thread
from multiprocessing import Process


def piao(name):
    print('%s piaoing' % name)
    time.sleep(2)
    print('%s piao end' % name)


if __name__ == '__main__':
    # p1=Process(target=piao,args=('egon',)) # 线程开销小
    # p1.start()

    t1 = Thread(target=piao, args=('egon',))  # 进程开销大
    t1.start()
    print('主线程')

# 2、同一进程内的多个线程共享该进程的地址空间
# 1.进程之间地址空间是隔离的
from multiprocessing import Process
import os


def work():
    global n
    n = 0


if __name__ == '__main__':
    n = 100
    p = Process(target=work)
    p.start()
    p.join()
    print('主', n)

'''
主 100
'''

# 2.同一进程内开启的多个线程是共享该进程地址空间的
from threading import Thread
import os


def work():
    global n
    n = 0


if __name__ == '__main__':
    n = 100
    t = Thread(target=work)
    t.start()
    t.join()
    print('主', n)

'''
主 0
'''

# 3、瞅一眼pid
# 1、在主进程下开启多个线程,每个线程都跟主进程的pid一样
from threading import Thread
import os


def work():
    print('hello', os.getpid())


if __name__ == '__main__':
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    print('主线程/主进程pid', os.getpid())

'''
hello 7939
hello 7939
主线程/主进程 7939
'''

# 2、开多个进程,每个进程都有不同的pid
from multiprocessing import Process
import os


def work():
    print('hello', os.getpid())


if __name__ == '__main__':
    p1 = Process(target=work)
    p2 = Process(target=work)
    p1.start()
    p2.start()
    print('主线程/主进程', os.getpid())

'''
主线程/主进程 7951
hello 7952
hello 7953
'''