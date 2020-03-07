#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 14:03

import re

f = open("兼职模特空姐联系方式.txt", 'r', encoding='UTF-8')

phone_list = re.findall("[0-9]{11}", f.read())

print(phone_list)

# phone_list = [ ]
#
# for line in f:
#     name,region,height,weight,phone = line.split()
#     if phone.startswith("1"):
#         phone_list.append(phone)
#
#
# print(phone_list)

"""
re的匹配语法有以下几种

re.match 从头开始匹配
re.search 匹配包含
re.findall 把所有匹配到的字符放到以列表中的元素返回
re.split 以匹配到的字符当做列表分隔符
re.sub 匹配字符并替换
re.fullmatch 全部匹配
"""
