#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/31 15:21


class People:
    school = 'luffycity'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(People):
    school = 'luffycity'

    def __init__(self, name, age, sex, level, salary):
        super().__init__(name, age, sex)
        self.level = level
        self.salary = salary

    def teach(self):
        print('%s is teachin' % self.name)


class Student(People):
    school = 'luffycity'

    def __init__(self, name, age, sex, class_time):
        super().__init__(name, age, sex)
        self.class_time = class_time

    def learn(self):
        print('%s is learning' % self.name)


class Course:
    def __init__(self, course_name, course_period, course_price):
        self.course_name = course_name
        self.course_period = course_period
        self.course_price = course_price

    def tell_info(self):
        print('课程名<%s> 课程价钱<%s> 课程周期<%s>' % (self.course_name, self.course_period, self.course_price))


class Date:
    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def tell_info(self):
        print('%s-%s-%s' % (self.year, self.mon, self.day))


# teacher1 = Teacher('alex', 18, 'male', 10, 3000)
# teacher2 = Teacher('egon', 28, 'male', 30, 3000)
# student1 = Student('张三', 28, 'female', '08:30:00')

# python = Course('python', 3000, '3mons')
# linux = Course('linux', 2000, '4mons')

# teacher1.course = python
# teacher2.course = python
# student1.course1 = python
# student1.course2 = linux

# print(python)
# print(teacher1.course)
# print(teacher2.course)

# print(teacher1.course.course_name)
# teacher2.course.tell_info()
# student1.course1.tell_info()
# student1.course2.tell_info()

# student1.courses = []
# student1.courses.append(python)
# student1.courses.append(linux)

student1 = Student('张三', 28, 'female', '08:30:00')
d = Date(1988, 4, 20)
python = Course('python', 3000, '3mons')

student1.brith = d
student1.brith.tell_info()

student1.course = python
student1.course.tell_info()
