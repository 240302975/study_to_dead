#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 14:41

# 1.请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li＝[‘alex’, ‘eric’, ‘rain’]
li = ['alex', 'eric', 'rain']
a = '_'
print(a.join(li))  # 将序列中的元素以指定的字符连接生成

# 2.查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。
li = ["alec", " aric", "Alex", "Tony", "rain"]  # 列表
tu = ("alec", " aric", "Alex", "Tony", "rain")  # 元组
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}  # 字典
for i in li:  # 循环
    i.strip()  # 移除空格
    if i.startswith('a') or i.startswith('A') and i.endswith('c'):  # 打印符合条件的
        print(i)
for i in tu:
    i.strip()
    if i.startswith('a') or i.startswith('A') and i.endswith('c'):
        print(i)
for k, v in dic.items():  # 以列表返回可遍历的(键, 值) 元组数组
    v = v.strip()
    if v.startswith('a') or v.startswith('A') and v.endswith('c'):
        print(v)

# 3.写代码，有如下列表，按照要求实现每一个功能
li = ['alex', 'eric', 'rain']
# 计算列表长度并输出
print(len(li))
# 列表中追加元素“seven”，并输出添加后的列表
li.append('seven')
print(li)
# 请在列表的第1个位置插入元素“Tony”，并输出添加后的列表
li.insert(0, "Tony")
print(li)
# 请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
li[1] = "kelly"
print(li)
# 请删除列表中的元素“eric”，并输出修改后的列表
del li[li.index('eric')]  # index先查找
print(li)
# 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
print(li.pop(1))
print(li)
# 请删除列表中的第3个元素，并输出删除元素后的列表
li.pop(2)
print(li)
# 请删除列表中的第2至4个元素，并输出删除元素后的列表
li = ['1', '2', '3', '4', '5']
del (li[1:4])
print(li)
# 请将列表所有的元素反转，并输出反转后的列表
print(li[::-1])

li.reverse()
print(li)
# 请使用for、len、range输出列表的索引
for i in range(len(li)):
    print(i)
# 请使用enumrate输出列表元素和序号（序号从100开始）
for index, val in enumerate(li, 100):  # enumerate(sequence, [start=0])
    print(val, index)
# 请使用for循环输出列表的所有元素
for i in li:
    print(i)

# 4.写代码，有如下列表，请按照功能要求实现每一个功能
li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
# 请根据索引输出“Kelly”
print(li[2][1][1])
# 请使用索引找到’all’元素并将其修改为“ALL”，如：li[0][1][9]…
print(li[2][2].upper())

# 5.有如下变量，请实现要求的功能
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
# 讲述元组的特性
# 不可变，有序。元组内第一层元素不可变（如tu元组中的alex，k3，44）。第二层及以上可以通过深copy浅copy修改

# 请问tu变量中的第一个元素“alex”是否可被修改？
# 不能被修改

# 请问tu变量中的”k2”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# 答：list，可修改
li = tu[1][2]["k2"]
li.append("Seven")
print(tu)

# 请问tu变量中的”k3”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# tu变量中的k3对于的是tuple元组，不可以修改

# 6.转换
# 将字符串s = “alex”转换成列表
s = "alex"
print(list(s))
# 将字符串s = “alex”转换成元祖
s = "alex"
print(tuple(s))
# 将列表li = [“alex”, “seven”]转换成元组
li = ["alex", "seven"]
print(tuple(li))
# 将元组tu = (‘Alex’, “seven”)转换成列表
tu = ('Alex', 'seven')
print(list(tu))
# 将列表li = [“alex”, “seven”]转换成字典且字典的key按照10开始向后递增
li = ["alex", "seven"]
lis = [10, 11]
print(dict(zip(lis, li)))  # zip() --> # {10: 'alex', 11: 'seven'}

# 7.元素分类
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
max66 = []  # 空列表
mix66 = []
for i in li:
    if i > 66:
        mix66.append(i)
    else:
        max66.append(i)
dic = {"k1": mix66, "k2": max66}
print(dic)

# 8.在不改变列表数据结构的情况下找最大值li = [1,3,2,7,6,23,41,243,33,85,56]。（编程题）
li = [1, 3, 2, 7, 6, 23, 41, 243, 33, 85, 56]
l2 = sorted(li)  # sorted 不会对原列表结构产生变化
print(l2[-1])

# 9.在不改变列表中数据排列结构的前提下，找出以下列表中最接近最大值和最小值的平均值的数li = [-100,1,3,2,7,6,120,121,140,23,411,99,243,33,85,56]。（编程题）
li = [-100, 1, 3, 2, 7, 6, 120, 121, 140, 23, 411, 99, 243, 33, 85, 56]
l2 = sorted(li)  # 重新排序列表
print(l2)  # [-100, 1, 2, 3, 6, 7, 23, 33, 56, 85, 99, 120, 121, 140, 243, 411]
half = l2[-1] / 2 + l2[0] / 2
print('最大值和最小值的平均值:%f' % half)

half_like = li[0]
for i in li:
    if abs(i - half) < abs(half_like - half):
        half_like = i
print('最接近平均值 的是', half_like)

# 10.利用for循环和range输出9 * 9乘法表。（编程题）
for i in range(1, 10):
    for j in range(1, i + 1):
        s = i * j
        print("{}*{}={}".format(j, i, s), end=" ")  # 空格切分
    print("")  # 表示换行

# 11.求100以内的素数和。
t = 0
for x in range(100):
    # 判断如果ｘ是素数，则打印，如果不是素数就跳过
    if x < 2:
        continue
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        t += x
print(t)
