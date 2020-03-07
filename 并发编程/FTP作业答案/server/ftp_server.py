#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 21:33


import os
import sys

BASE_DIR = os.path.normpath(os.path.join(__file__, '..'))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    from core import management
    management = management.ManagementTool()
    # management.execute()

    management.start()