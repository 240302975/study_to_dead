#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/17 23:54

import random
import string

print(random.randint(10, 100))  # #返回10-100之间的一个随机数，包括100
print(random.randrange(1, 10, 2))  # 随机选取1-10间的奇数
print(random.random())  # 返回一个随机浮点数
print(random.choice('abcsdfsfsfsde3#$@1'))  # 返回一个给定数据集合中的随机字符
print(random.sample('abcdefghij', 3))  # 从多个字符中选取特定数量的字符

# 生成随机字符串
print("".join(random.sample(string.digits + string.ascii_lowercase, 5)))

s = string.digits + string.ascii_lowercase
print(s)

# 洗牌必须为列表
a = list(range(100))
random.shuffle(a)
print(a)
