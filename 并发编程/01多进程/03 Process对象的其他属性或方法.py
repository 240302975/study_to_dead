#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/5 23:30

# join方法
from multiprocessing import Process
import time, os


def task():
    print('子进程：%s is running,parent id is <%s>' % (os.getpid(), os.getppid()))
    time.sleep(1)
    print('子进程：%s is done,parent id is <%s>' % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    p = Process(target=task)  # target表示调用对象，即子进程要执行的任务
    p.start()

    p.join()  # 等待p停止,才执行下一行代码
    print('主进程：', os.getpid(), os.getppid())
    print(p.pid)

# 并行
from multiprocessing import Process
import time, os


def task(name, n):
    print('子进程：%s is running' % name)
    time.sleep(n)


if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=task, args=('子进程1', 5))
    p2 = Process(target=task, args=('子进程2', 3))
    p3 = Process(target=task, args=('子进程3', 2))

    p_l = [p1, p2, p3]

    for p in p_l:
        p.start()

    for p in p_l:
        p.join()
    print('主', time.time() - start)

# 串行
from multiprocessing import Process
import time, os


def task(name, n):
    print('子进程：%s is running' % name)
    time.sleep(n)


if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=task, args=('子进程1', 5))
    p2 = Process(target=task, args=('子进程2', 3))
    p3 = Process(target=task, args=('子进程3', 2))

    p_l = [p1, p2, p3]

    for p in p_l:
        p.start()
        p.join()

    print('主', time.time() - start)

# 了解：is_alive  terminate  name
from multiprocessing import Process
import time, os


def task(name):
    print('子进程：%s is running' % name)
    time.sleep(1)


if __name__ == '__main__':
    # p = Process(target=task, args=('子进程1', 5))
    # p.start()
    #
    # p.join()
    # print('主',os.getpid(),os.getppid())
    # print(p.pid)
    # print(p.is_alive())  # 判断进程是否存活

    p = Process(target=task,name='sub-Process')  # 进程名
    p.start()
    p.terminate()  # 关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
    time.sleep(3)
    print(p.is_alive())  # 结果为True
    print('主')
    print(p.name)