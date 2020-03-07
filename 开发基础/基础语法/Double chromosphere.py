#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 8:53

red_ball = []  # 空列表
blue_ball = []
count = 1  # 双色球开始计数
print("----双色球选购，五百万大奖等你来中----")
while count < 7:  # 6个红球
    red_input = input("\033[31m[%d]select red ball:\033[0m" % count).strip()  # \033[31m \033[0m更改字体为红色
    if red_input.isdigit():  # 判断数字
        red_input = int(red_input)  # 转换
        if red_input in red_ball:  # 判断重复
            print("number", red_input, "is already exist in red ball list")
        elif 0 < red_input < 33:  # 判断范围
            red_ball.append(red_input)  # append 增
            count += 1
        else:
            print("only can select n between 1-32")
count = 1  # 重置为1
while count < 3:
    blue_input = input("\033[34m[%d]select blue ball:\033[0m" % count).strip()  # \033[34m \033[0m更改字体为蓝色
    if blue_input.isdigit():
        blue_input = int(blue_input)
        if blue_input in blue_ball:
            print("number", blue_input, "is already exist in red ball list")
        elif 0 < blue_input < 17:
            blue_ball.append(blue_input)
            count += 1
        else:
            print("only can select n between 1-16")
else:
    print("")  # 空出一行
    print("\033[31mRed ball:\033[0m", red_ball)
    print("\033[34mBlue ball:\033[0m", blue_ball)
    print("祝你好运，欢迎下次再来.")  # sep="",解决换行不对齐，但是太长了放弃
