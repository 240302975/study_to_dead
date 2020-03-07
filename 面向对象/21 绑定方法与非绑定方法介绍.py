#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/1 21:35

"""
在类内部定义的函数，分为两大类：
    一：绑定方法：绑定给谁，就应该由谁来调用，谁来调用就会把调用者当作第一参数自动传入
        绑定到对象的方法：在类内定义的没有被任何装饰器修饰的

        绑定到类的方法：在类内定义的被装饰器classmethod修饰的方法

    二：非绑定方法：没有自动传值这么一说，就类中定义的一个普通工具，对象和类都可以使用
        非绑定方法：不与类或者对象绑定
"""


class Foo:
    def __init__(self, name):
        self.name = name

    def tell(self):  # 绑定对象
        print('名字是%s' % self.name)

    @classmethod  # 绑定到类
    def func(cls):
        print(cls)

    @staticmethod  # 非绑定方法
    def func1(x, y):
        print(x + y)


f = Foo('egon')
# Foo.tell(f)
# print(f.tell)
# f.tell()

# print(Foo.func)  # <bound method Foo.func of <class '__main__.Foo'>>
# Foo.func()
Foo.func1(1, 2)
f.func1(1, 3)
