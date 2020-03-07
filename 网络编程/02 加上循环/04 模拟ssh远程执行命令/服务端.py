#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/7 10:47

import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口重用
phone.bind(('127.0.0.1', 9900))
phone.listen(1)

print('starting...')
while True:  # 链接循环
    conn, client_addr = phone.accept()  # 建立链接
    print(client_addr)

    while True:  # 通信循环
        try:
            # 1、收命令
            cmd = conn.recv(1024)
            print('客户端的数据', cmd)

            # 2、执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('gbk'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            # 3、把命令的结果返回给客户端
            print(len(stdout)+len(stderr))
            conn.send(stdout + stderr)  # +是一个可以优化的点
        except ConnectionResetError:  # 适用于windows操作系统
            break
    conn.close()

phone.close()
