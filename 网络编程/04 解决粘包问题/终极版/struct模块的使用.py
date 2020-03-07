#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/8 21:14

import struct
import json

# res = struct.pack('i', 1280)
# print(res, type(res), len(res))  # struct.error: argument out of range
#
# # client.rexc(4)
# obj = struct.unpack('i', res)  # 解码
# print(obj)
#
# res = struct.pack('l', 1280000000000)  # 类型有‘i’模式和‘l’模式


header_dic = {
    'filename': 'a.txt',
    'md5': 'xxdxxx',
    'total_size': 1335448491651113
}

header_json = json.dumps(header_dic)
header_bytes = header_json.encode('utf-8')
# print(type(header_bytes))
# print(len(header_bytes))
struct.pack('i', len(header_bytes))
