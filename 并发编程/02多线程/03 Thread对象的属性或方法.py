#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 13:01

from threading import Thread, currentThread, active_count, enumerate
import time


def task():
    print('%s is running' % currentThread().getName())  # 返回当前的线程变量
    time.sleep(2)
    print('%s is done' % currentThread().getName())


if __name__ == '__main__':
    t = Thread(target=task, name='子线程1')
    t.start()
    # t.setName('孙子线程1')  # 设置线程名
    # t.join()  # 主线程等待子线程结束
    # print(t.getName())  # 返回线程名
    # currentThread().setName('爷爷线程')  # 主线程设置线程名
    # print(t.is_alive())  # 返回线程是否活动

    # print('主线程', currentThread().getName())  # 默认叫MainThread
    # t.join()  # 这里只剩下主线程
    print(active_count())  # 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果
    
    print(enumerate())
    # 返回一个包含正在运行的线程的list。
    # 正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
