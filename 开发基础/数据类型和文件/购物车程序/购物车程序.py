#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 20:31

exit_flag = False
user_file = open("userinfo.txt", 'r+')  # 读取用户信息记录
user_info = user_file.read()
user_info = eval(user_info)
username = input("请输入您的账号：")
password = input("请输入您的密码：")
while True:
    if username in user_info:
        if password in user_info[username]:  # 密码如果能对应用户名，就欢迎登录
            salary = int(user_info[username][password])
            print("\033[32;1m欢迎登陆，当前余额为%s\033[0m" % salary)
            break
        else:
            password = input("\033[31;1m密码输入错误，请重新输入：\033[0m")
            continue
    else:
        password_salary = {}
        salary = input("欢迎首次登录，请输入您的工资：")
        if salary.isdigit():
            salary = int(salary)
            with open("userinfo.txt", "r+") as wirte_userinfo:
                password_salary[password] = salary
                user_info[username] = password_salary
                user_info = str(user_info)
                wirte_userinfo.seek(0)
                wirte_userinfo.write(user_info)
                wirte_userinfo.tell()
                break
        else:
            print("\033[31;1m工资请输入数字，请重新输入：\033[0m")
            continue

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

history_file = open("history_shopping.txt", "r+")  # 读取历史购买记录文件
history_shopping = str(history_file.read())
shoppinglist_dict = eval(history_shopping)  # 将历史记录信息转换为字典
if username not in shoppinglist_dict:
    shoppinglist_dict[username] = []
shoppinglist = shoppinglist_dict[username]  # 不是首次登录，将之前历史记录赋值到变量
shoppinglist_now = []  # 本次购物记录留空
user_choice = input("\n是否选择查询历史购物记录(y/n):")
if user_choice == 'y':
    print('历史购物记录'.center(40, '-'))
    print(shoppinglist)
    print('结束'.center(40, '-'))
else:
    print('谢谢您的信任，请继续购物'.center(40, '-'))

while not exit_flag:
    print('商品清单'.center(40, '-'))
    for index, item in enumerate(goods):
        print(index, item)
    print('end'.center(40, '-'))
    number = input("请输入要想购买的商品编号(或者按q直接退出)：")
    if number == 'q':
        exit_flag = True
        if type(user_info) == str:
            user_info = eval(user_info)
        else:
            pass
        user_info[username][password] = str(salary)
        user_file.seek(0)
        user_file.write(str(user_info))
        user_file.tell()
        user_file.close()
        print("goods".center(40, '-'))
        print(shoppinglist_now)
        print("\033[32;1m当前余额为%s,欢迎下次光临！\033[0m" % salary)
        shoppinglist.extend(shoppinglist_now)
        shoppinglist_dict[username] = shoppinglist
        history_file.seek(0)
        history_file.write(str(shoppinglist_dict))
        history_file.tell()
        history_file.close()
    elif number.isdigit() == False:
        print("\033[31;1m您的输入不是商品编号，请输入商品编号\033[0m")
    elif int(number) >= (len(goods)) or int(number) < 0:
        print("\033[31;1m您所购买的商品不在购物清单\033[0m")
    else:
        number1 = int(number)
        if goods[number1].get('price') < (salary):
            salary -= goods[number1].get('price')
            print("\033[1;34;47m添加[ %s ]到您的购物车,购物之后您的余额是[ %s]\033[0m" % (
                goods[number1].get('name'), salary))
            shoppinglist_now.append(goods[number1])
        else:
            print("\033[1;34;47m您的余额只有%s，无法购买\033[0m" % salary)
