#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/8 21:14

import struct

res = struct.pack('i', 1280)
print(res, type(res), len(res))  # struct.error: argument out of range

# client.rexc(4)
obj = struct.unpack('i', res)  # 解码
print(obj)

res = struct.pack('l', 1280000000000)  # 类型有‘i’模式和‘l’模式
