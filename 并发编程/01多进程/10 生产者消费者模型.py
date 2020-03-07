#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/6 21:50

from multiprocessing import Process, Queue
import time


def producer(q):
    for i in range(3):
        res = '包子%s' % i
        time.sleep(0.5)
        print('生产者生产了%s' % res)

        q.put(res)


def consumer(q):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(1)
        print('消费者吃了%s' % res)


if __name__ == '__main__':
    # 容器
    q = Queue()

    # 生产者们
    p1 = Process(target=producer, args=(q,))

    # 消费者们
    c1 = Process(target=consumer, args=(q,))

    p1.start()
    c1.start()

    p1.join()
    q.put(None)
    print('主')


# 1、程序中有两类角色
#
# 一类负责生产数据（生产者）
# 一类负责处理数据（消费者）


# 2、引入生产者消费者模型为了解决的问题是
#
# 平衡生产者与消费者之间的速度差
# 程序解开耦合


# 3、如何实现生产者消费者模型
#
# 生产者<--->队列<--->消费者
