#!/usr/bin/env python
# -*- coding: utf-8 -*-
columns = ['id', 'name', 'age', 'phone', 'dept', 'enrolled_date']
with open(r'staff_table', 'r', encoding='utf-8') as fp:
    staff_list = [line.strip().split(',') for line in fp]  # 列表结构形式员工信息
data = dict(zip(columns, map(list, zip(*staff_list))))  # 将员工信息存到如下结构中
print(data)
"""
data = {'age': ['25', '28', '21', '44', '23', '19', '21', '22', '20', '26'],
        'phone': ['13651054608', '13451024608', '13451054608', '15653354208', '13351024606', '18531054602',
                  '13235324334',
                  '13151054603', '13351024602', '13698424612'],
        'name': ['Alex Li', 'Jack Wang', 'Rain Wang', 'Mack Qiao', 'Rachel Chen', 'Eric Liu', 'Chao Zhang',
                 'Kevin Chen',
                 'Shit Wen', 'Shanshan Du'],
        'enrolled_date': ['2013-04-01', '2015-01-07', '2017-04-01', '2016-02-01', '2013-03-16', '2012-12-01',
                          '2011-08-08',
                          '2013-04-01', '2017-07-03', '2017-07-02'],
        'dept': ['IT', 'HR', 'IT', 'Sales', 'IT', 'Marketing', 'Administration', 'Sales', 'IT', 'Operation'],
        'id': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']}
"""

info = list(zip(data['id'], data['name'], data['age'], data['phone'], data['dept'], data['enrolled_date']))
res = (','.join(info[0]))
print(res)

"""
info = [('1', 'Alex Li', '25', '13651054608', 'IT', '2013-04-01'),
        ('2', 'Jack Wang', '28', '13451024608', 'HR', '2015-01-07'),
        ('3', 'Rain Wang', '21', '13451054608', 'IT', '2017-04-01'),
        ('4', 'Mack Qiao', '44', '15653354208', 'Sales', '2016-02-01'),
        ('5', 'Rachel Chen', '23', '13351024606', 'IT', '2013-03-16'),
        ('6', 'Eric Liu', '19', '18531054602', 'Marketing', '2012-12-01'),
        ('7', 'Chao Zhang', '21', '13235324334', 'Administration', '2011-08-08'),
        ('8', 'Kevin Chen', '22', '13151054603', 'Sales', '2013-04-01'),
        ('9', 'Shit Wen', '20', '13351024602', 'IT', '2017-07-03'),
        ('10', 'Shanshan Du', '26', '13698424612', 'Operation', '2017-07-02')]

res='1,Alex Li,25,13651054608,IT,2013-04-01'
"""
