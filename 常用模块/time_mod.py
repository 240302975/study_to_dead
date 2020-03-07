#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/17 21:21

import time

print(time.time())  # 返回当前时间的时间戳
print(time.localtime())  # 将一个时间戳转换为当前时区的struct_time
t1 = time.gmtime()  # 转换为UTC时区

print(time.mktime(t1))  # 将一个struct_time转化为时间戳

time.sleep(3)  # 线程推迟指定的时间运行,单位为秒
print("------")
print(time.asctime())
print(time.ctime())

print(time.strftime("%Y.%m-%d %H:%M %p %j %z", time.localtime()))  # 年月日，小时分钟
# 把一个代表时间的元组转化为格式化的时间字符串

print(time.strptime("2020/04/01 9:30 ", "%Y/%m/%d %I:%M "))  # 把一个格式化时间字符串转化为struct_time
