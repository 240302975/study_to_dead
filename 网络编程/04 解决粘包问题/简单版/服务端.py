#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/8 16:50

import socket
import subprocess
import struct

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口重用
phone.bind(('127.0.0.1', 9909))
phone.listen(5)

print('starting...')
while True:  # 链接循环
    conn, client_addr = phone.accept()  # 建立链接
    print(client_addr)

    while True:  # 通信循环
        try:
            # 1、收命令
            cmd = conn.recv(8096)
            print('客户端的数据', cmd)

            # 2、执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('gbk'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            # 3、把命令的结果返回给客户端
            # 第一步：制作固定长度的报头
            total_size = len(stdout) + len(stderr)  # 固定长度；真实数据描述信息
            header = struct.pack('i', total_size)
            # 第二步：把报头发送给客户端

            conn.send(header)

            # 第三步：再发送真实的数据
            conn.send(stdout + stderr)  # +是一个可以优化的点
        except ConnectionResetError:  # 适用于windows操作系统
            break
    conn.close()

phone.close()
