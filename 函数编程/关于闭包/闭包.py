#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 23:13


def outer():
    name = 'alex'

    def inner():
        print("在inner里打印外层函数的变量", name)

    return inner  # 注意这里只是返回inner的内存地址，并未执行


f = outer()  # .inner at 0x1027621e0>
f()  # 相当于执行的是inner()


# 闭包的意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域。
# 这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域

def make_adder(addend):
    def adder(augend):
        return augend + addend

    return adder


res1 = make_adder(12)
res2 = make_adder(13)
print(res1(100))
print(res2(100))
