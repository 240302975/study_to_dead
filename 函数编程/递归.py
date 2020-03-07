#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 23:39

# 100/2 = 50
# 50/2 = 25

# while实现
n = 100
while n > 0:
    n = int(n / 2)
    print(n)


# 函数实现
def calc(a):
    print(a)
    a = int(a / 2)  # 50
    if a > 0:
        calc(a)
    print(a)


calc(100)
