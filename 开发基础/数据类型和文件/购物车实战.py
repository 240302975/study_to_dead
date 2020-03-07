#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 14:43

# 定义一个商品列表，里面写入商品的值和价格
product_list = [
    ('iphone', 5000),
    ('coffee', 31),
    ('bicyle', 888),
    ('iwatch', 2666),
    ('Mac Pro', 12000),
    ('book', 88)
]
shopping_list = []  # 空列表，存放购买的商品

salary = input("请输入你的工资:")
if salary.isdigit():  # isdigit() 方法检测字符串是否只由数字组成,是则返回True,否则返回False
    salary = int(salary)
    while True:
        for index, i in enumerate(product_list):  # index作为下标索引
            print(index, i)
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        user_choice = input("请输入你要购买的商品[按q退出]:")
        if user_choice.isdigit():
            user_choice = int(user_choice)  # 判断choice是否为数字
            if len(product_list) > user_choice >= 0:
                product_choice = product_list[user_choice]
                if product_choice[1] <= salary:  # 买得起
                    shopping_list.append(product_choice)  # 买得起，就放入购物车
                    salary -= product_choice[1]  # 计算余额
                    print("Add %s into your shopping_list,your balance is %s" % (product_choice, salary))
                else:
                    print("你的余额只剩%s啦，还买个叼啊！" % salary)
                    print("---------shopping list-----------")
                    for s_index, s in enumerate(shopping_list):
                        print(s_index, s)
                    print("---------shopping list-----------")
                    print("你的余额为：%s" % salary)
                    break
            else:
                print("没有这个商品")
        elif user_choice == "q":
            print("---------shopping list-----------")
            for s_index, s in enumerate(shopping_list):
                print(s_index, s)
            print("---------shopping list-----------")
            print("你的余额为：%s" % salary)
            exit()
        else:
            print("输入错误")
else:
    print("输入错误")
