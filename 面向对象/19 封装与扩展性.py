#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/1 16:41


class Room:
    def __init__(self, name, owner, weight, length, height):
        self.name = name
        self.owner = owner
        self.__height = height
        self.__weight = weight
        self.__length = length

    def tell_area(self):
        return self.__weight * self.__length * self.__height


r = Room('卫生间', 'alex', 10, 20, 30)
print(r.tell_area())
