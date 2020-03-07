#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 20:57

s = "小猿圈"
print(s.encode("utf-8"))
f = open("bytes.txt", "w", encoding="utf-8")  # 默认加载文件都是用utf-8编码
f.write("你好未来")
f.close()
'''
wb 二进制创建

rb 二进制读

ab 二进制追加
'''