#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 20:18


# 写函数，计算传入数字参数的和。（动态传参）
def num(*args):
    a = 0
    for i in args:
        a += i
    return a


print(num(1, 2, 3, 4))

# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
import os


def my_change(name, old_msg, new_msg):
    with open(name, encoding="utf-8", mode="r+")as v, open("name.txt", encoding="utf-8", mode="w")as v1:
        v1.write(v.read().replace(old_msg, new_msg))
    os.remove(name)
    os.rename("name.txt", name)


my_change("file.txt", "male", "boy")


# 写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
def my_space(obj):
    if obj:  # 判断obj不是空的
        if type(obj) == str:
            for item in obj:
                if item.isspace():
                    return True
            else:
                return False
        else:
            for i in obj:
                if not i:  # 如果执行这里，表示i一定为空
                    return True
            else:
                return False
    else:
        return True


val = my_space("jkl kb")
print(val)


# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容（对value的值进行截断），并将新内容返回给调用者，注意传入的数据可以是字符、list、dict
def my_length(dic):
    for key in dic:
        value = dic[key]
        print(value)
        if len(value) > 2:
            dic[key] = value[:2]
    return dic


val = my_length({"k1": "v1v1", "k2": [11, 22, 33, 44], "k3": "dsvf"})  # PS:字典中的value只能是字符串或列表
print(val)

# 解释闭包的概念
"""
概念：即函数定义和函数表达式位于另一个函数的函数体内(嵌套函数)。这些内部函数可以访问他们所在的外部函数中声明的所有局部变量和参数。
当其中一个这样的内部函数在包含他们的外部函数之外被调用时，就会形成闭包。内部函数会在外部函数返回后被执行，当这个内部函数执行时，它仍然可以访问其外部函数的局部变量、参数以及其他内部函数。

闭包的意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域
"""


# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]
def card():
    temp_list = []
    poker = []  # 扑克牌
    for i in range(2, 11):  # 每个花色2-10
        temp_list.append(i)
    temp_list.extend(["J", "Q", "K", "A"])  # 末尾追加JQKA
    for i in temp_list:  # 遍历
        for card_type in ["黑桃", "红桃", "方块", "草花"]:  # 牌色
            a = (card_type, i)
            poker.append(a)
    return poker


res = card()
print(res)


# 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
def func(*args):
    a = max(args)
    b = min(args)
    return {"max": a, "min": b}


back = func(1, 3, 343, 34, 5, 743, 999)
print(back)

# 写函数，专门计算图形的面积
#   其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
#   调用函数area(‘圆形’,圆半径) 返回圆的面积
#   调用函数area(‘正方形’,边长) 返回正方形的面积
#   调用函数area(‘长方形’,长，宽) 返回长方形的面积


import math


def area(name, *args):
    def area_rectangle(x, y):
        return "长方形的面积为:", x * y

    def area_square(x):
        return "正方形的面积为:", x ** 2

    def area_round(r):
        return "圆形的面积为:", math.pi * r * r

    if name == '长方形':
        return area_rectangle(*args)
    elif name == '正方形':
        return area_square(*args)
    elif name == '圆形':
        return area_round(*args)


print(area('长方形', 2, 3))
print(area('正方形', 3))
print(area('圆形', 6))


# 写函数，传入一个参数n，返回n的阶乘
def cal(n):
    a = 1
    for i in range(n, 0, -1):
        a = a * i
    return a


print(cal(6))

# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
FLAG = False  # 加一个变量防止多次登录验证


def wrapper(f):
    def inner(*args, **kwargs):
        """登录程序"""
        global FLAG  # 将FLAG变量设置成全局变量
        if FLAG:
            ret = f(*args, **kwargs)
            return ret
        else:
            username = input('username:')
            password = input('password:')
            if username == '123' and password == '345':
                FLAG = True
                ret = f(*args, **kwargs)
                return ret
            else:
                print('登录失败')

    return inner


@wrapper
def func_1():
    print('func1 is running!')


@wrapper
def func_2():
    print('func2 is running!')


func_1()
func_2()

# 生成器和迭代器的区别？
"""
1）迭代器是一个更抽象的概念，任何对象，如果它的类有next方法和iter方法返回自己本身。对于string、list、dict、tuple等这类容器对象，使用for循环遍历是很方便的。
在后台for语句对容器对象调用iter()函数，iter()是python的内置函数。iter()会返回一个定义了next()方法的迭代器对象，它在容器中逐个访问容器内元素，next()也是python的内置函数。
在没有后续元素时，next()会抛出一个StopIteration异常

2）生成器（Generator）是创建迭代器的简单而强大的工具。它们写起来就像是正规的函数，只是在需要返回数据的时候使用yield语句。
每次next()被调用时，生成器会返回它脱离的位置（它记忆语句最后一次执行的位置和所有的数据值）

两者区别：生成器能做到迭代器能做的所有事,而且因为自动创建了__iter__()和next()方法,生成器显得特别简洁,而且生成器也是高效的，使用生成器表达式取代列表解析可以同时节省内存。
除了创建和保存程序状态的自动方法,当发生器终结时,还会自动抛出StopIteration异常
"""

# 生成器有几种方式获取value？
"""
next()
for循环
"""


# 通过生成器写一个日志调用方法， 支持以下功能
#     根据指令向屏幕输出日志
#     根据指令向文件输出日志
#     根据指令同时向文件&屏幕输出日志
import time


def logger(filename, channel='file'):
    """
    :param filename: log filename
    :param channel: 输出的目的地，屏幕(terminal)，文件(file)，屏幕+文件(both)
    :return:
    """
    count = 0

    def print_file():
        with open(filename, "a", encoding="utf-8") as f:
            f.write(s)

    def print_terminal():
        print(s, end="")

    def print_both():
        with open(filename, "a", encoding="utf-8") as f:
            f.write(s)
        print(s, end="")

    func_dic = {
        'file': print_file,
        'terminal': print_terminal,
        'both': print_both,
    }
    print_func = func_dic[channel]
    while True:
        msg = yield
        s = "%s [%d] %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), count, msg)
        print_func()
        count += 1


log_obj = logger(filename="web.log", channel='both')
log_obj.__next__()
log_obj.send('user xiao login success')
log_obj.send('user qing login success')


# 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
name = ['alex', 'wupeiqi', 'yuanhao', 'nezha']


def sb(x):
    return x + '_sb'


res = map(sb, name)
print(list(res))

# 用filter函数处理数字列表，将列表中所有的偶数筛选出来
num = [1, 3, 5, 6, 7, 8]


def func(x):
    if x % 2 == 0:
        return True


ret = filter(func, num)  # filter()过滤序列，返回一个迭代器对象，最后用 list() 来转换。
print(list(ret))


# 如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
#   计算购买每支股票的总价
# 　用filter过滤出，单价大于100的股票有哪些
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 计算购买每支股票的总价
m = map(lambda y: y['shares'] * y['price'], portfolio)  # map会根据提供的函数对指定序列做映射
print(list(m))

# 用filter过滤出，单价大于100的股票有哪些
f = filter(lambda d: d['price'] >= 100, portfolio)
print(list(f))


# 有列表 li = ['alex', 'egon', 'smith', 'pizza', 'alen'],请将以字母“a”开头的元素的首字母改为大写字母；
li = ['alex', 'egon', 'smith', 'pizza', 'alen']
for i in range(len(li)):
    if li[i][0] == 'a':
        li[i] = li[i].capitalize()
    else:
        continue
print(li)


# 有列表 li = [‘alex’, ‘egon’, ‘smith’, ‘pizza’, ‘alen’], 请以列表中每个元素的第二个字母倒序排序
li = ['alex', 'egon', 'smith', 'pizza', 'alen']
t = list(sorted(li, key=lambda x: x[1], reverse=True))
print(t)


# 有名为poetry.txt的文件，其内容如下，请删除第三行
import os

f1 = open('poetry.txt', 'r', encoding='utf-8')

s = '晴川历历汉阳树，芳草萋萋鹦鹉洲。'
with open('poetry1.txt', 'w', encoding='utf-8') as f2:
    ff1 = 'poetry.txt'
    ff2 = 'poetry1.txt'
    for line in f1:
        if s in line:
            line = ''
            f2.write(line)
        else:
            f2.write(line)
f1.close()
f2.close()
os.replace(ff2, ff1)


# 有名为username.txt的文件，其内容格式如下，写一个程序，判断该文件中是否存在”alex”, 如果没有，则将字符串”alex”添加到该文件末尾，否则提示用户该用户已存在
with open('username.txt', 'r+', encoding='utf-8') as f:
    str1 = 'alex'
    i = f.read()
    print(i)
    if str1 in i:
        print("the user already exist in")
    else:
        f.write('\nalex')


# 有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行
import os

a = 'user_info.txt'
b = 'user_info1.txt'
with open(a, 'r', encoding='utf-8') as f:
    with open(b, 'w', encoding='utf-8') as f2:
        for i in f:
            if '100003' in i:
                pass
            else:
                f2.write(i)
os.replace(b, a)

# 有名为user_info.txt的文件，其内容格式如下，写一个程序，将id为100002的用户名修改为alex li
import os
f_name = r'user_info.txt'
f_new_name = '%s.new' % f_name
update_id = '100002'
update_name = 'alex li'
f_new = open(f_new_name, 'w', encoding='utf-8')
with open(f_name, 'r', encoding='utf-8') as f:
    for line in f:
        if update_id in line:
            line = ','.join([update_name, update_id])
            f_new.write(line + '\n')
        else:
            f_new.write(line)
f_new.close()
os.replace(f_new_name, f_name)


# 写一个计算每个程序执行时间的装饰器
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args)
        stop_time = time.time()
        d_time = stop_time - start_time
        print(d_time)
    return wrapper


@timer  # @timer调用时间
def sayhi():
    print("hello word")


sayhi()


# lambda是什么？请说说你曾在什么场景下使用lambda？
"""
lambda函数就是可以接受任意多个参数(包括可选参数)并且返回单个表达式值得函数
    好处：
        1.lambda函数比较轻便，即用即扔，适合完成只在一处使用的简单功能
        2.匿名函数，一般用来给filter，map这样的函数式编程服务
        3.作为回调函数，传递给某些应用，比如消息处理
"""

# 题目：写一个摇骰子游戏，要求用户压大小，赔率一赔一。要求：三个骰子，每个骰子的值从1-6，摇大小，每次打印摇出来3个骰子的值。
import random


def roll_dice(numbers=3, points=None):
    """
    定义骰子，循环三次
    :param numbers:
    :param points:
    :return:
    """
    if points is None:
        points = []

    print('----- 摇骰子 -----')
    while numbers > 0:
        point = random.randrange(1, 7)
        # print('roll dice is {}'.format(point))
        points.append(point)
        numbers -= 1

    return points


def roll_result(total):
    """
    定义大小，三个大或者一个小两个大。三个小或者两个小一个大
    :param total:
    :return:
    """

    is_big = 11 <= total <= 18
    is_small = 3 <= total <= 10
    if is_big:
        return "big"
    elif is_small:
        return "small"


def start_game():
    money = 1000
    while money > 0:
        print('----- 游戏开始 -----')
        choices = ['big', 'small']
        your_choice = input("请下注， big or small:")
        your_bet = input("下注金额:")
        if your_choice in choices:
            if your_bet.isdigit():
                points = roll_dice()
                total = sum(points)
                you_win = your_choice == roll_result(total)
                if you_win:
                    print("骰子点数", points, total)
                    money += int(your_bet)
                    print("恭喜， 你赢了%s元， 你现在的本金%s 元" % (your_bet, money))
                else:
                    print("骰子点数", points, total)
                    money -= int(your_bet)
                    print("很遗憾， 你输了%s元， 你现在的本金%s 元" % (your_bet, money))

            else:
                print('格式有误，请重新输入')
        else:
            print('格式有误，请重新输入')
    else:
        print("game over")


start_game()
