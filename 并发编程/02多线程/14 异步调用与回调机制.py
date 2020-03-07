#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/12 15:33

# 提交任务的两种方式
# 1、同步调用:提交完任务后，在原地等待任务执行完毕，拿到结果，再执行下一行代码，导致程序是串行执行
from concurrent.futures import ThreadPoolExecutor
import time
import random


def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(3, 5))
    res = random.randint(7, 13) * '#'
    return {'name': name, 'res': res}


def weigh(shit):
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了《%s》kg' % (name, size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)

    shit1 = pool.submit(la, 'alex').result()
    weigh(shit1)

    shit2 = pool.submit(la, 'wupeiqi').result()
    weigh(shit2)

    shit3 = pool.submit(la, 'yuanhao').result()
    weigh(shit3)


# 2、异步调用：提交完任务后，不在原地等待任务执行完毕，拿到结果，再执行下一行代码，导致程
from concurrent.futures import ThreadPoolExecutor
import time
import random


def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(1, 2))
    res = random.randint(7, 13) * '#'
    return {'name': name, 'res': res}


def weigh(shit):
    shit = shit.result()
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 %s kg' % (name, size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)

    pool.submit(la, 'alex').add_done_callback(weigh)

    pool.submit(la, 'wupeiqi').add_done_callback(weigh)

    pool.submit(la, 'yuanhao').add_done_callback(weigh)
