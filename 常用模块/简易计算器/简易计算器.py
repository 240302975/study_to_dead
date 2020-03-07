#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 22:02

# 开发一个简单的python计算器，实现加减乘除及拓号优先级解析
"""
用户输入 1 - 2 ( (60-30 +(-40/5) (9-25/3 + 7 /399/42998 +10 568/14 )) - (-43)/ (16-32) )等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式
(不能调用eval等类似功能偷懒实现)，运算后得出结果，结果必须与真实的计算器所得出的结果一致
"""
import re


def cal(matched):
    """
    计算匹配的表达式 num1 [+-*/] num2(可为负数，支持浮点
    :param matched: 表达式
    :return:
    """
    num1 = float(matched.group(1))
    sign = matched.group(2)
    num2 = float(matched.group(3))
    res = 0
    if sign == '+':
        res = num1 + num2
    elif sign == '-':
        res = num1 - num2
    elif sign == '*':
        res = num1 * num2
    elif sign == '/':
        res = num1 / num2
    print(num1, sign, num2, '=', str(round(res, 2)))
    return str(round(res, 10))  # 保留10位


def cal_str(str_cal):
    """
    计算括号中内容，循环：生成表达式，替换。
    :param str_cal: (表达式)
    :return: 一个数值。 或者一个表达式： -num1 [+-*/] num2（正负都可以）
    """
    # 除括号
    if str_cal[0] == '(':
        str_cal = str_cal[1:-1]
    # 乘除
    pattern = re.compile(r'(\d+\.?\d*)([*/])(-?\d+\.?\d*)')
    while pattern.search(str_cal):
        str_cal = re.sub(pattern, cal, str_cal)
    # 加减
    pattern = re.compile(r'(\d+\.?\d*)([+\-])(-?\d+\.?\d*)')
    while pattern.search(str_cal):
        str_cal = re.sub(pattern, cal, str_cal)

    return str_cal


def cal_kh(s):
    # 剔除多余空字符
    s = re.sub(r'\s+', '', s)
    # 变换，格式：(- =>(0-

    # 判断表达式合理性
    # 1.括号成对
    if len(re.findall(r'\(', s)) != len(re.findall(r'\)', s)):
        print("括号数量不匹配")
        exit(0)
    # 2. 括号位置合理
    if re.search(r'(\([+*/])|([+\-*/]\))', s):
        print("括号位置不合理")
        exit(0)

    # 判断是否含有()，有： 调用 cal_str,并循环替换。直到没有
    pattern = re.compile(r'\([^()]+\)')
    while re.search(pattern, s):
        for str_cal in pattern.findall(s):
            # print(str_cal)
            # print('=' * 50)
            s = s.replace(str_cal, cal_str(str_cal))

    # 调用cal_str返回最终表达式结果
    return cal_str(s)


if __name__ == '__main__':
    s = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    print(eval(s))  #
    print(cal_kh(s))
