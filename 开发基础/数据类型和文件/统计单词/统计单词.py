#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 20:10

import re
count = {}
f = open('word', 'r')
b = f.read()

cd = re.split('[ \\n]+', b)  # 注意split的用法

print(cd)
for i in cd:
    count[i] = count.get(i, 0) + 1  # 注意get()方法的用法
print(count)
