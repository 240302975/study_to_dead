#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/4 22:40

# 1、什么是异常：异常是错误发生的信号，一旦程序出错，并且程序没有处理这个错误，那么就会抛出异常，并且程序的运行随之终止

# print('1')
# print('2')
# print('3')
# int('aaa')
# print('4')
# print('5')

"""
# Traceback (most recent call last):  
#   File "E:/study_to_dead/开发基础/面向对象/29 异常处理.py", line 7, in <module>
#     int('aaa')
# ValueError: invalid literal for int() with base 10: 'aaa'  
"""

# 异常的追踪信息：Traceback
# 异常类：ValueError
# 异常值：invalid literal for int() with base 10: 'aaa'


# 2、错误分为两种：
# 语法错误
'''
    #语法错误示范一
    if
    #语法错误示范二
    def test:
        pass
    #语法错误示范三
    class Foo
        pass
    #语法错误示范四
    print(haha)
'''

# 逻辑错误
'''
    #TypeError:int类型不可迭代
    for i in 3:
        pass
    #ValueError
    num=input(">>: ") #输入hello
    int(num)
    
    #NameError
    aaa
    
    #IndexError
    l=['egon','aa']
    l[3]
    
    #KeyError
    dic={'name':'egon'}
    dic['age']
    
    #AttributeError
    class Foo:pass
    Foo.x
    
    #ZeroDivisionError:无法完成计算
    res1=1/0
    res2=1+'str'
'''

# 3、异常处理
# 强调一：如果错误发生的条件是可预知的，我们需要用if进行处理：在错误发生之前进行预防
# AGE = 10
# while True:
#     age = input('>>: ').strip()
#     if age.isdigit():  # 只有在age为字符串形式的整数时,下列代码才不会出错,该条件是可预知的
#         age = int(age)
#         if age == AGE:
#             print('you got it')
#             break


# 强调二：如果错误发生的条件是不可预知的，则需要用到try...except：在错误发生之后进行处理
# 基本语法为
'''
try:
    被检测的代码块
except 异常类型：
    try中一旦检测到异常，就执行这个位置的逻辑
'''
# 举例
try:
    f = open('a.txt', 'r', encoding='utf-8')
    g = (line.strip() for line in f)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    f.close()
