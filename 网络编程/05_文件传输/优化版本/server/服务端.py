#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/8 16:50

import json
import os
import socket
import struct


def get(conn, cmds):
    filename = cmds[1]

    # 3、以读的方式打开文件，读取文件内容发送给客户端
    # 第一步：制作固定长度的报头
    header_dic = {
        'filename': filename,  # 'filename':'a.txt'
        'md5': 'xxdxxx',
        'file_size': os.path.getsize(filename)  # 获取文件大小
    }

    header_json = json.dumps(header_dic)

    header_bytes = header_json.encode('gbk')

    # 第二步：先发送报头的长度
    conn.send(struct.pack('i', len(header_bytes)))

    # 第三步：再发报头
    conn.send(header_bytes)

    # 第四步：再发送真实的数据
    with open(filename, 'rb') as f:
        # conn.send(f.read())
        for line in f:
            conn.send(line)


def put(conn, cmds):
    pass


def run():
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
                res = conn.recv(8096)  # b'get a.txt'
                print('客户端的数据', res)

                # 2、解析命令，提取相应命令参数
                cmds = res.decode('utf-8').split()  # ['get','a.txt']
                if cmds[0] == 'get':
                    get(conn, cmds)
                if cmds[0] == 'put':
                    input(conn, cmds)

            except ConnectionResetError:  # 适用于windows操作系统
                break
        conn.close()

    phone.close()


if __name__ == '__main__':
    run()
