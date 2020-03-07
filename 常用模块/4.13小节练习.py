#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 23:43

# 导入模块的方式有哪几种，官方不推荐哪种？
"""
import module_a  #导入
from module import xx
from module.xx.xx import xx as rename #导入后重命令
from module.xx.xx import *  #导入一个模块下的所有方法，不建议使用
module_a.xxx  #调用
"""

# 如何让你写的模块可以被系统上任何一个py文件导入
"""
把自己写的模块放在一个带有“site-packages”字样的目录里
"""

import random


def yzm():
    code = ''  # 拼接随机生成的数字或字母
    for i in range(0, 4):
        '''循环4次生成4个字母或数字'''
        # 生成数字
        # 注意：将数字转换成字符串
        num = str(random.randint(0, 9))
        # 生成字母  ASC码A:65~z:90
        zm = chr(random.randint(65, 90))
        # 随机产生一个内容
        lst = [num, zm]
        ret = random.choice(lst)
        code = ''.join([code, ret])  # 把code和ret用空字符串拼接
        # 第一次一个空字符串+'a'   code='a'
    print(code)


yzm()
