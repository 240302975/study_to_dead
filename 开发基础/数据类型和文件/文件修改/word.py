#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 21:16

# 修改其中的内容
f = open("a.txt", mode="r", encoding="utf-8")  # 读模式打开文件
data = f.readlines()  # 读取所有行,data为列表
# with open("a.txt", "r", encoding="utf-8") as f_r:
#     lines = f_r.readlines()
data_new = []  # 用空列表接收
for line in data:  # 循环每一行
    if "不要回答" in line:  # 判断"不要回答"是否存在
        line = line.replace('不要回答', '111')  # replace  str.replace(old, new[，max])
    data_new.append(line)
f.close()

f = open("a.txt", mode="w", encoding="utf-8")  # 写模式打开文件
for line in data_new:  # 循环每一行
    f.write(line)  # 写入
f.close()


# 删除最后一行
f = open("a.txt", mode="r", encoding="utf-8")  # 读模式打开文件
data = f.readlines()  # 读取所有行,data为str
print(data)
print(data.pop())  # 打印删除行
f.close()

f = open("a.txt", mode="w", encoding="utf-8")  # 写模式打开文件
for line in data:  # 循环每一行
    f.write(line)  # 写入
f.close()
