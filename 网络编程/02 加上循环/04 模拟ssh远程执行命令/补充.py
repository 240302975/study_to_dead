#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/7 22:16

# windows
# dir:查看某一个文件夹下的子文件名与子文件夹名
# ipconfig:查看本地网卡的ip信息
# tasklist:查看运行的进程


# linux:
# ls:查看某一个文件夹下的子文件名与子文件夹名
# ipconfig:查看本地网卡的ip信息
# ps aux:查看运行的进程


# 执行系统命令，并且拿到命令的结果
# import os
#
# res = os.system('dir \\')
# print('命令的结果是：', res)

import subprocess

obj = subprocess.Popen('dir \\', shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
print(obj)
print('stdout 1-->:', obj.stdout.read().decode('gbk'))
print('stdere 2-->:', obj.stderr.read().decode('gbk'))
