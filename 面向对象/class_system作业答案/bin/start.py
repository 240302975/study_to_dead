#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/22 21:33

import os
import sys
import platform

if platform.system() == "Windows":
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])

else:
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])

sys.path.insert(0,BASE_DIR)
#print(sys.path)

from core import main
from conf import settings

if __name__ == '__main__':
    obj = main.Manage_center()
    obj.run()
