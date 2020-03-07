#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 12:21

FLAG = False  # 加一个变量防止多次登录验证


def wrapper(f):
    def inner(*args, **kwargs):
        """登录程序"""
        global FLAG  # 将FLAG变量设置成全局变量
        if FLAG:
            ret = f(*args, **kwargs)
            return ret
        else:
            username = input('username:')
            password = input('password:')
            if username == '123' and password == '345':
                FLAG = True
                ret = f(*args, **kwargs)
                return ret
            else:
                print('登录失败')

    return inner


@wrapper
def func_1():
    print('func1 is running!')


@wrapper
def func_2():
    print('func2 is running!')


func_1()
func_2()