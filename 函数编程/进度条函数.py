#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 20:45


# =========实现打印进度条函数==========
import sys
import time


def progress(percent, width=50):
    if percent >= 1:
        percent = 1
    show_str = ('[%%-%ds]' % width) % (int(width * percent) * '#')
    print('\r%s %d%%' % (show_str, int(100 * percent)), file=sys.stdout, flush=True, end='')


# =========应用==========
data_size = 1025
recv_size = 0
while recv_size < data_size:
    time.sleep(0.1)  # 模拟数据的传输延迟
    recv_size += 10  # 每次收10

    percent = recv_size / data_size  # 接收的比例
    progress(percent, width=70)  # 进度条的宽度70
