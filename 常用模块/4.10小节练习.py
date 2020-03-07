#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 17:17

# 验证手机号是否合法
import re


def phone():
    n = input("请输入一个手机号：")
    if re.match(r'1[34578]\d{9}', n):
        print("您输入的的手机号码是：\n", n)
        # 中国联通：
        # 130，131，132，155，156，185，186，145，176
        if re.match(r'13[012]\d{8}', n) or \
                re.match(r"15[56]\d{8}", n) or \
                re.match(r"18[56]", n) or \
                re.match(r"145\d{8}", n) or \
                re.match(r"176\d{8}", n):
            print("该号码属于：中国联通")
        # 中国移动
        # 134, 135 , 136, 137, 138, 139, 147, 150, 151,
        # 152, 157, 158, 159, 178, 182, 183, 184, 187, 188；
        elif re.match(r"13[456789]\d{8}", n) or \
                re.match(r"147\d{8}|178\d{8}", n) or \
                re.match(r"15[012789]\d{8}", n) or \
                re.match(r"18[23478]\d{8}", n):
            print("该号码属于：中国移动")
        else:
            # 中国电信
            # 133,153,189
            print("该号码属于：中国电信")
    else:
        print("请输入正确的手机号")


if __name__ == '__main__':
    phone()


# 验证邮箱是否合法
import re

re_email = re.compile(r'^[a-zA-Z0-9\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')


def is_valid_email(addr):
    if re_email.match(addr):
        print("True")
    else:
        print('False')


is_valid_email('someone@gmail.com')
is_valid_email('240302975@qq.com')
