#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 22:51

# 全局替换
import sys  # sys.argv读取外部指令（注意这是一个列表,可以用[number]调用)
import os

# 添加统计功能
count = 0

filename = sys.argv[3]  # 文件名
newFileName = '%s.new' % filename  # 新文件名，用来覆盖用

oldStr = sys.argv[1]  # 老字符串
newStr = sys.argv[2]  # 新字符串

f = open(filename, mode='r+', encoding='utf-8')  # 以读写模式打开文件
f_new = open(newFileName, mode='w+', encoding='utf-8')  # 读模式打开新文件，注意：w和w+会把以前的内容清空掉

data = f.readlines()  # 逐行读取文件
for line in data:
    if oldStr in line:  # 如果oldStr存在在本行中
        count += 1
        new_line = line.replace(oldStr, newStr)  # 替换
    else:
        new_line = line
    f_new.write(new_line)

f.close()
f_new.close()

os.rename(newFileName, filename)  # 文件覆盖操作
print("一共替换了%d处" % count)