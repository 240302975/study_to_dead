#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 22:58


# 取绝对值
def get_abs(n):
    if n < 0:
        n = int(str(n).strip("-"))
    return n


def add(x, y, f):
    return f(x) + f(y)


res = add(3, -6, get_abs)
print(res)


# 取余数
def get_remainder(n):
    c = n % 5
    return c


def add(x, y, f):
    return f(x) + f(y)


res = add(3, 6, get_remainder)
print(res)
