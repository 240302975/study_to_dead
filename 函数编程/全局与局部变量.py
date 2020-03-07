#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 21:00


def test():
    return 1, 2, 3, 4, 5


print(test())

name = "Alex Li"  # 全局变量


def change_name():
    global name  # 在函数内部声明(创建)一个全局变量
    name = "金角大王,一个有Tesla的高级屌丝"  # 局部变量
    print("after change", name)


change_name()
print("在外面看看name改了么?", name)


d = {"name": "Alex", "age": 26, "hobbie": "大保健"}
l = ["Rebeeca", "Katrina", "Rachel"]


def change_data(info, girls):
    info["hobbie"] = "学习"
    girls.append("XiaoYun")


change_data(d, l)
print(d, l)
