#!/usr/bin/env python # -*- coding: utf-8 -*-
import re  # 导入正则模块
import time  # 导入时间模块


def load_log_file():  # 将文件取出，方便调用
    f = open('网站访问日志', 'r')
    log_data = []
    for line in f:
        log_data.append(line)
    f.close()
    return log_data


def total_pvuv(data):  # 统计传入数据的总PV UV
    pv = 0
    users = []
    for i in data:
        i = i.split(' ')[0]  # 用户IP在第一个元素
        users.append(i)  # 将所有IP加入users列表
        pv += 1  # 计算总行数即 PV
    uv = len(set(users))  # 使用集合的去重功能，计算集合的元素，得到UV
    user_list = list(user for user in set(users))
    user_views = dict.fromkeys(user_list, 0)
    return user_list, user_views, pv, uv


def pv_uv(*args):  # 显示总的PV和UV
    print('----总PV是:%s 总UV是 %s ----' % (total_pvuv(*args)[2], total_pvuv(*args)[3]))


def pv_uv_hours(sel_time):  # 将数据按小时划分成 24份存入小时为key的字典中，sel_time是想打印的时间
    hour_list = dict.fromkeys(range(0, 24), [])
    if sel_time == 'all':
        print('---total pv is :%s --- total uv is : %s---' % (total_pvuv(data)[2], total_pvuv(data)[3]))
        print('==========')
    elif sel_time.isdigit() and int(sel_time) in hour_list.keys():  # 判断输入是否是数字
        for i in data:
            string = re.search(r'\d{1,2}/\D{3,4}/\d{4}:\d{2}', i).group(0).split(':')  # 将日期和小时取出
            zero_time = time.mktime(time.strptime(string[0], "%d/%b/%Y"))  # 设定当天的0点坐标
            hour = time.mktime(time.strptime('/'.join(string), "%d/%b/%Y/%H"))  # 计算当条日志是几点
            index = int((hour - zero_time) / 3600)  # 计算当条日志是几点
            if int(index) == int(sel_time):  # 将日志条目按时间追加到对应字典内
                hour_list[int(sel_time)].append(i)
        hour_pvuv = total_pvuv(hour_list[int(sel_time)])  # 计算sel_time的pv,uv
        print('%s点的pv:%s uv:%s ' % (sel_time, hour_pvuv[2], hour_pvuv[3]))
    else:
        print('\033[31;0m error input \033[0m')


def top10_ip_pv(*args):  # 计算前十访问的用户IP和点击次数
    t = total_pvuv(data)[1]
    for i in data:
        i = i.split(' ')
        if i[0] in t.keys():  # 如果ip存在与users表中，计数器+1
            t[i[0]] += 1

    top10_uv_ip = sorted(t.items(), key=lambda t: t[1], reverse=True)  # 将列表排序
    print('TOP10 序号(用户IP，访问PV：)')
    for k, v in enumerate((top10_uv_ip[0:10]), 1):  # 取出前10个元素，以序号1开始显示
        print(k, v)


def top10_url(*args):  # 找出访问量最大的前10的页面
    urls = []
    for i in data:
        i = i.split('\"')[1].split(' ')  # url在 ""内
        if len(i) > 1:  # 日志中有 - - - 类似的异常信息，排除掉
            urls.append(i[1])
    url_list = set(urls)  # url去重后 做key
    url_views = dict.fromkeys(url_list, 0)  # 用url做key，默认次数0为value
    for i in urls:  # 遍历urls，命中的计数器+1
        url_views[i] += 1
    top10_url_list = sorted(url_views.items(), key=lambda url_views: url_views[1], reverse=True)  # 对url列表进行排序
    print('TOP10 URL(URL：，访问次数：)')
    for k, v in enumerate((top10_url_list[0:10]), 1):  # 取前10的url和次数，从序号1开始打印
        print(k, v)


def device_list(*args):  # 列出所有设备，和对应设备的pv值
    dev = []
    for i in data:
        try:
            device = re.search("Mozilla/(.*?)/", i).group(0)  # 设备名 是被第一对()括起来的
        except AttributeError:  # 日志里有'- '的值，正则匹配时返回空对象，空对象是没有group方法的，报AttributeError
            continue
        dev.append(device)
    dev_list = set(dev)  # 用集合给设备名去重
    dev_views = dict.fromkeys(dev_list, 0)  # 生成key为设备名的字典准备计算PV
    for i in dev:  # 遍历设备表统计出现次数
        dev_views[i] += 1
    top_dev_list = sorted(dev_views.items(), key=lambda dev_views: dev_views[1], reverse=True)  # 对列表进行排序
    print('TOP DEV(DEV：，访问次数：)')
    for k, v in enumerate(top_dev_list, 1):  # 打印所有设备和每台设备的PV
        print(k, v)


def which_hour(*args):  # 询问打印哪个小时的 PV UV值
    hour = input('which hour? 0 - 23/all >>>')
    pv_uv_hours(hour)  # 根据小时，去对应切片中寻找并打印该小时的pv uv


data = load_log_file()
while True:
    MSG = '''\033[34;0m
choose one function
------------
1 统计本日志文件的总pv、uv
2 列出全天每小时的pv、uv数
3 列出top 10 uv的IP地址，以及每个ip的pv点击数
4 列出top 10 访问量最多的页面及每个页面的访问量
5 列出访问来源的设备列表及每个设备的访问量\033[0m
'''
    print(MSG)  # 提示用户可选项
    cmd = input(">>>(1-5)")  # 接收用户的输入
    choice = {'1': pv_uv,
              '2': which_hour,
              '3': top10_ip_pv,
              '4': top10_url,
              '5': device_list}  # 定义一个字典，对应相应的功能
    if cmd in choice:  # 按用户的选择执行对于方法
        choice[cmd](data)
    else:  # 输入不正确时提示输入有误
        print('\033[31;0m error input \033[0m')
