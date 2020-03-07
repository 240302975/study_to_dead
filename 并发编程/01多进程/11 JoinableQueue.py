#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/6 21:50

from multiprocessing import Process, JoinableQueue
import time


def producer(q):
    for i in range(3):
        res = '包子%s' % i
        time.sleep(0.5)
        print('生产者生产了%s' % res)

        q.put(res)
    q.join()  # 等到消费者把自己放入队列中的所有的数据都取走之后，生产者才结束


def consumer(q):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(1)
        print('消费者吃了%s' % res)
        q.task_done()  # 发送信号给q.join()，说明已经从队列中取走一个数据并处理完毕了


if __name__ == '__main__':
    # 容器
    q = JoinableQueue()

    # 生产者们
    p1 = Process(target=producer, args=(q,))

    # 消费者们
    c1 = Process(target=consumer, args=(q,))
    c1.daemon = True  # 消费者也没必要存在了，应该随着主进程一块死掉，因而需要将生产者们设置成守护进程

    p1.start()
    c1.start()

    p1.join()  # 生产者调用此方法进行阻塞，直到队列中所有的项目均被处理。
    # 阻塞将持续到队列中的每个项目均调用q.task_done（）方法为止
    print('主')
