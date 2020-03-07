#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 15:43

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

# 保存进入的每一层记录
current_layer = menu
parent_list = []
while True:
    for key in current_layer:
        print(key)
    choice = input("请输入地址，或者按b返回上一层，按q退出程序>>>:").strip()
    if len(choice) == 0: continue
    if choice in current_layer:
        parent_list.append(current_layer)  # 进入下一层之前保存当前层
        current_layer = current_layer[choice]  # 将子层赋值给动态字典
    elif choice == 'b':
        if len(parent_list) != 0:
            current_layer = parent_list.pop()  # 取出列表的最后一个值，并返回这个值
        else:
            print("已经是最后一层")
    elif choice == 'q':
        break
    else:
        print("您所输入的地址不存在，请重输")
