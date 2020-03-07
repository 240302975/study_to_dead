#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/29 0:01

# python一切皆对象，在python3里统一了类与类型的概念

# print(type([1, 2]))

print(list)


class LuffyStudent:
    school = 'luffycity'

    def __init__(self, name, sex, age):
        self.Name = name
        self.Sex = sex
        self.Age = age

    def learn(self):
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')


l1 = [1, 2, 3]  # l=list([1,2,3])
l2 = []
# l1.append(4)  # list.append(l1,4)
list.append(l1, 4)
print(l1)
