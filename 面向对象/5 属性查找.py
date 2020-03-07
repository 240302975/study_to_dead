#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/27 21:58

"""
在现实世界中：
    对象1：王二丫
        特征：
            学校 = 'luffycity'
            名字 = '王二丫'
            性别 = '女'
            年龄 = 18
        技能：
            学习
            吃饭
            睡觉

    对象2：李三炮
        特征：
            学校 = 'luffycity'
            名字 = '李三炮'
            性别 = '男'
            年龄 = 38
        技能：
            学习
            吃饭
            睡觉

    对象3：张铁蛋
            特征：
                学校 = 'luffycity'
                名字 = '张铁蛋'
                性别 = '男'
                年龄 = 38
            技能：
                学习
                吃饭
                睡觉

    总结现实中路费学院得学生类
        相似得特征
            学校 = 'luffycity'

        相似得技能
            学习
            吃饭
            睡觉
"""


class LuffyStudent:
    school = 'luffycity'

    def __init__(self, name, sex, age):
        self.Name = name
        self.Sex = sex
        self.Age = age

        # stu1.Name = 'alex'
        # stu1.Sex = 'sex'
        # stu1.Age = 'age'

    def learn(self, book):
        print('%s is learning %s' % (self.Name, book))

    def eat(self):
        print('%s is eating' % self.Name)


# 后产生对象
stu1 = LuffyStudent('王二丫', '女', 18)
stu2 = LuffyStudent('李三炮', '男', 38)
stu3 = LuffyStudent('张铁蛋', '男', 48)
# print(stu1.__dict__)
# print(stu2.__dict__)
# print(stu3.__dict__)

# 对象:特征与技能的结合体
# 类：类是一系列对象相似的特征与相似得技能的结合体


# 类中的数据属性:是所有对象共有的
# print(LuffyStudent.school)
# print(stu1.school)
# print(stu2.school)


# 类中的函数属性:是绑定给对象使用的，绑定到不同的对象是不同的绑定方法，对象调用绑定方法时，会把对象本身当作第一个传入，传给self

# print(LuffyStudent.learn
# LuffyStudent.learn(stu1)
# LuffyStudent.learn(stu2)
# LuffyStudent.learn(stu3)


# stu1.learn('chinese')
# # stu2.learn('chinese')
# # stu3.learn('chinese')

stu1.x = 'from stu1'
LuffyStudent.x = 'from Luffycity class'
print(stu1.x)
