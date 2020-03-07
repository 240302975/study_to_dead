#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 23:34

import time


def time_logger(flag=0):
    def show_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print('spend %s' % (end_time - start_time))

            if flag:
                print('将这个操作的时间记录到日志中')

        return wrapper

    return show_time


@time_logger(3)
def add(*args, **kwargs):
    time.sleep(1)
    sum = 0
    for i in args:
        sum += i
    print(sum)


add(2, 7, 5)
