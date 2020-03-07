#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/22 21:35


class Student(object):
    """学生类，包含姓名，年龄"""

    def __init__(self, student_name, student_age):
        self.student_name = student_name
        self.student_age = student_age
