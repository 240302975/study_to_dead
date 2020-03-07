#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 23:15

# 1.打开文件，加载内容，把内容转换成dict
# 2.while

f = open("stock_data_new.txt", encoding='utf-8')
stock_data = {}

query_colums = ["最新价", "涨跌幅", "换手率"]

# 先把第一行存读出来，存下来，变成列表
columns = f.readline().strip().split(",")

for line in f:
    line = line.strip().split(",")
    stock_data[line[2]] = line

while True:
    match_count = 0
    cmd = input("股票查询接口，请输入查询指令>>:").strip()
    if len(cmd) == 0:
        continue  # 规避""
    for s_name in stock_data:
        if cmd in s_name:  # 是否模糊匹配
            print(stock_data[s_name])
            match_count += 1
    # 输入：最新价、涨跌、换手率；换手率>20
    # 要确保用户输入的要查的列是可允许的。
    # 只支持> and <
    if ">" in cmd:
        q_name, q_val = cmd.split(">")  # 换手率>2 拆分后q_name='换手率'，q_val='20'
        q_name = q_name.strip()
        q_val = float(q_val)
        if q_name in query_colums:  # 代表这是支持的可进行查询的列
            q_name_index = columns.index(q_name)  # 取到这一列对应的下标
            print(columns)  # colums是表头
            for s_name, s_vals in stock_data.items():
                # 不知道 用户输入的是["最新价", "涨跌幅", "换手率"]这里面的哪个值
                # 解决方案是，拿q_name去跟文件 第一行的列名里，去找对应的列的下标。拿到这个下标后，再循环去到每行去取对应的值
                if float(s_vals[q_name_index].strip("%")) > q_val:  # 3.28% > 20
                    print(s_vals)  # 打印符合条件的
                    match_count += 1
    elif "<" in cmd:  # 和大于正好相反
        q_name, q_val = cmd.split("<")
        q_name = q_name.strip()
        q_val = float(q_val)
        if q_name in query_colums:
            q_name_index = columns.index(q_name)
            print(columns)
            for s_name, s_vals in stock_data.items():
                if float(s_vals[q_name_index].strip("%")) < q_val:  # 3.28% < 20
                    print(s_vals)
    if match_count > 0:
        print("匹配到%s条" % match_count)
