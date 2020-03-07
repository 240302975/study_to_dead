#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/6 21:25

# 队列：多个进程之间通信使用
from multiprocessing import Queue

q = Queue(3)
# put ,get ,put_nowait,get_nowait,full,empty
q.put('hello')
q.put({'a': 1})
q.put([3, 3, 3])
print(q.full())  # 满了
# q.put(4) #  因为最开始q = Queue(3)，再放就阻塞住了

print(q.get())
print(q.get())
print(q.get())
print(q.empty())  # 空了
# print(q.get()) #再取就阻塞住了
