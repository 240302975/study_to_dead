#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/29 15:21

"""
练习1：编写一个学生类，产生一堆学生对象（5分钟）

要求：
有一个计数器（属性），统计总共实例了多少对象
"""


# 计数器应该为类属性
class Student:
    school = 'luffycity'
    count = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        # self.count += 1
        Student.count += 1  # 调用类里的count

    def learn(self):
        print('%s is learning' % self.name)


stu1 = Student('alex', 'male', 38)
stu2 = Student('jinxing', 'female', 78)
stu3 = Student('egon', 'male', 18)

print(Student.count)
print(stu1.count)
print(stu2.count)

"""
练习2：模仿LOL定义两个英雄类（10分钟）

要求：
英雄需要有昵称、攻击力、生命值等属性；
实例化出两个英雄对象；
英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡。
"""


class Garen:
    camp = 'Demacia'

    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity
        # r1.life_value -= g1.aggresivity


class Riven:
    camp = 'Noxus'

    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity


g1 = Garen('草丛伦', 100, 20)

r1 = Riven('锐雯', 80, 50)

print(r1.life_value)
g1.attack(r1)
print(r1.life_value)
