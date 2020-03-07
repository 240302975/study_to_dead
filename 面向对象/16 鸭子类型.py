#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/1 0:45


# 二者都像鸭子,二者看起来都像文件,因而就可以当文件一样去用
class File:
    def read(self):
        pass

    def write(self):
        pass


def write():
    print('disk write')


def read():
    print('disk read')


class Disk:
    pass


def read():
    print('text read')


def write():
    print('text write')


class Text:
    pass


# f=open(...)
# f.read()
# f.write()

disk = Disk()
text = Text()

read()
write()

read()
write()

# 序列类型：列表list，元组tuple，字符串str，但他们直接没有直接的继承关系
# str,list,tuple都是序列类型
s = str('hello')
f = list([1, 2, 3])
t = tuple(('a', 'b'))

# 我们可以在不考虑三者类型的前提下使用s,l,t
# def len(obj):
#     return obj.__len__()


print(len(s))
print(len(f))
print(len(t))
