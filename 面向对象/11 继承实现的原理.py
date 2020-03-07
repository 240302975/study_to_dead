#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/30 15:58

# 1、新式类
# 2、经典类
# 在python2中-》经典类：没有继承object的类，以及它的子类都称之为经典类


class Foo:
    pass


class Bar(Foo):
    pass


# 在python2中-》新式类：继承object的类，以及它的子类都称之为新式类
class Foo(object):
    pass


class Bae(Foo):
    pass


# 在python3中-》新式类：一个类没有继承object类，默认就继承object
class Foo:
    pass


print(Foo.__base__)


########################################################
# 验证多继承情况下的属性查找

class A(object):
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B):
    def test(self):
        print('from D')


class E(C):
    def test(self):
        print('from E')


class F(D, E):
    # def test(self):
    #     print('from F')
    pass


f1 = F()
f1.test()
print(F.__mro__)  # 只有新式才有这个属性可以查看线性列表，经典类没有这个属性

# 新式类继承顺序:F->D->B->E->C->A
# 经典类继承顺序:F->D->B->A->E->C
# python3中统一都是新式类
# pyhon2中才分新式类与经典类
