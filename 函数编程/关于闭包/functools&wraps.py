#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 23:51

def foo():
    print("hello foo")


print(foo.__name__)


#####################

def logged(func):
    def wrapper(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return wrapper


@logged
def cal(x):
    return x + x * x


print(cal.__name__)

'''
@logged
def f(x):
   return x + x * x
   
等价于：

def f(x):
    return x + x * x
f = logged(f)
不难发现，函数f被wrapper取代了，当然它的docstring，__name__就是变成了wrapper函数的信息了。
'''

from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return wrapper


@logged
def cal(x):
    return x + x * x


print(cal.__name__)  # cal
