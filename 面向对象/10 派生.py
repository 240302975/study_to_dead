#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/29 23:53


class Hero:
    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity


class Garen(Hero):
    camp = 'Demacia'

    def attack(self, enemy):  # 派生，添加新的属性，如果和父类重名，以自己为准
        print('from Garen Class')


class Riven(Hero):
    camp = 'Noxus'


g1 = Garen('草丛伦', 100, 20)
r1 = Riven('锐雯', 80, 50)
print(g1.camp)
g1.attack(r1)
print(r1.life_value)
