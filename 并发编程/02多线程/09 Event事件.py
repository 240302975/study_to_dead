#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/10 23:03

from threading import Thread, Event
import time

event = Event()  # 设置一个事件实例


# event.is_set()：返回event的状态值；
# event.clear()：恢复event的状态值为False。
def student(name):
    print('学生%s 正在听课' % name)
    event.wait(3)  # 如果 event.isSet()==False将阻塞线程
    print('学生%s 课间活动' % name)


def teacher(name):
    print('老师%s 正在授课' % name)
    time.sleep(2)
    event.set()  # 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度


if __name__ == '__main__':
    stu1 = Thread(target=student, args=('alex',))
    stu2 = Thread(target=student, args=('wxx',))
    stu3 = Thread(target=student, args=('yww',))
    t1 = Thread(target=teacher, args=('egon',))

    t1.start()
    stu1.start()
    stu2.start()
    stu3.start()

# 服务器连接
from threading import Thread, Event, currentThread
import time

event = Event()  # 设置一个事件实例


def conn():
    n = 0
    while not event.is_set():  # 是否被设置
        if n == 3:
            print('%s try too many times' % currentThread().getName())
            return
        print('%s try %s' % (currentThread().getName(), n))  # 连接中
        event.wait(0.5)  # 设置超时时间
        n += 1
    print('%s is connected' % currentThread().getName())  # 连接成功


def check():
    print('%s is checking' % currentThread().getName())  # 正在检测
    time.sleep(5)
    event.set()


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=conn)
        t.start()
    t = Thread(target=check)
    t.start()
