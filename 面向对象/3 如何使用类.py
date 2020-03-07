#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/26 22:06


class LuffyStudent:
    school = 'luffycity'  # 数据属性

    def learn(self):  # 函数属性
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')


# 查看类的名称空间
# print(LuffyStudent.__dict__)
# print(LuffyStudent.__dict__['school'])
# print(LuffyStudent.__dict__['learn'])

# 查
print(LuffyStudent.school)  # LuffyStudent.__dict__['school']
print(LuffyStudent.learn)  # LuffyStudent.__dict__['learn']

# 增
LuffyStudent.county = 'China'
# print(LuffyStudent.__dict__)
print(LuffyStudent.county)

# 删
del LuffyStudent.county

# 改
LuffyStudent.school = 'Luffycity'
