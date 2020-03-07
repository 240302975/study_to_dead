#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 17:07

"""
作业需求：
  1.输入用户名密码
  2.认证成功后显示欢迎信息
  3.输错三次后锁定

实现思路：
  1.判断用户是否在黑名单，如果在黑名单提示账号锁定。
  2.判断用户是否存在，如果不存在提示账号不存在。
  3.判断账号密码是否正确，如果正确登录进去。如果不正确有三次输入密码机会。三次全部输错，账号锁定。
"""
import json

with open('account.txt', 'r') as f:
    account = json.loads(f.read())  # 读取数据
lock_list = {}  # {'user':'count'}
count = 0
while True:
    user = input("输入用户名[按q退出]：")
    if user.strip() == 'q':
        break
    if user in account:
        if account[user]["status"]:  # 判断是否锁定
            if not lock_list.__contains__(user):  # not表示不存在，即为True
                lock_list[user] = 0  # value的起始值设为0
                if lock_list[user] >= 3:  # 锁定
                    account[user]["status"] = False  # 输错3次,status改为False
                    print("该用户密码连续输入3次错误，账户已锁定")
                    with open("account.txt", "w") as f:
                        f.write(json.dumps(account))  # json.dumps()将字典形式的数据转化为字符串
                    break
                password = input("请输入密码：")  # value为0时输入密码
                if password == account[user]["pwd"]:
                    print("登陆成功")
                    with open("account.txt", "w") as f:
                        f.write(json.dumps(account))
                    break
                else:
                    print("用户名或密码错误")
                    count += 1
                    lock_list[user] = count
            else:
                option = input("该账户已被锁定，是否解锁该账户？Y/N")
                if option.lower() == "y":
                    account[user]["status"] = True
    else:
        print("用户名不存在，请重新输入！")
