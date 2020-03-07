#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 23:00

import re


def ip_uv(data):
    """
    ip地址匹配
    :param data:
    :return:
    """
    uv = re.search("\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}|-", data).group()
    return uv


def time_uv(data):
    """
    时间匹配
    :param data:
    :return:
    """
    time_u = re.search("(?P<time>\\d{4}:\\d.)", data).group()

    return time_u


def url_pv(data):
    """
    URL匹配
    :param data:
    :return:
    """
    url = re.search("\\w+ /.*HTTP/\\d.\\d", data).group()
    return url


def facility_uv(data):
    """
    访问设备匹配
    :param data:
    :return:
    """
    facility = re.search("Mozilla/.*", data)
    return facility


ip = []  # IP地址集合
IP = set()
time_pu = []
pu_time = {}
pv_url = []  # URL列表
facility_pv = []  # 访问设备列表
top_pv = {}
top_uv = {}
f = open(file="网站访问日志", mode="r")
for line in f:
    if re.search("^- - - ", line):
        continue
    elif facility_uv(line) is not None:
        ip.append(ip_uv(line))
        IP.add(ip_uv(line))
        pv_url.append(url_pv(line))
        facility_pv.append(str(facility_uv(line).group()))
        time_pu.append(time_uv(line))

facility_u = dict(zip(facility_pv, pv_url))
# print("uv总数:", len(IP))
# print("pv总数:", len(pv_url))
# for k, v in facility_u.items():
#     print("设备访问量：%s  访问设备设备名称：%s  " % (len(v), k,))
# for top in set(pv_url):
#     top_pv[pv_url.count(top)] = top
# for e in reversed(sorted(top_pv.keys())[-10:]):
#     print("top页面访问量：", e, ":", top_pv[e])
# for top_ip in set(ip):
#     top_uv[ip.count(top_ip)] = top_ip
# for a in reversed(sorted(top_uv.keys())[-10:]):
#     print("topIP点击数：", a, ":", top_uv[a])
# for uv in reversed(sorted(top_uv.keys())):
#     print("每小时的uv数：", uv, ":", top_uv[uv])
# for pu in set(time_pu):
#     pu_time[time_pu.count(pu)] = pu
# for pv in reversed(sorted(pu_time.keys())):
#     print("每小时的pv数：", pv, ":", pu_time[pv])


while True:
    MSG = '''\033[34;0m
网站访问日志分析作业答案
------------
1 统计本日志文件的总pv、uv
2 列出全天每小时的pv、uv数
3 列出top 10 uv的IP地址，以及每个ip的pv点击数
4 列出top 10 访问量最多的页面及每个页面的访问量
5 列出访问来源的设备列表及每个设备的访问量\033[0m
'''
    print(MSG)          # 提示用户可选项
    cmd = int(input(">>>(1-5):").strip())     # 接收用户的输入
    if cmd == 1:
        print("uv总数:", len(IP))
        print("pv总数:", len(pv_url))
    elif cmd == 2:
        for uv in reversed(sorted(top_uv.keys())):
            print("每小时的uv数：", uv, ":", top_uv[uv])
        for pu in set(time_pu):
            pu_time[time_pu.count(pu)] = pu
        for pv in reversed(sorted(pu_time.keys())):
            print("每小时的pv数：", pv, ":", pu_time[pv])
    elif cmd == 3:
        for top_ip in set(ip):
            top_uv[ip.count(top_ip)] = top_ip
        for a in reversed(sorted(top_uv.keys())[-10:]):
            print("topIP点击数：", a, ":", top_uv[a])
    elif cmd == 4:
        for top in set(pv_url):
            top_pv[pv_url.count(top)] = top
        for e in reversed(sorted(top_pv.keys())[-10:]):
            print("top页面访问量：", e, ":", top_pv[e])
    elif cmd == 5:
        for k, v in facility_u.items():
            print("设备访问量：%s  访问设备设备名称：%s  " % (len(v), k,))
    else:       # 输入不正确时提示输入有误
        print('\033[31;0m error input \033[0m')
