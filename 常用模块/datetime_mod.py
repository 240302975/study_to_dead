#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/17 23:36

# datetime.date：表示日期的类。常用的属性有year, month, day；
# datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond；
# datetime.datetime：表示日期时间。
# datetime.timedelta：表示时间间隔，即两个时间点之间的长度。
# datetime.tzinfo：与时区有关的相关信息。


# d.timestamp(),d.today(), d.year,d.timetuple()等方法可以调用

# datetime.datetime.now()  # 当前时间
# datetime.datetime.now() + datetime.timedelta(4) #当前时间 +4天
# datetime.datetime.now() + datetime.timedelta(hours=4) #当前时间+4小时

# d.replace(year=2999,month=11,day=30)
