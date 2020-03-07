#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/1 11:14


# class A:
#     __x = 1  # _A__x=1
#
#     def __init__(self, name):
#         self.__name = name  # self._A__name = 'egon'
#
#     def __foo(self):  # def _A__foo(self)
#         print('run foo')
#
#     def bar(self):
#         self.__foo()  # delf._A__foo()
#         print('from bar')


# print(A.__dict__)
# print(A.__x)
# print(A.__foo)

# a = A('egon')
# print(a.__name)  #a.__dict__['__name']
# print(a.__dict__)

# a.bar()
"""
这种变形的特点：
    1、在类外部无法直接使用：obj.__AttrName
    2、在类内部是可以直接使用：obj.__AttrName
    3、子类无法覆盖父类__开头的属性
"""

# class Foo:
#     def __func(self):  # _Foo__func
#         print('from foo')
#
#
# class Bar(Foo):
#     def __func(self):  # _Bar__func
#         print('from bar')
#
#
# b = Bar()
# b.func()

'''
变形需要注意的问题是：
    1、并没有真正意义上限制我们从外部直接访问属，__类名__属性就可以直接访问
    2、变形的过程只在类的定义时发生一次，在定义后的赋值操作，不会变形
    3、在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的
'''


# class B:
#     __x = 1
#
#     def __init__(self, name):
#         self.__name = name


# 验证问题一:
# print(B._B__x)

# 验证问题二：
# B.__y = 2
# print(B.__dict__)
# b = B('egon')
# print(b.__dict__)
#
# b.__age = 18
# print(b.__dict__)


# 验证问题三：
# class A:
#     def foo(self):
#         print('A.foo')
#
#     def bar(self):
#         print('A.bar')
#         self.foo()  # b.foo()
#
#
# class B(A):
#     def foo(self):
#         print('B.foo')
#
#
# b = B()
# b.bar()

class A:
    def __foo(self):  # _A__foo
        print('A.foo')

    def bar(self):
        print('A.bar')
        self.__foo()  # self._A__foo()


class B(A):
    def __foo(self):  # _B__foo
        print('B.foo')


b = B()
b.bar()