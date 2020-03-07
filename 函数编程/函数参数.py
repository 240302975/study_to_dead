#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 22:31

# 下面这段代码
a, b = 5, 8
c = a * b
print(c)


# 改成用函数写
def calc(x, y):
    res = x * y
    return res  # 返回值，意味着函数的终止


print(calc(2, 3))


def stu_register(name, age, country, course):  # 默认参数，位置移到最后面
    """
    学籍注册程序
    :param name: str
    :param age: integer
    :param country: JP,CN,US
    :param course: python，linux
    :return:
    """
    print("-----注册学生信息-----")
    print("姓名:", name)
    print("age:", age)
    print("国籍:", country)
    print("课程:", course)


stu_register("王山炮", 22, "CN", "python")
stu_register("张叫春", 21, "CN", "linux")
stu_register("刘老根", 25, "CN", "linux")  # 关键参数需要指定(age=22,name="alex")


# 位置参数 > 关键参数\默认参数

# 非固定参数
def stu_register(name, age, *args):  # *args 会把多传入的参数变成一个元组形式
    print(name, age, args)


stu_register("Alex", 22)
# 输出
# Alex 22 () #后面这个()就是args,只是因为没传值,所以为空
stu_register("Jack", 32, "CN", "Python")


# 输出
# Jack 32 ('CN', 'Python')


def stu_register(name, age, *args, **kwargs):  # *kwargs 会把多传入的参数变成一个dict形式
    print(name, age, args, kwargs)


stu_register("Alex", 22)
# 输出
# Alex 22 () {}#后面这个{}就是kwargs,只是因为没传值,所以为空
stu_register("Jack", 32, "CN", "Python", sex="Male", province="ShanDong")
# 输出
# Jack 32 ('CN', 'Python') {'province': 'ShanDong', 'sex': 'Male'}

locals()


def register(name, *args, **kwargs):
    print(name, args, kwargs)


register("Alex", 22, "Math", sex="M")
