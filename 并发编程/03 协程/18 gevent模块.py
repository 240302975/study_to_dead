#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/13 17:38

import gevent
import time


def eat(name):
    print('%s eat 1' % name)
    gevent.sleep(3)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    gevent.sleep(4)
    print('%s play 2' % name)


start_time = time.time()
g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, 'alex')

g1.join()  # 等待g1结束
g2.join()  # 等待g2结束
stop_time = time.time()
print(stop_time - start_time)

'''
gevent.sleep(2)模拟的是gevent可以识别的io阻塞,
而time.sleep(2)或其他的阻塞,gevent是不能直接识别的需要用下面一行代码,打补丁,就可以识别了
from gevent import monkey;monkey.patch_all()必须放到被打补丁者的前面，如time，socket模块之前
或者要用gevent，需要将from gevent import monkey;monkey.patch_all()放到文件的开头
'''

from gevent import monkey;monkey.patch_all()
import gevent
import time


def eat():
    print('eat food 1')
    time.sleep(2)
    print('eat food 2')


def play():
    print('play 1')
    time.sleep(1)
    print('play 2')


g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)
gevent.joinall([g1, g2])  # 等待所有进程
print('主')

# 我们可以用threading.current_thread().getName()来查看每个g1和g2，查看的结果为DummyThread-n，即假线程
