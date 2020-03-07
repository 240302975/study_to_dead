#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/15 20:21

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 基础目录
sys.path.append(BASE_DIR)

if __name__ == "__main__":
    from core import management

    argv_parser = management.ManagementTool(sys.argv)
    argv_parser.excute()  # 解析并执行指令
