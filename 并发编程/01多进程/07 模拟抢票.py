#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/6 20:10

import json
import time
from multiprocessing import Process, Lock


def search(name):  # 查询余票
    dic = json.load(open('db.txt'))
    time.sleep(1)
    print('%s 查到剩余票数【%s】' % (name, dic['count']))


def get(name):  # 购票
    dic = json.load(open('db.txt'))
    time.sleep(1)  # 模拟读数据的网络延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(1)  # 模拟写数据的网络延迟
        json.dump(dic, open('db.txt', 'w'))
        print('\033[31m%s 购票成功\033[0m' % name)


def task(name, lock):
    search(name)
    with lock:  # 相当于lock.acquire(),执行完自代码块自动执行lock.release()
        get(name)


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):  # 模拟并发10个客户端抢票
        name = '<路人%s>' % i
        p = Process(target=task, args=(name, lock))
        p.start()
