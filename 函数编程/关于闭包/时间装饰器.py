#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 23:31

import time


def show_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend %s' % (end_time - start_time))

    return wrapper


@show_time  # foo=show_time(foo)
def foo():
    print('hello foo')
    time.sleep(1)


@show_time  # bar=show_time(bar)
def bar():
    print('in the bar')
    time.sleep(2)


foo()
print('***********')
bar()