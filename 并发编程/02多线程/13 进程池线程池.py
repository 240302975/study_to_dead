# 线程池、进程池
# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
# import os, time, random
#
#
# def task(name):
#     print('name:%s pid:%s run' % (name, os.getpid()))
#     time.sleep(random.randint(1, 3))
#
#
# if __name__ == '__main__':
#     # pool=ProcessPoolExecutor(4)
#     pool = ThreadPoolExecutor(5)  # 不指定默认为CPU的核数
#
#     for i in range(10):
#         pool.submit(task, 'egon%s' % i)  # 异步提交任务
#
#     pool.shutdown(wait=True)  # 相当于进程池的pool.close()+pool.join()操作
#     # wait = True，等待池内所有任务执行完毕回收完资源后才继续
#     # wait = False，立即返回，并不会等待池内的任务执行完毕
#     # 但不管wait参数为何值，整个程序都会等到所有任务执行完毕
#     print('主')
#
# import os
# import random
# import time
# from concurrent.futures import ThreadPoolExecutor
# from threading import currentThread
#
#
# def task():
#     print('name:%s pid:%s run' % (currentThread().getName(), os.getpid()))
#     time.sleep(random.randint(1, 3))
#
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(5)
#
#     for i in range(10):
#         pool.submit(task)
#
#     pool.shutdown(wait=True)
#
#     print('主')


# map方法
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import os, time, random


def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n ** 2


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=3)

    # for i in range(11):
    #     future=executor.submit(task,i)

    executor.map(task, range(1, 12))  # map取代了for+submit
