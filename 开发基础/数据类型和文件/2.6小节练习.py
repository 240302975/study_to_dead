#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 23:03

# 2.6字典练习
# 1.用你能想到的最少的代码生成一个包含100个key的字典，每个value的值不能一样
key = {}
for i in range(100):
    key.setdefault(i, i)
print(key)

# 2.{‘k0’: 0, ‘k1’: 1, ‘k2’: 2, ‘k3’: 3, ‘k4’: 4, ‘k5’: 5, ‘k6’: 6, ‘k7’: 7, ‘k8’: 8, ‘k9’: 9}
# 请把这个dict中key大于5的值value打印出来。
dic = {'k0': 0, 'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6, 'k7': 7, 'k8': 8, 'k9': 9}
for k, v in dic.items():  # 返回一个包含所有（键，值）元组的列表，由k，v接收
    if v > 5:
        print(dic[k])  # k为k0，k1，k2……，dic[k]=v

# 3.把题2中value是偶数的统一改成-1
for k, v in dic.items():
    if v % 2 == 0:
        dic[k] = -1
print(dic)

# 4.请设计一个dict, 存储你们公司每个人的信息， 信息包含至少姓名、年龄、电话、职位、工资，并提供一个简单的查找接口，用户按你的要求输入要查找的人，你的程序把查到的信息打印出来
info = {
    '张三': {'age': 20, '电话': 123, '职位': '经理', '工资': '8000'},
    '李四': {'age': 21, '电话': 456, '职位': '工程师', '工资': '4000'},
    '王五': {'age': 22, '电话': 789, '职位': '保洁', '工资': '3000'},
}
name = input("输入名字:").strip()
print(info.get(name, "输出错误，没找到这个人"))  # 返回字典中key对应的值，若key不存在字典中，则返回default的值

# 5.用一行代码将数值转换
a = [1, 2, 3]
b = (3, 2, 1)
a, b = b, a
print(a, b)

# 6.利用所学知识，将id前3位与字典中相对应的地区进行匹配，得出id中各属地出现的次数，得出结果形如：{"河南":3,"河北":2,"北京":1,"内蒙":1}
id = [120121198903119561,
      120121198903110561,
      120121196903119561,
      130482198307144762,
      130482198307144662,
      110121197805144347,
      150121197502122799]

addrs = {
    120: "河南",
    130: "河北",
    110: "北京",
    150: "内蒙",
}
dic = {}
for i in id:
    addrs_key = int(str(i)[0:3])  # 取前三位
    dic_key = addrs[addrs_key]  # 地区,没有则不统计
    if dic.get(dic_key):
        dic[dic_key] += 1  # 统计次数
    else:
        dic[dic_key] = 1
print(dic)

# 7.将字符串s转变为形如{'key1': '1', 'key2': '2', 'key3': '3'}的字典
s = "key:1-key:2-key:3"
ls = s.split("-")  # ['key:1', 'key:2', 'key:3']
dic = {}
for i in ls:
    k, v = (i.split(":"))  # ['key','1']
    dic[k + v] = v  # key1:1
print(dic)
