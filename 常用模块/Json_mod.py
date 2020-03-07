#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 21:48

import json

data = {'k1': 123, 'k2': 'Hello'}
# json.dumps 将数据通过特殊的形式转换位所有程序语言都认识的字符串
j_str = json.dumps(data)  # 注意json dumps生成的是字符串，不是bytes
print(j_str)
# dump入文件
with open('result.json', 'w') as fp:
    json.dump(data, fp)
# 从文件里load
with open("result.json") as f:
    d = json.load(f)
    print(d)
"""
json vs pickle:
JSON:

优点：跨语言(不同语言间的数据传递可用json交接)、体积小

缺点：只能支持int\str\list\tuple\dict

Pickle:

优点：专为python设计，支持python所有的数据类型

缺点：只能在python中使用，存储数据占空间大
"""
