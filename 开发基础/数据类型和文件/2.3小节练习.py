#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 12:27

# None 什么也没有
# 空 Empty
name = None
age = None
weight = None
height = None

if name is None:
    print("你还没起名字")

# # 三元计算
a = 10
b = 5

if a > 15:
    c = a
else:
    c = b
d = a if a > 15 else b  # d = 值1 if 条件A else 值2

# 2.3列表练习
names = ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'eva', '鸡头']
# 1.通过names.index()的方法返回第2个eva的索引值
print(names.index("eva", names.index("eva") + 1))  # ','之后意味着从指定位置开始搜索

# 2.把以上的列表通过切片的形式实现反转
print(names[::-1])

# 3.打印列表中所有下标为奇数的值
print(names[1::2])  # 从1开始，步长为1

# 4.通过names.index()方法找到第2个eva值 ，并将其改成EVA
names[names.index("eva", names.index("eva") + 1)] = "EVA"
print(names)

