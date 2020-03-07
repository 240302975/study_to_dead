#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 10:05

"""
深浅copy都是对源对象的复制，占用不同的内存空间。
如果源对象只有一级目录的话，源做任何改动，不影响深浅拷贝对象
如果对象不止一级目录，源做任何改动，都要影响浅拷贝，但不影响深 拷贝
"""
# 字典嵌套可变对象 （源和浅copy变了，深copy没变）
import copy  # 导入copy模块

info = {'name': 'tom', 'age': 18, 'job': ['it', 'design']}  # 原始字典
info_copy = copy.copy(info)  # 浅拷贝
info_deep = copy.deepcopy(info)  # 深拷贝

print(id(info))
print(id(info_copy))
print(id(info_deep))  # 3个不同的对象,id不一样
info['job'][0] = 'boss'  # 源和浅copy变了，深copy没变
print(info)  # {'age': 18, 'job': ['boss', 'design'], 'name': 'tom'}
print(info_copy)  # {'age': 18, 'job': ['boss', 'design'], 'name': 'tom'}
print(info_deep)  # {'age': 18, 'job': ['it', 'design'], 'name': 'tom'}
