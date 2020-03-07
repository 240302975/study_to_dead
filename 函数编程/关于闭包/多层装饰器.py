#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 23:48


def makebold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"

    return wrapper


def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"

    return wrapper


@makebold
@makeitalic
def hello():
    return "hello alvin"


hello()