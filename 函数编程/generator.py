#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 23:36

# 生成器 generator
for i in range(100000):
    print(i)
    if i > 100:
        break

# 这种一边循环一边计算后面元素的机制，称为生成器：generator
count = 0
while count < 1000000:
    print(count)
    count += 1
    if count > 100:
        break

print([x * x for x in range(10)])

g = (x * x for x in range(10))
for i in g:
    print(i)
