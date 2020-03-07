#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 21:39

import pickle

data = {'k1': 123, 'k2': 'Hello'}
# pickle.dumps 将数据通过特殊的形式转换位只有python语言认识的字符串
p_str = pickle.dumps(data)  # 注意dumps会把数据变成bytes格式
print(p_str)
# pickle.dump 将数据通过特殊的形式转换位只有python语言认识的字符串，并写入文件
with open('result.pk', "wb") as fp:
    pickle.dump(data, fp)  # 序列化
# pickle.load  从文件里加载
f = open("result.pk", "rb")
d = pickle.load(f)  # 反序列化
print(d)

# dump 写入文件
# dumps 生成序列化的字符串
# load 从文件加载
# loads 把序列化的字符串反向解析
