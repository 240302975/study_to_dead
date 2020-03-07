#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/6 14:36

from multiprocessing import Process
import time
import random


def task(n):
    time.sleep(random.randint(1, 3))
    print('-------->%s' % n)


if __name__ == '__main__':
    p1 = Process(target=task, args=(1,))
    p2 = Process(target=task, args=(2,))
    p3 = Process(target=task, args=(3,))

    p1.start()
    p2.start()
    p3.start()

    print('-------->4')

# 保证最先输出-------->4
# 由于time.sleep的存在，所以肯定最先输出-------->4

# 保证最后输出-------->4
# join方法

# 保证按顺序输出（这么写没有意义，变成串行了）
'''
p_l=[p1,p2,p3,p4]

for p in p_l:
    p.start()

for p in p_l:
    p.join()
'''