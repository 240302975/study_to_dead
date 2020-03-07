#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 19:53

"""
根据用户输入的用户名&密码，找到对应的json文件，把数据加载出来进行验证
用户名为json文件名，密码为 password。
判断是否过期，与expire_date进行对比。
登陆成功后，打印“登陆成功”，三次登陆失败，status值改为1，并且锁定账号。
"""
# 第一版普通登陆
# import json
# import os
# import time
# # import hashlib
#
# count = 0
# exit_flag = False
#
# while count < 3:
#     user = input('输入用户名：')
#     f = user.strip() + '.json'
#     if os.path.exists(f):
#         fp = open(f, 'r+', encoding='utf-8')
#         j_user = json.load(fp)
#         if j_user["status"] == 1:
#             print('账号已经锁定')
#             break
#         else:
#             expire_dt = j_user["expire_date"]
#
#             current_st = time.time()
#             expire_st = time.mktime(time.strptime(expire_dt, '%Y-%m-%d'))
#             # print(expire_st,current_st)
#             if current_st > expire_st:
#                 print('用户已经过期')
#                 break
#             else:
#                 while count < 3:
#                     pwd = input('输入密码： ')
#                     if pwd.strip() == j_user["password"]:
#                         print('用户[%s]登录成功' % user)
#                         exit_flag = True
#                         break
#                     else:
#                         print('密码不对')
#                         if count == 2:
#                             print('用户登录已超过3次，锁定账号')
#                             j_user["status"] = 1
#                             fp.seek(0)
#                             fp.truncate()  # 清空文件内容
#                             json.dump(j_user, fp)  # 写入锁定信息
#                     count += 1
#     if exit_flag:
#         break
#     else:
#         print('用户不存在')
#         count += 1

# 第二版MD5登陆
import json
import os
import time
import hashlib
count = 0
exit_flag = False
md = hashlib.md5()

while count < 3:
    user = input('输入用户名： ')
    f = user.strip() + '.json'
    if os.path.exists(f):
        fp = open(f, 'r+', encoding='utf-8')
        j_user = json.load(fp)
        if j_user["status"] == 1:
            print('账号已经锁定')
            break
        else:
            expire_dt = j_user["expire_date"]

            current_st = time.time()
            expire_st = time.mktime(time.strptime(expire_dt, '%Y-%m-%d'))
            # print(expire_st,current_st)
            if current_st > expire_st:
                print('用户已经过期')
                break
            else:
                while count < 3:
                    pwd = input('输入密码： ')
                    md.update(pwd.strip().encode('utf-8'))
                    md5_pwd = md.hexdigest()
                    if md5_pwd == j_user["password"]:
                        print('用户[%s]登录成功' % user)
                        exit_flag = True
                        break
                    else:
                        print('密码不对')
                        if count == 2:
                            print('用户登录已超过3次，锁定账号')
                            j_user["status"] = 1
                            fp.seek(0)
                            fp.truncate()  # 清空文件内容
                            json.dump(j_user, fp)  # 写入锁定信息
                            fp.close()
                    count += 1
    if exit_flag:
        break
    else:
        print('用户不存在')
        count += 1
