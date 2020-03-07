#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 0:20


import xlwt
import re

workbook = xlwt.Workbook()
worksheet = workbook
style = xlwt.XFStyle()
al = xlwt.Alignment()
al.horz = xlwt.Alignment.HORZ_RIGHT
style.alignment = al
reg = re.compile(r'"(\d+)":\["(.*?)",(\d+),(\d+),(\d+)\]')
count = 0
with open('student.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
    s = reg.findall(content)
    print(s)
    for i in s:
        for j in range(len(i)):
            if j < 2:
                worksheet.write(count, j, label=i[j])
            else:
                worksheet.write(count, j, label=i[j], style=style)
        count += 1

workbook.save('student.xls')
