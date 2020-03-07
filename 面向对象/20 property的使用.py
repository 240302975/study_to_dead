#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/1 19:53

"""
BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）

成人的BMI数值：

过轻：低于18.5

正常：18.5-23.9

过重：24-27

肥胖：28-32

非常肥胖, 高于32

体质指数（BMI）=体重（kg）÷身高^2（m）

EX：70kg÷（1.75×1.75）=22.86
"""


# 将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后计算出来的
# 这种特性的使用方式遵循了统一访问的原则
# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
#
# p = People('egon', 70, 1.73)
# # p.height = 1.82
# # print(p.bmi)
# p.bmi = 333  # 报错AttributeError: can't set attribute

class People:
    def __init__(self, name):
        self.__name = name

    @property  # 查看
    def name(self):
        # print('getter')
        return self.__name

    @name.setter  # 修改
    def name(self, val):
        # print('setter', val)
        if not isinstance(val, str):
            print('名字必须是字符串类型')
            return
        self.__name = val

    @name.deleter  # 删除
    def name(self):
        print('deleter')
        print('不允许删除')


p = People('egon')
# print(p.get_name())
# p.name = 123
# print(p.name)
del p.name
