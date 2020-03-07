#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 23:26


# 比如有时我们需要对某些文件的特殊行进行分析，先
# 要提取出这些特殊行。

def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc

    return the_filter


# 如果我们需要取得文件"result.txt"中含有"pass"关键字的行，则可以这样使用例子程序
filter = make_filter("pass")
filter_result = filter("result.txt")
