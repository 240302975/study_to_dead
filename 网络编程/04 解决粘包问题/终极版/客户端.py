#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/8 16:50

import socket
import struct
import json

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通信，基于TCP协议

phone.connect(('127.0.0.1', 9909))

while True:
    # 1、发命令
    cmd = input('>>:').strip()
    if not cmd:
        continue
    phone.send(cmd.encode('gbk'))

    # 2、拿命令的结果，并打印
    # 第一步:先收报头
    obj = phone.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 第二步：再收报头
    header_bytes = phone.recv(header_size)

    # 第三步：从报头中解析出对真实数据的描述信息（数据长度）
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    print(header_dic)
    total_size = header_dic['total_size']

    # 第四步：接收真实的数据
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        res = phone.recv(1024)  # 1024是一个坑
        recv_data += res
        recv_size += len(res)
    print(recv_data.decode('gbk'))

phone.close()
