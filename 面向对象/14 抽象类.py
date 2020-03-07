#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/31 20:47

import abc


class Animal(metaclass=abc.ABCMeta):  # 只能被继承，不能被实例化
    all_type = 'animal'

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def eat(self):
        pass

# animal = Animal


class People(Animal):
    def run(self):
        print('people is working')

    def eat(self):
        print('people is eating')


class Pig(Animal):
    def run(self):
        print('pig is running')

    def eat(self):
        print('pig is eating')


class Dog(Animal):
    def run(self):
        print('is zouing')

    def eat(self):
        print('is eating')


peo1 = People()
pig1 = Pig()
dog1 = Dog()

peo1.eat()
pig1.eat()
print(peo1.all_type)
