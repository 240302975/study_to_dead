#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 0:31

# 如何获得一个路径下面所有的文件路径：
import os

path = r'C:\Users\Administrator\Desktop'
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
'''
os.walk：输入一个路径名称，以yield的方式（其实是一个生成器）返回一个三元组 dirpath, dirnames, filenames，

dirpath：为目录的路径，为一个字符串。

dirnames：列出了目录路径下面所有存在的目录的名称。

filenames：列出了目录路径下面所有文件的名称。
'''