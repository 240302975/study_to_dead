#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 21:30


import os
import sys


BASE_DIR = os.path.normpath(os.path.join(__file__, '..'))
print(BASE_DIR)
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    from core import main
    client = main.FTPClient(('127.0.0.1', 8080))
    client.interactive()
