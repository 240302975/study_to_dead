#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/6 20:33

# 把文件db.txt的内容重置为：{"count":1}
from multiprocessing import Process, Lock
import time, json


def search(name):
    dic = json.load(open('db.txt'))
    print('%s 查到剩余票数%s' % (name, dic['count']))


def get(name):
    dic = json.load(open('db.txt'))
    time.sleep(1)  # 模拟读数据的网络延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(1)  # 模拟写数据的网络延迟
        json.dump(dic, open('db.txt', 'w'))
        print('\033[31m%s 购票成功\033[0m' % name)
    else:
        print('\033[31m%s 购票失败\033[0m' % name)


def task(name):
    search(name)
    get(name)


if __name__ == '__main__':
    for i in range(10):
        name = '<路人%s>' % i
        p = Process(target=task, args=(name,))
        p.start()
        p.join()  # join方法依次执行

# join是将一个任务整体串行，
# 而互斥锁的好处则是可以将一个任务中的某一段代码串行，比如只让task函数中的get任务串行
