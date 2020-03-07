#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/23 14:42

import os
import sys

# 程序主目录文件
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.insert(0, BASE_DIR)

# 数据库目录
DATABASE = os.path.join(BASE_DIR, "database")

# 用户属主目录
HOME_PATH = os.path.join(BASE_DIR, "home")

# 用户字典
USERS_PWD = {"alex": "123456", "eric": "6666"}

# 磁盘配额   10M
LIMIT_SIZE = 10240000

# ftp服务端口
IP_PORT = ("0.0.0.0", 9999)
